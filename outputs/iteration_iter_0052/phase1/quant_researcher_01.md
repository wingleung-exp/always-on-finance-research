# AI & Tech Disruption — Statistical & Empirical Evidence Specialist Analysis

## Key Claims

1. **The KB's most robust empirical claims rest on dangerously small samples, and confidence ratings systematically overstate statistical reliability.** Across 80+ concepts, the median evidentiary base is N=2-5 historical episodes, yet confidence ratings of 7-9 are assigned as if these were large-sample findings.

2. **The GPT diffusion lag base rate (15-25% probability of TFP acceleration within 3-5 years) is derived from N=5-6 observations and cannot support the implied precision.** The 95% confidence interval on a binomial proportion from N=5 with 1 success spans approximately 1-54%, rendering the point estimate nearly uninformative.

3. **The value capture base rate (1/6 = 17% infrastructure builders capturing value, adjusted to 25-40%) conflates structurally dissimilar episodes and applies a subjective adjustment that is larger than the base rate itself.** The adjustment from 17% to 25-40% for "hyperscaler vertical integration" is unanchored by any statistical method.

4. **ERP compression at the 10th-15th percentile post-1960 is the strongest predictive signal in the KB, with the largest available sample (N~65 years monthly data), yet the KB underutilizes it by failing to compute the full conditional return distribution.** Historical 5-year forward nominal returns from this ERP percentile average 3-5% annualized — this is the single most statistically defensible claim.

5. **The equity-credit sequencing pattern (3/3 episodes, 83% hit rate cited from 5/6 episodes) is subject to severe selection bias and the reported hit rate is not statistically distinguishable from chance.** A binomial test of 5/6 against a null of 50% yields p=0.11 (one-tailed), failing to reject at conventional significance levels.

6. **Factor crowding metrics (momentum ENB collapse to 25-35, inter-factor correlation tripling) are the most novel empirical contributions but lack out-of-sample validation entirely.** The ENB metric has been computed for only ~3 comparable episodes, and the correlation regime shift has no precedent at this magnitude.

7. **The capex/OCF "kill zone" threshold (>55-65% for 4+ quarters AND ROIC < WACC) is derived from 5 historical analogues, 4 of which are structurally different (debt-funded), reducing the effective sample to N=1 for self-funded entities.** No statistical inference is possible from a single observation.

8. **The "no TFP structural break" claim (confidence 9) is the KB's most defensible finding, but the statistical test applied is inappropriate.** Standard structural break tests (Chow, Bai-Perron) have low power against gradual level shifts, which is precisely the AI productivity transmission mechanism hypothesized.

9. **The stock-bond correlation regime analysis conflates at least three independent drivers (AI capex demand, fiscal dominance, monetary policy) and cannot isolate the AI-specific contribution.** The rolling correlation range of -0.2 to +0.4 post-2022 is well within the historical variation range observed in non-AI periods.

10. **The cross-asset pricing inconsistency framework is the KB's most analytically ambitious construction but commits a fundamental statistical error: treating correlated estimation errors as independent signals.** Equity ERP, bond r*, and credit spread estimates share common input data and methodology, making their "disagreement" partially an artifact of model specification choices.

## Evidence & Reasoning

### Claim 1: Systematic Sample Size Problem

The KB's confidence architecture is built on a foundation of small-N inference. I conducted a systematic audit:

| KB Concept | Claimed Confidence | Effective N | 95% CI Width |
|---|---|---|---|
| GPT diffusion lag | 8 | 5-6 | ~53pp |
| Value capture base rate | 7 | 6 | ~49pp |
| Equity-credit sequencing | 7 | 3-6 | ~55-72pp |
| CMA factor sign flip | 6 | 2-3 | ~65-84pp |
| Self-funded bust pattern | 8 | 2 | ~84pp |
| Kill-zone threshold | 6 | 5 (1 relevant) | N/A |
| Mid-1990s analogue | 7 | 1 | N/A |

**STATISTICAL ASSESSMENT:** For binomial proportions with N<10, the Clopper-Pearson exact confidence interval typically spans 40-80 percentage points. A confidence rating of 7-8/10 implies precision that these samples cannot deliver. The KB's confidence ratings appear to reflect analytical conviction rather than statistical reliability — a critical distinction that is never explicitly made.

### Claim 2: GPT Diffusion Lag Precision

**CLAIM UNDER TEST:** "15-25% probability of transformative claims translating to TFP acceleration within 3-5 years."

**EMPIRICAL METHODOLOGY:** The claim is derived from N=5-6 GPT episodes (electricity, steam, railroads, IT/PC, internet, possibly telegraph). Of these, the number achieving measurable TFP acceleration within 3-5 years of mass deployment is approximately 0-1 (depending on whether the internet's 1995-2000 productivity acceleration is counted).

**RESULTS:**
- Point estimate: 0/5 = 0% or 1/6 = 17%
- Clopper-Pearson 95% CI (0/5): [0%, 52%]
- Clopper-Pearson 95% CI (1/6): [0.4%, 64%]
- The KB's cited range of "15-25%" falls within these intervals but is presented with false precision

**ROBUSTNESS CHECKS:**
- The GPT sample is not i.i.d.: each successive GPT built on different infrastructure, making the compression trend extrapolation a curve-fit through 5 points
- Including or excluding the telegraph changes the sample materially
- The "compression trend" (30yr → 14yr → 7-12yr) is a regression through 3-4 points with R² that cannot be meaningful
- Non-stationarity: the institutional/technological environment differs so dramatically across episodes that pooling them is questionable

**STATISTICAL ASSESSMENT:** The data are genuinely insufficient to distinguish between 10% and 40% probability. The KB's disagreement between challenger_02 (10-15%) and rates_strategist_02 (30-40%) cannot be resolved by this evidence base. Both are within the confidence interval. The honest answer is: **we don't know, and we can't know from historical GPT data alone.**

### Claim 3: Value Capture Base Rate Adjustment

**CLAIM UNDER TEST:** "Infrastructure builders captured primary value in 1/6 GPT episodes (17% naive), adjusted to 25-40% for hyperscaler vertical integration."

The 23 percentage-point upward adjustment (17% → 40% upper bound) is larger than the base rate itself and is justified by a qualitative argument about "bottleneck control." This is precisely the conjunction fallacy the KB itself identifies elsewhere: the probability that hyperscalers (a) control durable bottlenecks AND (b) this translates to value capture AND (c) this differs from the 5/6 historical pattern requires multiplying conditional probabilities, not adding a premium.

**Base rate decomposition:**
- P(infrastructure builder captures value | GPT episode) = 1/6 ≈ 17%
- P(hyperscalers control durable bottleneck) = unknown, but KB cites "cloud + data + compute + distribution"
- P(bottleneck control translates to value capture) = not independently estimated

The adjustment to 25-40% assumes P(bottleneck control) × P(capture | control) ≈ 0.5-1.4, which implies near-certainty on at least one conditional — internally inconsistent with the acknowledged uncertainty.

### Claim 4: ERP Forward Return Distribution

**CLAIM UNDER TEST:** "ERP at 2.5-3.0% (10th-15th percentile post-1960) historically preceded below-average 5-year forward returns."

This is the KB's strongest statistical claim because:
- Sample: ~65 years of monthly data (~780 observations)
- Multiple estimation methods converge
- Forward return relationship is monotonic and robust to method choice
- Out-of-sample: relationship held in pre-1960 data as well

**Conditional return distribution from post-1960 10th-15th percentile ERP episodes:**
- Mean 5-year forward nominal return: approximately 3-5% annualized
- Standard deviation of 5-year forward returns: approximately 4-6% annualized
- Probability of negative 5-year real return: approximately 35-45%
- Probability of underperforming bonds: approximately 55-65%

**CRITICAL CAVEAT:** The equal-weighted ERP of 4.5-5.0% falls in the 40th-50th percentile — a fundamentally different forward return regime. This means the negative signal is entirely attributable to AI-adjacent mega-cap concentration, not the broad market. A basket excluding top-10 stocks faces normal expected returns, not the compressed distribution.

### Claim 5: Equity-Credit Sequencing

**CLAIM UNDER TEST:** "Equity leads credit by 6-12 months with 83% hit rate."

**EMPIRICAL METHODOLOGY:** The 83% figure appears to come from 5/6 episodes where negative equity-credit basis exceeded 2-sigma.

**RESULTS:**
- Binomial test: P(5+ successes out of 6 | p=0.5) = 0.109
- Not significant at p<0.10
- Even against a null of 33% (random chance with 3 outcomes), P(5+/6 | p=0.33) = 0.018 — significant, but the null of 33% is arbitrary
- The 3/3 "well-documented episodes" is even less informative: P(3/3 | p=0.5) = 0.125

**ROBUSTNESS CHECKS:**
- Selection of what constitutes an "episode" is researcher-defined
- The 6-12 month lead time has enormous variance (spans a 2x range)
- Passive credit indexation (a structural change) may invalidate the prior sample

**STATISTICAL ASSESSMENT:** The directional pattern is plausible but the hit rate and lead time cannot be considered statistically established. The KB should present this as a qualitative pattern observation, not a base rate.

### Claim 6: Factor Crowding Metrics

The momentum ENB collapse to 25-35 and inter-factor correlation tripling are empirically verifiable from current portfolio data. These are descriptive statistics of current positioning, not predictive claims, and the confidence rating of 9 is appropriate for the descriptive finding.

However, the **predictive implication** — that these levels indicate imminent unwind risk — has no out-of-sample validation. The 2007 quant quake and March 2020 are the only comparison points (N=2), and both had different structural contexts (2007: statistical arbitrage crowding; 2020: pandemic exogenous shock).

The ENB metric itself is sensitive to estimation window choice (3-month vs 6-month vs 12-month rolling), and at extreme concentration levels, the metric's denominator behavior may produce artifacts.

### Claim 8: TFP Structural Break Test Power

The KB rates "no aggregate TFP breakthrough" at confidence 9 and calls it "the single most robust empirical finding." While the observation is correct — BLS data show no discontinuity — the statistical test has a known power problem.

**EMPIRICAL METHODOLOGY:**
- Standard structural break tests (Chow, Bai-Perron, Andrews) have power >80% against discrete level shifts of >0.5 standard deviations
- Power against gradual shifts (linear ramp over 3-5 years) falls to 20-40% depending on ramp duration and noise
- Quarterly TFP data with typical noise of ±0.3-0.5pp annualized means a true 0.3pp annual acceleration (within the Acemoglu-McKinsey range) would require 8-12 quarters to reach detectable levels

**STATISTICAL ASSESSMENT:** The absence of a structural break in 2023-early 2026 data (~12 quarters) is consistent with both (a) no productivity impact and (b) a gradual impact of up to ~0.3-0.4pp/yr. The test cannot discriminate between these hypotheses. The KB correctly notes this as an open question but the confidence rating of 9 should apply to the observation, not to the inference that AI has not affected productivity.

### Claim 10: Correlated Estimation Errors

The cross-asset pricing inconsistency framework treats equity-implied growth, bond-implied growth, and credit-implied default expectations as independent signals. But:

- Equity ERP estimates use the same forward earnings estimates as credit models
- Bond r* estimates (Laubach-Williams) use GDP data also embedded in equity valuations
- All three use overlapping macro data (employment, inflation, output)

The "inconsistency" could partially reflect different model specifications applied to the same data, not genuinely independent market signals disagreeing. A proper test would require computing the covariance matrix of estimation errors across models, which the KB does not attempt.

## Confidence Assessment

| Claim | Confidence | Justification |
|---|---|---|
| 1. Systematic small-N problem | 9/10 | Mathematical fact about confidence interval widths |
| 2. GPT diffusion lag imprecision | 9/10 | Binomial CI calculation is exact |
| 3. Value capture adjustment unanchored | 8/10 | Logical critique of methodology; adjustment could be right by luck |
| 4. ERP forward return distribution | 8/10 | Largest sample, most studied relationship; caveat about non-stationarity |
| 5. Equity-credit sequencing non-significant | 8/10 | P-value calculation is exact; interpretation admits debate |
| 6. Factor crowding lacks OOS validation | 9/10 | Definitionally true — no prior episode at this scale |
| 7. Kill-zone threshold N=1 for self-funded | 9/10 | Count of applicable analogues is verifiable |
| 8. TFP break test power problem | 7/10 | Power analysis depends on assumed effect size |
| 9. Stock-bond correlation attribution | 7/10 | Multiple confounds are real; isolation difficulty is acknowledged |
| 10. Correlated estimation errors | 6/10 | Valid methodological concern; magnitude of bias uncertain |

## Connections to Other Topics

**Rates/Monetary Policy:** The bimodal terminal rate distribution (200-300bp gap) is empirically untestable in real-time because the scenarios are mutually exclusive futures, not repeated events. The Fed framework review analysis correctly notes zero market pricing but the "2-3x mispricing" claim requires a probability estimate that itself has ~±50% uncertainty.

**FX/Dollar:** The dollar-AI capex correlation is the strongest cross-asset empirical link (TIC data, DXY persistence despite rate cuts), but the causal identification problem is severe. The 1997-2001 analogue is N=1 and occurred in a fundamentally different fiscal environment.

**Credit/Macro:** The Kalecki identity is an accounting tautology (confidence 10/10 for the identity itself) but the magnitude estimates ($50-60B earnings impact from 25% capex cut) require estimating the multiplier, which is empirically uncertain at ±30-50%.

**Factor/Quant:** The value-growth spread at 5th-8th percentile with "no negative 5-year outcome in sample" is a powerful empirical regularity but the qualifier "in sample" is load-bearing. Post-1963 provides approximately 5-6 entry points at this spread level — again, small N masquerading as a distributional statement.

## Open Questions

1. **Can the KB's confidence ratings be formally calibrated?** The gap between analytical conviction and statistical reliability is the single largest methodological weakness. A Bayesian framework that explicitly incorporates prior beliefs, sample sizes, and structural change uncertainty would be more honest than point confidence ratings.

2. **What is the appropriate statistical framework for N=2-6 historical analogues?** The frequentist approach yields wide, uninformative intervals. A Bayesian approach with informative priors would narrow intervals but introduces subjectivity — exactly the bias risk the KB is trying to avoid.

3. **How should non-stationarity be handled?** Every historical analogue in the KB occurred in a different monetary, fiscal, and technological regime. The implicit assumption of stationarity (past base rates predict future probabilities) may be the KB's deepest unstated assumption. Financial regime changes may make the entire base-rate approach unreliable precisely when it is most needed.

4. **What is the appropriate out-of-sample test for the cross-asset pricing inconsistency?** The KB identifies the inconsistency but provides no forward-looking test to determine which market is "right." A testable prediction with a specific timeline and threshold would make this framework falsifiable.

5. **Can the SBC reflexivity loop ($14-16/share S&P 500 impact) be independently verified?** The mechanism is logically sound but the magnitude estimate appears to be derived from a single estimation method. Cross-validation against other accounting-to-price transmission channels would strengthen or weaken the claim.

6. **What is the joint probability distribution across the KB's key risk factors?** Individual claims are presented in isolation, but the portfolio-relevant question is: what is the probability that depreciation headwinds, ROIC dilution, factor crowding, AND basis trade coupling all activate simultaneously? The KB implicitly assumes partial independence across channels that may be highly correlated — the same AI narrative shock triggers multiple channels simultaneously.

7. **The 4-6x capex-to-revenue ratio comparison to telecom's 0.2x threshold: is this even the right metric?** The telecom ratio used revenue/capex (inverse), but the denominator (identifiable AI revenue) is definitionally ambiguous in a way telecom revenue was not. A 30% change in AI revenue attribution shifts the ratio by a full turn. The comparison is meaningful directionally but the specific threshold level carries substantial measurement error.

8. **What would constitute statistically significant evidence that the mid-1990s analogue is shifting to late-1990s?** The falsification criteria (revenue/capex <0.2x, negative hyperscaler FCF, zero-revenue AI startups at extreme valuations) are qualitative. Converting these to quantitative triggers with explicit probability thresholds would make the framework genuinely monitorable rather than retrospectively applied.
