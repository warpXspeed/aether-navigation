# Craft Architecture & Applied Systems

## Overview
This directory houses the engineering specifications, hardware architecture, and subsystem designs for vessels operating under Scalar Relaxation Cosmology (SRC) and Dynamic Fluid Medium (DFM) principles.

While the `principles/` directory establishes *why* medium-state navigation works, this section details *how* to build the physical systems capable of coupling with planetary core discharges, managing Lorentz/Eddy steering, and executing decoherence control cycles.

## Subdirectory Structure
- `01-requirements-and-constraints.md` — Engineering parameters, material constraints, and environmental operating limits.
- `02-concept-architecture.md` — Overall vessel geometry, core integration, and field generation topology.
- `03-subsystems.md` — Detailed breakdowns of plasma field modulation, decoherence control units, and navigational feedback sensors.
- `04-test-plan-and-safety.md` — Empirical validation protocols, containment safeguards, and risk mitigation for medium-state transitions.

*We aren't looking for "antigravity machines" because we aren't trying to fight a force. We are building the craft to navigate the medium.*

# 01 - Requirements and Constraints

## 1.1 Purpose
This document establishes the baseline engineering requirements, physical constraints, and performance parameters for a craft designed to navigate the Dynamic Fluid Medium (DFM) rather than relying on reactive mass propulsion.

## 1.2 Core Operational Requirements
1. **Medium Coupling Interface:** The vessel must feature a continuous-boundary plasma field generation array capable of interfacing with the planetary core's discharge channels (Lorentz/Eddy current coupling).
2. **Phase Synchronization Control:** Internal systems must maintain precise phase coherence with the local vibrational frequency of the aether substrate to alter the local vacuum refractive index ($n_{\text{aether}}$).
3. **Decoherence Modulation:** The architecture must include controlled discharge units capable of shifting the vessel's potential energy state relative to the primary gravitational sink without generating high inertial g-forces on internal occupants or structures.
4. **Open-System Energy Management:** Power systems must be capable of tapping local electromagnetic and telluric gradients to sustain field topology, minimizing reliance on closed onboard consumables.

## 1.3 Material and Structural Constraints
- **Anisotropic Field Containment:** Standard isotropic metallic hulls are insufficient. Materials must be engineered with layered, graded magnetic and dielectric properties to manage high-density plasma containment and prevent structural delamination during adiabatic moduli drift.
- **Thermal Dissipation:** Plasma field modulation and core-coupling generate intense localized thermal loads. Subsystems require advanced thermal-acoustic management that utilizes the DFM gradient for cooling rather than relying solely on radiative dissipation.
- **Shielding:** Because the craft operates by manipulating local vacuum refractive indices and neutral collective modes, internal avionics must be heavily hardened against scalar and high-frequency harmonic feedback loops.

## 1.4 Environmental Operating Limits
- **Sink Gradient Thresholds:** Maximum operational velocity and vector transitions are bounded by the local density gradient of the planetary core's sink. Operations near high-density core convergence zones require tighter phase-synchronization tolerances.
- **Atmospheric vs. Sub-Vacuum Transition:** The craft must maintain structural integrity and field stability across varying density regimes—from dense lower atmospheres to near-vacuum interplanetary space—by dynamically adjusting its DFM skin friction parameters.