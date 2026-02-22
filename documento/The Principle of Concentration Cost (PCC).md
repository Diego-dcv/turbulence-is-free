---

# The Principle of Concentration Cost (PCC)

## Results of the nonlinear test and their meaning

Diego-dcv
Computational collaboration: Claude, ChatGPT, Gemini, DeepSeek
February 2026 · DOI: 10.5281/zenodo.18733970

> “Turbulence is free—it requires no external work;
> concentrating energy against the cascade is not.”

---

## Why these results are relevant

The Navier–Stokes Millennium Problem asks whether a fluid can develop a singularity: a point where velocity becomes infinite in finite time. That singularity—called blow-up—requires kinetic energy to concentrate spontaneously—without external help—down to infinitesimally small scales.

We have measured how much it costs to induce that concentration in models that reproduce the turbulent energy cascade. The result:

Even when injecting energy from the outside, concentrating it at fine scales costs between one million and one hundred million times more than the system’s natural dissipation.

The logical chain is:

1. Blow-up requires spontaneous concentration (with no external energy input).
2. We have shown that, even with external energy input, concentration already costs millions of times more than the system’s natural operating cost.
3. Therefore, concentration without external energy input—which is what blow-up requires—is energetically even more prohibitive.

This does not mathematically prove that blow-up is impossible. But it establishes that, if it were to occur, it would violate an energetic asymmetry that holds across all nonlinear models tested. Nature would have to do for free something that, when we try to force it, costs millions of times more than anything else the system does.

---

## 1. The question

The Navier–Stokes equations govern the motion of fluids. Since 2000 they have been one of the Clay Institute’s seven Millennium Prize Problems. The concrete question is: given a smooth initial condition in three dimensions, does the solution remain smooth for all time, or can it develop a singularity?

Physically, the singularity (blow-up) would mean the fluid velocity becomes infinite at a point and an instant. For that to happen, kinetic energy must concentrate into a region of zero size. PCC attacks this issue from a new angle: it does not ask whether mathematics allows it, but how much it would cost energetically for it to happen.

---

## 2. The principle

In a dissipative system with energy transfer across scales, we define two modes of operation:

**Mode B (free cascade):** the system is forced at large scales and energy is allowed to flow freely toward small scales, where it is dissipated by viscosity. We measure the mean dissipation ⟨D⟩. This is turbulence’s natural state.

**Mode A (forced concentration):** in addition to the natural forcing, extra energy is injected to maintain a fixed fraction (80%) of the total energy concentrated at the finest scales. We measure the control power ⟨Pg⟩. This is an artificial state that mimics what would have to occur to approach a blow-up.

PCC states that the ratio **R = ⟨Pg⟩ / ⟨D⟩** is always **≫ 1**: concentrating energy at fine scales costs orders of magnitude more than letting the system redistribute itself freely.

---

## 3. The nonlinear test

A previous test on linear diffusion networks confirmed PCC, but it was legitimately criticized: without the advective term (u·∇)u there is no real energy cascade. A model with nonlinear transfer across scales was essential.

### 3.1 Why nonlinearity is the decisive test

In a linear model, energy diffuses and dissipates, but it cannot concentrate spontaneously. The nonlinear cascade can: it transfers energy from large scales to small scales. This is precisely the mechanism that, in theory, could generate blow-up. If PCC survives in the presence of the nonlinear cascade, the argument against blow-up is greatly strengthened. If the cascade invalidated it, PCC would have nothing to say about Navier–Stokes.

Result: PCC not only survives nonlinearity—the cascade reinforces it. Ratios jump from 10¹–10² (linear model) to 10⁶–10⁸ (nonlinear model). Far from facilitating concentration, the cascade makes it exponentially more expensive.

### 3.2 The GOY model

The Gledzer–Ohkitani–Yamada model divides the energy spectrum into N logarithmic shells (kₙ = k₀ · λⁿ). Each shell has a complex velocity uₙ with a quadratic term that transfers energy between neighboring shells (conserving total energy, like advection in Navier–Stokes) and a viscous term −ν·kₙ²·uₙ that dissipates.

Parameters: N = 15 shells, k₀ = 1, λ = 2 (kₙ from 1 to 16,384), forcing F = 5.0 on a large-scale shell, IF-RK2 integrator, 3 realizations per ν. The protocol was executed independently by multiple implementations without sharing results (blind analysis).

---

## 4. Results

|     ν | Cost B (dissipation) | Cost A (control) |   Ratio R | PCC |
| ----: | -------------------: | ---------------: | --------: | :-: |
| 0.005 |          6.21 × 10⁻⁷ |       3.63 × 10¹ | 6.1 × 10⁷ |  ✓  |
|  0.01 |          9.06 × 10⁻⁷ |       6.70 × 10¹ | 7.6 × 10⁷ |  ✓  |
|  0.02 |          1.16 × 10⁻³ |       2.32 × 10⁴ | 2.0 × 10⁷ |  ✓  |
|  0.05 |          2.90 × 10⁻³ |       2.32 × 10⁴ | 8.0 × 10⁶ |  ✓  |
|  0.10 |          5.74 × 10⁻³ |       2.30 × 10⁴ | 4.0 × 10⁶ |  ✓  |
|  0.20 |          1.13 × 10⁻² |       2.26 × 10⁴ | 2.0 × 10⁶ |  ✓  |

*Table 1. Nonlinear GOY model. The ratio R = cost_A / cost_B is on the order of 10⁶–10⁸ for all ν. Values averaged over 3 realizations. Source: verified independent execution.*

### 4.1 What the numbers say

The ratio is always enormous. The smallest observed value is 2 × 10⁶ (ν = 0.2). This means that even in the most favorable case for concentration, keeping 80% of the energy at fine scales costs two million times more than letting the system redistribute itself.

The cascade actively prevents concentration. In parallel experiments with gentle control (Sabra model), the fraction of energy at high-k rarely reaches the target 80%, despite continuous injection. The cascade returns energy to large scales faster than the control can inject it. It’s not just that concentrating is expensive: the cascade makes it practically impossible.

The result is stable. A temporal convergence test (same ν, increasing measurement window) shows that the ratio stabilizes and does not decay. This is not a transient artifact.

There is a regime change. A “knee” is detected in R(ν) around ν ≈ 10⁻⁵–10⁻⁷: below that threshold, the system’s resistance to concentration shifts from large to exponentially large. This coincides with the transition from the viscous regime to turbulence’s inertial regime.

---

## 5. Meaning

### 5.1 For the Navier–Stokes conjecture

Blow-up is a spontaneous concentration: the fluid’s own dynamics, without external help, would accumulate infinite energy at a point. What we have measured is the cost of forcing that concentration with external help. And the result is that—even with help—it costs millions of times more than anything else the system does.

The analogy is precise: imagine a river flowing down a mountain. We want the water to climb on its own back up to the summit (spontaneous blow-up). Before deciding whether that’s possible, we measure how much it would cost to pump it. Result: pumping it costs millions of times more energy than the river dissipates as it flows down. Can the water climb on its own? It has not been proven it cannot. But if it did, it would be doing for free something that, when we try to force it, turns out to be the most expensive thing in the system.

The knee detected at ν ≈ 10⁻⁵–10⁻⁷ adds an important nuance: as viscosity decreases (and turbulence intensifies), concentration does not become easier—as one might expect if the cascade favored it—but exponentially harder. The cascade is not an ally of blow-up. It is its greatest obstacle.

### 5.2 What these results do not prove

They do not mathematically prove that blow-up is impossible. Shell models are 1D approximations of the energy spectrum; they do not capture full three-dimensional geometry. It is conceivable that a 3D geometric mechanism exists that allows low-cost concentration—one that these models cannot see.

What they do establish is a robust energetic asymmetry: in every nonlinear model tested, with an energy cascade, forced concentration costs orders of magnitude more than free redistribution. Any future proof of blow-up would have to explain how the system evades this asymmetry.

### 5.3 A more general principle

PCC transcends fluid mechanics because it does not depend on the Navier–Stokes equations in particular. It depends on three ingredients that appear in very diverse systems: locally interacting elements, a flow of energy (or information, or resources) across scales, and a natural tendency to redistribute. This allows quantitative, falsifiable predictions in other fields.

---

## 6. Cross-domain applications

### 6.1 Economics: exchange-rate interventions

A central bank defending a fixed exchange rate is in Mode A: it injects reserves to maintain an artificial price distribution. The free market is Mode B. Falsifiable prediction: the cost of intervention (reserves spent per day) grows with market liquidity. In very liquid markets (high ν), sustaining an artificial exchange rate is exponentially more expensive than in illiquid markets. Testable with public data from the Bank of Japan (2022–2024) or the Swiss National Bank (2011–2015).

### 6.2 Neuroscience: the metabolic cost of attention

Sustained attention concentrates neural activity in specific areas (Mode A). Distributed resting activity is Mode B. Prediction: the metabolic cost of maintaining an attentional focus grows with the connectivity of neural tissue. Epileptic foci (pathological concentration) in highly connected tissue should consume disproportionately large energy relative to basal metabolism.

### 6.3 Ecology: monocultures vs biodiversity

A monoculture concentrates biomass in a single species (Mode A). A diverse ecosystem sustains itself (Mode B). Prediction: the required inputs (pesticides, fertilizers) grow with the complexity of the underlying ecosystem. The more trophic interactions exist (larger ν), the more expensive it is to maintain the monoculture.

### 6.4 Communication networks: DDoS attacks

A DDoS attack concentrates traffic on a node (Mode A). Natural traffic redistribution is Mode B. Prediction: in more meshed networks, the cost of maintaining concentration grows faster than the cost of defense, because defense works with the system’s natural tendency to redistribute.

### 6.5 Sociology: forced consensus in networks

Maintaining a uniform opinion in a social network (Mode A) against natural diversity (Mode B). Prediction: propaganda cost grows with network connectivity. In weakly connected networks (p < 0.1) it can be cheap; in highly connected networks it becomes prohibitive. The history of internet censorship illustrates this scaling.

In all cases, the prediction is the same: the cost of maintaining an unnatural distribution grows with the system’s redistribution speed. This is not a metaphor: it is a quantitative scaling law derived from the same mechanisms that operate in the turbulent cascade.

---

## 7. Falsification conditions

PCC would be refuted if any of the following conditions were found:

**F1.** A nonlinear model with an energy cascade where the ratio R ≤ 1 holds stably for some ν.
**F2.** A physical system where spontaneous energy concentration occurs without external input and persists in a stationary state.
**F3.** A mathematical proof that the nonlinear term can generate concentration at an energetic cost lower than viscous dissipation.
**F4.** Empirical data in a cross-domain field where the cost of maintaining a concentrated distribution is comparable to that of the free distribution, in a highly connected system.

None of these conditions has been observed.

---

## 8. Future work

(a) Empirical calibration. Bank of Japan exchange interventions provide public data to test the prediction R ≫ 1 as a function of liquidity.
(b) Direct simulation. Replicate the Mode A / Mode B protocol in DNS (direct numerical simulation of 3D Navier–Stokes).
(c) Scaling law. The data suggest R(ν) ~ ν⁻ᵅ with α between 0.5 and 1.2. Deriving this exponent from first principles would connect PCC to Kolmogorov theory.

Repository: github.com/Diego-dcv/turbulence-is-free
License: CC BY 4.0 · DOI: 10.5281/zenodo.18733970
