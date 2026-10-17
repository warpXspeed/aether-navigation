#!/usr/bin/env python3
"""
dfm_steering_sim.py (Upgraded to Field-Equation Drive)
======================================================
Field-Driven Medium-State Trajectory Simulator — Aether Navigation / SRC

Upgraded from a kinematic proxy to calculate steering forces directly from:
  1. Dynamic DFM density (rho_dfm) and adiabatic moduli drift.
  2. Local vacuum refractive index modulation (n_aether).
  3. Traveling harmonic soliton wave actuation across the vessel array.

Dependencies: numpy, matplotlib
Run: python dfm_steering_sim.py
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# 1. PHYSICAL & SUBSTRATE PARAMETERS
# ----------------------------------------------------------------------
MU_SINK         = 1.0     # core sink strength (gravitational sink)
R_BODY          = 1.0     # planetary body radius
DFM_K           = 1.0     # baseline bulk modulus of aether substrate
OMEGA_CORE      = 0.62    # core primary oscillation frequency
ADIA_DRIFT_RATE = 0.02    # baseline adiabatic moduli drift

# ----------------------------------------------------------------------
# 2. CRAFT STATE AND ACTUATION PARAMETERS
# ----------------------------------------------------------------------
CRAFT = {
    "x": 4.0, "y": 0.0,          # position
    "vx": 0.0, "vy": 0.45,       # velocity
    "phase_lock": 0.0,           # phase synchronization state [0, 1]
    "decoherence": 0.0,          # sink-detuning (potential-well shift) [0, 1]
    "wave_amplitude": 0.8,       # traveling harmonic soliton drive strength
    "wave_frequency": 2.5,       # soliton propagation frequency
}

DT = 0.01
T_MAX = 40.0
STEPS = int(T_MAX / DT)

# Command schedule: (t_start, t_end, action)
COMMANDS = [
    (5.0, 8.0,   "grab"),
    (12.0, 16.0, "detune"),
    (20.0, 23.0, "grab"),
    (30.0, 33.0, "slip"),
]

def medium_density(x, y, t):
    """Local Dynamic Fluid Medium density (rho_dfm) with adiabatic drift."""
    r = np.hypot(x, y) + 1e-9
    drift = 1.0 + ADIA_DRIFT_RATE * np.sin(OMEGA_CORE * t) * np.cos(np.arctan2(y, x))
    return DFM_K * MU_SINK / (r * r) * drift

def vacuum_refractive_index(x, y, t, craft):
    """
    Calculates local n_aether based on baseline DFM density and 
    traveling harmonic wave actuation (peristaltic magnetic pressure).
    """
    rho = medium_density(x, y, t)
    # Traveling wave soliton contribution from coil array actuation
    soliton_mod = craft["phase_lock"] * craft["wave_amplitude"] * np.cos(
        craft["wave_frequency"] * t - np.arctan2(y, x)
    )
    # Effective bulk modulus modulated by soliton pressure
    k_eff = DFM_K * (1.0 + soliton_mod)
    return np.sqrt(max(0.01, k_eff / rho))

def sink_flow_gradient(x, y, t):
    """Flow acceleration vector toward the core's energetic sink."""
    r = np.hypot(x, y) + 1e-9
    rho = medium_density(x, y, t)
    mag = rho * MU_SINK / (r * r)
    return -mag * x / r, -mag * y / r

def update_craft(craft, t, mode="dfm"):
    """Advance craft one timestep using field-equation derived forces."""
    x, y = craft["x"], craft["y"]
    fx, fy = sink_flow_gradient(x, y, t)

    if mode == "newtonian":
        ax, ay = fx, fy
    else:
        # Potential-well detuning (decoherence modulation)
        coupling = max(0.0, craft["phase_lock"] * (1.0 - craft["decoherence"]))
        
        # Base sink coupling
        ax = coupling * fx
        ay = coupling * fy

        # Field-driven steering via gradient of refractive index (nabla ln(n_aether))
        eps = 1e-3
        n_center = vacuum_refractive_index(x, y, t, craft)
        n_dx = vacuum_refractive_index(x + eps, y, t, craft)
        n_dy = vacuum_refractive_index(x, y + eps, t, craft)
        
        grad_ln_nx = (np.log(n_dx) - np.log(n_center)) / eps
        grad_ln_ny = (np.log(n_dy) - np.log(n_center)) / eps

        # Medium-coupled Lorentz force vectoring along refractive index gradients
        steering_gain = 0.3 * craft["phase_lock"] * (1.0 - craft["decoherence"])
        ax -= steering_gain * grad_ln_nx
        ay -= steering_gain * grad_ln_ny

    craft["vx"] += ax * DT
    craft["vy"] += ay * DT
    craft["x"] += craft["vx"] * DT
    craft["y"] += craft["vy"] * DT

def run_commands(craft, t):
    """Apply command schedule to craft control states."""
    for t0, t1, action in COMMANDS:
        if t0 <= t <= t1:
            if action == "grab":
                craft["phase_lock"] = min(1.0, craft["phase_lock"] + 0.5 * DT)
            elif action == "slip":
                craft["phase_lock"] = max(0.0, craft["phase_lock"] - 1.5 * DT)
            elif action == "detune":
                craft["decoherence"] = min(0.95, craft["decoherence"] + 0.4 * DT)
        else:
            craft["decoherence"] = max(0.0, craft["decoherence"] - 0.2 * DT)

def run(mode):
    import copy
    craft = copy.deepcopy(CRAFT)
    path, refractive_indices = [], []
    for i in range(STEPS):
        t = i * DT
        if mode == "dfm":
            run_commands(craft, t)
        update_craft(craft, t, mode)
        path.append((craft["x"], craft["y"]))
        refractive_indices.append(vacuum_refractive_index(craft["x"], craft["y"], t, craft))
    return np.array(path), np.array(refractive_indices)

def main():
    newton_path, _ = run("newtonian")
    dfm_path, dfm_n = run("dfm")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    body = plt.Circle((0, 0), R_BODY, color="k", alpha=0.6)
    ax1.add_patch(body)
    ax1.plot(newton_path[:, 0], newton_path[:, 1], "r--", label="Newtonian ballistic baseline")
    ax1.plot(dfm_path[:, 0], dfm_path[:, 1], "b-", lw=2, label="DFM Field-Driven Steering")
    ax1.plot(dfm_path[0, 0], dfm_path[0, 1], "go", label="start")
    ax1.set_xlabel("x"); ax1.set_ylabel("y")
    ax1.set_title("Trajectory: Field Equation Driven DFM Navigation")
    ax1.legend(); ax1.set_aspect("equal"); ax1.grid(alpha=0.3)

    ax2.plot(np.arange(STEPS) * DT, dfm_n, "b-", label="n_aether (local)")
    for t0, t1, action in COMMANDS:
        ax2.axvspan(t0, t1, alpha=0.15, color="orange")
        ax2.text((t0 + t1) / 2, dfm_n.mean(), action, ha="center", fontsize=8)
    ax2.set_xlabel("time"); ax2.set_ylabel("Vacuum Refractive Index (n_aether)")
    ax2.set_title("Dynamic n_aether Modulation via Soliton Drive")
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("dfm_steering_sim.png", dpi=150)
    print("Saved updated simulation plot to simulations/scripts/dfm_steering_sim.png")
    plt.show()

if __name__ == "__main__":
    main()

