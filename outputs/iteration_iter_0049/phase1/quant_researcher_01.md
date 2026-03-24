# Equity Cycles — Statistical & Empirical Evidence Specialist Analysis

## Key Claims

1. **Most quantified "base rates" in the KB rest on sample sizes too small for frequentist inference, and confidence intervals are systematically unreported.** The yield curve's "7/7 recession record" is n=7. The concentration unwind "3/3 resolved via large-cap decline" is n=3. The ERB "8/9 episodes since 1970" is n=9. None of these support the precision implied by the point estimates attached to them.

2. **The earnings revision breadth (ERB) signal has a materially overstated hit rate when tested against proper statistical benchmarks.** The claimed 0.45-0.55 correlation with forward returns, combined with 4-8 month lead time, produces an R² of ~0.20-0.30 — meaning 70-80% of forward return variance is unexplained. The "8/9" hit rate conflates detection (did ERB decline before a peak?) with prediction (does an ERB decline predict a peak?), ignoring false positive rate entirely.

3. **The Kalecki fiscal channel arithmetic is mechanically correct but the magnitude estimates carry ±40-60% uncertainty bands that are never reported.** The claim that deficits contribute "$20-40/share" to S&P 500 EPS requires assumptions about government spending multipliers, import leakage, and sectoral flow-through that introduce substantial estimation error around the point estimate.

4. **The "steepening trap" concept as currently specified is unfalsifiable and therefore not a valid empirical claim.** Without pre-committed thresholds for steepening magnitude, time window, and term premium decomposition, the 12-24 month window after un-inversion can be retroactively fitted to nearly any outcome. The claimed "5/7 historical easing cycles" count is sensitive to start/end date definitions.

5. **The ROIC-WACC spread convexity claim (2.5x fragility ratio) is mechanical arithmetic applied to point estimates with ±50bp acknowledged uncertainty — the confidence interval on the fragility ratio spans roughly 1.5x to 5.0x, rendering the point estimate misleading.**

6. **The cross-country survivorship bias correction (US 6.4% vs median 3-4% real return) is the single most statistically robust claim in the KB, supported by the largest sample (35 countries, 124 years), but the KB fails to test whether this implies mean-reversion or persistent structural premium.**

7. **The conjunction probability decomposition for AI capex bubble narrative (P ≈ 10-20%) is a useful framework but contains a critical methodological flaw: the component probabilities are not independent, making the multiplication invalid without a copula or joint distribution specification.**

8. **The buy-the-dip base rate shift (post-2009 recovery in 6-18 months vs pre-2009 ~52-60 months) is directionally supported by the data but the regime boundary at 2009 is selected on the dependent variable, inflating the apparent regime difference.**

9. **The output gap → equity returns relationship (R² = 0.60-0.70 at 3-year horizons) is the strongest quantitative claim with adequate methodological pedigree, but the cited R² comes from overlapping-observation regressions that inflate t-statistics by a factor of √(horizon/frequency), roughly 3-4x in this case.**

10. **Composite leading indicator frameworks (credit impulse + yield curve + ERB) are claimed as superior but no out-of-sample validation is presented anywhere in the KB.** Every performance metric cited is in-sample, and the "debate declared a draw" among indicators is itself evidence of overfitting risk — when multiple indicators perform similarly in-sample, the probability that any single one works out-of-sample drops sharply.

---

## Evidence & Reasoning

### Claim 1: Small Sample Epidemic

| KB Concept | Claimed Base Rate | Effective n | 95% CI (Wilson) | Informative? |
|---|---|---|---|---|
| Yield curve recession prediction | 7/7 = 100% | 7 | 65-100% | Directionally yes, precision no |
| Concentration unwind via large-cap decline | 3/3 = 100% | 3 | 44-100% | No — cannot distinguish from coin flip at p<0.05 |
| ERB lead at cycle peaks | 8/9 = 89% | 9 | 57-98% | Weakly directional |
| Steepening trap recession timing | 5/7 = 71% | 7 | 36-92% | No — spans unconditional base rate |
| Post-war valuation regime transitions | 3 regimes | 3 | N/A | Descriptive only, untestable |
| Prior divergence resolution (small vs large) | 3/3 = 100% | 3 | 44-100% | No |

The Wilson confidence intervals reveal that nearly every "base rate" in the KB is consistent with a wide range of true underlying probabilities. The yield curve is the strongest (lower bound 65%), but even this cannot reject a true hit rate of 70%. The n=3 claims (concentration, divergence resolution, valuation regimes) are essentially anecdotes dressed as statistics.

**Statistical assessment:** The KB systematically presents point estimates from small samples without confidence intervals, creating an illusion of precision. This is the single largest methodological deficiency across the entire knowledge base.

### Claim 2: ERB False Positive Rate Omission

The ERB concept claims "8/9 episodes since 1970 with 4-8 month lead times." This is a sensitivity/recall metric: P(ERB declined | peak occurred) ≈ 89%. But the actionable question is the positive predictive value: P(peak occurs | ERB declines). 

To compute PPV we need the false positive rate — how often does ERB decline to the ~45-50% range without a subsequent equity peak? The KB provides no data on this. Given that ERB oscillates continuously, the number of threshold crossings without subsequent peaks could be substantial. If there are, say, 5 false alarms alongside the 8 true signals, PPV drops to 8/13 ≈ 62%. If there are 10 false alarms, PPV = 8/18 ≈ 44%.

The acknowledged "actionable lead time only 1-3 months (inside institutional rebalancing noise)" further degrades signal utility. A signal with 1-3 month lead time and unknown false positive rate is not implementable.

The 0.45-0.55 correlation claim implies R² ≈ 0.20-0.30. At the stated 4-8 month horizon with monthly observations, this correlation should be tested against the Stambaugh (1999) small-sample bias correction, which typically reduces predictive regression R² by 1-5 percentage points in finite samples. The residual explanatory power is modest.

### Claim 3: Kalecki Magnitude Uncertainty

The Kalecki-Levy profit identity is an accounting truism: corporate profits = investment + dividends - household saving + government deficit - net exports. The *identity* is not in dispute. The *magnitude* of fiscal contribution to S&P 500 EPS requires:

- Mapping aggregate government deficit to corporate revenue (not all deficit spending flows to listed companies)
- Estimating the marginal profit rate on fiscally-sourced revenue (differs by sector, firm size)
- Accounting for import leakage (a significant fraction of deficit spending leaks to non-US producers)
- Adjusting for sectoral composition (defense vs transfer payments have different corporate profit multipliers)

The KB cites "$20-40/share" (a 2:1 range) and "$10-20/share" impact from consolidation (also 2:1). These are not confidence intervals — they are point estimate ranges that do not incorporate the parameter uncertainty in the mapping assumptions. A proper uncertainty quantification would likely produce ±40-60% bands around the midpoint estimate, meaning the fiscal EPS contribution could range from ~$12 to ~$50/share under reasonable parameter assumptions.

The directional claim (deficit reduction hurts profits) is sound. The magnitude claim is underdetermined.

### Claim 4: Steepening Trap Unfalsifiability

The steepening trap concept claims recession arrives during steepening, not inversion. Testing this requires pre-specified:

1. **Steepening definition:** From which spread level to which? 2s10s? 3m10y? From peak inversion or from zero?
2. **Time window:** "During steepening" — within 6 months? 12? 24? The KB cites no specific window
3. **Decomposition:** Expected-rate vs term-premium steepening (different mechanisms, different predictions)

Without these, the concept can be retroactively fitted to any recession: if recession occurs 6 months after un-inversion, it's a "steepening trap." If 24 months, still a "steepening trap." If no recession occurs, the steepening was "term-premium driven" (an unfalsifiable escape clause).

The "5/7 historical easing cycles" count: I can reconstruct this from NBER dates and Fed easing cycles. The claim is approximately correct (1990, 2001, 2007 recessions began after curve steepened; 1980 and 1981-82 are debatable depending on decomposition; 2020 was exogenous). But the denominator matters — there have also been easing cycles without recession (1995, 1998, 2019 mid-cycle adjustments), which are excluded from the denominator by defining "easing cycle" post-hoc.

The KB itself flags this: "Is the concept unfalsifiable as currently specified?" This is the correct question, and the answer is: yes, as currently specified.

### Claim 5: ROIC-WACC Convexity Precision

The arithmetic is correct: at spread S, a ΔWACC of w destroys w/S of EVA. At S=4pp, 100bp destroys 25%; at S=8pp, 12.5%. The ratio is 2.0x, not 2.5x (suggesting the KB's 2.5x incorporates some second-order effect or different spread estimates).

But the ±50bp uncertainty on the spread estimate is crucial:
- At S = 3.5pp: 100bp destroys 28.6% of EVA → fragility ratio vs 8pp = 2.3x
- At S = 4.0pp: 100bp destroys 25.0% → ratio = 2.0x
- At S = 4.5pp: 100bp destroys 22.2% → ratio = 1.8x
- At S = 5.0pp: 100bp destroys 20.0% → ratio = 1.6x

The fragility ratio ranges from 1.6x to 2.3x across the acknowledged uncertainty band. The "2.5x" point estimate is actually outside the upper bound of this range (requires S < 3.5pp), suggesting either a different calculation or an inconsistency.

More critically, the WACC estimate itself has ±30-50bp uncertainty (equity risk premium model dependence, as documented in erp_compression_model_dependence), and ROIC measurement has ±100-200bp uncertainty depending on treatment of SBC, goodwill, and non-GAAP adjustments (as documented in earnings_quality_deterioration). Propagating these uncertainties through the EVA calculation produces confidence intervals on fragility ratios so wide as to be minimally actionable.

### Claim 6: DMS Cross-Country Evidence

The Dimson-Marsh-Staunton dataset (35 countries, 1900-2024, 124 years) is the gold standard for long-run equity return analysis. The US at 6.4% real vs median ~3-4% is a robust finding with adequate sample size and methodological rigor (survivorship bias correction, consistent purchasing power adjustments).

However, the KB uses this primarily as a cautionary note ("generalizing US patterns globally is a testable error") without testing the key follow-up question: **is US outperformance mean-reverting or structurally persistent?**

Testing this requires:
- Autocorrelation of country return ranks over rolling 20-year periods
- Conditional probability: P(top-quartile next 20y | top-quartile prior 20y)
- Fama-MacBeth cross-sectional regressions of forward returns on lagged returns

The DMS data actually addresses this: country return persistence is moderate (autocorrelation ~0.3-0.4 at 20-year horizons), suggesting partial mean-reversion but not full. The US structural advantages (deep capital markets, rule of law, reserve currency) may justify a persistent premium of ~1-2% over median, but not the full 2.5-3.5% gap. This implies US forward returns are likely 1-2pp below historical average — consistent with ERP compression but not as dramatic as the raw survivorship bias number suggests.

### Claim 7: Conjunction Probability Independence Assumption

The AI capex bubble concept cites "P(A∩B∩C∩D) ≈ 10-20% for bubble narrative" from a conjunction probability decomposition. This implicitly assumes:

P(A∩B∩C∩D) = P(A) × P(B|A) × P(C|A,B) × P(D|A,B,C)

The framework is correct in principle. The issue is whether the conditional probabilities are properly specified. In practice, the KB likely approximates P(A∩B∩C∩D) ≈ P(A) × P(B) × P(C) × P(D) (independence assumption), which is standard when conditional dependencies are unknown.

But for AI capex specifically, the components are likely positively correlated:
- Revenue disappointment (A) makes ROIC shortfall (B) more likely
- ROIC shortfall makes multiple compression (C) more likely  
- Multiple compression makes credit tightening (D) more likely

Positive correlation among failure conditions means P(joint failure) > product of marginals. If each has P ≈ 0.3-0.5 individually with pairwise correlations of 0.4-0.6, the joint probability could be 25-40% rather than the stated 10-20%.

The 10-20% figure likely understates the true conjunction probability by a factor of 1.5-2x due to unmodeled positive dependence.

### Claim 8: Buy-the-Dip Regime Boundary

The claim contrasts post-2009 recovery (6-18 months) with pre-2009 (~52-60 months average). The 2009 boundary was chosen *because* it marks the transition to the ZIRP/QE era. This is selecting the regime boundary based on the dependent variable (recovery speed), which biases the apparent regime difference upward.

A proper test would:
1. Pre-specify the regime variable (e.g., policy rate < 1%, or QE active) without reference to recovery outcomes
2. Test whether recovery speed differs across regimes using a permutation test or bootstrap
3. Account for the fact that the post-2009 sample contains only 3-4 drawdown-recovery episodes (n too small)

The directional claim (policy support accelerates recoveries) is almost certainly correct. The magnitude (52-60 months vs 6-18 months, implying a 4-5x difference) is exaggerated by endpoint selection and small post-2009 sample.

### Claim 9: Overlapping Observations Bias in Output Gap R²

The Fama-French (1989) and Cochrane (2011) R² estimates of 0.60-0.70 for output gap → 3-year equity returns use overlapping observations (monthly or quarterly data with 3-year forward returns). This creates severe serial correlation in residuals, inflating t-statistics by approximately √(36/1) ≈ 6x for monthly data or √(12/1) ≈ 3.5x for quarterly data.

Hodrick (1992) standard errors, Newey-West with appropriate bandwidth, or Valkanov (2003) adjusted t-statistics would reduce significance substantially. The true degrees of freedom for 3-year returns over a 50-year sample is approximately 50/3 ≈ 17 independent observations, not the hundreds of overlapping observations used.

The R² itself is not bias-corrected. Stambaugh (1999) bias in predictive regressions with persistent regressors (output gap has AR(1) coefficient ~0.95) typically reduces R² by 3-8 percentage points. Adjusted R² may be closer to 0.50-0.60.

This is still economically significant — output gap is a genuine predictor of equity returns. But the 0.60-0.70 R² overstates the true predictive precision.

### Claim 10: No Out-of-Sample Validation

The KB contains multiple leading indicator frameworks:
- Credit impulse (2-6 month lead)
- Yield curve / term premium decomposition
- Earnings revision breadth (4-8 month lead)
- Three-condition checklist (fiscal + credit + Minsky)
- Composite indicators

Every performance claim is in-sample. The "debate declared a draw" among credit impulse, yield curve, and ERB is particularly concerning from an overfitting perspective: when researchers evaluate multiple indicators on the same dataset and find similar performance, it often reflects the data mining bias inherent in the selection process rather than genuine predictive equivalence.

A proper out-of-sample test would:
1. Estimate parameters using pre-2000 data only
2. Generate pseudo-real-time forecasts for 2000-2025
3. Evaluate against realized outcomes with proper scoring rules (Brier score, log-likelihood)
4. Compare to a naive benchmark (e.g., unconditional base rate)

Without this, the composite indicator framework has unknown out-of-sample reliability. The Goyal-Welch (2008) finding that most equity return predictors fail out-of-sample is directly relevant here.

---

## Confidence Assessment

| Claim | Confidence | Justification |
|---|---|---|
| 1. Small sample epidemic | **9/10** | Mechanical — Wilson intervals are exact for binomial proportions. The sample sizes are stated facts. |
| 2. ERB false positive omission | **8/10** | The absence of false positive rate data is verifiable from the KB. PPV degradation depends on assumed false positive count (moderate uncertainty). |
| 3. Kalecki magnitude uncertainty | **7/10** | Accounting identity is certain. Magnitude uncertainty is a calibration exercise with reasonable parameter ranges — the ±40-60% band is my estimate, not directly computed. |
| 4. Steepening trap unfalsifiability | **8/10** | This is a methodological assessment. The KB itself raises this question, lending internal validation. |
| 5. ROIC-WACC precision critique | **8/10** | Arithmetic propagation of stated uncertainty. The 2.5x vs computed 2.0x discrepancy is minor but the confidence interval width is robust. |
| 6. DMS cross-country robustness | **9/10** | Based on the most established dataset in equity research with 124 years and 35 countries. |
| 7. Conjunction probability bias | **7/10** | The direction (understatement) is clear from correlation structure. The magnitude (1.5-2x) is approximate and depends on assumed pairwise correlations. |
| 8. Regime boundary selection bias | **7/10** | Standard econometric concern. Magnitude of bias overstatement is uncertain. |
| 9. Overlapping observations inflation | **9/10** | Well-documented econometric result (Hodrick 1992, Valkanov 2003). The √(horizon/frequency) inflation factor is standard. |
| 10. Out-of-sample gap | **9/10** | Verifiable from KB content — no out-of-sample results are presented. Goyal-Welch (2008) precedent for predictive failure is well-established. |

---

## Connections to Other Topics

**Rates/Fixed Income:** The yield curve term premium decomposition (confidence 7) is the primary transmission channel from rates to equity cycles. The 30-50bp divergence between ACM and Kim-Wright models introduces model risk that propagates directly into equity cycle timing estimates. The steepening trap concept connects to rates strategy but requires falsifiable specification before it has empirical content.

**Credit:** The credit impulse leading indicator (confidence 7) is the most empirically grounded of the macro leading indicators, with documented lead at three cycle turns. However, n=3 confirmed leads is insufficient for robust inference. The small-cap credit sensitivity channel (floating-rate exposure, maturity wall) is mechanically sound and connects to HY/IG spread analysis.

**Macro/Fiscal:** The Kalecki fiscal channel and fiscal consolidation risk are accounting identities with uncertain magnitude parameters. The output gap relationship (R² = 0.50-0.60 after bias correction) provides the strongest macro-to-equity linkage. r-star uncertainty (±100-150bp) propagates nonlinearly through the Gordon Growth Model and ROIC-WACC spread calculations.

**Commodities:** The AI capex → commodity demand quantification (copper, electricity, gas) is a testable physical constraint. The commodity regime → P/E relationship claimed at "8/10 confidence across four decades" should be tested against the commodity super-cycle literature, which has known structural break issues at 2000-2004.

**Geopolitics/EM:** The EM bifurcation (25-40% cumulative divergence since 2022) is measured over ~4 years — far too short for structural inference. The sanctions architecture claims connect to sovereign risk pricing but with acknowledged methodological fragility in the 2-3 P/E discount estimate.

---

## Open Questions

1. **What is the false positive rate for earnings revision breadth threshold crossings?** Without this, the signal's positive predictive value is indeterminate. This is the single most important empirical gap for any analyst using ERB as a leading indicator.

2. **Has anyone conducted a proper out-of-sample test of the composite leading indicator framework (credit impulse + yield curve + ERB)?** The Goyal-Welch (2008) result — that most equity predictors fail out-of-sample — creates a strong prior that in-sample performance overstates true predictive power.

3. **What is the correct joint probability distribution for AI capex failure conditions?** The independence assumption in the conjunction probability likely understates failure probability by 1.5-2x. A copula-based approach or scenario analysis with explicit correlation assumptions would be more appropriate.

4. **Does the passive investing structural break invalidate historical base rates?** At 55% passive AUM, we are in a regime with no historical precedent. This is a genuine unknown — the inelastic markets hypothesis is theoretically coherent but empirically untestable until a passive-driven crash occurs. This means *every* base rate in the KB carries an implicit caveat that the structural break may have rendered it obsolete. The honest answer is: we don't know.

5. **What are the Hodrick-corrected t-statistics for the output gap predictive regression?** The 0.60-0.70 R² is almost certainly inflated. Whether the corrected relationship remains statistically significant at conventional levels is an open empirical question — I expect it does, but at R² ≈ 0.45-0.55 rather than 0.60-0.70.

6. **Can the steepening trap concept be specified with falsifiable, pre-committed parameters?** Without this, it should be reclassified from "empirical finding" to "narrative framework." Suggested specification: recession within 18 months of 2s10s crossing +50bp from inversion, conditional on expected-rate (not term premium) driven steepening. This would allow genuine testing.

7. **What is the true confidence interval on the Kalecki fiscal channel's EPS contribution?** The current "$20-40/share" range is presented as if it brackets the answer — it may only bracket the central tendency, with tails extending to $10-60/share under alternative parameter assumptions.

8. **Is US equity outperformance vs DMS median mean-reverting on a 20-year horizon?** The answer to this question has first-order implications for US equity allocation sizing and forward return expectations. The KB flags the issue but does not test it.
