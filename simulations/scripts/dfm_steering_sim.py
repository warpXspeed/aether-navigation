#!/usr/bin/env python3
"""
dfm_steering_sim.py
===================
Medium-State Trajectory Simulator — Aether Navigation / SRC framework

Models a craft navigating the Dynamic Fluid Medium (DFM) near a planetary
body, contrasting:

  1. NEWTONIAN BASELINE — passive ballistic trajectory under a fixed
     gravitational parameter (mu).
  2. DFM STEERING       — open-system navigation via:
       - local medium density (rho_dfm) gradients (adiabatic moduli drift)
       - Lorentz/Eddy steering authority (medium adhesion / release)
       - decoherence control (potential-well transitions via sink detuning)

The "gravity" field here is NOT treated as an attractive force. It is modeled
as a directional flow toward the planetary core's energetic sink, whose local
coupling strength is modulated by the craft's phase-synchronization state.

Dependencies: numpy, matplotlib (pip install numpy matplotlib)
Run:  python dfm_steering_sim.py
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# 1. MEDIUM AND SINK PARAMETERS (units: arbitrary / normalized)
# ----------------------------------------------------------------------
MU_SINK          = 1.0     # nominal sink coupling (replaces GM in Newtonian use)
R_BODY           = 1.0     # planetary body radius
DFM_K            = 1.0     # baseline bulk modulus of aether substrate
OMEGA_CORE       = 0.62    # planetary core primary oscillation frequency
ADIA_DRIFT_RATE  = 0.02    # baseline adiabatic moduli drift per time unit

# ----------------------------------------------------------------------
# 2. CRAFT STATE AND CONTROL PARAMETERS
# ----------------------------------------------------------------------
CRAFT = {
    "x": 4.0, "y": 0.0,          # position
    "vx": 0.0, "vy": 0.45,       # velocity (drift along medium streamlines)
    "phase_lock": 0.0,           # phase synchronization with local aether mode
    "decoherence": 0.0,          # sink-detuning state (0 = fully coupled)
    "eddy_authority": 0.5,       # Lorentz/Eddy steering gain
}

DT = 0.01
T_MAX = 40.0
STEPS = int(T_MAX / DT)

# Simple command schedule: (t_start, t_end, action)
# Actions: "grab" (increase medium adhesion), "slip" (release),
#          "detune" (decoherence / potential-well shift)
COMMANDS = [
    (5.0, 8.0,  "grab"),
    (12.0, 16.0, "detune"),
    (20.0, 23.0, "grab"),
    (30.0, 33.0, "slip"),
]

def medium_density(x, y, t):
    """
    Local Dynamic Fluid Medium density (rho_dfm).

    Combines the static sink gradient with a slow, history-preserving
    adiabatic moduli drift (aether 'memory' term). Path history effects
    are approximated here by a global drift phase.
    """
    r = np.hypot(x, y) + 1e-9
    drift = 1.0 + ADIA_DRIFT_RATE * np.sin(OMEGA_CORE * t) * np.cos(np.arctan2(y, x))
    return DFM_K * MU_SINK / (r * r) * drift

def sink_flow(x, y, rho):
    """
    Directional flow of the medium toward the core's energetic sink.
    Returns flow acceleration vector. NOT a force — it is the local
    streamline the craft drifts along when fully coupled.
    """
    r = np.hypot(x, y) + 1e-9
    mag = rho * MU_SINK / (r * r)
    return -mag * x / r, -mag * y / r

def coupling_factor(craft):
    """
    Effective coupling to the primary sink.

    phase_lock  ~ [0, 1] : phase synchronization with aether mode
    decoherence ~ [0, 1] : potential-well detuning (sink decoupling)
    """
    return max(0.0, craft["phase_lock"] * (1.0 - craft["decoherence"]))

def update_craft(craft, t, mode="dfm"):
    """Advance craft one timestep. mode = 'dfm' or 'newtonian'."""
    rho = medium_density(craft["x"], craft["y"], t)
    fx, fy = sink_flow(craft["x"], craft["y"], rho)

    if mode == "newtonian":
        # Passive ballistic: full coupling, no medium steering.
        ax, ay = fx, fy
    else:
        k = coupling_factor(craft)
        ax, ay = k * fx, k * fy

        # Lorentz/Eddy steering: asymmetric plasma-sheath vectoring.
        # Steers along streamlines perpendicular to the density gradient.
        grho_x = (medium_density(craft["x"] + 0.01, craft["y"], t)
                  - medium_density(craft["x"] - 0.01, craft["y"], t))
        grho_y = (medium_density(craft["x"], craft["y"] + 0.01, t)
                  - medium_density(craft["x"], craft["y"] - 0.01, t))
        gmag = np.hypot(grho_x, grho_y) + 1e-12
        # perpendicular to gradient = along-isodensity streamline
        ax += CRAFT["eddy_authority"] * (-grho_y / gmag) * 0.05
        ay += CRAFT["eddy_authority"] * ( grho_x / gmag) * 0.05

    craft["vx"] += ax * DT
    craft["vy"] += ay * DT
    craft["x"] += craft["vx"] * DT
    craft["y"] += craft["vy"] * DT

def run_commands(craft, t):
    """Apply the command schedule to craft control states."""
    for t0, t1, action in COMMANDS:
        if t0 <= t <= t1:
            if action == "grab":
                craft["phase_lock"] = min(1.0, craft["phase_lock"] + 0.5 * DT)
            elif action == "slip":
                craft["phase_lock"] = max(0.0, craft["phase_lock"] - 1.5 * DT)
            elif action == "detune":
                craft["decoherence"] = min(0.95, craft["decoherence"] + 0.4 * DT)
        else:
            # relax control states back toward neutral baseline
            craft["decoherence"] = max(0.0, craft["decoherence"] - 0.2 * DT)

def run(mode):
    import copy
    craft = copy.deepcopy(CRAFT)
    path, locks = [], []
    for i in range(STEPS):
        t = i * DT
        if mode == "dfm":
            run_commands(craft, t)
        update_craft(craft, t, mode)
        path.append((craft["x"], craft["y"]))
        locks.append(coupling_factor(craft))
    return np.array(path), np.array(locks)

def main():
    newton_path, _ = run("newtonian")
    dfm_path, dfm_lock = run("dfm")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    body = plt.Circle((0, 0), R_BODY, color="k", alpha=0.6)
    ax1.add_patch(body)
    ax1.plot(newton_path[:, 0], newton_path[:, 1],
             "r--", label="Newtonian ballistic baseline")
    ax1.plot(dfm_path[:, 0], dfm_path[:, 1],
             "b-", lw=2, label="DFM medium-state steering")
    ax1.plot(dfm_path[0, 0], dfm_path[0, 1], "go", label="start")
    ax1.set_xlabel("x"); ax1.set_ylabel("y")
    ax1.set_title("Trajectory: force-fighting vs. medium navigation")
    ax1.legend(); ax1.set_aspect("equal"); ax1.grid(alpha=0.3)

    ax2.plot(np.arange(STEPS) * DT, dfm_lock, "b-")
    for t0, t1, action in COMMANDS:
        ax2.axvspan(t0, t1, alpha=0.15, color="orange")
        ax2.text((t0 + t1) / 2, 0.5, action, ha="center", fontsize=8)
    ax2.set_xlabel("time"); ax2.set_ylabel("sink coupling factor")
    ax2.set_title("Phase-lock / decoherence command profile")
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("dfm_steering_sim.png", dpi=150)
    print("Saved dfm_steering_sim.png")
    plt.show()

if __name__ == "__main__":
    main()

