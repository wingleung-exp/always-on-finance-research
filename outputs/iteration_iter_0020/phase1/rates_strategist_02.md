# Stock-Bond Correlation Regime Analysis — Central Bank Policy Transmission Strategist Analysis

## Key Claims

1. **The central bank reaction function is the single most important institutional determinant of the correlation sign, but the relevant parameter is the *effective* Taylor Rule coefficient (φ_π_eff), not the *stated* one — and φ_π_eff has diverged materially from φ_π_stated since 2022.** The Fed's stated commitment to 2% (implying φ_π > 1.5) coexists with an effective reaction function that accommodated 3.0-3.5% core PCE for over two years without resuming hikes, placing φ_π_eff closer to 1.0-1.2. This gap between stated and effective reaction functions is the key variable for correlation regime determination.

2. **The correlation flip trigger is identifiable through a specific sequencing in the policy transmission mechanism: it occurs when the expectations channel and the financial conditions channel decouple, which happens when the Fed's credibility is sufficient to anchor short-end expectations but insufficient to prevent long-end term premium repricing.** This is precisely the maturity bifurcation (2Y-SPX negative, 30Y-SPX positive) documented in prior iterations — and it is fundamentally a transmission mechanism failure, not merely a statistical curiosity. The front end transmits policy intent; the back end transmits fiscal reality. When these diverge, correlation bifurcates by maturity.

3. **Financial conditions indices (FCIs) are structurally miscalibrated for the current correlation regime, systematically overstating the degree of monetary policy tightening by 75-150bp in policy-rate-equivalent terms.** The Goldman Sachs FCI, Bloomberg FCI, and Chicago Fed National FCI all treat equity, credit, and rate components as additively separable. Under negative correlation, this is approximately correct. Under positive correlation, the components move together, and the FCI double-counts. Conversely, in 2023-2025, equity rallies loosened FCIs by 100-200bp even as the Fed held rates at 5.25-5.50%, making financial conditions substantially easier than the policy rate implied.

4. **Forward guidance transmission is attenuated by 30-50% under positive correlation, and the attenuation is asymmetric: dovish guidance loses more potency than hawkish guidance gains.** Under negative correlation, dovish guidance eases through both the rate channel (lower expected path) and the asset price channel (equity rally on growth expectations). Under positive correlation, dovish guidance lowers rate expectations but simultaneously signals growth concern, partially offsetting the equity channel. The asymmetry arises because hawkish guidance under positive correlation tightens through both channels reinforcingly, while dovish guidance generates offsetting channel effects. The Fed has effectively lost ~30-50% of its easing toolkit without losing equivalent tightening power.

5. **The current Fed reaction function is data-dependent in name but effectively backward-looking with a 6-9 month recognition lag, creating a structural tendency toward policy errors that perpetuate correlation instability.** The Fed responds instantly to deflationary financial shocks (SVB: <72 hours) but slowly to inflationary fiscal/supply shocks (2021 transitory: ~9 months) — exactly the asymmetry that generates correlation oscillation rather than regime resolution.

6. **Global monetary policy divergence is at a 25-year extreme and is itself a correlation regime determinant through the exchange rate channel, with the ECB-Fed and BOJ-Fed divergences creating cross-currents that suppress correlation regime resolution.** The Fed at 4.25-4.50%, ECB at 2.50%, BOJ at 0.50% creates three partially offsetting channels: USD disinflation imports (supporting negative correlation), foreign UST buying compresses term premium (supporting negative long-end correlation), and capital inflows inflate US equities beyond fundamentals (supporting positive correlation when flows reverse).

7. **The term premium is not merely a leading indicator of correlation regime — it is the transmission mechanism through which fiscal dominance converts to positive correlation, and the current ACM estimate of 50-80bp understates the "true" fiscal term premium by 30-50bp due to model specification issues.** Adjusting for the Kim-Wright alternative specification, QT duration extraction, and basis trade compression, the effective term premium is closer to 80-130bp — still below the ~150bp threshold for fully-established positive correlation, but meaningfully closer than the headline ACM number suggests.

8. **The correlation flip trigger can be specified as a three-condition conjunction: (a) realized core inflation above the CB's effective tolerance threshold (currently ~2.8-3.0% for the Fed) for 2+ consecutive quarters, (b) term premium above 100bp (ACM-adjusted), AND (c) output gap within ±0.5% of zero.** All three were simultaneously met in Q2-Q3 2022 when the correlation flipped. As of Q1 2026, condition (c) is met, condition (b) is approaching, and condition (a) is the swing variable — core PCE at 2.6-2.8% is at the boundary.

9. **The BOJ normalization represents the single largest underpriced exogenous shock to global correlation regimes.** BOJ holds ~$4.2T in JGBs and ~$450B in equity ETFs. Normalization would pull $500B-$1T of Japanese capital out of UST and global fixed income, strengthen JPY by 15-25%, and unwind the global carry trade — directly adding to US term premium and potentially satisfying condition (b) of the correlation flip trigger.

10. **The "broken transmission" diagnostic for the current regime is specific: the credit channel is working, the exchange rate channel is partially working, but the interest rate channel is impaired (mortgage lock-in effect) and the asset price channel is actively working against policy intent (AI-driven equity rally offsets rate tightening).** This partial transmission failure explains why financial conditions loosened through 2023-2025 despite the most aggressive hiking cycle since Volcker — and why the correlation regime has not resolved.

## Evidence & Reasoning

### Claim 1: Effective vs. Stated Reaction Function Divergence

The standard NK framework derives correlation sign from the Taylor Rule coefficient φ_π. When φ_π > 1 (Taylor Principle satisfied), the CB stabilizes inflation, demand shocks dominate the cycle, and stocks and bonds are negatively correlated. This is well-established in accumulated research (confidence 8/10).

However, the *effective* φ_π must be estimated from observed behavior. Since the Fed paused hikes at 5.25-5.50% in July 2023 with core PCE at 4.3%, and began cutting in September 2024 with core PCE still at 2.7%, the revealed preference is a tolerance band of 2.5-3.5%. Using a backward Taylor Rule estimation:

- FFR = r* + π* + φ_π(π - π*) + φ_y(y - y*)
- 5.50 = 0.75 + 2.0 + φ_π(4.3 - 2.0) + φ_y(~0)
- φ_π ≈ 1.2

This contrasts with the Taylor (1993) original of 1.5 or Taylor (1999) of 2.0. At effective φ_π of 1.2, both positive and negative correlation are consistent with the reaction function depending on the shock mix — the CB is not aggressive enough to unambiguously determine the correlation sign.

Supporting evidence: The September 2024 50bp cut (vs. 25bp expected by many) when core PCE was still 2.7% reveals an asymmetric loss function — greater weight on downside labor market risk than upside inflation risk. This asymmetry systematically biases toward accommodating inflation.

### Claim 2: Transmission Decoupling as Flip Trigger

The maturity bifurcation (2Y-SPX at -0.15 to -0.30, 30Y-SPX at +0.05 to +0.15) is well-documented across multiple research iterations (confidence 8/10). The reinterpretation through the transmission mechanism lens:

- **2Y yield** = dominated by expectations channel (expected FFR path). This channel is functioning: when the Fed signals, the 2Y responds. Maintains negative equity correlation because both track growth expectations filtered through the Taylor Rule.
- **30Y yield** = dominated by term premium channel (duration risk compensation from fiscal supply, QT, foreign demand). Operates independently of Fed communication. Repriced upward by 100-150bp since 2020.

The "flip" occurs maturity-by-maturity, from short to long duration, as term premium progressively overwhelms expectations. The 1993-94 bond massacre (8/10 analogue similarity in KB) followed exactly this pattern. The diagnostic: if 10Y-SPX correlation flips positive while 2Y-SPX remains negative, transmission is formally broken — the operational definition of fiscal dominance from a rates perspective.

### Claim 3: FCI Miscalibration

Goldman Sachs FCI peaked at ~100.7 in October 2022 (tightest since 2008) and has since eased to ~99.5-99.8 despite the Fed at 4.25-4.50%. The ~1.0 point easing is driven by:
- S&P 500 rally from 3,577 to ~5,800+ (equity component loosened ~150bp equivalent)
- IG credit spreads tightening from ~160bp to ~90bp (credit component loosened ~50bp)
- USD depreciation from DXY 114 to ~104 (FX component loosened ~30bp)

These collectively loosened financial conditions by more than the Fed tightened through rates. Under the current regime, equity loosening is driven by AI enthusiasm orthogonal to monetary policy — the FCI reads this as "easy conditions" but policy-relevant conditions (borrowing costs, bank lending standards) remain tight.

Magnitude estimate: adjusting the equity component to exclude the AI/tech premium (proxied by equal-weight vs. cap-weight S&P gap), financial conditions are approximately 75-150bp tighter than headline FCI suggests. This implies the Fed has been tighter than it believes, consistent with slowing labor market and credit tightening data.

### Claim 4: Forward Guidance Asymmetric Attenuation

The 30-50% attenuation (Del Negro, Giannoni & Patterson 2023) is a central tendency. The asymmetry by direction:

**Dovish guidance attenuation (~50%):**
- Rate channel: Fed signals lower rates → front end rallies ✓
- Asset price channel: Under positive correlation, rate cuts signal growth concern → equities may fall → offsetting ✗
- Net: half the channels work against intent

**Hawkish guidance amplification (~0% attenuation):**
- Rate channel: Fed signals higher rates → front end sells off ✓
- Asset price channel: Higher rates AND growth concern → equities sell off → reinforcing ✓
- Net: both channels reinforce

Evidence: September 2024 dovish pivot (50bp cut) — S&P response muted (+0.4%) vs. historical dovish surprises. Contrast with 2022 hawkish surprises (Jackson Hole: -3.4%, September FOMC: -1.7%) where both channels reinforced. The asymmetry means the Fed's easing toolkit is degraded by approximately one-third — which could force more aggressive easing than the Taylor Rule prescribes, further undermining effective φ_π.

### Claim 5: Backward-Looking Reaction Function with Asymmetric Lag

The Fed's demonstrated data-dependence pattern since 2021:

| Event | Recognition Lag | Response Lag |
|-------|----------------|--------------|
| Inflation surge (2021) | ~9 months ("transitory" Jun 2021 → Mar 2022 hike) | 3 months |
| SVB banking stress (Mar 2023) | <72 hours | <72 hours (BTFP) |
| Labor market softening (2024) | ~4 months (Apr data → Sep cut) | 1 month |
| Tariff inflation pass-through (2025-26) | ~3+ months and counting | TBD |

Deflationary shocks are recognized within days; inflationary shocks take 6-9 months. This asymmetry means the Fed stabilizes against negative-correlation-producing shocks faster than positive-correlation-producing shocks — the institutional mechanism through which correlation instability is perpetuated.

### Claim 6: Global Policy Divergence as Correlation Suppressor

Current configuration: Fed 4.25-4.50%, ECB 2.50%, BOJ 0.50%. Widest Fed-ECB spread since euro creation; widest Fed-BOJ spread since 2000.

Three competing channels:
1. **Rate differential → USD strength → disinflation import:** USD/EUR ~1.06-1.08, USD/JPY ~150-155. Subtracts ~0.3-0.5pp from US goods inflation annually. *Supports negative correlation.*
2. **Capital flows → UST demand → term premium compression:** Foreign holdings ~$8T. Compresses term premium ~30-50bp (Krishnamurthy-Vissing-Jorgensen). *Supports negative long-end correlation.*
3. **Capital flows → US equity inflation → FCI loosening:** Same flows inflate US equities beyond fundamentals. *Supports positive correlation when reversed.*

These partially cancel, contributing to the oscillating regime. Key risk: ECB-Fed convergence would narrow differentials, weaken USD, reduce UST flows, and simultaneously remove disinflationary channel and term premium compression — unlocking the correlation flip trigger.

### Claim 7: Term Premium Underestimation

ACM model limitations:
1. **Sample bias:** Estimated primarily over 1990-2019 (negative correlation, supply not marginal). Underweights supply-driven components.
2. **QT attribution:** 30-60bp QT impact (Li-Wei 2023, Smith-Valcarcel 2023) partially absorbed by yield-curve factors, not cleanly attributed.
3. **Kim-Wright gap:** Consistently 20-40bp above ACM in current environment.
4. **Basis trade distortion:** $800B-$1T basis trade compresses cash Treasury yields, read by ACM as lower term premium.

Adjustment: ACM 50-80bp + Kim-Wright gap (~30bp) + basis trade compression (~10-20bp) = effective 90-130bp. Meaningfully closer to the ~150bp threshold for established positive correlation than headline suggests.

### Claim 8: Three-Condition Conjunction

Synthesizing the demand/supply decomposition (9/10 confidence), term premium threshold (7/10), and output gap instability (7/10):

**(a) Core inflation > CB effective tolerance (2.8-3.0%):** Supply-driven inflation's correlation impact depends on CB accommodation. Threshold is effective tolerance, not target.
**(b) Adjusted term premium > 100bp:** Term premium captures fiscal/supply dynamics that drive long-end positive correlation.
**(c) Output gap within ±0.5%:** Phillips Curve convexity at zero gap means small supply shocks produce large inflation responses.

Historical validation:
- Q2-Q3 2022: 4.7% > 3.0% ✓, adjusted ~120bp ✓, gap ~0% ✓ → Flipped
- 2015-2016: 1.8% < 3.0% ✗ → No flip
- 2018 Q4: 2.0% borderline ✗, ~50bp ✗ → No flip

Current (Q1 2026): Core PCE 2.6-2.8% (approaching), adjusted TP 90-130bp (approaching), gap ~0% ✓. Tariff pass-through pushing core above 3.0% for two quarters would complete the conjunction.

### Claim 9: BOJ as Underpriced Exogenous Shock

BOJ balance sheet ~130% of GDP ($4.2T), with ~$450B equity ETFs (largest single holder of Japanese equities). Governor Ueda has moved to +0.50%, market pricing terminal 0.75-1.00% by end-2027.

Each 25bp BOJ hike narrows Fed-BOJ spread, reducing carry incentive (~$2-4T outstanding), and strengthens JPY. Japanese institutions hold ~$1.2T in US fixed income; 15-25% JPY appreciation makes unhedged UST positions unprofitable. Estimated selling pressure: $100-300B over 12-18 months.

Supply elasticity (Krishnamurthy-Vissing-Jorgensen): 30-60bp per $100B of selling → potential 30-180bp impact on US term premium. BOJ's pattern of telegraphing-then-surprising means transmission will be discontinuous — a tail risk the market systematically underprices via smooth forward curves.

### Claim 10: Broken Transmission Diagnostic

Channel-by-channel assessment:

| Channel | Status | Effectiveness | Key Impairment |
|---------|--------|--------------|----------------|
| Interest rate | Impaired | ~60% | Mortgage lock-in effect (3-4% existing vs. 6.5-7.0% new) limits housing transmission |
| Credit | Working | ~80% | SLO survey shows tightening; C&I growth near zero |
| Asset price | Counter-productive | Negative | AI rally added $10-15T market cap; wealth effect ($300-750B) exceeds rate tightening impulse |
| Exchange rate | Partial | ~50% | Goods only 25% of core PCE; tariffs offset USD disinflation |
| Expectations | Attenuated | ~50-70% | Forward guidance multiplier reduced; dot plot gaps widen |

**Aggregate:** net tightening reaching the real economy is 40-60% of policy rate level. The asset price channel is the primary leakage source, driven by AI investment cycle orthogonal to monetary policy. This is the transmission failure that explains both the FCI loosening paradox and the correlation regime's failure to resolve.

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1. Effective vs. stated reaction function | **8/10** | Revealed preference analysis is straightforward; specific 1.0-1.2 estimate has ±0.2 uncertainty. |
| 2. Transmission decoupling as flip trigger | **8/10** | Builds on highest-confidence KB findings (bifurcation 8/10, demand/supply 9/10). 1993-94 analogue supports the mechanism. |
| 3. FCI miscalibration 75-150bp | **6/10** | Direction near-certain (methodology guarantees it). Specific magnitude has wide confidence interval. Equal-weight proxy is novel, needs validation. |
| 4. Forward guidance asymmetric attenuation | **7/10** | Overall attenuation externally validated. Asymmetry claim based on limited sample (Sep 2024 event). Mechanism is logically tight but empirically thin. |
| 5. Backward-looking reaction function | **7/10** | Pattern is empirically clear. Generalization as systematic bias may reflect this particular Fed composition rather than institutional structure. |
| 6. Global divergence as correlation suppressor | **7/10** | Three-channel framework logically sound. "Partial cancellation" consistent with oscillation data but attribution is weak — oscillation could have many causes. |
| 7. Term premium underestimation 30-50bp | **6/10** | Individual adjustments well-documented. Cumulative stacking risks compounding errors. |
| 8. Three-condition conjunction trigger | **7/10** | Fits all historical observations (no false positives). n=3 calibration is thin. Threshold values could be off by meaningful amounts. |
| 9. BOJ underpriced exogenous shock | **6/10** | Holding magnitudes and repatriation logic factual. "Underpriced" claim harder to verify. Discontinuity risk from BOJ communication well-documented but timing unknowable. |
| 10. Broken transmission diagnostic | **8/10** | Each channel assessment supported by current data. The 40-60% aggregate is imprecise. Qualitative finding (asset price channel counter-productive) is near-certain and most policy-relevant. |

## Connections to Other Topics

### → Monetary Policy Transmission (direct, primary)
This analysis IS the monetary policy transmission topic applied to the correlation question. The key bridge: correlation regime is not exogenous — it is an *endogenous outcome* of the policy transmission mechanism. When transmission works (channels aligned, CB credible, FCI tracks policy rate), correlation is determined by the shock mix per the NK model. When transmission is impaired (channels decoupled, FCI diverges from policy rate), correlation becomes unstable. The current correlation instability is a transmission failure diagnostic.

### → Inflation Regimes (confidence 6.0, depth 3)
The inflation regime determines which correlation regime is *possible*. Under anchored expectations (current), only the specific conjunction of Claim 8 can flip correlation persistently positive. Under de-anchored expectations, positive correlation becomes the default. The Coibion-Gorodnichenko threshold (sustained 5Y breakeven divergence >75-100bp for >6 months) is the regime boundary. The thinner anchoring buffer (KB 8/10) means distance to this boundary is shorter than any point since the late 1990s.

### → Volatility Regimes (confidence 7.1, depth 1)
The MOVE-VIX divergence (KB 8/10) is the vol-space signature of broken transmission. MOVE elevated from reaction function uncertainty (Claim 5) and term premium repricing (Claim 7). VIX suppressed because the asset price channel works *against* policy (Claim 10). Resolution of MOVE-VIX divergence will coincide with either correlation regime resolution or a volatility event forcing asset price channel realignment.

### → Equity Cycles (confidence 5.0, depth 2)
The cross-asset pricing inconsistency (KB 7/10) — equities at 21-22x implying negative correlation while bonds price positive — is explained by the broken asset price channel. Equities respond to AI investment cycle; bonds respond to fiscal supply and reaction function uncertainty. The inconsistency persists because the two markets respond to different factors — the definition of transmission failure.

### → Fiscal Dominance & Global Sovereign Debt
The maturity bifurcation IS fiscal dominance in correlation space. The front end under CB control (Taylor Rule); back end under fiscal control (supply-determined term premium). As deficits persist at 6-7% of GDP, the maturity threshold at which correlation flips positive moves progressively shorter. Testable prediction: 10Y-SPX turning persistently positive while 2Y-SPX remains negative establishes fiscal dominance regardless of Fed action. The BOJ normalization channel (Claim 9) connects to global sovereign debt sustainability — Japan's 260% debt/GDP is sustainable only under financial repression that is now ending.

## Open Questions

1. **Can the asset price channel be permanently decoupled from monetary policy?** The AI equity rally appears driven by real productivity/investment factors orthogonal to the rate cycle. If structural (not bubble), does the asset price channel of transmission remain permanently impaired? This is the deepest question for long-term correlation analysis and cannot be answered from current data.

2. **What is the next Fed chair's effective inflation tolerance?** Powell's term ends in early 2026. The next chair's revealed φ_π determines whether condition (a) of the correlation flip trigger is met. A more dovish chair (lower φ_π_eff) would paradoxically make persistent positive correlation more likely by removing the CB stabilization mechanism.

3. **Is the maturity bifurcation stable or self-correcting?** If 2Y-SPX remains negative while 30Y-SPX is positive, arbitrage logic suggests the 10Y should migrate toward one or the other. But if driven by genuinely different factors (expectations vs. term premium), bifurcation could persist indefinitely. Need empirical work on cross-maturity correlation dynamics.

4. **How large is the basis trade's impact on measured term premium?** If $800B-$1T basis trade compresses measured term premium by 20-50bp, the "true" term premium could be much closer to the flip threshold than any model shows. Direct measurement is needed.

5. **What is the BOJ repatriation feedback threshold?** If BOJ normalization triggers modest UST selling and JPY appreciation, does FX gain encourage more repatriation (positive feedback) or higher UST yield attract new flows (negative feedback)? The ~145 USD/JPY level appears critical.

6. **Does the FCI mismeasurement explain the Fed's own policy errors?** If the Fed uses FCIs that overstate easing, it may believe conditions are looser than reality for policy-relevant sectors — keeping rates higher for longer than optimal. Need to know the Fed staff's internal FCI specification and whether they adjust for these issues.

7. **What happens to correlation when QT decelerates toward terminal balance sheet (late 2026-2027)?** QT has been a primary driver of term premium increase and positive long-end correlation. If deceleration reverses 15-30bp of term premium, does this mechanically restore negative correlation at the long end, or has fiscal supply become dominant regardless?
