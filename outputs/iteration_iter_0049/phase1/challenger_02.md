# Equity Cycles — Behavioral Finance Critic & Historical Falsifier Analysis

## Key Claims

1. **The KB exhibits systematic narrative coherence bias: 25+ concepts and 15+ relationships have been assembled into a single, internally consistent "late-cycle fragility" story, which is itself a red flag for confirmation bias in the analytical process.**

2. **Confidence levels across the KB are miscalibrated — systematically too high for structural-break claims and too narrow in their implied probability distributions, particularly for concepts rated 7-8 that rest on small-sample historical analogies.**

3. **The "3/3 prior concentration episodes resolved via large-cap decline" base rate is a textbook case of reference-class gerrymandering — the sample is too small and the selection criteria too subjective to support the implied predictive power.**

4. **The Kalecki fiscal channel's quantified EPS impact ($10-20/share from consolidation) embeds false precision that obscures genuine uncertainty by at least 3x the stated range.**

5. **The steepening trap concept remains unfalsifiable as specified, despite being flagged as such in its own open questions — an analytical failure that 49 iterations should have resolved.**

6. **The credit impulse, yield curve, and earnings revision breadth "composite indicator" framework suffers from backtest inflation that the KB acknowledges but does not adequately penalize in confidence ratings.**

7. **The KB's treatment of passive investing as a "structural break" that may invalidate all historical base rates is a having-it-both-ways fallacy: you cannot simultaneously invoke historical base rates for cycle timing AND claim those base rates may be obsolete.**

8. **The ROIC-WACC convexity claim (2.5x fragility ratio) treats a mechanical accounting identity as a market prediction, committing the fallacy of composition by assuming aggregate spread compression translates linearly to aggregate market fragility.**

9. **Multiple concepts anchor on US-centric data while the KB itself documents US survivorship bias — an internal contradiction that undermines the precision of most quantified claims.**

10. **The AI capex conjunction probability decomposition (P(A∩B∩C∩D) ≈ 10-20% for bubble narrative) is presented as a bias correction but is itself vulnerable to the conjunction fallacy in reverse — decomposing a single scenario into artificially independent sub-events to make the probability appear lower.**

## Evidence & Reasoning

**Claim 1 — Narrative Coherence Bias:**
Count the directionality. Of 25 concepts, at least 18 point toward "fragility," "late-cycle," "overvaluation," or "deterioration." The concepts that could support a bullish counter-narrative (market_concentration_superior_economics with >25% ROIC, AI capex hedge-financed from FCF, Kalecki fiscal floor intact) are consistently framed as temporary or conditional, while bearish concepts are framed as structural. This asymmetry is not inherent in the data — it reflects the analytical community's prior. Kahneman's WYSIATI (What You See Is All There Is) applies: the KB contains almost no concepts about potential positive surprises (productivity acceleration, innovation-driven margin expansion, demographic tailwinds in specific sectors). The absence of bullish structural concepts is itself evidence of confirmation bias in concept selection.

**Claim 2 — Confidence Miscalibration:**
The KB assigns confidence 7-8 to claims like "equity cycle macro causation" (confidence 8) and "valuation regime inflation dependence" (confidence 8). These ratings imply ~80% probability of being correct. But the supporting evidence for both relies on post-war US data with N=3 to N=7 regime transitions — sample sizes where a single counterexample shifts the base rate by 14-33%. Tetlock's superforecasting research shows that even expert forecasters achieve ~70% accuracy on well-defined, time-bounded questions. For structural claims about regime shifts with no defined time horizon, 80% confidence is almost certainly overfit. The confidence 5 ratings (EM bifurcation, sanctions discount, passive structural break) are more appropriately calibrated to their evidence base.

Specific miscalibrations:
- `small_cap_structural_underperformance` at confidence 8: "3/3 prior comparable divergences resolved via large-cap decline" is a sample of three. Three observations cannot support 80% confidence in a structural claim. The appropriate confidence for N=3 with zero variance is ~60-65% after accounting for selection bias in identifying the comparison set.
- `equity_cycle_macro_causation` at confidence 8: The coefficient of variation >0.7 for peak-to-peak intervals is presented as evidence against cycle timing, but the 7/7 yield curve recession prediction is presented as evidence FOR macro causation — these are not the same claim, yet both prop up the same confidence rating.

**Claim 3 — Reference-Class Gerrymandering:**
The "3/3 prior concentration episodes" (Nifty Fifty, 1999 tech, 2007 financials) supporting `market_concentration_superior_economics` are selected on the dependent variable. The criteria for inclusion are post-hoc: "periods where top-10 concentration exceeded X% and subsequently declined." This excludes periods where concentration persisted or resolved benignly. The 1950s-60s AT&T/GM/GE concentration, the 2012-2015 Apple dominance, and multiple international examples (Samsung in Korea, TSMC in Taiwan index) are omitted. The KB partially acknowledges this by noting current ROIC >25% differentiates from prior episodes, but then still invokes the 3/3 base rate as if it's informative. You cannot both argue "this time has different fundamentals" AND "but the base rate says it ends badly." The appropriate treatment is to acknowledge that N=3 with acknowledged structural differences provides essentially no predictive power.

**Claim 4 — Kalecki False Precision:**
The claim that fiscal consolidation from 6.5% to 4.0% deficit/GDP reduces S&P 500 EPS by "$10-20/share (4-8%)" presents an accounting identity as a market forecast. The Kalecki-Levy identity is an accounting truism about how aggregate profits decompose. Converting this to a specific EPS impact requires assumptions about: (a) which spending categories are cut, (b) the fiscal multiplier for those categories, (c) the speed of consolidation, (d) private sector offset through investment and net exports, (e) monetary policy response, and (f) second-round effects through confidence and financial conditions. Each assumption carries ±30-50% uncertainty. The compound uncertainty makes the actual range more like $5-40/share, not $10-20. The Godley 1999 prediction is cited as out-of-sample validation, but Godley made many predictions — citing the successful one is survivorship bias in forecasting track records.

**Claim 5 — Steepening Trap Unfalsifiability:**
The `steepening_trap` concept states: "Recession historically arrives during yield curve steepening, not inversion." Its own open questions ask: "Is the concept unfalsifiable as currently specified given the wide window that can be retroactively fitted?" This is iteration 49. The concept was introduced in iter_0024 and updated in iter_0031. After 25 iterations with this question flagged, the concept still lacks falsifiable criteria. What specific 2s10s level, over what time horizon, with what decomposition, would constitute a failed prediction? Without this, the steepening trap is a narrative, not a forecast. The "5/7 historical easing cycles show recession beginning after steepening commenced" statistic sounds precise but is not — "after steepening commenced" can mean 3 months or 30 months, making it trivially true and analytically useless.

**Claim 6 — Backtest Inflation:**
The `earnings_revision_breadth` concept acknowledges "signal quality is degraded by market bifurcation and backtest inflation" but still carries confidence 6. The claimed "8/9 episodes since 1970 with 4-8 month lead times" is a backtest. The actionable lead time of "only 1-3 months" (acknowledged in the KB) means the indicator is inside institutional rebalancing noise. A 0.45-0.55 correlation with forward returns explains 20-30% of variance — this is real but modest predictive power that does not warrant the prominence the KB gives it. The credit impulse similarly has its track record cited at three turning points (2007, 2009, 2022) — this is cherry-picked performance at notable turns, not a systematic backtest.

**Claim 7 — Having-It-Both-Ways Fallacy:**
The `passive_investing_structural_break` concept (confidence 5) states passive investing "may" invalidate historical base rates. But the entire KB framework relies on historical base rates: yield curve 7/7 record, concentration 3/3 resolution, drawdown archetypes, ERB 8/9 record. If passive flows have truly altered cycle dynamics, then every confidence rating above 5 in the KB should be adjusted downward by 1-2 points for structural uncertainty. The KB cannot logically maintain high confidence in historical-pattern-based claims while simultaneously acknowledging that the structural environment may have changed enough to break those patterns. This is not a minor inconsistency — it is a fundamental logical flaw in the entire framework.

**Claim 8 — ROIC-WACC Composition Fallacy:**
The `roic_wacc_spread_convexity` claim that "100bp WACC increase destroys 25% of EVA at 4pp spread" is mechanically correct for a single firm. But aggregating this to "the current S&P 500 is approximately 2.5x more fragile" commits the fallacy of composition. The S&P 500 contains firms with ROIC-WACC spreads ranging from negative to 30%+. The aggregate spread is a weighted average that masks enormous dispersion. A rate shock does not uniformly increase WACC by 100bp across all firms (duration, leverage, and business model differences mean differential transmission). The 2.5x fragility ratio is a thought experiment, not an empirical finding. Its confidence of 5 is appropriate but the framing as "the single strongest original claim" overstates its analytical value.

**Claim 9 — Internal US Bias Contradiction:**
The `us_equity_survivorship_bias` concept correctly identifies that US 6.4% real returns are an outlier in a 35-country sample. But 90%+ of the KB's quantified claims use US data exclusively. The output gap R-squared (Fama-French 1989, Cochrane 2011) is US-only. The yield curve 7/7 record is US-only. The ERB 8/9 record is US-only. The three concentration episodes are US-only. If the KB genuinely believes US experience is non-generalizable (confidence 5 assigned to survivorship bias), it should flag the US-only evidence base as a systematic limitation of every other concept. It does not.

**Claim 10 — Reverse Conjunction Fallacy:**
The `ai_capex_sustainability` concept decomposes the bubble narrative into P(A∩B∩C∩D) ≈ 10-20%. This is presented as showing the bubble narrative is unlikely. But the decomposition assumes approximate independence of the sub-events (A, B, C, D). If the events are correlated — which they would be in a systemic scenario — the joint probability could be significantly higher. More importantly, you don't need ALL four conditions for a bad outcome. P(at least one of A, B, C, D) could be 50-70% even if each individual P is 30-40%. The conjunction decomposition is mathematically valid only for the specific scenario where all four conditions manifest simultaneously, but the KB uses it to implicitly argue against any negative AI capex outcome.

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1. Narrative coherence bias | 8/10 | Directly observable in concept inventory — 18/25 bearish-leaning is a measurable skew |
| 2. Confidence miscalibration | 7/10 | Tetlock's calibration research is robust; small-sample problem is mathematical, not debatable |
| 3. Reference-class gerrymandering | 8/10 | N=3 with post-hoc selection is a textbook statistical error regardless of outcome |
| 4. Kalecki false precision | 7/10 | Accounting identity vs. market forecast distinction is clear; uncertainty propagation math is standard |
| 5. Steepening trap unfalsifiability | 9/10 | The KB itself identifies this problem and has not resolved it over 25 iterations |
| 6. Backtest inflation | 7/10 | Well-documented problem in quantitative finance; acknowledged but under-penalized in KB |
| 7. Having-it-both-ways fallacy | 8/10 | Logical contradiction is binary — either base rates are reliable or they may not be |
| 8. ROIC-WACC composition fallacy | 6/10 | The mechanical math is correct for single firms; whether aggregation is misleading depends on dispersion, which I haven't quantified |
| 9. US bias contradiction | 8/10 | Directly observable — count the US-only citations vs. the survivorship bias acknowledgment |
| 10. Reverse conjunction fallacy | 6/10 | Depends on actual correlation structure of sub-events, which is genuinely uncertain |

**Meta-calibration note:** I assign myself 7/10 average confidence across these claims. My own analysis suffers from the same small-sample and narrative-construction problems I identify in the KB. I am more confident in the logical and structural critiques (claims 3, 5, 7, 9) than in the quantitative recalibrations (claims 2, 4, 8).

## Connections to Other Topics

**To inflation/rates topics:** The `valuation_regime_inflation_dependence` concept at confidence 8 connects directly to inflation research that presumably exists in other topic categories. If the inflation KB has a structural floor of 2.3-2.8%, this is a specific, testable claim whose verification should propagate back to equity cycle valuations. The stock-bond correlation regime shift depends entirely on whether this inflation claim holds. Cross-topic consistency check: does the inflation KB's confidence in the 2.3-2.8% floor warrant the equity KB's confidence 8 in valuation regime dependence?

**To credit/fixed income topics:** The credit impulse leading indicator and yield curve decomposition both straddle equity and fixed income. The 2-6 month credit impulse lead is asserted in the equity KB but should be verified against whatever the credit/rates KB says about current credit conditions. The 30-50bp ACM vs. Kim-Wright divergence is a rates-topic detail that propagates material uncertainty into equity cycle timing.

**To geopolitical topics:** The sanctions architecture and EM bifurcation concepts are equity-cycle concepts driven by geopolitical inputs. The confidence 5 ratings are appropriate for their evidence base but create a dangling dependency — if geopolitical research elevates or downgrades the permanence of the current sanctions regime, the equity KB should update accordingly.

**To fiscal policy topics:** The Kalecki channel is the single most load-bearing cross-topic connection. The claim that 6-7% deficit/GDP sustains 7-15% of S&P 500 EPS means fiscal policy research directly sets the floor for equity cycle analysis. Any fiscal topic KB should be checked for consistency with this channel's quantification.

**To AI/technology topics:** The AI capex sustainability concept is the primary bullish structural driver. Its conjunction probability decomposition should be cross-referenced with whatever technology/AI topic research exists on TAM realization, adoption curves, and productivity measurement.

## Open Questions

1. **Can the KB produce a single, specific, time-bounded, falsifiable prediction from its framework?** After 49 iterations, the accumulation of conditional, regime-dependent, model-dependent claims has produced an analytically sophisticated but operationally vague conclusion ("late-cycle, fiscally obscured, fragile but floor intact"). What would change your view? What observation in the next 6-12 months would be inconsistent with the framework?

2. **What is the base rate for "late-cycle" calls?** Analysts have been calling "late cycle" since approximately 2018. The median duration of a "late-cycle" call before either a recession or an acceleration is itself an informative statistic that the KB does not track. How many false "late-cycle" calls have been made in the post-GFC era?

3. **Where is the bullish structural concept inventory?** The KB should contain at minimum: (a) AI productivity acceleration scenarios with quantified impact, (b) demographic dividend from immigration/workforce participation, (c) energy cost reduction from renewables scaling, (d) financial innovation expanding credit access, (e) institutional quality advantages sustaining US premium. The absence of these is not because they don't exist — it's because the analytical process has a bearish selection bias.

4. **What is the actual out-of-sample track record of this framework's precursor analyses?** If prior iterations generated actionable signals, what was the hit rate? Without tracking this, the KB is accumulating analytical sophistication without accountability.

5. **How should the passive investing structural break be resolved?** This is flagged as "the most important open question" but has been at confidence 5 for 25+ iterations. Either design a test or downgrade every historical-base-rate-dependent concept by 1-2 confidence points. The current treatment — acknowledging the problem while ignoring its implications — is analytically dishonest.

6. **What is the appropriate confidence penalty for US-only evidence?** If US survivorship bias is real (confidence 5 in the KB), then every US-only backtest should carry a systematic confidence discount. Quantify this discount and apply it consistently, or remove the survivorship bias concept as non-actionable.

7. **Is the three-condition checklist (fiscal impulse, credit impulse, Minsky fragility) predictive or descriptive?** "Condition 3 met, condition 2 approaching, condition 1 intact" has been the reading for how long? If conditions can remain in "approaching" status indefinitely, the checklist is descriptive of current conditions, not predictive of future ones. Specify: what does "approaching threshold" mean in measurable terms, and over what time horizon does the threshold become binding?
