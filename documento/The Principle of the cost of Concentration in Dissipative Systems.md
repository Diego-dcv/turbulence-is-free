
---

# THE PRINCIPLE OF THE COST OF CONCENTRATION

## IN DISSIPATIVE SYSTEMS

### Falsification, limits, and cross-domain applications

—
Based on computational evidence independently replicated by four AI models (Claude, ChatGPT, DeepSeek, Grok)

Diego-dcv
With the collaboration of Claude (Anthropic), ChatGPT (OpenAI), DeepSeek and Grok (xAI)
February 2026

> “In dissipative systems, redistribution is free — it requires no external work. Concentration has a price that grows without bound.”
> — Derived from this research 

---

## 0. Background

This document continues a previous work (“On the regularity of Navier–Stokes in 3D: An energetic–variational hypothesis”, February 2026) in which, starting from a dialogue between an architect and an AI, a specific conjecture was proposed: in the Navier–Stokes equations, the energetic cost of concentrating vorticity in a region of scale (L) diverges as (L \to 0), which would make blow-up (finite-time singularity) energetically impossible. 

To test that conjecture, a simplified computational experiment was designed (a diffusion “toy model” on networks) and distributed to four independent AI models with instructions to implement it, run it, and report results. All four AIs confirmed the central hypothesis within the model, adding nuances and critiques that significantly enrich the analysis. 

In this second document we take a different step: we provisionally assume the hypothesis to be true and attempt two things. First, to falsify it: systematically identify conditions under which it fails or reverses, in order to delimit its domain of validity. Second, to apply it: explore what implications the underlying principle might have in fields beyond fluid mechanics, if it were truly general. 

**Fundamental distinction.** This document concerns the Principle of the Cost of Concentration (PCC) as a general heuristic principle for dissipative systems, supported by simulations in a simplified model (linear diffusion on a network). The conjecture that the PCC implies 3D Navier–Stokes regularity is a derived, speculative hypothesis that would require (a) showing that the PCC survives in the presence of nonlinearity and (b) formally constructing the functional (C(L)) mentioned in the previous document. The reader must distinguish at all times between what the toy model supports and what remains an open research program. 

---

# PART I — THE PRINCIPLE

## 1. Statement

**Principle of the Cost of Concentration (PCC).** In a dissipative system with sufficient connectivity, the energetic cost of maintaining a concentrated state (energy localized in a few nodes or regions) is strictly greater — and grows without bound — than the cost of maintaining a distributed state (energy spread out). Redistribution is the minimum-cost state; concentration requires continuous external injection whose cost grows with the system’s viscosity (diffusion rate). 

The principle has three components:

1. **Thermodynamic component (Roger Penrose):** the distributed state is statistically more probable because there are incomparably more microscopic configurations compatible with it than with the concentrated state. 

2. **Energetic component (Jean Leray):** in dissipative systems, total energy decreases monotonically. The “budget” available for concentration is finite and keeps shrinking. 

3. **Structural component (architectural analogy):** the system’s internal structures (vortices in fluids, stresses in structures, intermediate nodes in networks) are mechanisms of self-regulation that redistribute energy to prevent collapse, not symptoms of collapse. 

---

## 2. Computational evidence: four independent replications

The experimental protocol was distributed to four AIs, with none of them knowing the others’ results. Each implemented the code independently, with slightly different parameters: 

| AI       |   N | Runs | Ratio (ν=0.01) | Ratio (ν=0.1) | Ratio (ν=0.5) | Confirms?    |
| -------- | --: | ---: | -------------: | ------------: | ------------: | ------------ |
| Claude   |  30 |    1 |           ~10² |          ~10³ |          ~10⁴ | Yes          |
| ChatGPT  |  70 |  5–8 |         ~2×10⁴ |         ~10¹³ |       ~2×10¹⁴ | Yes          |
| DeepSeek | 100 | 5–10 |      Variable* |     Variable* |     Variable* | Yes (p>0.12) |
| Grok     |  80 |    3 |           ~10² |          ~10⁴ |          ~10⁶ | Yes (ν>0.01) |

(*) DeepSeek varied connectivity (p) in addition to (\nu). For (p = 0.15) (standard protocol), its ratios range from ~10² (low ν) to ~10⁴ (high ν). For (p < 0.10), the ratio can fall below 1. 

**Important methodological note:** the differences in orders of magnitude across AIs (10² vs. 10¹³) come from different definitions of (cost_B): standard deviation vs. L1 norm, averaging window of 50 vs. 100 steps, etc. When ChatGPT reformulated using energetic metrics (control work vs. actual dissipation), ratios drop to ~10³–10⁵, which is the more reliable range. The extreme values (10¹³) are artifacts of a (cost_B) that tends to zero “by construction.” What is robust is not the absolute numbers, but two qualitative facts: (1) the ratio is always ≫ 1 in the regime of interest, and (2) it increases monotonically with (\nu). 

---

# PART II — FALSIFICATION

If the hypothesis is scientifically valid, it must be falsifiable. With the help of the four AIs, we identified the conditions under which the principle fails or weakens. These conditions delimit its domain of validity. 

## 3. Failure condition 1: Insufficient connectivity

**Discovered by:** DeepSeek (systematic analysis varying (p)) 

**Finding:** for networks with connection probability (p < 0.10) (approximately), there exists a viscosity window in which the ratio (cost_A/cost_B) drops below 1. That is, concentrating is cheaper than distributing. In the extreme case ((p = 0.05)), the minimum ratio reaches ≈0.6 at (\nu \approx 0.04). 

**Physical interpretation:** when the network has too few connections, energy lacks enough pathways to redistribute. It is like a building with too few beams: loads cannot find alternative routes and remain where they are. In that regime, concentration is “cheap” because diffusion is ineffective — energy has no way out. 

**Critical connectivity (reported by DeepSeek, pending replication):** (p \approx 0.12) for (N = 100). Above this value, the hypothesis holds over the entire (\nu) range. Below it, there exists a failure window. Whether this threshold depends on network size (N) or on the mean degree remains open. 

**Relevance to real fluids:** a fluid is a continuum medium in which each point interacts with all its neighbors in all directions. Connectivity is maximal. This failure mode does not apply to Navier–Stokes, but it is crucial for applications in social, economic, or biological networks with low connection density. 

---

## 4. Failure condition 2: Near-zero viscosity (diffusion rate)

**Discovered by:** Grok and ChatGPT (analysis of extreme limits) 

**Finding:** for (\nu < 0.005\text{–}0.01), the system is “frozen.” Diffusion is so slow that energy barely moves. In Mode A, maintaining concentration costs almost nothing because the system does not “push back” against injection. In Mode B, the residual deviation is practically null. The ratio becomes indeterminate or numerically unstable. 

**Physical interpretation:** in the model, small (\nu) means slow diffusion: energy hardly transfers between nodes. This is a “frozen” system, not because of high viscosity but because of the absence of diffusive dynamics. (Note: in real fluids, small (\nu) corresponds to low viscosity and high Reynolds number — the turbulent regime — which is where the PCC would be strongest. The more direct analogy would be a medium without interactions, such as isolated particles or an ultra-rarefied gas.) 

**Relevance to NS:** the Millennium Problem assumes (\nu > 0). In our model, (\nu) is the diffusion rate (analogous to viscosity); the failure occurs as this rate tends to zero, i.e., when the system loses its redistribution mechanism. In a real fluid with (\nu > 0), this regime is not reached. 

---

## 5. Failure condition 3: Absence of nonlinearity

**Identified by:** ChatGPT (methodological critique) 

**Argument:** the network diffusion model is linear. In a linear system, blow-up is structurally impossible: diffusion always smooths. Navier–Stokes has a nonlinear term — advection ((u \cdot \nabla)u) — that can transfer energy to small scales (cascade) and potentially concentrate vorticity. Our model does not capture that mechanism. 

**Partial counterargument:** if the principle holds even without cascade (in the linear model), it is reasonable to hypothesize that cascade would reinforce it rather than weaken it — because cascade is precisely a mechanism that redistributes energy toward small scales, where viscosity dissipates it. However, this is not proven and is the most serious critique of the scope of our experiment. 

**Suggested line of work (ChatGPT):** implement a shell model (GOY or Sabra) that includes a conservative nonlinear term (energy cascade across scales) in addition to the dissipative term. Measure whether the principle survives in the presence of nonlinearity. This would be the critical test. 

---

## 6. Failure condition 4: Local vs. global concentration

**Identified by:** Claude (theoretical analysis) and ChatGPT (formal critique) 

**Argument:** total system energy decreases (Leray, 1934), but this does not prevent local concentration. A river loses global energy while forming an intense whirlpool at a point. In gravitation (Penrose), mass concentration increases entropy (a black hole is maximum entropy). If the kinetic energy of a fluid behaved like gravity rather than like heat, concentration could be thermodynamically favorable. 

**State of the question:** everything suggests that fluid kinetic energy behaves like thermal energy (it disperses), not like gravity (it concentrates). But “everything suggests” is not a proof. This remains an open frontier. 

---

## 7. Summary of failure conditions

| Failure condition    | Critical parameter   | Applies to real fluids?   | Applies to other fields? | Severity |
| -------------------- | -------------------- | ------------------------- | ------------------------ | -------- |
| Low connectivity     | (p < 0.12)           | No (maximal connectivity) | Yes (critical)           | High     |
| Near-zero viscosity  | (\nu < 0.005)        | No ((\nu > 0) always)     | Yes (“frozen” systems)   | Low      |
| Lack of nonlinearity | linear model         | Yes (critical)            | Partially                | High     |
| Local concentration  | gravity-like analogy | Open                      | Open                     | Unknown  |

The conclusion of this section is nuanced: the PCC is robust within its domain of validity (sufficient connectivity, positive viscosity, dynamic regime), but it has clear and well-identified limits. The most serious frontier is the absence of nonlinearity in the current model, which should be addressed in the next experimental phase. 

---

# PART III — APPLICATIONS

If the PCC is general — if it applies to any dissipative system with sufficient connectivity — the implications are cross-domain. We present six fields in which the principle has a direct translation, with domain-specific parameters and falsifiable predictions. 

## 8. Cellular biology: ion pumps

**Analogy:** the Na⁺/K⁺ ATPase pump is our Mode A operating in every cell. The human body spends between 20% and 30% of its basal energy exclusively on maintaining ionic concentration gradients across cell membranes. If pumps stop (ischemia, poisoning), the system equilibrates and the cell dies. 

**PCC translation:** “viscosity” is membrane permeability. “connectivity” is the density of ion channels. The principle predicts that the higher the permeability (more porous membrane), the higher the cost of maintaining the gradient. This matches the clinical observation that cells with damaged membranes (higher permeability) die faster. 

**Falsifiable prediction:** the energetic consumption of ion pumps (measurable via ATP consumption) should grow superlinearly with membrane permeability, not linearly. If it grows linearly, the PCC does not apply in this domain. 

**Application:** oncology. Tumors maintain a hyper-concentrated metabolism (Warburg effect). Therapies that increase cellular “viscosity” (transporter inhibitors) would force the tumor to spend more energy to maintain its metabolic concentration. 

---

## 9. Neuroscience: focused attention vs. mind-wandering

**Analogy:** sustaining attention on a task (Mode A) has a measurable metabolic cost. The brain’s default state (default mode network) is mind-wandering: free diffusion of mental activity. The brain “prefers” distribution. 

**PCC translation:** “viscosity” is synaptic efficacy. “connectivity” is the density of connections between brain areas (connectome). The principle predicts that in poorly connected neural networks (low (p)), maintaining a focus may be cheaper: this would help explain why epileptic foci arise in regions with abnormal connectivity. 

**Falsifiable prediction:** cerebral glucose consumption (measurable by PET) during sustained-attention tasks should grow superlinearly with task duration, not linearly. “Willpower depletion” would be the manifestation of the rising cost of concentration. 

---

## 10. Economics: market regulation

**Analogy:** a central bank that fixes an exchange rate (Mode A) continuously injects currency to maintain an artificial “price concentration.” Letting the currency float (Mode B) allows natural redistribution of supply and demand. 

**PCC translation:** “viscosity” is the speed of information transmission and market liquidity. “connectivity” is the number of participants and interconnection between markets. The principle predicts that in globalized markets (high connectivity, high liquidity), maintaining an artificial price is vastly more costly than in isolated markets. 

**Falsifiable prediction:** the cost of FX interventions (measurable in reserves burned per day) should grow superlinearly with the liquidity of the intervened market. Historical datasets: Swiss franc crisis (2015), Bank of Japan interventions (2022–2024), yuan peg. 

**Failure condition (DeepSeek):** in very illiquid markets (low (p)), intervention can be cheaper than natural volatility. This explains why price controls persist in isolated economies but fail in open ones. 

---

## 11. Sociology: polarization and propaganda

**Analogy:** maintaining a homogeneous opinion in a population (Mode A: propaganda, censorship) requires continuous resource injection. Letting opinions diffuse freely (Mode B) produces diversity — the “turbulent” but stable state. 

**PCC translation:** “viscosity” is the frequency and intensity of social interactions. “connectivity” is the density of the social network. Digital social networks drastically increased connectivity and also viscosity (the speed at which ideas diffuse). Under the PCC, this should make propaganda more expensive, not cheaper. 

**Apparent paradox:** social networks seem to facilitate polarization rather than prevent it. But polarization is not concentration at one point — it is concentration at two opposing points. The mechanics differ: recommendation algorithms act as continuous “injection pumps” that maintain concentration. Without algorithms (no injection), the PCC predicts diversity would reassert itself. 

**Falsifiable prediction:** during periods when recommendation algorithms are disabled or weakened (regulatory changes, prolonged outages), measured polarization should decrease. Conversely, more aggressive algorithms should correlate with higher cost of maintaining consensus. 

---

## 12. Communication networks: centralization vs. distribution

**Analogy:** prioritizing traffic toward a central node (QoS, Mode A) versus distributing it evenly (best effort, Mode B). 

**PCC translation:** “viscosity” is bandwidth. “connectivity” is network meshing. The principle predicts that in dense networks (Internet backbone), prioritizing a flow is extremely costly because the network reroutes traffic through alternative paths. In poorly meshed networks (rural zones, low (p)), prioritization can be more efficient. 

**Direct application:** net neutrality policy. The PCC suggests network neutrality (Mode B) is energetically more efficient than prioritization (Mode A) in dense networks, but not necessarily in sparse ones. 

---

## 13. Ecology: biodiversity vs. monoculture

**Analogy:** sustaining a monoculture (biomass concentrated in one species) requires continuous injection: pesticides, fertilizers, irrigation. Letting the ecosystem evolve freely produces biodiversity (distributed state) at lower cost. 

**PCC translation:** “viscosity” is the interaction rate among species (predation, competition, symbiosis). “connectivity” is the complexity of the food-web network. 

**Falsifiable prediction:** total energetic cost (agricultural inputs) of a monoculture per unit biomass produced should grow over time (the land “pushes back” increasingly against concentration), whereas that of a polyculture should stabilize or decrease. Comparable agronomy data exist. 

**Failure condition:** very simple ecosystems (islands, deserts; low (p) in the trophic network) where a dominant species can persist at low cost. 

---

# PART IV — SYNTHESIS

## 14. A principle with a name

Across this work, by a non-conventional route, we have arrived at something that resembles a general principle: 

In any dissipative system with sufficient connectivity, energy redistribution is the minimum-cost state. Concentration requires external injection whose cost grows superlinearly with the system’s diffusion rate. Internal structures (vortices, stresses, intermediate nodes) are mechanisms of self-regulation, not symptoms of instability. 

In a sense, this principle is the dynamic version of the second law of thermodynamics. The second law says equilibrium is the most probable state. The PCC adds: moving away from equilibrium has a cost that grows with the system’s ability to redistribute. 

---

## 15. What is missing

**For mathematics (Navier–Stokes):** formally prove that there exists a concentration-cost function (C(L)) that diverges as (L \to 0) for 3D NS. This requires exploiting the specific structure of NS nonlinearity, which Terence Tao’s averaged equations do not have. This is the Millennium Problem. 

**For the computational model:** introduce nonlinearity (GOY/Sabra shell model or an advective term on a graph) and verify whether the PCC survives. This is the next experimental step and is feasible with modest resources. 

**For applications:** calibrate the model with real data in each domain (central-bank reserves, cellular ATP consumption, polarization metrics on social networks, agricultural inputs) and verify empirically whether the superlinear relationship between cost and diffusivity holds. 

---

## 16. How this work was done

This document is the result of an unusual process that deserves to be recorded:

An architect (Diego-dcv), with a physical-structural intuition, began a conversation with an AI (Claude) about Navier–Stokes. The conversation produced, along an unplanned path — via analogies with building structures, Penrose’s second law thermodynamics framing, Zeno’s paradox, and the practical experience of skimming fat from broth — a hypothesis that could be formulated and tested. 

An experimental protocol was designed and distributed to four different AIs without any of them knowing the others’ results. All four confirmed the hypothesis with their own nuances: ChatGPT was the most critical (it identified the absence of nonlinearity), DeepSeek the most meticulous (it found the critical connectivity), Grok the most intuitive (it proposed the strongest biological applications), and Claude provided the theoretical framework and synthesis. 

No single participant — neither the human nor any AI — would have produced this result alone. The architect would not have had access to the technical literature. The AIs would not have generated the structural analogy, the connection to Zeno, nor the reframing of blow-up as a “failure of self-regulation.” The result is genuinely collaborative and interdisciplinary. 

—
Contact: i-arquitectura.es 

---

# Annex A: Experimental protocol

Protocol distributed to the four AIs (verbatim text):

> “Generate a random network of N nodes (connection probability 0.15). Total energy = 1. At each step, diffuse energy among neighbors (transfer = ν × difference × 0.1). Mode A: inject energy to maintain 80% in one node; measure cost = energy injected. Mode B: let it evolve freely toward equilibrium; measure cost = residual deviation × 0.01. Run 500 steps in each mode. Vary ν from 0.01 to 0.5. Report the ratio cost_A/cost_B as a function of ν.” 

---

# Annex B: References

* Leray, J. (1934). *Sur le mouvement d’un liquide visqueux emplissant l’espace*. *Acta Mathematica*, 63, 193–248. 
* Caffarelli, L., Kohn, R. & Nirenberg, L. (1982). *Partial regularity of suitable weak solutions for the Navier–Stokes equations*. *Comm. Pure Appl. Math.*, 35(6), 771–831. 
* Kolmogorov, A. N. (1941). *The local structure of turbulence in incompressible viscous fluid for very large Reynolds numbers*. *Doklady Akademii Nauk SSSR*, 30(4), 299–303. 
* Tao, T. (2016). *Finite time blowup for an averaged three-dimensional Navier–Stokes equation*. *J. Amer. Math. Soc.*, 29(3), 601–674. 
* Penrose, R. (2004). **The Road to Reality**. Jonathan Cape. 
* Galison, P. (2003). *Einstein’s Clocks, Poincaré’s Maps: Empires of Time*. W. W. Norton. 
* Mandelbrot, B. (1963). *The variation of certain speculative prices*. *The Journal of Business*, 36(4), 394–419. 
* Nahmod, A., Pavlović, N. & Staffilani, G. (2012). *Almost sure existence of global weak solutions for supercritical Navier–Stokes equations*. *SIAM J. Math. Anal.*, 44(6), 4006–4037. 
* Feynman, R. P. (1964). **The Feynman Lectures on Physics, Vol. 1**, Ch. 3. Addison-Wesley. 
* Foias, C. & Temam, R. (1979). *Some analytic and geometric properties of the solutions of the Navier–Stokes equations*. *J. Math. Pures Appl.*, 58, 339–368. 

---

If you want, I can also produce this as a **clean GitHub README.md** (same content, but tightened formatting, consistent terminology for “diffusion rate/viscosity,” and a “Reproducibility” block).
