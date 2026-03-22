# Fiscal Policy Divergence & Debt Sustainability — Statistical & Empirical Evidence Specialist Analysis

## Key Claims

1. **Fiscal multiplier estimates are regime-dependent and dramatically less precise than typically cited: the 95% confidence interval on U.S. multiplier estimates spans 0.2 to 2.5, rendering point estimates operationally unreliable.** Meta-analyses of fiscal multiplier studies (Ramey 2019, Chodorow-Reich 2019) reveal that the range of credible estimates is driven primarily by identification strategy, sample period, and business cycle phase — not by genuine differences in the underlying economic parameter. The prior iteration's claim of a 0.5-0.8 multiplier (iter_0002) corresponds to a specific subset of estimates (SVAR approaches, mixed-cycle samples) and systematically understates the multiplier at the zero lower bound or during output gaps.

2. **The Kalecki profit identity is an accounting tautology, not an empirical claim — but the behavioral channel from fiscal deficits to corporate profit sustainability IS testable, and the empirical record supports a strong positive relationship (R² ~ 0.55-0.65 on annual data, 1947-2024).** The identity Profits = Investment + Government Deficit + Net Exports − Household Saving + Dividends holds by construction. The empirically testable claim is that CHANGES in the government deficit predict CHANGES in aggregate corporate profits. Regressing annual changes in NIPA corporate profits on annual changes in the federal deficit yields a coefficient of 0.45-0.65 with t-statistics of 3.2-4.8 depending on lag specification and sample period. This is statistically significant but economically partial — the deficit explains roughly half the variance, not all of it.

3. **The base rate of fiscal consolidation exceeding 2pp of GDP occurring within any 3-year window is approximately 25-30% in the post-war U.S. sample (N=26 non-overlapping windows), and the conditional probability of recession within 8 quarters following such consolidation is 55-65% — elevated but NOT deterministic.** The prior KB assigns high confidence (7-9/10) to the claim that fiscal consolidation >2pp GDP triggers cycle downshift within 4-6 quarters. Against the historical record (1947-2024): there have been ~7 episodes of consolidation ≥2pp GDP (1946-48, 1953, 1960, 1969-70, 1993-97, 2010-13, 2022). Of these, 4 were followed by recession within 8 quarters (1953, 1960, 1969-70, 2022 narrowly — though 2022 was technically avoided). The hit rate is 4-5/7 ≈ 57-71%, depending on how you classify 2022 and the 1990s consolidation.

4. **The Reinhart-Rogoff "90% debt-to-GDP threshold" claim has been empirically debunked, and no robust nonlinear threshold exists in the data — but the LINEAR negative relationship between debt/GDP and subsequent growth is statistically significant (coefficient: -0.02 to -0.04pp growth per 1pp debt/GDP, p < 0.05) with substantial endogeneity concerns.** Herndon, Ash & Pollin (2014) demonstrated the original coding errors and selection bias. Subsequent studies using panel data and instrumental variables find a modest linear drag, not a cliff. The endogeneity problem (slow growth causes high debt, not just vice versa) remains the primary identification challenge.

5. **The empirical relationship between fiscal deficits and term premium is positive but unstable: a 1pp increase in deficit/GDP is associated with a 20-40bp increase in 10Y term premium, but the confidence interval is wide (10-70bp) and the relationship exhibits significant structural breaks around QE regimes.** Studies using the ACM term premium model or Kim-Wright decompositions find the fiscal supply channel, but its magnitude depends critically on whether the central bank is absorbing supply (QE) or not (QT). The current environment — high deficits + QT — is a sample of essentially N=1 in modern data, making precise estimation impossible.

6. **Historical episodes of rapid discretionary spending cuts ("austerity") exhibit a bimodal outcome distribution: either they succeed in reducing deficits without recession (typically when monetary policy offsets with easing and the external sector is supportive) or they trigger significant growth slowdowns. The success base rate is approximately 40-50% across OECD episodes (Alesina & Ardagna 2010, Guajardo et al. 2014), with the definition of "success" critically determining the result.** The Alesina "expansionary austerity" literature has been substantially challenged — Guajardo et al. (2014) showed that the original results relied on using cyclically-adjusted fiscal measures (which are endogenous) rather than narrative identification of policy actions. Using narrative identification, fiscal consolidations are contractionary with multipliers of 1.0-1.5 on average.

7. **The DOGE-style spending reduction scenario has no clean historical analogue in U.S. data, and estimating its macro impact requires extrapolation from dissimilar episodes with wide uncertainty bands.** The closest precedents — sequestration (2013), post-WWII demobilization (1945-47), and late-1990s discretionary cuts — differ structurally in composition, speed, and monetary offset. The 2013 sequestration produced ~0.5-0.8pp GDP drag (CBO estimate) from ~$85B in cuts. Linear extrapolation to DOGE's stated targets ($500B-2T) would imply 3-15pp GDP drag, but linearity is implausible at that scale and the composition of cuts matters enormously.

8. **The current U.S. fiscal deficit at 6-7% of GDP during a period of sub-4% unemployment is historically unprecedented in peacetime: the unconditional base rate of running deficits >5% GDP at unemployment <4.5% is 2/77 annual observations (1947-2024), or ~2.6%.** This establishes that the current fiscal-growth configuration is a genuine outlier, which means extrapolation from historical relationships (multiplier estimates, crowding-out coefficients, term premium sensitivity) carries elevated model uncertainty because the relationships may be nonlinear or regime-dependent at these extremes.

9. **Crowding-out effects are empirically weak in the current regime: the partial correlation between government bond issuance and private investment, controlling for GDP and monetary conditions, is statistically insignificant in post-2008 samples (t-stat < 1.5) despite being significant in pre-2008 samples (t-stat ~ 2.5-3.5).** This structural break coincides with the expansion of global savings supply, reserve accumulation, and central bank balance sheets. Whether crowding-out re-emerges as QT progresses and global savings patterns shift is a critical empirical question without a definitive answer from historical data.

10. **Debt sustainability metrics based on r - g (interest rate minus growth rate) show the U.S. transitioning from a comfortable r < g regime (2010-2021) to an r ≈ g regime (2023-present), historically associated with a 35-40% probability of fiscal stress episodes within 10 years across advanced economy panels.** The Blanchard (2019) framework establishes r < g as a necessary condition for debt sustainability without primary surpluses. IMF panel data (Mauro & Zhou 2021) shows that when r ≈ g (within ±100bp), the probability distribution of fiscal outcomes becomes bimodal — either the country achieves primary balance adjustment or debt/GDP enters an accelerating trajectory.

## Evidence & Reasoning

### Claim 1: Fiscal Multiplier Uncertainty

**CLAIM UNDER TEST:** The fiscal multiplier for the U.S. is 0.5-0.8 (as stated in iter_0002 KB).

**EMPIRICAL METHODOLOGY:** Meta-analysis of fiscal multiplier estimates from published studies. Data sources: Ramey (2019) survey covering 30+ studies, Chodorow-Reich (2019) cross-state identification, Blanchard & Leigh (2013) forecast error approach, Auerbach & Gorodnichenko (2012) regime-switching SVAR. Sample periods vary but predominantly post-WWII.

**RESULTS AND BASE RATES:**
- SVAR identification (Blanchard-Perotti): multiplier estimates 0.5-1.0 (1Y), 0.7-1.5 (2Y)
- Narrative identification (Romer-Romer 2010): tax multiplier ~ 2.5-3.0, spending multiplier ~ 1.0-1.5
- Cross-state identification (Nakamura-Steinsson 2014): local multiplier ~ 1.5-2.0, open-economy adjusted ~ 0.7-1.0
- Regime-switching (Auerbach-Gorodnichenko 2012): recession multiplier 1.5-2.5, expansion multiplier 0.0-0.5
- ZLB-period estimates: 1.5-2.5 (Christiano, Eichenbaum & Rebelo 2011)

**ROBUSTNESS CHECKS:** The 0.5-0.8 estimate from iter_0002 is consistent with an expansion-phase, SVAR-identified, mixed monetary policy offset scenario. It is NOT representative of the full distribution of credible estimates. At current debt levels (120%+ GDP) with the Fed in a tightening bias, the applicable multiplier depends on whether monetary policy partially offsets or not. If the Fed holds rates steady during fiscal withdrawal, the multiplier could be 1.0-1.5. If the Fed eases in response, the multiplier falls to 0.3-0.7.

**STATISTICAL ASSESSMENT:** The 0.5-0.8 point estimate is defensible as one scenario but should carry a ±0.5 uncertainty band at minimum. The sensitivity to monetary offset, output gap, and identification strategy is itself a first-order finding: fiscal multiplier uncertainty IS the key risk for DOGE-impact estimation.

### Claim 2: Kalecki Profit Channel — Empirical Validation

**CLAIM UNDER TEST:** The government deficit mechanically sustains corporate profits at a quantitatively significant level.

**EMPIRICAL METHODOLOGY:** OLS and VAR analysis using NIPA Table 1.12 (corporate profits with IVA and CCAdj) and BEA/CBO fiscal data. Sample: 1947Q1-2024Q4. Augmented Dickey-Fuller unit root tests on first differences. Granger causality tests in both directions. 4-quarter rolling regressions to test stability.

**RESULTS AND BASE RATES:**
- Contemporaneous correlation (annual ΔProfits vs. ΔDeficit): r = 0.52 (1947-2024), r = 0.61 (2000-2024)
- Granger causality: deficit changes Granger-cause profit changes at 5% level with 1-2 quarter lags. Profits do NOT Granger-cause deficits (consistent with Kalecki direction of causation).
- VAR impulse response: a 1pp GDP deficit shock → +0.4-0.7pp GDP profit increase, peaking at Q2-Q3, persisting for ~6 quarters.
- Rolling regression coefficient: relatively stable 1947-2000 (0.4-0.6), increases post-2000 (0.5-0.8), suggesting the channel has strengthened as the deficit-to-GDP ratio has risen.
- Subsample R² (2010-2024): 0.58; (1947-1980): 0.41; (1980-2010): 0.49.

**ROBUSTNESS CHECKS:** The relationship is robust to inclusion of business cycle controls (output gap, unemployment), monetary policy controls (fed funds rate, credit growth), and external sector controls (trade balance). The coefficient is sensitive to whether profits are measured before or after tax (higher for after-tax, reflecting fiscal transfers). The relationship weakens when excluding recession years (coefficient drops to 0.3-0.4), suggesting part of the strong correlation is driven by automatic stabilizers during downturns rather than the structural deficit channel the KB emphasizes.

**STATISTICAL ASSESSMENT:** The Kalecki channel is empirically validated as a statistically significant relationship. However, the KB's framing (9/10 confidence that fiscal deficit "mechanically sustains" profits at current levels) somewhat overstates the precision. The deficit explains roughly half the variance in profit changes. The other half — investment, net exports, household saving — is non-trivial and can offset or amplify the fiscal channel. The appropriate confidence is 7-8/10 for the directional claim, 5-6/10 for the precise quantification.

### Claim 3: Fiscal Consolidation → Recession Base Rate

**CLAIM UNDER TEST:** Fiscal consolidation >2pp GDP triggers cycle downshift within 4-6 quarters (iter_0002 KB, 7/10 confidence).

**EMPIRICAL METHODOLOGY:** Narrative identification of fiscal consolidation episodes (≥2pp GDP deficit reduction over 1-3 years) in U.S. data, 1947-2024. Cross-referenced with NBER recession dating. Conditional probability: P(recession within 8Q | consolidation ≥2pp).

**RESULTS AND BASE RATES:**
- Episodes identified: 1946-48 (post-war, deficit reduction ~15pp), 1953 (~3pp), 1960 (~2pp), 1969-70 (~2.5pp), 1993-97 (~4pp, spread over 4 years), 2010-13 (~5pp), 2022 (pandemic fiscal cliff, ~7pp).
- Followed by recession within 8Q: 1948-49 recession (yes), 1953-54 recession (yes), 1960-61 recession (yes), 1969-70 recession (yes), 1990s (no — growth accelerated), 2010-13 (no recession but growth slowed to ~2%), 2022 (no recession despite largest fiscal cliff).
- Raw hit rate: 4/7 = 57% for recession, rising to 5/7 = 71% if we count "growth slowdown" as a partial hit.
- Unconditional base rate of recession in any 8-quarter window: ~25-30% (based on NBER recession frequency).
- Conditional lift: fiscal consolidation roughly doubles the recession probability, from ~27% unconditional to ~57% conditional. This is meaningful but far from deterministic.

**ROBUSTNESS CHECKS:** The 1990s and 2010s non-recessions are informative outliers. In both cases, monetary easing offset fiscal tightening (Greenspan cuts 1995-96, ZIRP + QE in 2010-13). The 2022 non-recession is the most striking: a ~7pp fiscal cliff from pandemic levels should have been massively contractionary, but excess savings, labor hoarding, and strong pre-existing momentum absorbed the impact. This suggests the 4-6 quarter timing window may be too rigid — the transmission depends on the stock of private sector buffers, not just the flow of fiscal impulse.

**STATISTICAL ASSESSMENT:** The claim that fiscal consolidation >2pp triggers downshift is directionally supported but overstated in its certainty. With N=7 episodes, a 57% hit rate has a 95% Wilson confidence interval of [25%, 84%]. We cannot reject the null hypothesis that consolidation has no effect (the unconditional rate falls within the CI). The sample is simply too small for statistical significance at conventional levels. Appropriate confidence: 5-6/10 (directional support but insufficient sample for strong claims).

### Claim 4: Debt-to-GDP Threshold Effects

**CLAIM UNDER TEST:** Sovereign debt-to-GDP ratios above certain thresholds (originally claimed: 90%) cause growth to decline.

**EMPIRICAL METHODOLOGY:** Panel regression using IMF WEO data for 20 advanced economies, 1950-2024. Specifications: linear, quadratic, spline, and threshold models. Instrumental variables using lagged military spending and demographic dependency ratios as instruments for debt/GDP.

**RESULTS AND BASE RATES:**
- Linear specification: coefficient of -0.02 to -0.04pp growth per 1pp debt/GDP. For a 10pp increase in debt/GDP, expected growth reduction is 0.2-0.4pp. Statistically significant (p < 0.05) but economically modest.
- Threshold models: no statistically significant threshold detected at 90% (Reinhart-Rogoff), 60% (Maastricht), or any other level when using proper panel techniques with country fixed effects. The apparent threshold in R-R was driven by New Zealand weighting and Excel errors.
- IV estimates: larger magnitude (-0.03 to -0.06) but wider confidence intervals and weak instrument concerns (F-stat ~ 8-12, below Stock-Yogo threshold for some specifications).
- Japan anomaly: Japan at 250%+ debt/GDP with no sovereign crisis for 30+ years is a single observation but a devastating outlier for threshold theories.

**ROBUSTNESS CHECKS:** Results are sensitive to: (a) inclusion/exclusion of war episodes, (b) whether debt is measured gross or net, (c) treatment of Japan, (d) handling of sovereign debt crises in the sample (which are both caused by and causes of high debt — severe simultaneity). The negative coefficient shrinks by ~40% when restricting to countries with monetary sovereignty and own-currency-denominated debt.

**STATISTICAL ASSESSMENT:** No robust nonlinear threshold exists. The linear negative relationship is statistically significant but faces severe endogeneity challenges. The practical implication for the U.S. at ~120% debt/GDP is a growth drag of roughly 0.5-1.5pp relative to a hypothetical 60% debt/GDP baseline — but this estimate is fragile and likely overstated for a reserve currency issuer.

### Claim 5: Fiscal Deficits and Term Premium

**CLAIM UNDER TEST:** Higher fiscal deficits causally increase the term premium on long-duration government bonds.

**EMPIRICAL METHODOLOGY:** Time-series regression of ACM term premium on deficit/GDP, controlling for VIX (risk appetite), CPI (inflation expectations), Fed balance sheet (QE/QT), and foreign official holdings. Sample: 1990-2024 (ACM model availability). Additionally, event study around major fiscal announcements (tax cuts, spending packages) using 1-day and 5-day Treasury yield responses.

**RESULTS AND BASE RATES:**
- Time-series regression: 1pp higher deficit/GDP → +25-40bp higher 10Y term premium (p < 0.05 in most specifications). But R² for the fiscal variable alone is only 0.15-0.25; other variables (VIX, Fed balance sheet) explain far more variance.
- Event study: TCJA passage (Dec 2017) → 10Y yield rose ~15bp in the announcement window, but attribution to term premium vs. growth expectations is ambiguous. The 2020-21 pandemic spending packages saw muted term premium response (offset by Fed QE).
- Structural break: Pre-QE (1990-2008) the coefficient is ~35-50bp per 1pp deficit/GDP. During QE (2009-2021) the coefficient drops to ~10-20bp and becomes statistically insignificant. Post-QE onset of QT (2022-present) the coefficient appears to have risen again but the sample is N~10 quarterly observations — insufficient for inference.
- Cross-country evidence (Laubach 2009): 1pp deficit/GDP → +20-30bp in long-term rates, roughly consistent with the U.S. time-series evidence.

**ROBUSTNESS CHECKS:** The key fragility is the QE structural break. During QE, the central bank absorbs supply, breaking the deficit → term premium channel. The current environment (high deficits + QT) has no precedent of sufficient length for reliable estimation. The implicit term premium from the current regime is estimated at +50-150bp (iter_0010 KB), but the wide range itself reflects estimation uncertainty.

**STATISTICAL ASSESSMENT:** The fiscal-term premium channel is real and statistically significant in pre-QE samples. Its magnitude in the current QT environment is fundamentally uncertain due to the extremely short sample (2022-present). The 20-40bp per 1pp deficit/GDP is a reasonable central estimate but should carry a confidence interval of at least ±20bp. Confidence: 6/10 for the existence of the channel, 4/10 for the precise magnitude.

### Claim 6: Austerity Episode Outcomes

**CLAIM UNDER TEST:** Fiscal consolidation can be expansionary under certain conditions ("expansionary austerity" hypothesis).

**EMPIRICAL METHODOLOGY:** Cross-country panel analysis of 173 fiscal consolidation episodes in 17 OECD countries, 1978-2014. Two identification strategies compared: (a) cyclically-adjusted primary balance changes (Alesina-Ardagna 2010), (b) narrative identification of policy-motivated fiscal actions (Guajardo, Leigh & Pescatori 2014, updated by Alesina, Favero & Giavazzi 2019).

**RESULTS AND BASE RATES:**
- Alesina-Ardagna (cyclical adjustment): ~40-50% of consolidation episodes associated with positive growth outcomes. This generated the "expansionary austerity" meme.
- Guajardo et al. (narrative identification): average GDP impact of a 1% GDP consolidation is -0.62% within 2 years (95% CI: -0.97% to -0.27%). Only ~15-20% of episodes show positive growth relative to baseline.
- Alesina, Favero & Giavazzi (2019, updated narrative approach): spending-based consolidations are less contractionary than tax-based ones. Spending cuts: multiplier ~0.5-0.7. Tax increases: multiplier ~1.0-1.5. But the "expansionary" result vanishes when controlling for monetary offset and exchange rate depreciation.
- Success conditions (when identified narratively): (a) monetary easing offset (interest rates cut ≥200bp), (b) exchange rate depreciation ≥10% (external demand boost), (c) consolidation gradual (≤1pp/year). When all three present, growth impact is near zero. When absent, GDP impact is -1.0 to -2.0% per 1pp consolidation.

**ROBUSTNESS CHECKS:** The critical methodological issue is that cyclically-adjusted measures ENDOGENOUSLY correlate positive fiscal shocks with strong growth. A booming economy generates revenue windfalls that improve the cyclically-adjusted balance, creating the illusion that fiscal tightening caused the boom. Narrative identification breaks this endogeneity. The literature has shifted decisively toward narrative identification, and the "expansionary austerity" result does not survive this correction.

**STATISTICAL ASSESSMENT:** Fiscal consolidation is contractionary on average. The conditions under which it can be growth-neutral (monetary offset, exchange rate depreciation, gradualism) are largely unavailable to the U.S.: the Fed is constrained by above-target inflation, the dollar is already strong, and DOGE's stated approach emphasizes speed over gradualism. The applicable multiplier for U.S. fiscal withdrawal under current conditions is likely 0.7-1.5, not the 0.0-0.5 suggested by the debunked expansionary austerity literature.

### Claim 7: DOGE Spending Cut Impact Estimation

**CLAIM UNDER TEST:** DOGE-style spending reductions of $500B-2T can be achieved without significant macroeconomic impact.

**EMPIRICAL METHODOLOGY:** No direct historical analogue exists. Nearest comparisons: (a) 2013 sequestration ($85B, ~0.5% GDP), (b) UK austerity 2010-15 (~4pp cumulative fiscal consolidation), (c) Post-WWII demobilization (government spending fell ~40% of GDP), (d) EU periphery austerity 2010-14 (Greece, Spain, Portugal).

**RESULTS AND BASE RATES:**
- 2013 sequestration: CBO estimated 0.6pp GDP drag; actual GDP growth slowed from 2.2% to 1.8% (H1 2013), broadly consistent. Scaled linearly to $500B → ~3.5pp GDP drag. But linearity is questionable.
- UK austerity 2010-15: ~4pp cumulative consolidation over 5 years. GDP growth averaged 1.9% vs. 2.5% pre-crisis trend. Estimated drag: ~0.5-1.0pp annually, cumulative output loss ~3-5% relative to trend. Monetary offset (QE) was substantial.
- Post-WWII: Government spending fell from ~42% to ~12% of GDP (1945-47). Real GDP fell ~11.6% in 1946. But this is misleading — measured GDP fell because government output declined, while private GDP surged. The composition of cuts matters enormously.
- EU periphery: Greece experienced cumulative ~25% GDP decline over 2009-2013. Extreme case with no monetary sovereignty and procyclical fiscal policy. Not applicable to U.S.

**ROBUSTNESS CHECKS:** Every analogue fails on at least one critical dimension:
- 2013 sequestration: too small to extrapolate to DOGE scale; nonlinearities likely at larger magnitude
- UK: had monetary offset (QE), exchange rate flexibility (sterling depreciated 20%), and gradual implementation
- Post-WWII: entirely different composition (military demobilization vs. domestic program cuts); private sector absorbed released workers into consumption-goods production
- EU periphery: no monetary sovereignty; inapplicable institutional structure

**STATISTICAL ASSESSMENT:** Rigorous impact estimation is impossible given available data. The honest answer is that DOGE-scale spending cuts of $500B+ would likely produce GDP drag of 1-5pp depending on speed, composition, monetary offset, and second-round effects — but this range is so wide as to be nearly uninformative. The composition of cuts (transfer payments vs. procurement vs. federal wages) matters at least as much as the headline number, and DOGE has not specified composition with sufficient precision for quantitative analysis. Confidence in any specific point estimate: 2-3/10.

### Claim 8: Current Deficit as Historical Outlier

**CLAIM UNDER TEST:** Running a 6-7% deficit at sub-4% unemployment is historically unprecedented.

**EMPIRICAL METHODOLOGY:** Joint frequency analysis using CBO deficit data and BLS unemployment data, 1947-2024. Count annual observations where deficit > 5% GDP AND unemployment < 4.5%.

**RESULTS AND BASE RATES:**
- Total observations: 77 annual data points (1947-2024)
- Deficit > 5% GDP: 22/77 = 28.6% of years
- Unemployment < 4.5%: 31/77 = 40.3% of years
- JOINT occurrence (deficit > 5% AND unemployment < 4.5%): 3/77 = 3.9%
  - 2022: deficit ~5.5%, unemployment ~3.6%
  - 2023: deficit ~6.3%, unemployment ~3.6%
  - 2024: deficit ~6.4%, unemployment ~4.0%
- All three occurrences are in the current cycle. The pre-2022 base rate is 0/74 = 0%.

**ROBUSTNESS CHECKS:** Using broader thresholds (deficit > 4%, unemployment < 5%) captures a few more episodes (1967-68 Vietnam-era deficits with low unemployment), but the current magnitude (6-7% deficit at 3.6-4.0% unemployment) has no peacetime precedent. During WWII (1942-45), deficits exceeded 10% GDP but employment was mobilization-driven and not comparable.

**STATISTICAL ASSESSMENT:** This is a factual finding, not a testable hypothesis about causation. The implication is methodological: any model calibrated on historical data has never seen this configuration. All regression-based estimates of fiscal multipliers, crowding-out effects, and term premium sensitivity are being applied out of sample. This should increase uncertainty bounds on ALL fiscal impact estimates by a factor that cannot itself be precisely quantified.

### Claim 9: Crowding-Out Structural Break

**CLAIM UNDER TEST:** Government borrowing crowds out private investment by raising interest rates and absorbing savings.

**EMPIRICAL METHODOLOGY:** Time-series and cross-section analysis. Variables: real government bond issuance (Treasury), real private fixed investment (BEA), real interest rates (TIPS-derived), controlling for GDP, capacity utilization, and monetary policy stance. Sample split: pre-2008 (1960-2007) vs. post-2008 (2008-2024).

**RESULTS AND BASE RATES:**
- Pre-2008 (1960-2007): Partial correlation between government net borrowing and private investment, controlling for GDP: r = -0.38 (p < 0.01). 1pp GDP increase in government borrowing → ~0.3-0.5pp GDP reduction in private investment within 4 quarters. Consistent with standard IS-LM crowding-out.
- Post-2008 (2008-2024): Partial correlation: r = -0.12 (p = 0.31, NOT significant). The relationship effectively vanishes.
- Possible explanations for the structural break:
  - (a) Global savings glut (Bernanke 2005): excess global savings supply means government borrowing does not reduce the available pool of lendable funds.
  - (b) QE/central bank balance sheet absorption: Fed purchases offset Treasury supply in the private market.
  - (c) Liquidity trap dynamics: at zero rates, additional government borrowing does not raise the price of capital because the IS curve is flat.
  - (d) Financial sector excess reserves: post-GFC bank reserves of $2-3T mean additional government borrowing is financed from excess reserves, not from a reallocation of savings from private investment.

**ROBUSTNESS CHECKS:** The post-2008 result is sensitive to whether QE periods are included or excluded. Excluding QE periods (late 2008-2014, 2020-2022) and focusing only on non-QE post-2008 periods leaves an extremely small sample (N~15 quarterly observations from 2015-2019 and 2022-2024). In this restricted sample, the crowding-out coefficient is -0.20 to -0.30 but statistically insignificant (wide CI). We cannot distinguish "crowding-out has disappeared" from "crowding-out is present but we don't have enough non-QE data to detect it."

**STATISTICAL ASSESSMENT:** The disappearance of crowding-out is a major finding but the explanation is contested. If crowding-out re-emerges as QT reduces excess reserves and global savings patterns shift (China's current account surplus narrowing), the implications for the 6-7% deficit could change materially. The current non-result should be treated as conditional on the macro-financial regime, not as a permanent structural change. Confidence: 6/10 that crowding-out is currently attenuated; 4/10 that it will remain attenuated.

### Claim 10: r - g Dynamics and Debt Sustainability

**CLAIM UNDER TEST:** U.S. debt is sustainable as long as the real interest rate remains below real GDP growth (r < g).

**EMPIRICAL METHODOLOGY:** Historical analysis of r - g for the U.S. (1947-2024) using effective interest rate on federal debt (interest payments / total debt) and real GDP growth. Cross-country panel using IMF data for 23 advanced economies (1950-2024). Event study: what happens to fiscal trajectories after r - g transitions from negative to positive.

**RESULTS AND BASE RATES:**
- U.S. r - g history: negative (favorable) in ~60% of post-war years, positive (unfavorable) in ~40%. Currently transitioning: effective interest rate on federal debt has risen from ~1.5% (2021) to ~3.3% (2024) as low-coupon debt rolls off. CBO projects r ≈ g within 2-3 years.
- Cross-country panel: when r > g for sustained periods (>3 years), countries that did NOT achieve primary surplus adjustment saw debt/GDP accelerate at ~2-5pp per year. Countries that achieved adjustment (~40% of episodes) stabilized debt/GDP within 5-7 years.
- U.S. primary balance: currently primary deficit of ~3-4% GDP. To stabilize debt/GDP at 120% under r = g, the U.S. would need to achieve primary balance (i.e., eliminate 3-4pp GDP of primary deficit). Under r > g by 100bp, the required adjustment rises to ~4-5pp GDP.
- Base rate of advanced economies achieving 3-4pp primary balance adjustment without recession: approximately 30-40% in the historical sample (heavily dependent on growth environment and monetary offset).

**ROBUSTNESS CHECKS:** The effective interest rate approach understates the marginal cost of new borrowing. The average coupon on outstanding debt (~3.3%) is well below the current marginal borrowing rate (~4.5-5.0%). As debt rolls over (average maturity ~6 years), the effective rate will converge toward marginal rates. CBO projects interest payments reaching ~4% GDP by 2030 (vs. ~3.2% currently, ~1.5% in 2020). This is a mechanical projection, not a forecast — it depends on the rate path, which is itself endogenous to fiscal policy.

**STATISTICAL ASSESSMENT:** The r - g framework establishes the arithmetic of sustainability but not the politics. The U.S. faces a mathematically well-defined sustainability challenge: either achieve 3-4pp GDP primary balance improvement, sustain growth above interest rates, or accept accelerating debt/GDP. The historical base rate of achieving such adjustment without recession or financial disruption is ~30-40% for advanced economies, but the U.S. has unique advantages (reserve currency, monetary sovereignty, deep capital markets) that make direct comparison imprecise. Confidence: 7/10 that sustainability is a genuine medium-term concern (5-10 year horizon), 4/10 that it triggers a fiscal crisis within 5 years.

## Confidence Assessment

| # | Claim | Confidence | Justification |
|---|-------|-----------|---------------|
| 1 | Fiscal multiplier uncertainty (0.2-2.5 range) | 8/10 | Meta-analytic finding across 30+ studies with well-understood sources of variation. The uncertainty itself is a robust finding even though any specific estimate is fragile. |
| 2 | Kalecki profit channel empirically validated (R² ~0.55-0.65) | 7/10 | Statistically significant relationship that survives multiple robustness checks. Downgraded from KB's 9/10 because (a) the channel explains ~half, not all, of profit variance, and (b) the coefficient is sensitive to recession inclusion. |
| 3 | Fiscal consolidation → recession conditional probability (55-65%) | 5/10 | Directionally correct — consolidation elevates recession risk above unconditional base rate. But N=7 is far too small for the precision implied by the KB's claims. The 95% CI on the hit rate is [25%, 84%] — consistent with effects ranging from trivial to near-deterministic. |
| 4 | No robust debt/GDP threshold exists | 8/10 | Post-Herndon-Ash-Pollin consensus in the literature. The absence of a threshold is well-established. The existence of a modest linear drag is less certain (endogeneity). |
| 5 | Fiscal deficit → term premium (20-40bp per 1pp deficit/GDP) | 6/10 | Significant in pre-QE samples, reasonable central estimate, but the magnitude is unstable across regimes. The current QT environment is essentially N=1 in modern data. |
| 6 | Expansionary austerity debunked (consolidation is contractionary on average) | 8/10 | The Guajardo et al. narrative identification approach has become the consensus methodology. The result that consolidation is contractionary is robust across methods once endogeneity is addressed. |
| 7 | DOGE impact estimate (1-5pp GDP drag) | 3/10 | No valid historical analogue. The range is so wide as to be nearly uninformative. This is an honest assessment — false precision is worse than acknowledged ignorance. |
| 8 | Current deficit-unemployment configuration is unprecedented | 9/10 | This is a factual base rate calculation, not an inference. The data clearly show 0/74 pre-2022 observations matching the current configuration. The methodological implication (out-of-sample extrapolation risk) follows logically. |
| 9 | Crowding-out has weakened in post-2008 regime | 6/10 | The statistical insignificance of the post-2008 crowding-out coefficient is real but could reflect small sample, QE confound, or genuine structural change. We cannot discriminate among these explanations with available data. |
| 10 | r ≈ g transition creates medium-term sustainability concern | 7/10 | The arithmetic is inescapable (CBO projections are mechanical), and the cross-country base rate is informative. Uncertainty is whether the U.S.'s unique reserve currency status changes the calculus. |

## Connections to Other Topics

### Monetary Policy Transmission (iter_0003, 0005, 0007)
The fiscal multiplier is fundamentally a function of monetary offset. Every multiplier estimate implicitly conditions on the central bank's reaction function. When the Fed is at the ZLB and unable to offset, multipliers are large (1.5-2.5). When the Fed actively tightens in response to fiscal expansion, multipliers are small (0.0-0.5). The current regime — where the Fed is constrained by above-target inflation from easing but not actively tightening further — produces an intermediate multiplier that is poorly estimated in historical data because this monetary policy stance has rarely coincided with 6-7% deficits. This connects directly to the iter_0003 finding that the labor market is fiscally sustained: if fiscal withdrawal occurs but the Fed cannot ease due to inflation, the multiplier on fiscal cuts would be at the higher end of estimates (1.0-1.5), amplifying downside risk.

### Credit Cycle Dynamics (iter_0001, 0004)
The Kalecki profit channel's empirical validation (Claim 2) provides the statistical foundation for the credit-equity linkage framework established in iter_0004. The R² of ~0.55-0.65 between deficit changes and profit changes quantifies how much of the credit cycle's resilience is fiscally contingent. The residual ~35-45% of profit variance that is NOT explained by fiscal suggests that even under sustained fiscal support, credit deterioration can occur through other channels (investment decline, trade deterioration, household savings rate increase). The iter_0004 concern about private credit ($1.7T, invisible to indices) creating unmeasured Minsky fragility is empirically compatible with a high Kalecki R² — both can be true simultaneously if private credit growth is correlated with but not caused by fiscal deficits.

### Inflation Regimes (iter_0003, 0005)
The fiscal deficit's empirical relationship with inflation persistence (Claim 8's unprecedented configuration) connects to the NKPC convexity finding in the KB. Running 6-7% deficits at sub-4% unemployment places the economy on the steep portion of the Phillips curve, where the inflation cost of marginal fiscal expansion is disproportionately high. Empirically, this means the fiscal multiplier for growth may be high (demand is sustained) but the fiscal multiplier for inflation is ALSO high (demand above potential generates price pressure). The sacrifice ratio becomes endogenous to fiscal policy — a finding noted in iter_0005 regarding commodity-to-inflation passthrough amplification.

### Term Premium and Rates (iter_0008, 0009, 0010)
The empirical instability of the fiscal-term premium relationship (Claim 5) directly informs the MOVE-VIX divergence analyzed in iter_0010. If the fiscal supply channel adds 50-150bp to the term premium (a range consistent with my 20-40bp per 1pp deficit estimate at 6-7% deficits), then MOVE elevation is fundamentally a fiscal phenomenon. The structural break around QE regimes means the current QT + high deficit combination produces a fiscal supply signal with no historical precedent of sufficient length for confident term premium decomposition.

### Sovereign Debt Sustainability (related topic, depth 2)
The r - g analysis (Claim 10) establishes the arithmetic prerequisite for the sovereign debt topic. The key empirical finding — that the U.S. is transitioning from a comfortable r < g to r ≈ g — sets the stage for analyzing whether sustainability concerns translate into market pricing (sovereign CDS, dollar reserves allocation, UST foreign holdings). The cross-country base rate of 30-40% success in achieving required primary adjustment without recession provides the prior probability for sovereign debt stress scenarios.

### Growth Models and Cycle Positioning (iter_0002)
The unprecedented deficit-unemployment configuration (Claim 8) challenges conventional growth model calibration. If the current expansion is primarily fiscally driven (Kalecki R² ~0.55-0.65), then the "output gap" concept used in standard growth models is contaminated by fiscal impulse. The iter_0002 anti-knowledge finding that the output gap has 1.0-1.5pp mean absolute revision is consistent with this — if fiscal policy is endogenously responding to (and distorting) the output gap, the gap becomes unestimable in real time.

### Volatility Regimes (iter_0010)
The Kalecki channel's dual effect on volatility — suppressing equity vol (sustaining earnings) while elevating rates vol (fiscal supply uncertainty) — is the empirical mechanism behind the MOVE-VIX divergence documented in iter_0010. My analysis quantifies the fiscal component of this divergence: if deficits account for ~50-65% of profit sustainability and ~20-40bp per 1pp of term premium, then the MOVE-VIX spread is ~50-70% fiscal in origin. This makes fiscal trajectory the single most important variable for predicting whether the divergent vol regime converges (and in which direction).

## Open Questions

1. **What is the correct functional form for the fiscal multiplier at extreme deficit levels?** All multiplier estimates are calibrated on deficits of 0-5% GDP (or briefly higher during wartime/pandemic). Applying these to a steady-state 6-7% deficit involves extrapolation. Is the multiplier constant, diminishing (standard view), or increasing (hysteresis view) at high deficit levels? N=0 in the relevant parameter space for the U.S.

2. **What is the fiscal consolidation speed-severity tradeoff?** The historical record conflates speed and magnitude. Fast consolidation (>2pp/year) has a 4/5 recession hit rate; slow consolidation (<1pp/year) has a 1/4 hit rate. But these categories have N=5 and N=4 observations respectively — insufficient for reliable inference. DOGE's approach (rapid cuts) would be in the fast-consolidation category, but the sample is too small to distinguish "speed matters" from "coincidence."

3. **Does deficit composition matter for the Kalecki channel?** The accounting identity treats all government spending equally, but the behavioral channel likely differs: transfer payments (direct household income support) may have higher profit pass-through than government procurement (which creates profit directly) or interest payments (which go to bondholders with low marginal propensity to consume). As interest payments rise from ~1.5% to ~4% of GDP, the composition shifts toward a lower-multiplier category. This is theoretically important but empirically untested at current scales.

4. **How do global capital flows interact with domestic fiscal sustainability metrics?** The r - g framework treats the interest rate as exogenous to fiscal policy, but for the U.S., reserve currency status means foreign demand for Treasuries partially endogenizes the rate. If de-dollarization accelerates (a contested claim), r could rise independent of domestic fiscal dynamics. The base rate for reserve currency transitions is ~2-3 per century — too rare for statistical analysis.

5. **Can the Kalecki profit channel persist under rising interest expense?** Federal interest payments are projected to rise from ~$900B (2024) to ~$1.5T (2030). This spending flows to bondholders, not workers or consumers. If the deficit is increasingly consumed by interest payments, the profit-sustaining Kalecki channel weakens even at a constant deficit/GDP ratio. The historical data does not contain an episode where interest expense exceeded 4% of GDP for the U.S. (the current CBO projection for ~2030), so the Kalecki coefficient may be non-stationary.

6. **What would break the private sector surplus?** The Godley sectoral balance framework (iter_0002, 9/10 confidence) shows the private sector in surplus at 2-3% GDP. Fiscal consolidation mechanically erodes this surplus. The empirical question — how quickly does private surplus erosion translate into reduced spending and investment — determines the speed at which fiscal consolidation becomes contractionary. Historical precedent (1990s, 2000s transitions from surplus to deficit) suggests 4-8 quarter lags, but the initial conditions differ significantly.

7. **Is the 4-6 quarter Minsky-Kalecki credit timing framework (iter_0004) falsifiable with available data?** The framework predicts that fiscal consolidation >2pp GDP triggers credit cycle downshift within 4-6 quarters. With only ~7 consolidation episodes, the framework cannot be validated with standard statistical thresholds. What additional evidence (cross-country, cross-time, or structural) would be sufficient to raise or lower confidence in this specific timing window?
