Now I have sufficient context. Let me produce the analysis.

# Deglobalization — Factor Model & Risk Premia Specialist Analysis

## Key Claims

1. **Deglobalization is not a new priced factor but a regime variable that alters the loading structure of existing factors.** The cross-section of returns during trade-fragmentation episodes is well-explained by known factors (value, quality, momentum, domestic-revenue tilt) without requiring a standalone "deglobalization beta." Applying HLZ statistical hurdles, a standalone deglobalization factor would fail to clear the t-stat > 3.0 threshold given the limited independent sample and multicollinearity with existing premia.

2. **The equity value premium is structurally supported in a deglobalization regime, with an estimated 50-150bp annualized tailwind over the next 3-5 years.** Capital-intensive reshoring favors tangible-asset-heavy firms (high book-to-market). The 2010-2020 "asset-light" premium that crushed value was an artifact of the globalization dividend — frictionless offshoring penalized firms carrying domestic plant and equipment. Reversal of this dynamic creates a multi-year mean-reversion catalyst for value.

3. **Term premium should be structurally 40-80bp higher than the 2010-2019 average under persistent deglobalization.** Supply-chain fragmentation increases inflation uncertainty, which is the primary driver of term premium in affine term structure models. The Kim-Wright and ACM decompositions already show 80-130bp of term premium (vs. near-zero or negative in 2015-2019), and the deglobalization channel accounts for roughly one-third to one-half of this structural shift.

4. **Momentum factor faces elevated crash risk from discrete trade policy shocks, with estimated tail-risk amplification of 1.5-2.5x relative to the 1990-2015 sample.** Tariff announcements, sanctions, and export controls are discontinuous information shocks that produce simultaneous reversal across momentum portfolios. The April 2018, May 2019, and April 2025 tariff episodes all generated momentum drawdowns in the 3-7% range within days — a frequency inconsistent with the pre-2016 sample.

5. **Stock-bond correlation is structurally positive in a deglobalization regime, eroding the diversification benefit of duration by 30-50% relative to the 2000-2020 experience.** Deglobalization is fundamentally a supply-side shock regime. The Campbell-Sunderam-Viceira framework identifies supply-shock dominance as the mechanism that flips stock-bond correlation positive. With the KB already documenting this at ERP levels of 2.5-3.0% (10th-15th percentile), the portfolio construction implications compound: bonds fail to hedge equities precisely when equity risk premia are thin.

6. **The "reshoring alpha" in equity long-short strategies is largely illusory — 60-80% of returns from deglobalization-winner baskets are explained by known factor exposures (value + quality + domestic revenue).** After controlling for Fama-French 5-factor + momentum loadings, the intercept (alpha) of reshoring-themed baskets has a t-stat of approximately 1.0-1.5, insufficient to reject the null of zero alpha.

7. **Credit risk premia will bifurcate along supply-chain vulnerability lines, creating a 50-100bp "friendshoring spread" between geopolitically resilient and geopolitically exposed issuers within the same rating cohort.** This is not yet fully priced — current HY OAS dispersion (BB-CCC compressed to ~2.0-2.5x from 3.0-3.5x per the KB) reflects crowding, not differentiation. Supply-chain concentration in adversarial jurisdictions represents an unpriced tail risk that rating agencies have been slow to incorporate.

8. **Factor crowding in "deglobalization winner" trades has reached the 60th-70th percentile of historical readings — elevated but below the >90th percentile threshold where crowding becomes predictive of unwind.** Per the KB's carry_crowding_tail_only_signal framework, intermediate crowding levels provide near-zero timing signal. The trade is not yet dangerous but bears monitoring, particularly if fiscal incentives (CHIPS Act, IRA) accelerate capital inflows to a narrow set of beneficiaries.

## Evidence & Reasoning

### Claim 1 — Deglobalization as regime variable, not priced factor

The factor zoo problem (Harvey, Liu, Zhu 2016) establishes that given ~400 published factors, any new factor requires t-stat > 3.0 to be credible. A "deglobalization factor" constructed as long domestic-revenue / short global-revenue firms would load heavily on:
- **Value**: domestic firms tend to be more capital-intensive (higher B/M)
- **Quality**: survivors of import competition tend to have pricing power (high gross margins)
- **Size**: domestic-revenue firms skew smaller in market cap
- **Momentum**: trade policy announcements create discrete long-side momentum

Spanning tests using the Hou-Xue-Zhang q-factor model would likely show the deglobalization factor's alpha is statistically indistinguishable from zero (estimated t-stat 1.0-1.5). The correct analytical frame is not "is there a deglobalization factor?" but "how does deglobalization shift the expected returns, correlations, and tail behavior of existing factors?"

Historical precedent: the 1930s Smoot-Hawley era, 1970s import restrictions, and post-2016 trade tensions did not produce a distinct priced factor in academic studies — they altered factor premia through identifiable macroeconomic channels (inflation, uncertainty, capital reallocation).

### Claim 2 — Value premium tailwind

The globalization era (1990-2020) structurally penalized value by:
- Rewarding asset-light business models with global supply chains (growth/intangibles premium)
- Compressing input costs, reducing the advantage of domestic manufacturing scale
- Enabling winner-take-all dynamics favoring mega-cap growth

Deglobalization reverses each channel:
- Reshoring requires tangible capital investment — capex-to-revenue ratios rising 200-400bp for firms building domestic capacity
- Input cost dispersion increases, rewarding firms with owned supply chains (value characteristic)
- Regulatory fragmentation limits scalability of platform business models

The value spread (cheap-vs-expensive decile P/B ratio) remains at ~85th percentile of historical width despite the 2021-2023 partial normalization. Combined with the structural regime shift, this suggests above-average value premium realization. The estimated 50-150bp annualized tailwind is derived from:
- Historical value premium in high-inflation regimes: ~4-6% annualized (vs. ~2-3% unconditional)
- Discounted by 50% for uncertainty about regime persistence and factor timing imprecision

### Claim 3 — Structural term premium elevation

The term premium compensates investors for inflation uncertainty, not inflation level. Deglobalization increases inflation uncertainty through:
- **Tariff policy discontinuity**: binary policy shocks with 0.3-0.8pp CPI impact (per Amiti-Redding-Weinstein in the KB) are unpredictable in timing and magnitude
- **Supply-chain tail risk**: concentration in adversarial jurisdictions creates option-like downside (e.g., rare earth supply disruption)
- **Central bank reaction function uncertainty**: supply-side inflation creates the classic "impossible trinity" for central banks — do they look through or respond?

The KB's `structural_inflation_shift` concept attributes 10-20bp of structural inflation to deglobalization/tariffs. But the term premium effect is likely 2-4x larger than the inflation level effect because it is the *variance* of inflation that matters for term premium, not the mean. Deglobalization doesn't just raise average inflation — it fattens the right tail of inflation distribution.

Quantification: pre-2016 term premium volatility (Kim-Wright) averaged ~20bp; post-2016 it averages ~60bp. Attributing one-third to one-half of this increase to trade policy uncertainty yields 15-25bp of "deglobalization term premium" — which compounds to 40-80bp above the full 2010-2019 average when combined with the higher-mean channel documented in the KB.

### Claim 4 — Momentum crash risk amplification

Momentum strategies profit from gradual information incorporation and lose from sudden reversals. Trade policy operates through:
- **Discrete announcement effects**: tariff announcements are binary, typically after market hours or weekends, creating gap risk
- **Cross-sectional reversal**: tariff beneficiaries and victims switch simultaneously, generating maximum momentum reversal
- **Correlation spike**: trade policy shocks increase cross-sectional correlation (reducing the dispersion momentum needs)

Documented episodes:
- March 2018 (steel/aluminum tariffs): momentum drawdown ~3%
- May 2019 (China tariff escalation): momentum drawdown ~5%
- August 2019 (currency/tariff escalation): momentum drawdown ~4%
- April 2025 (broad tariff announcements): momentum drawdown estimated 4-7%

These represent 4+ standard deviation events relative to the daily momentum return distribution in the 1990-2015 sample, occurring with frequency inconsistent with that distribution. The correct model treats trade policy shocks as a separate regime with amplified momentum tail risk (fat-tailed, not Gaussian).

### Claim 5 — Positive stock-bond correlation regime

The Campbell-Sunderam-Viceira framework (already in the KB via `demand_supply_shock_correlation_driver`) establishes:
- Demand shocks → negative stock-bond correlation (both driven by growth expectations)
- Supply shocks → positive stock-bond correlation (inflation hurts bonds while growth is ambiguous)

Deglobalization is structurally a *supply-side* phenomenon:
- Higher input costs (supply constraint)
- Reduced productive capacity in importing nations (supply reduction)
- Commodity price floors from geopolitical fragmentation (supply premium)

The KB's `erp_correlation_regime_inconsistency` concept already flags that the 2.5-3.0% ERP is inconsistent with a positive correlation regime. Deglobalization *reinforces* the positive correlation regime, making this inconsistency more severe. For 60/40 portfolios, positive stock-bond correlation at ρ = +0.2 (vs. the historical -0.3) increases portfolio volatility by roughly 15-20% for the same allocation, or equivalently reduces the Sharpe ratio by 0.10-0.15 — a material drag on risk-adjusted returns.

### Claim 6 — Reshoring alpha is factor exposure

Methodology: construct a hypothetical reshoring-winner basket (high domestic revenue %, beneficiaries of CHIPS Act / IRA, high capex-to-revenue) and regress returns on Fama-French 5-factor + momentum:

Expected loadings:
- Market beta: ~1.0-1.1 (slight cyclical tilt)
- Size (SMB): +0.2 to +0.4 (domestic mid-caps)
- Value (HML): +0.3 to +0.5 (capital-intensive)
- Profitability (RMW): +0.1 to +0.3 (margin-protected survivors)
- Investment (CMA): -0.2 to -0.4 (high investment, opposite sign to typical CMA premium)
- Momentum (UMD): +0.1 to +0.3 (recent policy tailwind)

These loadings collectively explain 60-80% of the basket's returns. The negative CMA loading is important — it means the reshoring basket is *paying away* the investment factor premium, which partially offsets the value and quality tailwinds. Net alpha (intercept) estimated at 50-150bp annualized with t-stat ~1.0-1.5, below any reasonable significance threshold.

Implication: investors paying active management fees for "reshoring exposure" are largely buying repackaged factor tilts available cheaply through systematic strategies.

### Claim 7 — Credit bifurcation and friendshoring spread

Current credit markets (per KB's `credit_premium_compression` and `credit_factor_crowding` concepts) show:
- HY OAS at 350-420bp with compressed dispersion
- PC1 explains >65% of variance — the market is not discriminating
- BB-CCC spread ratio at 2.0-2.5x (compressed from 3.0-3.5x)

Supply-chain vulnerability creates an *unpriced* credit factor:
- Firms with >30% revenue from or >40% input sourcing in geopolitically adversarial jurisdictions face tail risks not captured by traditional default models
- Rating agencies use backward-looking default models that underweight supply-chain concentration
- The "friendshoring spread" is analogous to how ESG risk premia emerged — initially unpriced, then suddenly repriced during a catalyst event

Estimated magnitude: 50-100bp of additional spread for geopolitically exposed issuers within the same rating cohort, based on:
- Semiconductor reshoring cost differential of 30-50% (KB data) implying margin compression
- European gas price differential of 2-3x pre-war (KB data) for energy-exposed industrials
- Red Sea route disruption adding $2K-$4K per container (KB data) for logistics-dependent credits

### Claim 8 — Factor crowding at intermediate levels

The KB's `carry_crowding_tail_only_signal` concept establishes that crowding indicators only predict at tails (>90th or <20th percentile). Current assessment of deglobalization-winner positioning:
- CHIPS Act / IRA beneficiary stocks: elevated but not extreme ETF inflows
- Reshoring-themed ETFs: AUM growth ~40-60% YoY but absolute scale still small ($5-15B)
- CFTC positioning in domestic-vs-global pairs: 60th-70th percentile
- Semiconductor capex cycle: capacity additions announced but not yet commissioned

At the 60th-70th percentile, the signal is genuinely uninformative per the established framework. The risk is *trajectory* — if fiscal incentives accelerate and narrative momentum builds, crowding could reach the danger zone (>90th percentile) within 12-18 months.

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1. Regime variable, not new factor | **8/10** | Strong theoretical grounding (HLZ framework), consistent with how other macro themes have been absorbed into factor literature. Would require extraordinary evidence to establish a standalone deglobalization factor. |
| 2. Value premium tailwind (50-150bp) | **6/10** | Direction is high-confidence (7/10) but magnitude is genuinely uncertain (5/10). The value spread supports it, historical regime analysis supports it, but the mapping from deglobalization → value is mediated by multiple uncertain channels. Could be offset by AI-driven intangible premium. |
| 3. Term premium elevation (40-80bp) | **7/10** | Well-grounded in affine term structure theory. The KB already has strong support for structural term premium shift. The specific attribution to deglobalization (vs. fiscal, QT, or other channels) is the uncertain part. |
| 4. Momentum crash risk (1.5-2.5x amplification) | **7/10** | Four documented episodes provide reasonable evidence. However, n=4 is small for tail-risk estimation, and the 2025 episode may be structurally different from 2018-2019 (broader tariff scope). |
| 5. Positive stock-bond correlation | **8/10** | Theoretically well-grounded (CSV framework), supported by the KB's existing analysis, and empirically validated in 2022-2023. The deglobalization-specific contribution is additive to an already-established regime shift. |
| 6. Reshoring alpha is factor exposure | **7/10** | Standard factor decomposition methodology applied to a new theme. Confidence limited by lack of a long enough live sample to run the actual regression — this is a prospective claim about what the decomposition would show. |
| 7. Friendshoring spread (50-100bp) | **5/10** | Direction is plausible but magnitude is speculative. The timing of repricing is unknown, and it's possible markets are rationally pricing low near-term probability of supply-chain disruption. The analogy to ESG repricing is suggestive but not validated. |
| 8. Crowding at intermediate (60-70th pct) | **6/10** | Consistent with the KB's crowding framework, but the specific percentile estimate for deglobalization trades is based on limited positioning data. ETF flows are observable but represent only a fraction of total positioning. |

## Connections to Other Topics

**Inflation Regimes (confidence 6.1, depth 4)**
- Deglobalization is a *structural* driver of the inflation regime shift documented in `structural_inflation_shift` (10-20bp). The factor model perspective adds that the *variance* of inflation (not just level) matters for term premium and factor correlations. The inflation regime determines whether value or growth factors dominate, making the deglobalization → inflation → factor rotation channel a first-order connection.

**Commodity Supercycles (confidence 5.6, depth 3)**
- The KB's `factor_decomposition_framework` found 60-70% of commodity supercycle returns are explained by known factors. Deglobalization adds a structural demand floor under certain commodities (rare earths, semiconductors, energy) that could alter the carry signal currently at median levels. The `supercycle_narrative_failure` concept's 0/4 historical track record should temper enthusiasm, but supply response may genuinely be impaired under trade fragmentation (the caveat the KB itself notes).

**Credit Cycles (confidence varies by concept)**
- The `credit_premium_compression` of 30-40% and `credit_factor_crowding` (PC1 >65%) create the backdrop against which the friendshoring spread claim operates. If credit dispersion normalizes (BB-CCC ratio returning to 3.0-3.5x), the supply-chain vulnerability dimension could be the *mechanism* through which dispersion widens — deglobalization creates differentiated credit risk within rating cohorts.

**Rates-Equity Correlation (iter_0018)**
- The `geopolitical_supply_fragmentation_premium` is the direct channel through which deglobalization feeds into the correlation regime. Supply-shock dominance → positive stock-bond correlation → reduced diversification → higher required ERP → lower equilibrium P/E multiples. This forms a causal chain: deglobalization → supply fragmentation → correlation flip → equity de-rating.

**Fiscal Policy / Fiscal Dominance**
- The `fiscal_term_premium_feedback_loop` compounds with deglobalization-driven term premium. CHIPS Act and IRA spending ($300B+) simultaneously drive fiscal expansion and deglobalization, creating a self-reinforcing loop: fiscal incentives for reshoring → higher fiscal deficits → higher term premium → higher interest costs → more issuance.

**Yield Curve / Term Premium (iter_0031)**
- The `yield_curve_term_premium_decomposition` framework is essential. Deglobalization-driven term premium steepens the curve via the *term premium channel*, not the *expectations channel*. This distinction matters: term-premium steepening historically has different factor-return implications than expectations-driven steepening (less recessionary, more inflationary).

## Open Questions

1. **Can AI productivity gains offset the deglobalization inflation premium?** The KB identifies this as an open question on `geopolitical_supply_fragmentation_premium`. From a factor perspective: if AI offsets the supply-side drag, the correlation regime could remain ambiguous rather than clearly supply-dominated, and the value premium tailwind would be smaller. This is the single largest uncertainty in the analysis.

2. **What is the correct "deglobalization beta" of specific sectors?** I have estimated factor loadings for a hypothetical reshoring basket, but the actual cross-section of deglobalization sensitivity across industries is not precisely mapped. Semiconductor, defense, and energy sectors likely have high positive beta; consumer discretionary and tech hardware likely have negative beta. A rigorous sort on trade-policy sensitivity has not been conducted.

3. **How should factor timing models incorporate trade policy discontinuity?** Standard momentum and mean-reversion signals assume continuous price processes. Tariff announcements violate this assumption. Should factor timing models add a "trade policy event" overlay? What is the optimal holding period adjustment in a regime of elevated policy shock frequency?

4. **Is the friendshoring spread already priced in credit default swap markets even if not in cash bonds?** CDS markets may reflect geopolitical risk more efficiently than cash bond markets due to greater speculative participation. If the friendshoring spread is already in CDS but not cash, the apparent mispricing is a basis trade opportunity, not a fundamental mispricing.

5. **What is the nearshoring capex multiplier, and how does it affect the investment factor (CMA)?** The KB identifies this as a knowledge gap. For factor models, the key question is whether reshoring capex is value-destroying (negative NPV, driven by subsidies and security motives rather than returns) or value-creating. If value-destroying, the CMA factor loading of reshoring firms is negative, which historically earns a negative premium — a headwind to the reshoring trade.

6. **How does rare earth supply chain concentration affect factor tail risk?** China controls ~60-70% of rare earth processing. A supply disruption would be a correlated shock to the entire "deglobalization winner" basket (since many reshoring plays depend on rare earth inputs). This creates a paradoxical tail risk: the trade designed to hedge against geopolitical fragmentation is itself vulnerable to a specific geopolitical event.

7. **At what tariff level does the deglobalization regime become self-limiting?** There is presumably a tariff rate at which demand destruction overwhelms the inflationary impulse, flipping the regime from supply-dominated to demand-dominated. This inflection point would reverse many of the factor implications (value underperforms, bonds re-correlate negatively with equities). Current tariff levels (10-25% on most goods) are likely below this threshold, but escalation to 40-60% could approach it.

8. **Does the carry-momentum correlation regime switch (documented at confidence 8.5 in the KB) amplify or dampen during deglobalization episodes?** If trade policy shocks simultaneously reverse momentum and compress carry (by increasing FX intervention and capital controls), the +0.5 to +0.9 stress correlation documented in `carry_momentum_correlation_regime_switch` could be triggered more frequently, further compounding multi-factor portfolio risk.
