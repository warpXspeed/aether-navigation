# math/dfm-field-equations.md

# DFM Field Equations & Bridge Calculus

## 1. Purpose
This document establishes the mathematical bridge connecting the global topological state of the foundational scalar substrate ($\phi$) to local macroscopic stress tensors and physical coil-array actuation parameters. It formalizes the transition from Riemann theta functions to the traveling harmonic surface waves (solitons) utilized in the craft architecture.

---

## 2. Global Substrate Foundation ($\phi$-Lattice)
The fundamental substrate $\phi$ is governed by finite-gap compact Riemann surfaces. The macroscopic state vector $\mathbf{z}$ and the global period matrix $\mathbf{\Omega}$ define the field propagation via Riemann theta functions:

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mrow>
    <mi>&#x3B8;</mi>
    <mo stretchy="false">(</mo>
    <mi mathvariant="bold">z</mi>
    <mo>∣</mo>
    <mi mathvariant="bold">&#x3A9;</mi>
    <mo stretchy="false">)</mo>
    <mo>=</mo>
    <munder>
      <mo movablelimits="false">&#x2211;</mo>
      <mrow>
        <mi mathvariant="bold">n</mi>
        <mo>&#x2208;</mo>
        <msup>
          <mi mathvariant="double-struck">Z</mi>
          <mi>g</mi>
        </msup>
      </mrow>
    </munder>
    <mi>exp</mi>
    <mo>&#x2061;</mo>
    <mrow>
      <mo>(</mo>
      <mn>2</mn>
      <mi>&#x3C0;</mi>
      <mi>i</mi>
      <mrow>
        <mo>[</mo>
        <mrow>
          <mfrac>
            <mn>1</mn>
            <mn>2</mn>
          </mfrac>
          <msup>
            <mi mathvariant="bold">n</mi>
            <mi>T</mi>
          </msup>
          <mi mathvariant="bold">&#x3A9;</mi>
          <mi mathvariant="bold">n</mi>
          <mo>+</mo>
          <msup>
            <mi mathvariant="bold">n</mi>
            <mi>T</mi>
          </msup>
          <mi mathvariant="bold">z</mi>
        </mrow>
        <mo>]</mo>
      </mrow>
      <mo>)</mo>
    </mrow>
  </mrow>
</math>

---

## 3. The Dynamic Fluid Medium (DFM) Limit
The Dynamic Fluid Medium is defined strictly as the active kinematic and gradient operating regime of the $\phi$ substrate:

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mrow>
    <mtext>DFM</mtext>
    <mo>&#x2261;</mo>
    <msub>
      <mrow>
        <mrow>
          <mo fence="true" minsize="1.2em">(</mo>
          <mrow>
            <mo>&#x2207;</mo>
            <mi>&#x3D5;</mi>
            <mo>,</mo>
            <msub>
              <mi>&#x2202;</mi>
              <mi>t</mi>
            </msub>
            <mi>&#x3D5;</mi>
          </mrow>
          <mo fence="true" minsize="1.2em">)</mo>
        </mrow>
      </mrow>
      <mtext>local</mtext>
    </msub>
  </mrow>
</math>

The local stress tensor of the DFM (<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>T</mi><mrow><mi>&#x3BC;</mi><mi>&#x3BD;</mi></mrow><mtext>dfm</mtext></msubsup></math>) relates lattice deformation to local pressure and density:

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mrow>
    <msubsup>
      <mi>T</mi>
      <mrow><mi>&#x3BC;</mi><mi>&#x3BD;</mi></mrow>
      <mtext>dfm</mtext>
    </msubsup>
    <mo>=</mo>
    <msub>
      <mi>&#x3C1;</mi>
      <mtext>dfm</mtext>
    </msub>
    <mrow>
      <mo>(</mo>
      <mrow>
        <msub>
          <mi>&#x2202;</mi>
          <mi>&#x3BC;</mi>
        </msub>
        <mi>&#x3D5;</mi>
        <msub>
          <mi>&#x2202;</mi>
          <mi>&#x3BD;</mi>
        </msub>
        <mi>&#x3D5;</mi>
        <mo>-</mo>
        <mfrac>
          <mn>1</mn>
          <mn>2</mn>
        </mfrac>
        <msub>
          <mi>g</mi>
          <mrow><mi>&#x3BC;</mi><mi>&#x3BD;</mi></mrow>
        </msub>
        <msup>
          <mi>g</mi>
          <mrow><mi>&#x3B1;</mi><mi>&#x3B2;</mi></mrow>
        </msup>
        <msub>
          <mi>&#x2202;</mi>
          <mi>&#x3B1;</mi>
        </msub>
        <mi>&#x3D5;</mi>
        <msub>
          <mi>&#x2202;</mi>
          <mi>&#x3B2;</mi>
        </msub>
        <mi>&#x3D5;</mi>
      </mrow>
      <mo>)</mo>
    </mrow>
  </mrow>
</math>

---

## 4. The Bridge Calculus: From Global Phase to Coil Timing
To translate abstract topology into hardware actuation, we map the global phase coordinates $\mathbf{z}$ to the physical multi-phase coil firing sequence. 

Let the toroidal array consist of discrete coil stations indexed by $k$ around the perimeter. The current phase supplied to coil $k$ at time $t$ is defined as a traveling harmonic soliton:

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mrow>
    <msub>
      <mi mathvariant="normal">&#x3A6;</mi>
      <mi>k</mi>
    </msub>
    <mo stretchy="false">(</mi>
    <mi>t</mi>
    <mo stretchy="false">)</mo>
    <mo>=</mo>
    <mi>&#x3C9;</mi>
    <mi>t</mi>
    <mo>-</mo>
    <mi>k</mi>
    <mi mathvariant="normal">&#x394;</mi>
    <mi>x</mi>
    <mo>+</mo>
    <mi>&#x3B1;</mi>
    <mi>sin</mi>
    <mo>&#x2061;</mo>
    <mo stretchy="false">(</mo>
    <mi mathvariant="normal">&#x3A9;</mi>
    <mi>t</mi>
    <mo stretchy="false">)</mo>
  </mrow>
</math>

Where:
- $\omega$ is the base driving frequency.
- $\Delta x$ is the physical spatial separation between adjacent coils.
- $\alpha \sin(\Omega t)$ represents the modulated phase-lock feedback derived from the local DFM density sensor array.

---

## 5. Macroscopic Coupling & Refractive Index Modulation
The effective vacuum refractive index ($n_{\text{aether}}$) is modulated directly by the peristaltic magnetic pressure generated by the traveling wave array:

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mrow>
    <msub>
      <mi>n</mi>
      <mtext>aether</mtext>
    </msub>
    <mo>=</mo>
    <msqrt>
      <mfrac>
        <mrow>
          <msub>
            <mi>K</mi>
            <mtext>dfm</mtext>
          </msub>
          <mo>+</mo>
          <mi>&#x3B2;</mi>
          <mo stretchy="false">&#x2329;</mo>
          <msup>
            <mi>B</mi>
            <mn>2</mn>
          </msup>
          <mo stretchy="false">&#x232A;</mo>
        </mrow>
        <mrow>
          <msub>
            <mi>&#x3C1;</mi>
            <mtext>dfm</mtext>
          </msub>
          <mo>+</mo>
          <mi>&#x3B3;</mi>
          <mo stretchy="false">&#x2329;</mo>
          <msup>
            <mi>E</mi>
            <mn>2</mn>
          </msup>
          <mo stretchy="false">&#x232A;</mo>
        </mrow>
      </mfrac>
    </msqrt>
  </mrow>
</math>

Where $\beta$ and $\gamma$ are coupling coefficients translating electromagnetic energy densities into local $\phi$-lattice modulus variations. This establishes the exact mathematical pathway from coil activation to localized vacuum metric manipulation.
---

## 6. The Bridge Calculus: Riemann Phase Coordinates → Soliton Actuation

### 6.1 The Physical Meaning of the Phase Vector z(t)

The Riemann theta function's phase vector **z** is not abstract geometry. In the DFM
limit, each component of **z** corresponds to a propagating phase mode of the φ-substrate:

  z_j(t) = κ_j · x(t) − ω_j · t + δ_j

Where:
- κ_j is the wavenumber of the j-th lattice mode (spatial structure of the substrate disturbance),
- ω_j is the angular frequency of that mode,
- δ_j is the mode's phase offset relative to the core discharge (J_core).

A craft's coil array does not need to solve the full genus-g theta function in real time.
It needs to inject a *local phase perturbation* into **z**. This is the fundamental
engineering insight: **actuation is a boundary condition on z, not a global computation.**

### 6.2 The Coil Array as a Discrete Phase Injector

Consider a toroidal array of N coil stations. Station k sits at azimuthal angle:

  θ_k = 2πk / N

The array drives a *traveling harmonic perturbation* in the local substrate phase:

  Δz(t, θ_k) = A · cos(ω_s t − m θ_k)

Where:
- ω_s is the soliton drive frequency (the craft's commandable parameter),
- m is the azimuthal mode number (m = 1 gives a single-lobe wave circling the hull,
  the configuration used in the Phase-2 simulation),
- A is the drive amplitude, set by the injected magnetic pressure of the coils.

The wavenumber and frequency of this perturbation are locked by the substrate's own
dispersion relation. For the finite-gap φ-lattice, the linearized dispersion about a
background density ρ_dfm is:

  ω_s² = c_φ² κ_s²  +  ε_gap(κ_s)

Where c_φ = √(K_dfm / ρ_dfm) is the substrate's longitudinal wave speed (note: this is
exactly the quantity whose square root defines n_aether), and ε_gap is the finite-gap
band correction from the Riemann surface structure — the term that carries the lattice's
"memory." At low κ, the gap term dominates and the medium is stiff; at high κ, the
classical fluid limit is recovered. **The craft therefore operates at the κ where
ε_gap is comparable to ω²/c², because that is where the medium is most responsive to
coherent perturbation** — the tuning-fork regime, not the sledgehammer regime.

### 6.3 Amplitude Mapping: Coil Current → Substrate Stress

The drive amplitude A is proportional to the magnetic pressure applied by the coil
array against the local lattice:

  A = λ · (μ₀ / 2) · (I_k / I_ref)² · G(m)

Where:
- I_k is the peak current in station k,
- λ is the φ-coupling coefficient (the proportionality between applied magnetic
  energy density and induced lattice strain — the first experimentally measurable
  target of the benchtop program),
- G(m) is the array geometry factor: G(m) = 1 for the single-lobe mode, falling
  as ~1/m² for higher harmonics (the peristaltic energy-sharing penalty).

The resulting perturbation to the local refractive index follows directly:

  n_aether(x, t) = n₀ · [1 + A · cos(ω_s t − m θ) + O(A²)]

which is precisely the soliton_mod term implemented in the simulation
(vacuum_refractive_index in dfm_steering_sim.py). The simulation's wave_amplitude
parameter is A; its wave_frequency is ω_s. **The bridge is now closed in both
directions: equations → code, and code → equations.**

### 6.4 Steering Force from the Phase Perturbation

The medium-coupled Lorentz force of Section 5, evaluated with the perturbed n_aether,
yields the steering vector:

  F_nav ≈ −V_craft · ρ_dfm · c_φ² · ∇(A · cos(ω_s t − m θ))

Two consequences fall out immediately:

1. **Steering is perpendicular to the wavefront.** The gradient of the cosine
   perturbation points along the propagation direction of the soliton, so the craft
   is pushed along — not against — its own traveling wave. This is the "surfing"
   geometry: the vessel rides the face of the wave it generates.
2. **Thrust scales with A·ω_s·m.** Faster, higher-mode waves give finer vector
   control but demand higher power, setting up the performance envelope that the
   energy-budget derivation (χ) must bound.

### 6.5 The Cavitation Constraint (Dissipation Limit)

Define the rate of change of the local index during a command transition:

  R = |Δn_aether / Δt|

The φ-substrate tolerates perturbation only up to the point where the induced strain
exceeds the lattice's elastic regime. The cavitation threshold is:

  R_max = (c_φ / L_λ) · η_gap

Where L_λ is the soliton wavelength and η_gap is the dimensionless elasticity margin
of the lattice (analogous to the ratio of yield strength to Young's modulus in an
ordinary solid). In the simulation's command profile, the "slip" transition at t = 30
showed R ≈ 4–6 index units per unit time — this must be interpreted as the *upper
demonstration bound*, not an operationally safe rate. The steep monotonic climb in
n_aether after t = 35 would, in a physical medium, be the cavitation-risk zone: the
power ramp must be smoothed so R < R_max at every instant. This constraint belongs
in the flight software as a hard limiter, exactly as drafted in craft/04-test-plan.

### 6.6 The Decoherence Term as a Topological Sector Transition

The potential-well shift of Section 5 is now expressed precisely: the decoherence
factor D is the probability weight that the craft's neutral collective modes have
lost phase-lock with the local z-vector:

  D(t) = 1 − |⟨ψ_craft(t) | ψ_φ(x, t)⟩|²

Detuning (increasing D) does not shut off the sink; it decoheres the phase overlap
between the craft's internal condensate and the substrate mode structure. Because the
sink coupling term is proportional to the coherent overlap, the effective sink
coupling C_s = phase_lock · (1 − D) — recovering the simulation's coupling_factor
function from first principles.

---

## 7. Status of the Bridge

| Bridge Segment | Formalization | Epistemic Status |
| :--- | :--- | :--- |
| Riemann phase **z** → coil timing Δz(t, θ_k) | Section 6.1–6.2 | [Deduced Mechanism] |
| Coil current I_k → drive amplitude A | Section 6.3 | [Inferred Variable — λ needs benchtop measurement] |
| Amplitude A → steering force F_nav | Section 6.4 | [Deduced Mechanism] |
| Command rates → cavitation limit R_max | Section 6.5 | [Speculative Model — η_gap unknown] |
| Decoherence D → sink coupling C_s | Section 6.6 | [Deduced Mechanism] |

**Remaining unknowns requiring experiment:** the coupling coefficient λ and the
lattice elasticity margin η_gap. These are the two numbers the benchtop program
(interferometric refractive test, phase-delay test) is designed to extract. Every
other link in the chain is now closed.

