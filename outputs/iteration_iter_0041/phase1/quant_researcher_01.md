# Central Bank Balance Sheets — Statistical & Empirical Evidence Specialist Analysis

## Key Claims

1. **QT term premium effect is bounded at 30-60bp, roughly one-third to one-half the magnitude of QE compression (100-150bp), establishing a fundamental asymmetry.** The KB cites Li-Wei 2023 and Smith-Valcarcel 2023 as identification sources.

2. **The reserve demand curve exhibits a nonlinear kink, with the threshold location unknowable ex ante within a ~$1T band ($2.5-3.5T).** September 2019 and March 2023 are cited as confirming episodes.

3. **Central bank balance sheets exhibit a ratchet effect with a 0% historical base rate for full normalization across 6 QE episodes.** This is the empirical foundation for the permanent expansion thesis.

4. **The basis trade ($800B-$1T at 50-100x leverage) suppresses term premium by 20-40bp and unwinds pro-cyclically during stress.** March 2020 is the sole episode at comparable scale (n=1).

5. **The maturity bifurcation in stock-bond correlation (2Y-SPX negative, 30Y-SPX positive) is diagnostic of supply-driven term premium regimes.** This is testable against rolling correlation data.

6. **Covenant-lite structures produce bimodal default distributions, but this has never been tested through a full credit cycle without policy rescue (n=0).**

7. **Japanese institutional reallocation of $130-200B in foreign bonds would add 15-30bp to UST term premium.** The cross-border transmission elasticity is estimated without identified natural experiments.

8. **The SRF will prevent 2019-style repo dislocations when reserves approach scarcity.** This is an untested counterfactual (n=0 for activation at scale).

## Evidence & Reasoning

**Claim 1 (QT term premium asymmetry):**

CLAIM UNDER TEST: QT raises term premium by 30-60bp vs QE's 100-150bp compression.

EMPIRICAL METHODOLOGY: The cited studies (Li-Wei 2023, Smith-Valcarcel 2023) use event studies and term structure models. The critical identification problem: Treasury issuance roughly doubled during QT2, making clean attribution of observed term premium changes (~100bp total) to QT versus fiscal supply literally impossible with available data. This is a classic omitted variable / confounding problem.

RESULTS: Point estimates of 20-60bp for QT's contribution, but the confidence interval includes zero on the low end and the full 100bp observed move on the high end. The asymmetry claim (QT weaker than QE) is theoretically motivated (Vayanos-Vila preferred habitat, nonlinear reserve demand) but the empirical sample is: QT1 (2017-2019, interrupted by repo crisis) and QT2 (2022-present, confounded by fiscal expansion). **N=2 QT episodes, neither clean.** The claim that QT is definitively weaker than QE cannot be distinguished from the hypothesis that QT effects are simply noisier and harder to identify.

STATISTICAL ASSESSMENT: The directional claim (asymmetry exists) has moderate theoretical support but the magnitude (30-60bp vs 100-150bp) is not well-identified empirically. The KB's confidence of 8 is too high for the data quality. I would assign 5-6 given the identification challenges.

---

**Claim 2 (Reserve scarcity nonlinearity):**

CLAIM UNDER TEST: Reserve demand exhibits a kinked curve with discontinuous stress at the threshold.

EMPIRICAL METHODOLOGY: Two episodes cited — September 2019 (reserves ~$1.5T, 300bp+ intraday repo spike) and March 2023 (aggregate reserves ~$3.0T, distributional stress at regional banks). Copeland-Duffie-Yang (2021) theoretical framework.

RESULTS: The September 2019 episode provides one clean observation of reserve scarcity. But the March 2023 episode was primarily about credit risk (SVB) not aggregate reserve scarcity — reserves were ~$3.0T, well above any scarcity threshold. Conflating these weakens the base rate calculation. The Fed's own $1T uncertainty band ($2.5-3.5T) for the threshold effectively admits that the kink location cannot be estimated with useful precision. This is a regime where the key parameter has a coefficient of variation around 15-20% — and crucially, the consequences of being wrong are discontinuous.

STATISTICAL ASSESSMENT: The *existence* of nonlinearity is well-supported by theory and September 2019 (confidence 8). The *location* of the threshold is fundamentally unidentifiable ex ante (confidence 3-4). The KB's confidence of 8 conflates the existence claim with the location claim.

---

**Claim 3 (Ratchet effect / permanent expansion):**

CLAIM UNDER TEST: Central bank balance sheets never fully normalize after QE episodes.

EMPIRICAL METHODOLOGY: Count the number of QE episodes followed by complete normalization to pre-QE balance sheet/GDP ratios.

RESULTS: 0 out of 6 episodes (Fed QE1-3, Fed QE4/COVID, ECB APP/PEPP, BoJ QQE) have resulted in full normalization. QT2 has reduced the Fed balance sheet by ~25% over 45 months but not to pre-crisis ratios. **Base rate: 0/6 = 0%.** Using a Jeffrey's prior (Beta(0.5, 0.5) updated with 0 successes in 6 trials), the 95% credible interval for the probability of full normalization is [0%, 21%]. Even the upper bound is low.

ROBUSTNESS: However, defining "full normalization" matters enormously. If we define it as returning to pre-GFC reserve levels (~$15-45B), this is structurally impossible given floor-system monetary implementation — the claim becomes trivially true by definition. The more interesting question is whether balance sheets normalize to a structurally justified floor (ample reserves for the floor system + LCR demand). QT2 is ongoing and may achieve this. The ratchet claim is robust to the strong form but weaker for a modified definition.

STATISTICAL ASSESSMENT: Confidence 7-8 for the claim that balance sheets remain permanently larger than pre-episode levels. Confidence 4-5 for the claim that they ratchet upward indefinitely, since the structural floor is increasing for identifiable regulatory reasons unrelated to the ratchet dynamic.

---

**Claim 4 (Basis trade as synthetic QE):**

CLAIM UNDER TEST: Basis trade unwind at current scale ($800B-$1T) would produce systemic stress analogous to or exceeding March 2020.

EMPIRICAL METHODOLOGY: One observation — March 2020 — at scale of $200-300B (one-quarter to one-third of current). Current notional is 3-4x the 2020 level. Brunnermeier-Pedersen liquidity spiral theory provides the mechanism.

RESULTS: **N=1 for unwind at scale.** The 20-40bp term premium suppression estimate lacks an identified natural experiment — it is derived from cross-sectional holdings data and assumed demand elasticities. The scaling argument (3-4x larger → worse outcome) assumes linear or convex scaling of unwind effects, which is plausible but unvalidated. October 2023 provides a partial second observation but at different scale and with different triggers.

STATISTICAL ASSESSMENT: This is a legitimate tail risk but empirically unquantifiable. Claims about specific thresholds or magnitudes are not supportable with n=1. The KB appropriately flags the open question about whether unwind can occur without contagion, but assigns confidence 6.5 to a claim that fundamentally cannot be calibrated. I would assign confidence 5 — directionally correct, magnitude unknowable.

---

**Claim 5 (Stock-bond correlation bifurcation):**

CLAIM UNDER TEST: 2Y-SPX correlation is negative (-0.15 to -0.30) while 30Y-SPX correlation has turned positive (+0.05 to +0.15) during the QT regime, and this bifurcation is diagnostic of supply-driven term premium.

EMPIRICAL METHODOLOGY: Rolling correlations between Treasury returns at different maturities and equity returns. Sample: QT2 period (2022-present).

RESULTS: This is one of the more testable claims in the KB. Rolling 6-month and 12-month correlations can be computed directly. The positive 30Y-SPX correlation of +0.05 to +0.15 is *extremely* close to zero and falls within the range of sampling noise for typical rolling correlation windows. A 12-month rolling correlation estimated from daily data has a standard error of approximately 0.06-0.08. A point estimate of +0.10 is not statistically distinguishable from zero at conventional significance levels (t ≈ 1.2-1.6, p > 0.10).

ROBUSTNESS: The 2Y-SPX negative correlation is more robust and well-established. The 30Y claim, while theoretically motivated, rests on weak statistical evidence. The bifurcation narrative is compelling but the positive long-end correlation may be an artifact of the specific window.

STATISTICAL ASSESSMENT: Confidence 5. The direction is theoretically sensible, but the magnitude of the positive 30Y correlation is not distinguishable from zero in available data. The hedging implications people might draw from this are premature.

---

**Claim 6 (Covenant-lite bimodal defaults):**

CLAIM UNDER TEST: Covenant-lite structures produce bimodal default distributions (either successful refinance or sudden severe distress).

EMPIRICAL METHODOLOGY: The KB notes covenant-lite first-lien loans defaulted at 2.2% cumulative vs 3.8% covenant-heavy through COVID (S&P LCD data). But COVID was tested under "unprecedented policy support, not organic deterioration."

RESULTS: **N=0 full credit cycles without policy rescue for the current generation of covenant-lite structures.** The COVID evidence is contaminated by the largest fiscal/monetary intervention in history. The bimodality claim is mechanistically logical (no maintenance covenants → no gradual deterioration pathway) but entirely untested empirically in the relevant regime. Drawing default rate conclusions from COVID-era data for the next downturn is a textbook case of survivorship bias combined with sample selection on the treatment variable.

STATISTICAL ASSESSMENT: Confidence 4 for the specific distributional claim (bimodality). Confidence 7 for the directional claim that early warning signals are impaired. The KB's 6.0 is reasonable as a blend but should be much more explicit about the n=0 problem.

---

**Claim 7 (BoJ normalization spillovers):**

CLAIM UNDER TEST: 10-15% reallocation of Japanese foreign bond holdings (~$130-200B) would add 15-30bp to UST term premium.

EMPIRICAL METHODOLOGY: Back-of-envelope calculation from holdings data × assumed demand elasticity. No identified natural experiment for the cross-border term premium transmission coefficient.

RESULTS: The holdings data ($1.3T in foreign bonds) is verifiable from BoJ/MoF statistics. The assumed reallocation percentage (10-15%) and the demand elasticity mapping ($130-200B flow → 15-30bp yield impact) are not well-identified. Historical episodes of Japanese repatriation (2011 earthquake, various fiscal year-end effects) are too small and temporary to calibrate multi-hundred-billion dollar sustained flows. The 15-30bp estimate implies a demand elasticity of roughly 10-15bp per $100B of flow — within the range used in academic estimates but with wide uncertainty.

STATISTICAL ASSESSMENT: Confidence 4 for the point estimate. The directional risk (Japanese reallocation would widen UST yields) is well-supported at confidence 7. But the magnitude is essentially a scenario assumption, not an empirical estimate.

## Confidence Assessment

| # | Claim | KB Confidence | My Assessment | Justification |
|---|-------|:---:|:---:|---|
| 1 | QT term premium 30-60bp | 7.5 | 5.5 | N=2 confounded episodes; identification fails |
| 2 | Reserve scarcity nonlinearity (existence) | 8 | 8 | Theory + September 2019 |
| 2b | Reserve scarcity threshold (location) | 8 | 3.5 | $1T uncertainty band = effectively unidentified |
| 3 | Permanent balance sheet expansion | 8 | 7.5 | 0/6 base rate is robust; definition matters |
| 4 | Basis trade systemic unwind risk | 6.5 | 5 | N=1 at scale; magnitude unknowable |
| 5 | Stock-bond correlation bifurcation | 7 | 5 | Positive 30Y correlation ≈ noise at typical CIs |
| 6 | Covenant-lite bimodal defaults | 6 | 4.5 | N=0 full cycles without policy rescue |
| 7 | BoJ reallocation 15-30bp impact | 6.5 | 4 | Demand elasticity assumed, not estimated |
| 8 | SRF effectiveness | 7 | 3 | N=0 activations; pure conjecture either way |

**Pattern**: The KB systematically overstates confidence by 1.5-3 points across most claims. The primary drivers: (a) conflating theoretical plausibility with empirical identification, (b) underweighting small sample problems, (c) treating scenario analysis as estimation.

## Connections to Other Topics

- **Fiscal policy**: The compound duration absorption claim ($2.0-2.6T/year) is inseparable from fiscal deficit trajectories. Any empirical test of QT's term premium effect must jointly model fiscal issuance — the identification problem is that QT and fiscal expansion are occurring simultaneously and through the same channel (net duration supply).

- **Credit markets**: The maturity wall × CLO transmission chain depends on base rate levels, which are set by conventional monetary policy. The QT contribution is second-order relative to the rate level for CLO equity IRR calculations. The KB's emphasis on QT as the binding constraint may be misplaced if rate cuts restore CLO economics.

- **Currency markets**: BoJ normalization effects transmit through JPY appreciation and carry unwind before they affect term premium. The cross-asset transmission sequence matters for timing — currency moves lead, flow reallocation lags by quarters to years.

- **NBFI / financial stability**: The risk migration thesis connects balance sheet policy to regulatory architecture. The empirical gap is severe: we have n=1 for NBFI stress at scale (BoE LDI crisis, 2022) and it occurred in a different institutional/regulatory context.

## Open Questions

1. **The fundamental identification problem**: Can QT's term premium effect *ever* be cleanly estimated given that it always coincides with large fiscal supply changes? If not, the entire quantitative framework for calibrating QT's impact rests on model assumptions rather than empirical identification. This is the most important methodological limitation in the entire KB.

2. **Small-sample problem for tail risks**: Four of the eight highest-priority claims (basis trade unwind, SRF effectiveness, covenant-lite cycle behavior, reserve scarcity threshold) have effective sample sizes of 0-1. No statistical framework can generate reliable inference from these samples. The KB should be more explicit that these are *scenario analyses* and *theoretical predictions*, not empirical estimates.

3. **Non-stationarity**: The financial system is structurally different from the 2017-2019 QT1 period (basis trade 3-4x larger, RRP exhausted, private credit doubled, regulatory landscape changed). Drawing base rates from QT1 for QT2 is questionable. The two "QT episodes" may not be drawn from the same data-generating process.

4. **Multiple comparisons in the maturity wall**: The $900B-$1.5T figure for 2025-2028 is cited without comparison to previous maturity walls that were successfully refinanced. What is the base rate for maturity walls of this relative magnitude triggering actual default cycles vs being resolved through amend-and-extend, rate cuts, or alternative financing? Without this base rate, the claim is unfalsifiable.

5. **Bayesian updating from QT2's continued absence of crisis**: QT2 has proceeded for 45+ months without producing the systemic stress many predicted. Under Bayesian updating, this should *reduce* posterior probability estimates for several tail risk claims. The KB does not appear to incorporate this favorable evidence, suggesting asymmetric updating (weighting stress episodes but not tranquil ones). What is the implied survival function, and how much has 45 months of successful QT shifted our priors?

6. **Out-of-sample validation**: Not a single claim in the KB has been subjected to formal out-of-sample testing. All estimates are in-sample. Given the well-documented tendency for in-sample financial relationships to degrade out-of-sample, this is a significant gap that cannot be resolved with available data but should be flagged as a systematic limitation.
