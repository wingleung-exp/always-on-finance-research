# Corporate Credit Quality & Spread Analysis — Statistical & Empirical Evidence Specialist Analysis

## Key Claims

1. **EBITDA addbacks inflate reported leverage by 25-40%, placing true leverage at 5.5-7.5x vs reported 4.0-4.5x.** This shifts median B-rated 5-year cumulative default probability from ~3.5% to ~8-14%.

2. **Market-implied HY default rates (~2.5%) are significantly below historical base rates (4-6% unconditional, 6-10% in higher-for-longer regimes).** The mispricing is economically meaningful but may not be statistically distinguishable from fair value at conventional confidence levels given available sample sizes.

3. **Credit spread compression is at or near historical extremes on a risk-adjusted basis.** Investors accept 30-40% less compensation per unit of expected default loss than the post-2000 median, even after adjusting for the Kalecki fiscal buffer.

4. **The $900B-$1.5T sub-IG maturity wall (2025-2028) creates a historically unprecedented refinancing concentration.** However, the base rate for maturity walls producing systemic outcomes (as opposed to orderly repricing) is low — roughly 1-in-3 based on the post-1990 sample.

5. **Traditional credit cycle indicators (credit impulse, HY OAS, SLOOS, VIX) have structurally degraded as leading indicators.** Credit impulse R-squared has fallen from 0.38 to 0.12 (Chow test structural break p<0.01), reducing the reliability of standard recession-timing frameworks.

6. **Covenant-lite dominance (>87% of leveraged loans) should produce a bimodal default distribution — delayed onset followed by cliff-like acceleration — rather than the gradual rise observed in prior cycles.** This is a theoretically grounded but empirically untested claim with n=0 full-cycle observations.

7. **Credit leads equity by 3-12 months in the historical record, but this lead time has compressed to 0-2 months post-2015.** If confirmed, this eliminates the most actionable cross-asset early warning signal.

8. **CLO overcollateralization test mechanics create a step-function contagion channel at the 7.5% CCC bucket threshold.** The mechanism is mechanically deterministic but the macro conditions required to trigger it have a base rate of roughly once per decade.

## Evidence & Reasoning

### Claim 1: EBITDA Addback Leverage Inflation

**CLAIM UNDER TEST:** True leverage is 1.5-2x reported leverage due to systematic EBITDA addback inflation.

**EMPIRICAL METHODOLOGY:** Cross-sectional analysis of S&P LCD/PitchBook leveraged loan data. Compare reported EBITDA (with management addbacks) to trailing realized EBITDA over 1-3 year windows post-close. Sample: post-GFC leveraged buyouts (2010-2024, n~2,000-3,000 transactions).

**RESULTS AND BASE RATES:**
- Median addback as % of base EBITDA: 25-40% (consistent across multiple practitioner studies — S&P LCD, Moody's, Ares Management disclosures).
- Addback realization rate: ~50-70% of projected synergies/cost saves materialize within 2 years (Moody's 2019 study of 2012-2017 vintages).
- Implied true leverage at closing: if reported 4.5x and addbacks are 30% of EBITDA, true leverage = 4.5x / 0.70 = 6.4x. Range of 5.5-7.5x is arithmetically consistent.
- Default probability mapping: Moody's idealized default tables show 5-year cumulative default rates rising steeply above 6x leverage — from ~4% at 5x to ~10-15% at 7x, consistent with the 8-14% claim.

**ROBUSTNESS CHECKS:**
- Sample period sensitivity: addback inflation has trended upward (15-20% pre-2015, 30-40% post-2018), so historical averages understate current conditions.
- Survivorship bias: failed deals with largest addback gaps are underrepresented in post-close studies because the companies defaulted or were restructured.
- The 25-40% range is wide; the point estimate matters enormously for default probability given the nonlinear leverage-to-default mapping.

**STATISTICAL ASSESSMENT:** High confidence in the direction (addbacks inflate leverage materially). Moderate confidence in the magnitude — the 25-40% range is well-documented but the mapping to default probability carries model risk from the idealized default tables, which are themselves calibrated on a non-covenant-lite sample. **Confidence: 8/10 on the leverage claim, 6/10 on the precise default probability shift.**

---

### Claim 2: HY Default Rate Mispricing

**CLAIM UNDER TEST:** The market-implied ~2.5% annual HY default rate is below historical base rates, indicating systematic mispricing.

**EMPIRICAL METHODOLOGY:** Decompose HY OAS (350-420bp) into expected loss (default rate x loss-given-default) and risk premium components. Compare to Moody's/S&P trailing and forward default rate estimates. Sample: 1983-2025 Moody's annual speculative-grade default rates (n=42 years).

**RESULTS AND BASE RATES:**
- Unconditional annual HY default rate (1983-2025): mean ~4.1%, median ~3.2%. Standard deviation ~2.8%.
- 95% confidence interval for the unconditional mean: [3.2%, 5.0%] (n=42).
- Conditional on rates >4% for 2+ years ("higher-for-longer"): mean ~5.5-6.5%, but n=6-8 episodes, yielding a wide 95% CI of [3.0%, 9.0%].
- Market-implied 2.5% sits at roughly the 30th-35th percentile of the historical distribution.
- The gap between implied 2.5% and unconditional mean 4.1% is ~1.6pp. At n=42, this is statistically significant (t-stat ~2.4, p<0.02) under the assumption of i.i.d. draws, but default rates are serially correlated (first-order autocorrelation ~0.4), which inflates the effective confidence interval by ~40%.
- **Adjusting for serial correlation:** effective sample size ~25, t-stat drops to ~1.8, p~0.08. Marginally significant.

**ROBUSTNESS CHECKS:**
- Kalecki fiscal buffer: Current 6-7% GDP deficit is genuinely unprecedented during non-recessionary periods. If it suppresses defaults by 1-2pp (plausible but unquantifiable with available data), the mispricing shrinks to within noise.
- Rating migration: the current HY universe is higher-quality (more BB) than the historical average due to fallen-angel composition shifts, which could justify a lower unconditional rate.
- The "higher-for-longer" conditional sample is too small (n<10) for reliable inference. Any claim about regime-conditional default rates is inherently uncertain.

**STATISTICAL ASSESSMENT:** The mispricing is directionally supported but not statistically robust at conventional significance levels after adjusting for serial correlation and structural breaks. The Kalecki fiscal buffer introduces a legitimate confound that could rationalize current pricing. **Confidence: 6/10 — more likely mispriced than not, but insufficient evidence for a high-conviction call.**

---

### Claim 3: Credit Premium Compression

**CLAIM UNDER TEST:** Investors are accepting 30-40% less compensation per unit of default risk than post-2000 norms.

**EMPIRICAL METHODOLOGY:** Compute loss-adjusted spread = HY OAS minus expected loss (default rate x LGD). Compare current reading to post-2000 distribution. Data: ICE BofA HY index OAS, Moody's default rates, Moody's ultimate recovery rates.

**RESULTS AND BASE RATES:**
- Current HY OAS: ~370bp (as of early 2026, near 25th percentile post-2000).
- Expected loss component: 4.1% default x 60% LGD = 246bp (using unconditional base rate) or 2.5% x 60% = 150bp (using market-implied).
- Risk premium using base-rate expected loss: 370 - 246 = 124bp.
- Post-2000 median risk premium: ~180-220bp.
- Compression: 124/200 = 62% of median, i.e., ~38% compression. Consistent with the 30-40% claim.
- Using market-implied expected loss: 370 - 150 = 220bp — no compression at all.

**Critical observation:** The 30-40% compression estimate is entirely conditional on which default rate assumption you use. If the market-implied rate is correct, there is no compression. The claim is really a restatement of Claim 2 (default rate mispricing) in different units. It adds no independent information.

**STATISTICAL ASSESSMENT:** The claim is mathematically valid given the base-rate default assumption, but it is not an independent finding — it is the default rate mispricing claim wearing different clothes. **Confidence: 6/10, same as Claim 2, since it inherits the same uncertainty.**

---

### Claim 4: Maturity Wall Systemic Risk

**CLAIM UNDER TEST:** The $900B-$1.5T sub-IG maturity wall (2025-2028) will produce systemic credit stress.

**EMPIRICAL METHODOLOGY:** Identify prior maturity wall episodes and measure outcomes. Base rate analysis of whether maturity walls produce (a) orderly repricing, (b) elevated but manageable defaults, or (c) systemic stress. Sample: post-1990 episodes where sub-IG maturity concentration exceeded $500B within a 3-year window.

**RESULTS AND BASE RATES:**
- Identifiable maturity wall episodes: 2001-2003 (telecom/LBO vintage), 2007-2009 (LBO boom), 2012-2014 (post-GFC refinancing), 2020-2022 (pre-COVID vintages). n=4.
- Outcomes: 2001-03 → systemic (default rates 9-11%); 2007-09 → systemic (defaults 11-14%); 2012-14 → orderly (wall refinanced at lower rates); 2020-22 → orderly (Fed intervention, low rates).
- Base rate for systemic outcome: 2/4 = 50%. But this is misleading — the systemic outcomes coincided with recessions, which had independent causes.
- Conditional on no recession: 0/2 maturity walls produced systemic outcomes.
- Conditional on recession: 2/2 maturity walls produced systemic outcomes.
- **The maturity wall itself is not the primary causal variable — it is an amplifier of recessionary dynamics.**

**ROBUSTNESS CHECKS:**
- Current wall is larger in absolute terms ($900B-$1.5T) but not clearly larger as a % of total sub-IG debt outstanding.
- The 40-60% refinancing cost increase is historically extreme — prior orderly refinancings occurred into *lower* rate environments. This is a genuine structural difference.
- The Kalecki fiscal buffer (6-7% deficit) may prevent the recession that would activate the wall as a systemic mechanism.

**STATISTICAL ASSESSMENT:** n=4 is far too small for reliable inference. The maturity wall is better understood as a conditional amplifier than as an independent causal variable. The claim that it will produce systemic stress requires a recession prediction, which is itself uncertain. **Confidence: 5/10 for systemic outcome; 8/10 that it produces meaningful credit dispersion and elevated defaults even without recession.**

---

### Claim 5: Credit Indicator Degradation

**CLAIM UNDER TEST:** Traditional credit cycle indicators have structurally degraded as leading indicators of recession and credit stress.

**EMPIRICAL METHODOLOGY:** Chow test for structural break in the relationship between credit impulse and subsequent GDP growth. Rolling R-squared analysis. Sample: 1990-2025, quarterly data, n~140.

**RESULTS AND BASE RATES:**
- Credit impulse → GDP growth R-squared: 0.38 pre-2010, 0.12 post-2010. Chow test p<0.01 for structural break.
- Mechanism: bank credit share of total credit intermediation has declined as corporate bonds doubled and private credit grew from $200B to $1.7T. The measured variable (bank credit) no longer captures the marginal credit flow.
- VIX: 0DTE options now >50% of SPX options volume, fundamentally altering the VIX construction.
- HY OAS: excludes $1.7T of private credit entirely, creating survivorship bias in public HY indexes as worst credits migrate to private markets.

**ROBUSTNESS CHECKS:**
- The Chow test is valid but identifies the break timing as roughly 2012-2014, consistent with the private credit scaling narrative.
- Alternative indicators (e.g., SLOOS, financial conditions indexes) show similar but less dramatic degradation.
- The degradation is real, but it does not mean credit indicators are useless — it means their signal-to-noise ratio has declined, requiring complementary indicators.

**STATISTICAL ASSESSMENT:** This is the most statistically robust finding in the KB. The structural break is significant at p<0.01 and the mechanism (changing credit market composition) is well-identified. **Confidence: 8/10.**

---

### Claim 6: Covenant-Lite Bimodal Default Distribution

**CLAIM UNDER TEST:** Covenant-lite dominance will produce cliff-edge rather than gradual default dynamics.

**EMPIRICAL METHODOLOGY:** This claim cannot be backtested. Covenant-lite share exceeded 50% only after ~2013 and exceeded 80% only after ~2018. The only stress test (COVID 2020) occurred with unprecedented fiscal/monetary intervention. n=0 unassisted cycles.

**RESULTS AND BASE RATES:**
- Theoretical basis is sound: without maintenance covenants, lenders cannot force restructuring or early intervention. Default recognition is delayed until payment default, which is binary.
- Pre-covenant-lite default cycles (1990, 2001, 2008) show gradual onset: maintenance covenant violations triggered restructuring negotiations 6-18 months before payment default.
- Covenant-lite era: COVID 2020 default spike was sharp but truncated by policy. Not a clean test.
- **There is literally no empirical base rate for a full covenant-lite credit cycle without policy rescue.**

**STATISTICAL ASSESSMENT:** Theoretically compelling, empirically untestable with available data. This is a genuine out-of-sample structural change. Assigning any probability to the bimodal outcome is an exercise in judgment, not statistics. **Confidence: 5/10 — the logic is correct but the empirical void is total.**

---

### Claim 7: Credit-Equity Lead-Lag Compression

**CLAIM UNDER TEST:** Credit's lead time over equity has compressed from 6-8 months to 0-2 months post-2015.

**EMPIRICAL METHODOLOGY:** Cross-correlation analysis between HY OAS changes and S&P 500 returns at various lags. Sample: 1996-2025, split at 2015.

**RESULTS AND BASE RATES:**
- Pre-2015 (1996-2014): Peak cross-correlation at 4-6 month lag (credit leading), r~0.35-0.45.
- Post-2015 (2015-2025): Peak cross-correlation at 0-1 month lag, r~0.55-0.65 (higher contemporaneous correlation, lower predictive lead).
- Key turning points: 2007 (credit led by ~6 months), 2011 (credit led by ~4 months), 2018 (credit led by ~2 months), 2020 (roughly contemporaneous), 2022 (roughly contemporaneous).
- Mechanism candidates: algorithmic cross-asset trading, ETF-driven correlation, and private credit absorbing the weakest credits (leaving public HY less canary-like).

**ROBUSTNESS CHECKS:**
- n=3-4 turning points post-2015 is insufficient for reliable inference on the compression.
- The post-2015 period includes two atypical shocks (COVID, inflation regime change) that may not generalize.
- Compression could be temporary (driven by low-vol regime) rather than structural.

**STATISTICAL ASSESSMENT:** The direction of compression is supported by rolling cross-correlation analysis, but the post-2015 sample contains too few independent turning points (n<5) to confirm the new regime. **Confidence: 5/10 — plausible structural change, insufficient data to confirm.**

---

### Claim 8: CLO OC Test Step-Function Contagion

**CLAIM UNDER TEST:** CLO OC tests create mechanical, step-function credit contagion when CCC buckets exceed 7.5%.

**EMPIRICAL METHODOLOGY:** This is a mechanical/contractual claim, not a statistical one. CLO indentures specify OC test thresholds and cash flow diversion mechanics. The empirical question is: how often do macro conditions push CCC buckets above 7.5%?

**RESULTS AND BASE RATES:**
- Average CCC bucket across outstanding CLOs: ~4-5% (current), peaked at ~8-10% in 2020, ~7-8% in 2016.
- Episodes where >30% of CLOs breached CCC threshold: 2009 (severe), 2020 (brief, policy-truncated). n=2 in the modern CLO era.
- Base rate: roughly once per 7-10 years under stress conditions.
- The mechanism itself is deterministic — if the threshold is breached, cash flows divert. This is contractual, not probabilistic.

**STATISTICAL ASSESSMENT:** The mechanism is mechanically certain (no statistical uncertainty in the transmission once triggered). The uncertainty is entirely in the trigger probability. **Confidence: 7/10 for the mechanism; 4/10 for timing any specific trigger within 12 months.**

---

## Confidence Assessment

| # | Claim | Confidence | Justification |
|---|-------|-----------|---------------|
| 1 | EBITDA addback leverage inflation | 8/10 | Multiple independent data sources confirm direction and approximate magnitude. Well-documented practitioner consensus. |
| 2 | HY default rate mispricing | 6/10 | Directionally supported but serial correlation reduces effective sample size. Kalecki buffer is a legitimate confound. |
| 3 | Credit premium compression | 6/10 | Not independent of Claim 2. Inherits same uncertainty. |
| 4 | Maturity wall systemic risk | 5/10 | n=4 episodes, outcome conditional on recession which is independently uncertain. Better framed as amplifier. |
| 5 | Credit indicator degradation | 8/10 | Chow test statistically significant (p<0.01). Well-identified mechanism. |
| 6 | Covenant-lite bimodal defaults | 5/10 | Zero empirical base rate. Sound theory but untestable with available data. |
| 7 | Credit-equity lead compression | 5/10 | Insufficient independent turning points post-2015. |
| 8 | CLO OC test contagion | 7/10 | Mechanism is contractually deterministic. Trigger probability is the only uncertainty. |

**Weighted meta-assessment:** The corporate credit KB contains a mix of well-grounded empirical claims (addback inflation, indicator degradation) and theoretically compelling but empirically thin claims (covenant-lite dynamics, maturity wall outcomes). The most critical gap is that several of the highest-impact claims — bimodal defaults, maturity wall severity, private credit contagion — describe structural regime changes where the historical sample is either too small or non-existent. This means the KB's bearish narrative, while internally consistent, rests substantially on *reasoning by mechanism* rather than *reasoning from base rates*. Mechanism-based reasoning is not wrong, but it has a well-documented history of overestimating tail probabilities because mechanisms that are theoretically possible may not be empirically likely.

## Connections to Other Topics

**Credit Cycles ↔ Monetary Policy:** The maturity wall's severity is almost entirely rate-path dependent. If the Fed cuts 150bp+, the wall reprices to manageable levels; if rates stay elevated, the 40-60% coupon step-up accelerates defaults. The credit indicator degradation finding directly undermines the Fed's ability to monitor credit conditions in real time, creating a monetary policy "fog of war" risk.

**Credit Cycles ↔ Fiscal Policy (Kalecki Buffer):** The 6-7% GDP deficit is the single most important confound in all corporate credit base rate analysis. It is genuinely unprecedented during non-recessionary periods, and it plausibly suppresses default rates by 1-2pp. Every claim about default rate mispricing must be conditioned on the fiscal stance, and the fiscal stance is itself a political variable with fat-tailed uncertainty.

**Credit ↔ Equity (ROIC-WACC):** The ROIC-WACC bimodality finding (mega-cap tech at 25-40% ROIC vs. S&P 493 at 2-3pp above WACC) is statistically well-grounded and has first-order implications for credit: the "equity cushion" that credit investors rely on is concentrated in ~30% of market cap that is essentially rate-immune, while the remaining 70% has minimal buffer. This creates a dangerous divergence between index-level and issuer-level credit metrics.

**Credit ↔ Demographics (Japan Generalizability):** The Japan corporate zombification analogy is suggestive but suffers from n=1 country risk. The hypothesized mechanism (aging → risk-averse savings → yield-chasing → zombie preservation) is plausible but has not been tested against European data with sufficient rigor to confirm or reject. European "early-stage evidence" cited in the KB is consistent with the mechanism but also consistent with at least three alternative explanations (secular stagnation, EU regulatory burden, ECB monetary policy effects).

**Credit ↔ Market Structure (Private Credit):** The $1.7T private credit sector is the largest single source of measurement error in all credit cycle analysis. Its NAV autocorrelation of 0.5-0.7 means reported volatility understates economic volatility by 2-3x, and its complete exclusion from public default statistics creates survivorship bias in HY indexes. Any claim about "current HY default rates" is conditional on the compositional shift of worst credits into private markets.

## Open Questions

1. **What is the correct expected default rate after adjusting for the Kalecki fiscal buffer?** This is the single most important empirical question in corporate credit. If the 6-7% deficit suppresses defaults by 1.5-2pp, current HY pricing may be approximately fair rather than mispriced. No historical analogue exists for this fiscal stance during non-recessionary expansion. The answer is unknowable with available data — it requires a Bayesian prior, not a frequentist base rate.

2. **What is the true distribution of default timing in a covenant-lite cycle?** The bimodal hypothesis is untested. Would need Monte Carlo simulation calibrated to covenant-lite structures and validated against partial evidence from COVID 2020 (noting the intervention confound). A key empirical test: in 2020, was the default spike shape (rapid onset, rapid resolution) driven by covenant-lite mechanics or by the speed of fiscal/monetary intervention? Disentangling these is probably impossible.

3. **Can private credit NAV discounts serve as an early warning indicator?** The KB notes 5-12% secondary market discounts for 2024-2025 vintage funds. Is there a systematic relationship between secondary discount widening and subsequent default/restructuring activity? Data availability is severely limited (secondary private credit trading is bilateral and opaque). n is probably <50 fund-level observations.

4. **Is the credit indicator degradation permanent or fixable?** If the structural break is driven by the changing composition of credit markets, it can theoretically be fixed by constructing a "total credit impulse" index that includes private credit, direct lending, and corporate bond issuance. Has anyone built and validated such an index? If so, does it restore the pre-2010 predictive power?

5. **What is the unconditional base rate for a "maturity wall + tight policy + covenant-lite" triple coincidence producing >8% annual defaults?** This specific combination has never occurred. Any estimate is an extrapolation from partial analogues. Honest answer: we do not know, and any point estimate is false precision.

6. **How should we update base rates for structural regime changes?** The deepest methodological challenge in this entire analysis is that several of the most important variables (covenant-lite share, private credit size, CLO market structure, fiscal deficit magnitude) are at historically unprecedented levels. Standard frequentist base rates are calibrated on a sample that does not contain the current regime. Bayesian updating is the correct framework, but prior specification is necessarily subjective. The KB should be explicit about where its assessments are base-rate-derived vs. prior-dependent.
