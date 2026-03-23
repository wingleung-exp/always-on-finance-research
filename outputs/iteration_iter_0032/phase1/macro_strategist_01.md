# Deglobalization, Supply Chain Rewiring, & Trade Fragmentation — New Keynesian Macro Strategist Analysis

## MACRO REGIME ASSESSMENT (Framing Context)

Deglobalization must be analyzed through the New Keynesian lens as a **persistent negative supply shock**—analytically distinct from the transitory supply disruptions of 2021-22. In the canonical NK Phillips Curve (π_t = βE_t[π_{t+1}] + κx_t + u_t), deglobalization operates through the cost-push shock term (u_t), but critically, if agents update beliefs about the *persistence* of the shock, it also shifts the expectations term (βE_t[π_{t+1}]), creating a compounding inflationary mechanism. The central challenge for monetary policy is that a negative supply shock simultaneously raises inflation and lowers potential output—placing the central bank on the "wrong" side of the divine coincidence, where stabilizing inflation requires accepting a larger output gap.

The current phase represents what I characterize as **"structural supply-side reconfiguration at full employment"**: the economy is operating near potential (output gap estimate: -0.3% to +0.5% for the US as of Q1 2026), while supply networks are being deliberately rewired through policy choices (tariffs, CHIPS Act, EU Chips Act, defense reshoring mandates). This is historically unusual—most prior episodes of trade fragmentation (1930s Smoot-Hawley, 1970s oil embargoes) occurred either during recessions or amid clearly identifiable exogenous shocks. The current episode is *policy-chosen* fragmentation during an expansion, which alters the reaction function analysis considerably.

---

## Key Claims

**1. Deglobalization constitutes a permanent leftward shift of the aggregate supply curve, raising the structural inflation floor by 15-40bp on core PCE, with the midpoint estimate of ~25bp additive to the 2.3-2.8% structural floor already identified in the knowledge base.**

**2. The welfare-optimal monetary policy response to deglobalization-driven supply shocks is partial accommodation: the Taylor Rule prescription implies tolerating 15-25bp of additional inflation rather than closing the full supply-shock gap, because the sacrifice ratio for supply-side inflation is 2-3x larger than for demand-side inflation.**

**3. Trade fragmentation generates a persistent positive wedge between tradeable and non-tradeable goods inflation of approximately 0.5-1.5pp, reversing the 1995-2019 pattern where tradeable goods deflation subsidized above-target services inflation.**

**4. The capex cycle associated with reshoring/nearshoring/friendshoring is net inflationary in the medium term (2024-2029) but ambiguously disinflationary in the long run (2030+), creating a temporal mismatch that current market pricing inadequately reflects.**

**5. Deglobalization interacts with the fiscal stance through a "geopolitical ratchet": defense spending commitments (NATO 2-3% GDP targets), industrial policy subsidies (CHIPS Act $280B, IRA, EU equivalents), and reshoring incentives create structurally higher government spending that is politically non-discretionary, raising r-star by an estimated 15-30bp.**

**6. The tariff transmission mechanism is bimodal, not linear: for tariff rates below ~15%, pass-through to consumer prices is approximately 30-50% (firms absorb via margins); above ~25%, pass-through jumps to 60-90% as margin compression becomes unsustainable, creating a nonlinear inflation response function.**

**7. Global trade fragmentation into competing blocs (US-allied, China-aligned, non-aligned) reduces the effective labor supply available to advanced economies by approximately 15-25%, equivalent to a permanent negative labor supply shock that raises the NAIRU by 10-25bp.**

**8. The correlation regime between bonds and equities is structurally altered by deglobalization: supply-shock dominance implies positive bond-equity correlation (both sell off simultaneously), reducing the diversification benefit of 60/40 portfolios and raising the equity risk premium by 30-50bp.**

---

## Evidence & Reasoning

### Claim 1: Structural Inflation Floor Shift (+15-40bp)

The New Keynesian framework decomposes the deglobalization inflation channel into three transmission mechanisms:

**a) Direct cost channel (10-20bp):** Reshoring production from low-cost to higher-cost locations raises unit labor costs. The Mundell-Fleming open-economy IS-LM framework predicts that trade barriers operate like a negative terms-of-trade shock—domestic consumers pay more for the same basket. Empirical evidence from Amiti, Redding, and Weinstein (2019, *Journal of Economic Perspectives*) estimates the 2018-19 US tariffs produced 0.3-0.8pp direct CPI impact. Current tariff structures, if sustained at effective rates of 10-20% (weighted average), imply 0.2-0.5pp direct price-level effect, which translates to approximately 10-15bp annual inflation if tariff escalation continues at the pace observed since 2023.

**b) Supply chain redundancy cost (5-15bp):** The shift from just-in-time to just-in-case inventory management and from single-source to multi-source supply chains raises steady-state inventory costs by an estimated 3-8% of COGS for manufacturing firms (McKinsey Global Institute, 2023; Bonadio et al., 2021, *QJE*). In the NK framework, this is modeled as a permanent increase in the marginal cost parameter in the firms' pricing problem, which feeds directly into the Phillips Curve slope.

**c) Reduced competition channel (5-10bp):** Blanchard and Giavazzi (2003) demonstrate that trade openness reduces firm markups through import competition. The reverse—trade fragmentation—raises equilibrium markups. With import penetration from China declining from ~22% of US goods imports (2017) to ~14% (2025 est.), the competitive pressure on domestic firms' pricing has meaningfully diminished. The markup channel is slower-acting but more persistent than the direct cost channel.

**Interaction with existing KB:** The `structural_inflation_shift` concept estimates 10-20bp from deglobalization/tariffs. My estimate of 15-40bp is modestly wider because I include the markup channel and supply-chain-redundancy cost that the prior estimate appears to omit. The central tendency is consistent.

### Claim 2: Welfare-Optimal Partial Accommodation

The divine coincidence breaks down under supply shocks (Blanchard and Galí, 2007, *AER*). In the standard NK model with cost-push shocks, the optimal policy rule is:

x_t = -(κ/ε) × u_t

where ε is the weight on output stabilization relative to inflation stabilization, and κ is the Phillips Curve slope. For plausible calibrations (κ ≈ 0.03, ε ≈ 0.05), the optimal policy *partially* accommodates the supply shock—accepting ~60% of the inflation impulse and closing only ~40% of the output gap.

The practical implication: the Taylor Rule prescription for a 25bp supply-side inflation shock is a rate increase of approximately 15-20bp (using Taylor's original coefficient of 1.5 on inflation), compared to 35-40bp if the same inflation were demand-driven. The sacrifice ratio—the cumulative output loss per percentage point of disinflation—is empirically 2-3x larger for supply-side inflation (Ball, 1994; Cecchetti and Rich, 2001) because tight monetary policy cannot restore the lost supply; it can only destroy demand to offset the price impact.

**Policy assessment:** The Fed's current stance—maintaining restrictive real rates while signaling data-dependence—is broadly consistent with partial accommodation, but the risk is that the reaction function does not explicitly distinguish supply-side from demand-side inflation. If realized inflation prints reflect deglobalization pass-through (supply) but are treated as demand overheating, policy will be excessively tight, generating unnecessary output losses.

### Claim 3: Tradeable vs. Non-Tradeable Wedge Reversal

During 1995-2019, core goods inflation averaged approximately -0.5% annually in the US, while core services averaged +3.0%. This "globalization subsidy" allowed the Fed to deliver 2% headline inflation despite persistent above-target services inflation. The Barro-Gordon framework implies that this subsidy reduced the temptation to inflate, improving central bank credibility at no cost.

Deglobalization reverses this: core goods inflation is now at -1% to +0.5% (per `goods_disinflation_completion`) and trending toward +0.5% to +1.5% as supply-normalization disinflation exhausts itself. If services inflation remains sticky at 3.5-4.5% (per `services_inflation_persistence` in the KB), achieving 2% headline now requires goods *deflation*—which deglobalization is actively preventing.

The wedge calculation:
- 1995-2019: Goods (-0.5%) + Services (+3.0%) ≈ weighted average ~2.0%
- 2026 base case: Goods (+0.5 to +1.0%) + Services (+3.5 to +4.0%) ≈ weighted average ~2.5-3.0%

The structural wedge is approximately 0.5-1.5pp of additional compositional inflation pressure.

### Claim 4: Reshoring Capex Temporal Mismatch

The investment surge associated with reshoring—semiconductor fabs ($50-100B cumulative US investment through 2030), battery plants, critical mineral processing, defense manufacturing—is *demand* in the near term (raising IS curve) and *supply* in the long run (shifting potential output rightward once capacity comes online).

In the Solow-Swan framework, this is a temporary increase in the investment-to-GDP ratio that raises the steady-state capital-output ratio. During the transition path (estimated 3-7 years for semiconductor fabs, 2-4 years for battery plants), the economy experiences:
- Higher aggregate demand (construction employment, equipment orders)
- No offsetting supply increase (plants not yet operational)
- Upward pressure on r-star (higher investment demand competes for savings)

Post-completion, the supply-side benefit materializes—but only if the reshored production is competitively priced. Given that semiconductor production in the US costs 30-50% more than in Taiwan/South Korea (per the `geopolitical_supply_fragmentation_premium` concept in the KB), the long-run supply benefit is ambiguous: more output, but at higher marginal cost.

**Market implication:** The reshoring capex cycle supports short-duration inflationary pressure (2026-2029), which is underpriced in 2y-5y breakevens relative to 10y breakevens. The term structure of inflation compensation should be steeper than current pricing implies.

### Claim 5: Geopolitical Fiscal Ratchet and r-star

The Mundell-Fleming framework predicts that fiscal expansion under flexible exchange rates raises domestic interest rates and appreciates the currency (crowding out net exports). The deglobalization-driven fiscal commitments identified in the KB (`geopolitical_fiscal_constraints`: NATO defense 2-3% GDP, CHIPS Act $280B, EU Chips Act €43B) are effectively *non-discretionary* because they respond to geopolitical imperatives rather than business-cycle management.

This violates the Ricardian equivalence benchmark: even if households are forward-looking, they cannot offset government spending that is driven by security externalities rather than transfer payments. The fiscal multiplier for defense/industrial-policy spending is estimated at 0.6-1.0 (Ramey, 2011, *QJE*; Nakamura and Steinsson, 2014, *AER*), because it represents genuine resource absorption rather than transfers.

**r-star impact:** Using the Laubach-Williams framework, the sustained increase in government investment demand raises r-star by an estimated 15-30bp. This is additive to demographic and productivity effects on r-star and implies that the neutral rate—currently debated in the 0.5-1.5% real range—is biased toward the upper end.

### Claim 6: Bimodal Tariff Pass-Through

Empirical evidence from the 2018-19 tariff episode (Cavallo et al., 2021; Fajgelbaum et al., 2020, *QJE*) demonstrates that pass-through is nonlinear:
- At 10% tariff rates: approximately 30-50% pass-through to retail prices (firms compress margins, source from alternative suppliers, absorb via supply chain adjustments)
- At 25% tariff rates: approximately 60-90% pass-through (margin compression exhausts, alternative sourcing insufficient for differentiated goods)

This creates a threshold effect in the Phillips Curve: small tariff increases produce modest, absorbable inflation, but escalation beyond ~15-20% effective rates triggers nonlinear price adjustment. The inflation response function is convex in the tariff rate.

**Current risk assessment (probability-weighted):**
- Scenario A (50%): Tariffs stabilize at current effective rates (~12-18% weighted average) → 0.2-0.4pp CPI impact, largely absorbed
- Scenario B (30%): Tariff escalation to 25-30% effective rates → 0.6-1.2pp CPI impact, triggers visible inflation print deterioration
- Scenario C (20%): Broad-based 40%+ tariffs (trade war escalation) → 1.5-2.5pp CPI impact, recession risk from demand destruction

### Claim 7: Effective Labor Supply Reduction and NAIRU

The globalization of the 1990s-2010s effectively added approximately 1.5 billion workers to the global labor supply accessible to advanced economy firms (Freeman, 2006). Trade fragmentation into blocs reduces this effective supply. Using a back-of-envelope calibration:

- Pre-fragmentation: ~3.5 billion workers accessible via global supply chains
- Post-fragmentation (US-allied bloc): ~2.5-3.0 billion workers accessible
- Reduction: ~15-25% of effective labor supply

In the expectations-augmented Phillips Curve, this operates as a permanent upward shift in the NAIRU: with less labor market competition from trade, domestic workers' bargaining power increases (consistent with the Kalecki profit-squeeze mechanism identified elsewhere in the KB). The NAIRU shift is estimated at 10-25bp—modest individually but compounding with other structural shifts.

### Claim 8: Correlation Regime and Risk Premia

The existing KB concept (`transitional_oscillating_correlation`) correctly identifies that tariffs/reshoring are supply shocks that drive positive bond-equity correlation. In the NK framework, the sign of bond-equity correlation depends on whether the dominant shock is demand (negative correlation: stocks and bonds move opposite) or supply (positive correlation: both sell off on bad supply news).

If deglobalization becomes the *dominant structural narrative*, the conditional probability of supply-shock-driven macro volatility rises, shifting the ergodic correlation toward positive territory. The Campbell-Shiller decomposition implies that the equity risk premium must rise to compensate for lost diversification benefit. My estimate of 30-50bp ERP increase is calibrated to the 2022 episode, where supply-shock dominance produced simultaneous -20% equities and -15% long bonds.

---

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1. Structural inflation floor +15-40bp | **7/10** | Direction is high-confidence (multiple transmission channels, supported by KB consensus); magnitude range is wide because markup and redundancy channels are harder to calibrate than direct tariff pass-through |
| 2. Optimal partial accommodation | **8/10** | This is a well-established result in NK theory (Blanchard-Galí 2007); the uncertainty is whether the Fed's *actual* reaction function approximates the optimal one |
| 3. Tradeable/non-tradeable wedge reversal | **7/10** | The arithmetic is straightforward and the direction is supported by data; the uncertainty is whether goods inflation settles at +0.5% or +1.5%, which depends on tariff policy path |
| 4. Reshoring capex temporal mismatch | **6/10** | The theoretical logic is clean but the empirical magnitude of the capex cycle is uncertain—actual reshoring investment may disappoint relative to announcements (subsidy-chasing without completion is a real risk) |
| 5. Geopolitical fiscal ratchet (+15-30bp r-star) | **5/10** | The direction is compelling but r-star estimation is notoriously imprecise (Laubach-Williams confidence intervals span ±100bp); isolating the deglobalization component is difficult |
| 6. Bimodal tariff pass-through | **7/10** | Strong empirical support from the 2018-19 episode; the threshold estimate (~15-20%) is approximate but the nonlinearity is well-documented |
| 7. NAIRU shift from labor supply reduction | **4/10** | The theoretical channel is valid but the magnitude is highly speculative; domestic labor markets are not perfectly integrated with global supply chains, so the effective labor supply concept overstates the direct impact |
| 8. Correlation regime shift | **6/10** | The supply-shock logic for positive correlation is theoretically sound and confirmed in 2022; the uncertainty is whether deglobalization becomes the *dominant* shock source vs. one of several competing macro drivers |

**Overall framework confidence: 6.5/10** — The directional story (deglobalization is stagflationary, raises the structural inflation floor, complicates monetary policy, and alters correlation regimes) is high-confidence. The quantitative estimates carry wide confidence intervals because deglobalization is a slow-moving structural process with few clean historical analogues, and the policy path (tariff escalation vs. stabilization) is genuinely uncertain.

---

## Connections to Other Topics

**Inflation Regimes:** Deglobalization is a *first-order input* to the structural inflation shift. The KB's current estimate of 10-20bp from deglobalization/tariffs within the 30-80bp total structural shift should be updated to reflect the wider 15-40bp range once markup and redundancy channels are included. This also connects to `goods_disinflation_completion`: deglobalization is the primary mechanism preventing goods deflation from resuming, which historically offset services inflation.

**Monetary Policy & Taylor Rule:** The partial accommodation prescription directly informs the `fed_reaction_asymmetry` concept. If the Fed fails to distinguish supply-side from demand-side inflation, it will over-tighten relative to the optimal Taylor Rule. This is the central policy risk of deglobalization—not the inflation itself, but the *policy error* in responding to it.

**Credit Cycles & Corporate Credit:** Reshoring capex supports investment-grade credit (new issuance for manufacturing buildout) but raises funding costs via higher r-star. The bimodal tariff pass-through creates credit risk differentiation: firms with pricing power (high pass-through) vs. margin-squeezed firms (low pass-through). This connects to `corporate_credit_quality` from iter_0029.

**Commodity Supercycles:** Deglobalization is one of the structural conditions potentially differentiating the current commodity environment from the `supercycle_narrative_failure` base rate of 0/4. However, the NK framework suggests caution: higher commodity prices still induce supply response (the supply curve has not disappeared), but the response may be slower and more geographically concentrated under fragmented trade.

**Yield Curve & Term Premium:** The reshoring capex temporal mismatch implies *steepener* pressure: near-term inflation from demand (belly of the curve) and long-term uncertainty about supply-side resolution (term premium in the long end). This connects to `yield_curve_shape_inversion_term_premium` from iter_0031.

**Real Estate & Construction:** Reshoring investment competes for construction labor and materials with residential building, potentially exacerbating the housing supply deficit identified in `structural_inflation_shift` (10-20bp housing channel). The channels are not independent—they compound.

**EM FX & Trade:** The `two_tier_em_fx_ai_regime` and `em_tripartite_segmentation` concepts from the KB directly reflect the differentiated impact of deglobalization across emerging markets. Supply chain beneficiaries of nearshoring (Mexico, Vietnam, India for certain sectors) gain, while economies dependent on the old China-hub model lose.

**1966-69 Analogue:** The `first_wave_1966_69_analogue` is relevant because that episode also featured a combination of fiscal expansion and supply-side pressures (Vietnam War spending + emerging wage-price dynamics). The deglobalization overlay makes the current episode *more* supply-constrained than 1966-69, which strengthens the case for a "novel with historical elements" framing over a single-analogue approach.

---

## Open Questions

1. **What is the equilibrium tariff rate?** The entire inflation impact analysis is contingent on where tariff policy settles. A game-theoretic analysis of US-China tariff escalation dynamics is needed—is there a Nash equilibrium, or is this a prisoner's dilemma trending toward mutual escalation? The nonlinear pass-through (Claim 6) makes this question critical: the difference between 15% and 30% effective tariffs is not 2x the inflation impact but potentially 3-4x.

2. **Does reshoring capex actually materialize at announced scale?** Historical precedent suggests that subsidy-driven investment announcements overstate actual completion by 30-50% (Greenstone and Moretti, 2003 on enterprise zones). If reshoring capex disappoints, the near-term demand impulse is smaller but the long-term supply gap persists—a different and arguably worse combination.

3. **How does deglobalization interact with AI-driven productivity?** If AI delivers 0.5-1.5pp productivity growth acceleration (a wide range reflecting genuine uncertainty), it could partially or fully offset the supply-side inflation from deglobalization. The net effect of simultaneous negative supply shock (deglobalization) and positive supply shock (AI) is theoretically ambiguous and empirically unprecedented. This is the *highest-priority open question* for the macro regime.

4. **What is the monetary policy reaction function for supply-side inflation?** The formal NK model prescribes partial accommodation, but does the Fed's revealed preference match? The 2021-22 episode suggests the Fed initially under-reacted to supply shocks (transitory framing) then over-corrected. Will this experience bias them toward excessive tightening in response to deglobalization-driven inflation?

5. **How should we model the transition from "globalized" to "fragmented" equilibrium?** The NK framework is well-suited to analyzing *permanent* regime states but less equipped for the *transition dynamics*. The adjustment path—how quickly supply chains rewire, whether there are hysteresis effects from relationship-specific investments in the old regime—requires a richer model than the standard representative-agent NK setup.

6. **Is the trade fragmentation bilateral (US-China) or genuinely multilateral?** If fragmentation is bilateral with a large non-aligned bloc that trades freely with both sides, the effective supply reduction (Claim 7) is much smaller than if fragmentation produces hard blocs. The `export_ban_contagion` concept from the KB suggests that policy coordination failures can cascade, pushing bilateral fragmentation toward multilateral—but this is a tail risk, not a base case.

7. **What are the second-round effects through exchange rates?** In the Mundell-Fleming framework, tariffs appreciate the domestic currency (improvement in trade balance at given exchange rate → capital inflows to finance investment), which partially offsets the inflationary impact. But if trading partners retaliate with their own tariffs, the exchange rate channel is neutralized, leaving only the pure cost-push inflation. The net exchange rate effect depends on the game-theoretic tariff equilibrium (Question 1).

8. **Nearshoring capex multiplier—what is the empirical estimate?** The KB identifies this as a knowledge gap. My prior is that the fiscal multiplier for reshoring investment is 0.6-1.0 (similar to defense spending), but this has not been econometrically estimated for the current episode. The multiplier matters for both the demand-side inflation impulse and the r-star impact.
