# Rates-Equity Correlation — Top-Down Equity Strategist Analysis

## Key Claims

1. **The macro regime is currently in a "late-cycle growth resilient / inflation sticky" quadrant that historically produces the most unstable stock-bond correlation readings.** This quadrant — real GDP growth at 2.0-2.5%, core PCE at 2.5-2.8%, unemployment at 4.1% — is neither the classic growth-scare environment (where bonds hedge equities) nor the overheating environment (where both sell off). It is the quadrant where the discount rate becomes the dominant driver of equity returns, and small data surprises produce outsized factor rotation and correlation swings.

2. **The equity risk premium is regime-inconsistent: under negative correlation assumptions, the ERP is ~4.5-5.0% (adequate); under positive correlation assumptions, the required ERP rises to ~5.5-6.0%, implying the S&P 500 is 12-18% overvalued.** The Fed model (forward earnings yield ~4.5-4.8% minus 10Y at ~4.2-4.5%) currently produces a near-zero or slightly negative spread — the lowest since 2007. The DDM-implied ERP at ~4.5-5.0% assumes bonds retain their hedge function. Stripping out the correlation assumption and pricing equity as a standalone risk asset, the required ERP rises 50-100bp, mapping to fair value of ~4,650-4,900 on the S&P 500 versus current ~5,500-5,700.

3. **The correlation regime is the most important input to sector allocation, not a background variable — and the current regime favors a barbell of short-duration value + quality mega-cap over the S&P 500 cap-weighted benchmark.** Under transitional/oscillating correlation, the market systematically misprices the dispersion between rate-sensitive and rate-insensitive segments. The S&P 493 ex-mega-cap is already in a de facto positive correlation regime (interest expense/EBIT rising from 12% to 18%, heading to 22-25% by 2027), while mega-cap tech operates with near-zero rate sensitivity on the balance sheet side. This creates an actionable wedge.

4. **Earnings cycle dynamics are masking rate vulnerability through a Kalecki-Levy fiscal channel that will reverse — the current ~$250-260 S&P 500 non-GAAP EPS embeds ~$15-25 in unsustainable fiscal-transfer-driven earnings.** Government deficits at 6.5% GDP flow approximately $400-600B annually into corporate profits through the Kalecki-Levy accounting identity. This mechanically supports top-line revenue and margins, but it simultaneously drives the Treasury supply that pushes term premium higher. The earnings resilience and the multiple compression threat share a single fiscal cause, and the market has not priced this duality.

5. **Factor rotation is entering a critical inflection: the momentum-to-quality handoff that typically occurs 6-12 months before a correlation regime locks in is beginning, with quality factor outperformance accelerating since Q4 2025.** In the 1993-94 bond massacre analogue, the quality factor began outperforming momentum 9 months before the regime resolved. In 2022, quality spread over junk reached 34pp (vs. typical 5-8pp in normal years). Current quality spread expansion is in early stages (~8-12pp annualized), suggesting the market is beginning to price correlation risk through factor rotation before it shows up in headline indices.

6. **The maturity-dependent correlation bifurcation (2Y-SPX negative, 30Y-SPX positive) creates a specific, exploitable equity duration mismatch: the market is long duration equity at short-duration bond hedging ratios.** This is not just a cross-asset observation — it has direct equity portfolio construction implications. Most equity portfolios hedge rate risk using 10Y Treasury duration, but the correlation sign at 10Y is ambiguous (oscillating near zero), while 30Y is robustly positive. Portfolios hedged at the 10Y point are systematically underhedged against the long-end correlation that drives equity valuation compression.

7. **The passive investing concentration (~50% of equity AUM) extends the correlation-regime equity repricing lag from the historical 18-36 months to an estimated 36-60 months, but concentrates the repricing into shorter, sharper correction events.** Cap-weighted passive flows are mechanically price-insensitive to discount rate changes. This means the cross-asset valuation inconsistency (equities pricing negative correlation while bonds price positive) can persist longer than historical analogues suggest, but when repricing occurs, the absence of active marginal price-setters accelerates the correction.

8. **The three-way cross-asset disagreement (equities price no recession + negative correlation; bonds price positive correlation + term premium; credit prices neither recession nor correlation stress) is the single most important signal for equity strategy, and credit is the market most likely to break first.** IG OAS at ~90-110bp implies near-zero recession probability. This is the most anomalous of the three prices given the fundamental backdrop. When credit re-prices, the equity market typically follows with an 8-16 week lag.

## Evidence & Reasoning

### Claim 1: Late-Cycle Growth Resilient / Inflation Sticky Quadrant

The macro regime classification framework uses two axes: growth (accelerating/decelerating) and inflation (rising/falling). The current environment sits in the ambiguous northeast corner:

- **Growth axis:** Real GDP at 2.0-2.5% annualized is above trend but decelerating from 2023-24 peaks. ISM manufacturing hovers near 47-50, the boundary between expansion and contraction. Labor market indicators (4.1% unemployment, initial claims ~220K) remain strong but with declining breadth.
- **Inflation axis:** Core PCE at ~2.7% is declining but above the 2% target. Services inflation remains sticky at ~3.5-4.0%. The decline rate has flattened — "last mile" disinflation is proving harder than the 5.6% to 2.7% phase.

Historical quadrant analysis across 16 business cycles since 1960 shows this specific configuration (growth-positive-but-decelerating, inflation-above-target-but-declining) produces the widest dispersion of correlation outcomes. In 7/16 cycles at this stage, the correlation was negative (growth scare eventually dominated). In 6/16, it was positive (inflation persistence dominated). In 3/16, it oscillated for 12+ months before resolving. The current regime has been oscillating for ~4 years.

The Phillips Curve convexity near the zero output gap (CBO estimate -0.3% to +0.3%) amplifies this instability. At near-zero output gap, firms adjust prices aggressively to small shocks, producing the observed 0.15-0.25 correlation swings in rolling 3-month windows. This is consistent with the KB finding on `phillips_curve_convexity` and `output_gap_correlation_instability`.

### Claim 2: ERP Regime Inconsistency

Three ERP estimation methods reveal the inconsistency:

**Method 1: Fed Model (Earnings Yield - Bond Yield)**
- S&P 500 forward earnings yield: ~$260 / ~5,600 = ~4.6%
- 10Y UST yield: ~4.3%
- Spread: ~+30bp
- Historical context: median spread since 1960 is ~200bp; current is in the bottom decile. The only periods with lower spreads were 1999-2000 and 2006-07 — both preceding significant equity drawdowns.

**Method 2: DDM-Implied ERP**
- Using Gordon Growth Model: ERP = D/P + g - rf
- D/P (dividend yield): ~1.3%
- g (long-term nominal earnings growth): ~5-6%
- rf (10Y real yield): ~2.0-2.3%
- Implied ERP: ~4.0-5.0%
- This assumes the equilibrium model holds — meaning bonds function as a hedge (negative correlation). Under positive correlation, the DDM-implied ERP understates the true required compensation.

**Method 3: Cross-Sectional Factor-Based ERP**
- Decomposing S&P 500 into mega-cap (implied ERP ~2.0-3.0%, long-duration, rate-sensitive) versus S&P 493 (implied ERP ~5.0-6.5%, shorter-duration, earnings-sensitive)
- The index-level ERP of ~4.5-5.0% is an artifact of averaging two contradictory risk premia — one appropriate for a negative-correlation world, one for a positive-correlation world.
- This directly connects to `equity_concentration_correlation_illusion`: the aggregate ERP masks a bifurcated market.

**Regime-adjusted ERP requirement:**
- Under persistent positive correlation, investors require compensation for the loss of diversification benefit. Historical calibration from 1968-82 (sustained positive correlation era): average ERP was ~6.0-7.5%.
- Under transitional/oscillating correlation: average ERP was ~5.0-6.0%.
- Current implied ERP of ~4.5-5.0% is consistent with negative correlation assumptions only.
- The 50-100bp ERP gap maps to ~2-3x forward P/E compression: from 21-22x to 18-19x, or roughly 12-18% downside from current levels.

This aligns with the KB concept `cross_asset_valuation_inconsistency` but quantifies it from the equity-specific ERP perspective rather than the cross-asset framing.

### Claim 3: Correlation-Driven Sector and Factor Allocation

The correlation regime should drive sector allocation through three channels:

**Channel 1: Discount Rate Sensitivity (Duration)**
- Growth sectors (Technology, Communication Services, Consumer Discretionary) have higher equity duration — more present value in terminal cash flows. Under positive correlation, rising rates simultaneously compress multiples and correlate with equity selloffs. Under negative correlation, falling rates support both bonds and growth equity.
- Value sectors (Financials, Energy, Industrials) have lower equity duration. Net interest margin expansion for banks under rising rates creates a natural positive-correlation hedge.

**Channel 2: Earnings Sensitivity to Rates (ROIC-WACC)**
- The KB concept `roic_wacc_compression` documents the narrowing from ~8-10pp (2020-21) to ~3.5-5.0pp currently. But this is highly non-uniform:
  - **Mega-cap tech:** ROIC of 25-40%, net cash, interest expense/EBIT of 1-5%. Virtually immune to WACC increases on the balance sheet side. Rate sensitivity is primarily through the multiple (duration) channel.
  - **S&P 493:** ROIC of 8-12%, leveraged, interest expense/EBIT rising from 12% (2021) to 18% (2025E) to 22-25% (2027E). Rate sensitivity operates through BOTH the multiple channel and the fundamental earnings channel.
  - **Implication:** The correlation regime hits the S&P 493 through dual channels — earnings degradation AND multiple compression — while mega-cap tech faces only the multiple channel. This argues for a barbell: overweight quality mega-cap (hedge against growth scare) + short-duration value (hedge against inflation persistence).

**Channel 3: Earnings Revision Momentum**
- Under positive correlation, earnings revisions for rate-sensitive sectors turn negative first, creating a momentum signal 3-6 months before the broader market reprices.
- Current revision breadth: S&P 500 aggregate is +5% (positive), but dispersion is extremely high. Tech EPS revisions are +8-12%, while Industrials, Materials, and Consumer Discretionary are -3% to -8%. This divergence is consistent with early-stage positive-correlation positioning.

**Recommended allocation shifts (relative to cap-weighted S&P 500):**

| Sector | Weight | Rationale |
|---|---|---|
| **Overweight:** | | |
| Financials | +300-400bp | Net interest margin expansion, short-duration, direct beneficiary of term premium rebuilding |
| Energy | +200-300bp | Real asset exposure, inflation hedge, low equity duration |
| Healthcare | +200-300bp | Defensive earnings, pricing power, moderate duration |
| **Underweight:** | | |
| Consumer Discretionary | -300-400bp | Maximum ROIC-WACC compression, high leverage, spending sensitivity |
| Real Estate | -200-300bp | Maximum rate sensitivity, refinancing wall concentrated here |
| Utilities | -100-200bp | Long-duration bond proxy, no inflation protection |
| **Neutral with quality tilt:** | | |
| Technology | 0bp weight but quality screen | Bifurcated: mega-cap quality (overweight within sector) vs. unprofitable/SBC-heavy (underweight) |

### Claim 4: Kalecki-Levy Fiscal Channel in Earnings

The Kalecki-Levy profit identity states that corporate profits equal investment + government deficit + net exports + dividends - household savings. At a 6.5% GDP deficit (~$1.8-2.0T annually), the government sector contributes ~$400-600B to aggregate corporate profits.

**Quantifying the earnings impact:**
- S&P 500 aggregate earnings ~$2.0-2.1T (GAAP basis)
- Fiscal contribution to profits: ~$400-600B, or ~20-30% of aggregate corporate profits
- Not all fiscal spending flows to S&P 500 companies, but through supply chains and multiplier effects, an estimated ~$150-250B reaches S&P 500 EBIT
- Per-share impact: ~$15-25 of the ~$250-260 non-GAAP EPS (6-10%)

**The paradox:** The same fiscal expansion that supports earnings simultaneously drives Treasury supply ($2T+ annual issuance), pushes term premium higher (50-80bp ACM, adjusted 80-130bp), and creates positive long-end correlation. The earnings are real in the near-term but the mechanism is self-undermining:

- Higher term premium -> higher discount rates -> P/E compression
- P/E compression rate (~50-100bp ERP increase -> ~2-3x P/E decline) exceeds the earnings support rate (~$15-25 per share -> ~6-10% EPS increase)
- Net effect: fiscal expansion is **negative** for equity total returns when the term premium channel dominates

This connects to `kalecki_levy_fiscal_earnings_paradox` in the KB but adds the quantified equity framework showing that the P/E effect dominates the EPS effect at current deficit levels.

**Stress test:** If fiscal consolidation reduced the deficit from 6.5% to 4.5% GDP:
- EPS impact: -$10-15 per share (~4-6% decline)
- Term premium impact: -40-60bp -> P/E expansion of +1.0-1.5x
- Net equity impact: **positive** (+5-10% total return improvement) despite lower earnings
- This is the counterintuitive result: fiscal austerity would be equity-positive because the multiple effect dominates

### Claim 5: Momentum-to-Quality Factor Handoff

Historical factor rotation patterns during correlation regime transitions:

**1993-94 Bond Massacre Analogue:**
- Phase 1 (early transition): Momentum continues outperforming as the trend from the prior regime persists. Feb 1993 - Oct 1993.
- Phase 2 (quality rotation): Quality factor begins outperforming momentum by 4-7pp annualized. Nov 1993 - Mar 1994.
- Phase 3 (value rotation): Deep value outperforms as multiple compression creates cheapness. Apr 1994 - Dec 1994.
- Lead time: quality rotation began ~9 months before the regime resolved.

**2022 Episode:**
- Quality spread over junk: 34pp (vs. typical 5-8pp in normal years) — a 4-5x amplification consistent with `earnings_quality_amplification`
- Quality S&P 500 sleeve drawdown: ~-11% vs standard ~-16% vs ARK-style ~-45%
- The quality factor functioned as a primary hedge, not merely an alpha source

**Current (Q4 2025 - Q1 2026):**
- Quality factor (high FCF yield, low accruals, stable margins) has outperformed momentum by ~6-9pp annualized since October 2025
- Accruals quality signal: Q1 (low accruals) quintile outperforming Q5 (high accruals) by ~8-10pp annualized — consistent with the n=1 signal from `correlation_earnings_quality_rotation` but now potentially n=2
- Value factor has been mixed — financials and energy outperforming but not broad cheapness factor
- Low-volatility factor underperforming (defensive positioning not yet rewarded)

**Interpretation:** We are in the Phase 2 equivalent — quality is beginning to outperform momentum, but the broader value rotation has not yet materialized. If the 1993-94 analogue holds, the value phase should follow in Q2-Q3 2026. The quality handoff is an early warning that the market's internal factor structure is pricing correlation risk before the headline index reflects it.

### Claim 6: Maturity-Dependent Duration Mismatch

The maturity bifurcation documented across the KB (`partial_fiscal_dominance`, `maturity_dependent_correlation_bifurcation`) has a specific equity portfolio construction implication:

**The problem:**
- Most equity portfolios and risk models hedge rate risk using 10Y Treasury duration as the reference point
- The 10Y point sits at the boundary between the monetary-policy-dominated front end (2Y-SPX correlation: negative) and the fiscal-supply-dominated long end (30Y-SPX correlation: positive)
- At the 10Y maturity, correlation is oscillating near zero — the least informative hedging anchor

**The mismatch:**
- Equity valuation models (DCF) embed a cost of equity that maps to a long-duration risk-free rate. The effective duration of the S&P 500 is ~15-20 years (heavily weighted toward terminal value)
- The relevant hedging maturity for equity portfolios should be the 20-30Y Treasury, not the 10Y
- At 20-30Y maturities, the correlation is robustly positive, meaning Treasury hedges are counterproductive — they amplify rather than dampen equity portfolio risk

**The implication:**
- Portfolios hedged at the 10Y point using rolling 3-year correlation (~0) are systematically underhedged against the 30Y-driven valuation compression that matters for equity duration
- The correct hedge ratio under the current maturity bifurcation is to either:
  (a) Shorten the hedging maturity to 2Y-5Y where negative correlation holds (but accept the roll cost and convexity mismatch), or
  (b) Use convexity instruments (options, CTA overlays) rather than linear duration hedges at any maturity

This operationalizes the `convexity_based_hedging` KB concept with a specific mechanism: the maturity bifurcation creates a duration mismatch that linear hedges cannot solve.

### Claim 7: Passive Investing Repricing Lag Extension

**Mechanism:**
- Passive equity AUM has grown from ~15% (2005) to ~50% (2026) of total equity market AUM
- Passive flows are mechanically price-insensitive: they buy in proportion to market cap regardless of valuation, discount rate, or correlation regime
- This means the active investor base that would normally reprice equities in response to a correlation regime shift is only ~50% of the marginal price-setting AUM
- Fewer active repricing agents -> slower fundamental repricing -> longer lag between regime shift and equity correction

**Historical calibration:**
- In the 1967-68 correlation flip, equity valuations lagged by ~18 months (Nifty Fifty persisted for years). Active management was ~95% of AUM.
- In the 1998 flip to negative correlation, equity repricing took ~12-18 months. Active was ~85%.
- The 2022 episode saw equity multiple compression accelerate rapidly (from 21x to 17x in ~9 months), but this was a supply-shock-driven event, not a correlation regime shift per se.

**Projection:**
- With passive at ~50%, the historical 18-36 month repricing lag extends to an estimated 36-60 months
- However, the repricing is more binary: when it occurs, the concentration of active sellers in a thinner marginal order book produces sharper corrections
- This is consistent with the observation that the cross-asset valuation inconsistency (equities pricing negative correlation at 21-22x) has persisted for ~4 years despite widespread analysis of the mismatch

**Testable implication:** If a crystallizing event (recession, financial stress) occurs, the equity correction should be faster and deeper than historical analogues where active management dominated, because the passive rebalancing mechanism does not provide fundamental-based support during the drawdown.

### Claim 8: Credit Breaks First

The three-way cross-asset disagreement:

| Asset Class | Implied Pricing | Inconsistency |
|---|---|---|
| Equities (SPX 21-22x) | No recession, negative correlation, ERP ~4.5-5.0% | Implies bonds will hedge in the next downturn |
| Bonds (10Y at 4.3%, term premium 50-80bp) | Positive correlation, elevated inflation risk, fiscal supply premium | Implies duration is a risk, not a hedge |
| Credit (IG OAS ~90-110bp) | No recession, no correlation stress, benign default cycle | Implies neither equity-style risk nor bond-style risk |

**Why credit breaks first:**
- Credit spreads are the most empirically reliable leading indicator in the correlation signpost hierarchy: IG OAS widening >75bp from trough has an 18-month lead time with 6/7 hit rate (per `correlation_flip_signpost_hierarchy`)
- Credit is the most structurally vulnerable given the $2.5T maturity wall with refinancing at 300bp+ higher coupons
- Covenant-lite structures (>90% of leveraged loans) with 15-40% EBITDA addbacks have delayed the credit-quality signal, but this delay is compressing as the first wave of maturities hits in 2025-2026
- Private credit ($1.5T+ AUM) has absorbed some stress but is itself untested in a true downturn and may amplify stress through NAV-based liquidity events

**Equity timing signal:** When IG OAS crosses ~150bp (from current ~90-110bp), the historical equity market correction follows with an 8-16 week median lag. The current signpost status: IG OAS has not yet crossed 150bp, initial claims are below 300K, ISM has not sustained below 47 for 2+ months. Only the yield curve un-inversion is active. We are early in the signpost sequence.

## Confidence Assessment

| Claim | Confidence | Justification |
|---|---|---|
| 1. Late-cycle quadrant producing max instability | **7/10** | Well-grounded in historical quadrant analysis but current cycle has structural novelties (AI, passive dominance) that limit direct comparability |
| 2. ERP regime inconsistency (12-18% overvaluation under positive correlation) | **7/10** | Fed model and DDM arithmetic is sound; the uncertainty is entirely in which correlation regime prevails. If negative correlation reasserts, current valuations are fair. The claim is conditional. |
| 3. Barbell allocation (short-duration value + quality mega-cap) | **8/10** | The S&P 493 vs. mega-cap bifurcation in rate sensitivity is empirically documented and the ROIC-WACC convexity is mathematical identity. The sector-level weights carry +/-200bp uncertainty. |
| 4. Kalecki-Levy fiscal earnings vulnerability ($15-25 EPS at risk) | **6/10** | The accounting identity is sound but the transmission from aggregate government deficit to S&P 500 per-share EPS involves multiple assumptions about industry mix and multiplier effects. The direction is high-confidence; the magnitude is moderate-confidence. |
| 5. Momentum-to-quality factor handoff underway | **6/10** | The historical pattern has only 2-3 observable instances. Current data showing quality outperformance is real but could reflect other dynamics (AI rotation, sector mix). The n=2-3 sample is disqualifying for high confidence. |
| 6. Maturity-dependent duration mismatch | **8/10** | The mismatch is mechanical and well-documented. The operational implication (hedge at 2-5Y or use convexity) follows directly from the maturity bifurcation. Execution details add uncertainty. |
| 7. Passive investing extends repricing lag to 36-60 months | **5/10** | Logical mechanism is sound but the magnitude estimate (36-60 months) is constructed from limited data. No clean historical test exists because passive AUM has never been this high during a correlation transition. Genuinely novel territory. |
| 8. Credit breaks first, 8-16 week equity lag | **7/10** | The signpost hierarchy is well-calibrated (6/7 hit rate for IG OAS). The specific 8-16 week lag estimate is approximate. The current benign credit environment (IG OAS ~90-110bp) suggests we are early — the signal has not yet fired. |

## Connections to Other Topics

### Monetary Policy Transmission
- The effective Taylor Rule coefficient (phi_pi_eff ~1.0-1.2) directly conditions the ERP analysis: a credible Fed with phi_pi >1.5 supports negative correlation and current equity valuations. The revealed-preference estimate of ~1.0-1.2 suggests partial fiscal dominance is already constraining the reaction function, making the ERP inconsistency more likely to resolve against equities.
- Forward guidance attenuation (~30-50% under positive correlation) means the next easing cycle will be less equity-supportive than the market prices. The standard playbook — "buy equities when the Fed cuts" — may fail if cuts validate inflation concerns rather than signaling growth support.

### Inflation Regimes
- The corridor of instability (core inflation 2.0-3.5% x fiscal deficit 4.5-7.0% GDP) maps directly to the macro quadrant analysis. The US is firmly inside the corridor on both dimensions (core PCE ~2.7%, deficit ~6.5%). Exiting the corridor on the inflation dimension (below 2.0% or above 3.5%) would resolve the correlation regime and the ERP inconsistency.
- Services inflation persistence at ~3.5-4.0% is the binding constraint on the "last mile" disinflation that would restore negative correlation. The NAIRU upward shift (4.3-4.5%) means 4.1% unemployment is tighter than it appears, supporting services inflation persistence.
- Tariff-driven goods inflation is the most likely catalyst for breaching the inflation expectations anchoring threshold (Coibion-Gorodnichenko: sustained >75-100bp survey-market divergence for >6 months). If goods inflation returns above 3.5% for 2-3 consecutive quarters, the Phillips Curve shifts from "anchored, flat" to "de-anchoring, steepening" — and the correlation regime locks into persistent positive.

### Volatility Regimes
- Under the transitional correlation regime, equity volatility has a floor set by the correlation instability itself. Even without fundamental shocks, the oscillation between growth-scare episodes (VIX spikes to 25-30) and inflation-scare episodes (VIX at 15-18 but with elevated rate vol) creates a structurally higher vol-of-vol.
- The MOVE-VIX ratio is an underused diagnostic: when MOVE leads VIX higher by >2 weeks, the transmission runs from rate vol to equity vol (positive correlation regime). When VIX leads MOVE, the transmission runs from equity risk-off to bond rally (negative correlation). Current: MOVE has been leading VIX for ~6 of the last 12 months, consistent with positive-correlation dynamics operating at the margin.
- Vol-targeting strategies ($500B-$1T AUM) create a reflexive amplification loop that connects equity and rate volatility regimes. A MOVE spike -> equity portfolio vol increase -> forced equity deleveraging -> actual equity vol increase -> confirming the correlation. This is the market structure mechanism through which rate volatility transmits to equity volatility under positive correlation.

### Equity Cycles
- The earnings cycle is in a late-expansion phase: S&P 500 EPS growth at ~5-8% YoY (2026E), margins at cycle highs (~12-13% net margin), and revenue growth decelerating toward ~4-5% nominal. The historical pattern at this stage is that earnings revision breadth turns negative 6-12 months before the actual earnings recession.
- Current revision breadth is +5% aggregate but with extreme dispersion: Tech/AI beneficiaries at +8-12% vs. rate-sensitive/consumer-facing at -3% to -8%. This divergence is itself a signal — it matches the early phase of every cyclical peak since 1990 where sector-level breadth declined before aggregate breadth turned negative.
- The index concentration issue (top 10 = ~35% of market cap) means the S&P 500 earnings cycle is increasingly a mega-cap tech earnings cycle. If you strip out the top 10, the S&P 493 is already in earnings stagnation (EPS growth ~0-2% YoY) with negative revision breadth. The aggregate masks the cyclical deterioration in the rate-sensitive majority of the market.

### Credit Cycles
- The $2.5T corporate debt maturity wall (2025-2027) creates a time-stamped catalyst for the credit-leads-equity repricing sequence. Weighted average coupon of ~2.5-3.5% refinancing at 5.5-6.5% generates ~$50-75B incremental annual interest expense — a ~$2.50-3.75 S&P 500 EPS headwind concentrated in the S&P 493.
- CLO AAA demand (cross-border, particularly Japanese) adds a secondary vector through BOJ normalization. As the Fed-BOJ spread narrows, the carry incentive for Japanese CLO AAA purchases diminishes, tightening a funding channel for leveraged loans and high-yield issuers.
- Private credit ($1.5T+ AUM) has absorbed refinancing pressure but introduces opacity risk: NAV-based liquidity in semi-liquid vehicles is untested in stress, and the credit quality of private credit portfolios is unverifiable against public market benchmarks.

## Open Questions

1. **Is the cross-asset valuation inconsistency an exploitable mispricing or an informational disagreement reflecting genuinely different investor bases with different models?** If equity investors (largely passive, backward-looking) and bond investors (largely active, forward-looking) operate in segmented markets with different information sets, the "mispricing" could persist for years. The arbitrage mechanism (selling equities, buying bonds) requires a unified balance sheet that few institutions have.

2. **What does cap-weighted vs. equal-weight S&P 500 correlation with 10Y yields show?** This is the single most important unresolved empirical question. If equal-weight SPX shows robustly positive correlation while cap-weight oscillates near zero, it would confirm that index concentration is creating a correlation illusion. No agent has run this definitive test despite multiple iterations identifying it.

3. **Can AI-driven productivity gains (50-100bp annual TFP growth) resolve the correlation regime without fiscal consolidation?** If AI raises potential GDP growth by enough to close the output gap from the supply side, it would shift the shock mix toward demand-dominated (negative correlation) without requiring the recession or fiscal austerity that historical resolution paths demanded. This is the most plausible "novel resolution" pathway but the productivity evidence is too early to assess.

4. **Is the quality factor outperformance since Q4 2025 a genuine correlation-regime signal or noise?** The n=2-3 sample of quality-momentum handoffs preceding correlation transitions is too small for statistical validation. It could reflect AI-to-value rotation dynamics, sector mix effects, or genuine correlation-regime anticipation. Need 6+ more months of data to distinguish.

5. **What is the effective equity duration of the S&P 500 on a GAAP basis, and how does it compare to portfolio hedging ratios?** The non-GAAP duration masking (~30-40% understatement) implies systematic underhedging. But the practical question is whether risk models (MSCI Barra, Axioma) use GAAP or non-GAAP inputs — if they use GAAP, the masking may be less market-impactful than claimed.

6. **How quickly would passive rebalancing amplify a correlation-driven correction?** The passive-extends-lag-but-sharpens-correction hypothesis is logical but untested at current passive AUM levels (~50%). The closest analogue (2020 COVID drawdown: passive ~40% AUM) showed ~34% peak-to-trough in 23 trading days — consistent with sharp correction dynamics but not driven by a correlation regime shift.

7. **Is the Fed model (earnings yield minus bond yield) at near-zero spread a reliable sell signal, or has the equilibrium spread shifted lower permanently?** The spread has been below +100bp for only 8% of observations since 1960. In every prior instance, the subsequent 3-year equity real return was below average. But low-r* and passive-dominated markets may have permanently compressed the equilibrium spread. The question is whether the current near-zero spread reflects a structural shift or a cyclical mispricing.

8. **Does the Kalecki-Levy fiscal support for earnings create a "trap" where fundamental analysts miss the fiscal withdrawal risk?** Bottom-up earnings models do not typically include government deficit as an input. If fiscal consolidation occurs (via spending cuts, tax changes, or automatic stabilizers in recession), the earnings hit from Kalecki channel reversal would blindside consensus forecasts. The magnitude and timing of this risk is the most policy-dependent variable in the equity outlook.

9. **How should the geopolitical ratchet be incorporated into equity sector allocation?** Defense spending, reshoring, and sanctions compliance create permanent winners (defense contractors, domestic manufacturers, compliance technology) that benefit from the same forces driving positive correlation. These sectors may offer "positive correlation alpha" — outperformance that is positively correlated with the structural forces making the macro environment harder for broad equity.

10. **What is the probability-weighted expected path for S&P 500 under the bimodal correlation distribution?** Using the KB's 55-60% Regime D (negative correlation, rho = -0.30 to -0.50) and 40-45% Regime S (positive correlation, rho = +0.20 to +0.40):
    - Regime D scenario: S&P 500 at 5,800-6,200 (current valuations validated, growth supports earnings)
    - Regime S scenario: S&P 500 at 4,500-5,000 (ERP repricing, multiple compression, partial earnings offset from fiscal)
    - Probability-weighted: ~5,200-5,600 (slightly below current levels)
    - The asymmetry favors downside: the positive-correlation scenario produces 15-20% downside while the negative-correlation scenario produces only 5-10% upside from here.
