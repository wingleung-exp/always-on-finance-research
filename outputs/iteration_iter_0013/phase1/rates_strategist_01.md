# Central Bank Balance Sheet Normalization — Yield Curve & Term Premium Strategist Analysis

## Key Claims

1. **QT's primary yield curve transmission operates through the term premium channel, not the expectations channel, and this distinction is systematically underappreciated by markets.** The Fed's balance sheet reduction from ~$9T (peak 2022) to ~$6.7T (March 2026) has added an estimated 60–100bp to 10-year term premium via the duration extraction channel, as private markets must absorb Treasury and MBS duration that the Fed previously warehoused. This is mechanistically distinct from rate hikes and has different cross-asset implications.

2. **Reserve scarcity is a nonlinear threshold phenomenon, not a gradual process, and the threshold is unknowable ex ante—making it the single most dangerous tail risk in rates markets today.** The Fed's September 2019 repo spike occurred when reserves fell to ~$1.5T (~7% of GDP). Current reserves at ~$3.2–3.4T appear ample, but the distribution of reserves across the banking system is far more concentrated post-SVB, meaning the effective scarcity threshold is likely higher than 2019 levels. The system can appear liquid one day and seize the next.

3. **The RRP (Reverse Repo) facility drain has masked QT's impact on reserves through 2023–2024, but this buffer is now largely exhausted, meaning further QT now drains reserves dollar-for-dollar.** RRP usage fell from $2.3T (peak late 2022) to ~$100–200B (early 2026), absorbing the majority of QT's balance sheet reduction. The exhaustion of this buffer fundamentally changes the QT transmission—from here, every dollar of balance sheet reduction directly reduces bank reserves, tightening financial conditions through the plumbing rather than the price channel.

4. **The Fed, ECB, and BOJ are normalizing balance sheets at different speeds and from different starting points, creating a global term premium divergence that will define cross-market relative value for the next 2–3 years.** The Fed has slowed QT to $25B/month (Treasuries only, MBS passive runoff), the ECB is running full PEPP reinvestment wind-down alongside APP runoff (~€40B/month combined reduction), and the BOJ is still expanding its balance sheet in absolute terms despite exiting YCC. This asynchrony creates exploitable cross-market curve spread dislocations.

5. **The 5y5y forward rate has structurally repriced higher by 50–80bp since 2022, and roughly half of this repricing reflects higher long-run term premium expectations tied to the permanent regime shift away from central bank balance sheet accommodation.** Markets are pricing that central banks will not return to pre-2020 balance sheet levels, but will also not resume large-scale asset purchases absent severe crisis. This "higher neutral balance sheet, but no marginal buyer" equilibrium embeds a structurally higher term premium floor relative to the 2012–2019 QE era.

6. **Treasury supply absorption capacity is the binding constraint on term premium, and it is deteriorating: the private sector must absorb ~$2T+ in net Treasury issuance annually while the Fed is a net seller and foreign official demand stagnates.** The marginal buyer has shifted from price-insensitive (central banks, foreign official reserves) to price-sensitive (hedge funds via basis trades, asset managers, households). This buyer composition shift means that every incremental supply shock—whether from wider deficits or QT acceleration—transmits more directly into term premium than during the QE era.

7. **The basis trade (~$800B–$1T notional, 50–100x leverage) has become a structural substitute for central bank demand in Treasury markets, but it provides liquidity that is pro-cyclical and fragile rather than counter-cyclical and robust.** Hedge fund basis trade positioning effectively replaces some of the demand that central bank QE previously provided, keeping term premium lower than supply fundamentals alone would imply. However, this "synthetic QE" unwinds precisely when markets need it most (March 2020, October 2023), creating a volatility accelerator rather than dampener.

8. **The yield curve shape is currently in a "term premium steepener" regime where 2s10s positivity is driven by term premium at the long end rather than expectations of rate cuts, making it a poor recession signal and a strong signal of fiscal/supply stress.** ACM decomposition shows that roughly 70–80% of current 2s10s slope (~40–60bp positive) is attributable to elevated 10-year term premium rather than expectations of a lower policy rate path. This is the inverse of the 2006–2007 "conundrum" period where compressed term premium flattened the curve and masked tightening expectations.

9. **ECB balance sheet normalization is creating a structural widening force on BTP-Bund spreads that is only partially offset by TPI (Transmission Protection Instrument), and this represents a regime change from the 2015–2022 compression era.** The ECB's reduction in Italian government bond (BTP) holdings removes the single largest price-insensitive buyer, transferring duration risk to private investors who demand higher spread compensation. TPI is designed as a backstop, not a flow buyer, meaning it cannot replicate the continuous compression effect of APP/PEPP reinvestments.

10. **The BOJ's balance sheet evolution will be the most consequential for global rates markets over 2026–2027, because Japan's $4T+ in overseas fixed income investments creates a transmission channel from BOJ normalization to UST and European sovereign term premium.** As the BOJ allows JGB yields to rise and eventually reduces its balance sheet (currently ~130% of GDP), Japanese institutional investors face incentives to repatriate capital, reducing demand for foreign bonds. The potential flow (~$200–400B in UST holdings by Japanese life insurers and pension funds at risk of reallocation) is material relative to annual net Treasury issuance.

## Evidence & Reasoning

### Claim 1: QT Transmits Through Term Premium, Not Expectations

The theoretical foundation comes from portfolio balance models (Vayanos-Vila 2009, Greenwood-Vayanos 2014) showing that central bank asset purchases reduce term premium by extracting duration from private portfolios. QT is the reverse: returning duration to private markets, which must be compensated. Empirically:

- Fed staff estimates (Bonis, Ihrig, Wei 2017) placed the stock effect of QE at ~100bp on 10-year term premium at peak holdings.
- With the Fed having reduced holdings by ~$2.2T from peak, a proportional reversal implies 50–80bp of term premium restoration, consistent with ACM model estimates showing 10-year term premium moving from roughly -50bp (late 2020) to +50–100bp (early 2026).
- The key insight is that this channel operates independently of the fed funds rate path. You can have rate cuts and rising term premium simultaneously—which is exactly what occurred in late 2024/early 2025 when the Fed cut 75bp while 10-year yields rose.

This distinction matters because term premium moves do not carry the same recession-signaling information as expectations moves. A term premium rise is a supply/demand phenomenon; a rate expectations rise signals tighter monetary conditions.

### Claim 2: Reserve Scarcity Nonlinearity

The evidence base:

- **September 2019**: Overnight repo rates spiked to 10% when aggregate reserves appeared ample (~$1.5T). The problem was distributional—reserves were concentrated at large banks and could not flow to repo counterparties quickly enough. The Fed had to restart balance sheet expansion.
- **Post-SVB concentration**: After the March 2023 banking stress, reserves became even more concentrated among the largest banks, with smaller banks drawing down reserves and relying more on FHLB advances and Fed facilities. This means the system-wide reserve level that triggers scarcity is likely $2–2.5T or higher, not $1.5T.
- **The Copeland-Duffie-Yang (2021) framework**: Shows that reserve demand curves are kinked—nearly flat when reserves are abundant, then steep to vertical at scarcity. The location of the kink is unobservable until it is hit.

The implication for curve strategy: the transition from ample to scarce reserves creates a regime change in rates volatility, particularly at the front end and in repo-Treasury basis relationships. This is a convex risk that is not priced in options markets.

### Claim 3: RRP Buffer Exhaustion

The mechanical accounting:

- **Peak RRP (Dec 2022)**: ~$2.3T. This represented money market fund cash parked at the Fed, earning the ON RRP rate, effectively outside the banking system.
- **QT absorption**: As the Fed reduced its balance sheet, the primary adjustment was a drain of RRP balances rather than bank reserves. T-bill issuance attracted MMF flows out of RRP and into Treasury bills, meaning QT was "financed" by RRP rather than reserves.
- **Current RRP (~$100–200B)**: With RRP nearly exhausted, further QT must come from bank reserves. This is why the Fed slowed QT pace to $25B/month in May 2025—to avoid hitting reserve scarcity prematurely.
- **Monitoring indicators**: The best real-time proxies for reserve stress are the SOFR-IORB spread, the Fed funds effective rate relative to IORB, and FHLB advance usage. When SOFR consistently prints above IORB, reserves are approaching scarcity.

### Claim 4: Asynchronous Global Normalization

Comparative balance sheet dynamics as of early 2026:

| Central Bank | Balance Sheet (% GDP) | QT Pace | Phase |
|---|---|---|---|
| Fed | ~25% (~$6.7T) | $25B/month (slowed) | Late-stage QT |
| ECB | ~45% (~€6.5T) | ~€40B/month (APP+PEPP) | Active normalization |
| BOJ | ~130% (~¥750T) | Still expanding (net) | Pre-normalization |

This asynchrony means:
- UST term premium stabilizing as Fed QT slows, while Bund term premium rising as ECB reduces holdings.
- JGB yields artificially suppressed by BOJ ownership of ~55% of the market, creating the largest duration risk overhang globally.
- Cross-market opportunities in UST-Bund spread trades, JGB-UST basis, and sovereign curve relative value.

### Claim 5: Structural 5y5y Repricing

The 5y5y forward rate (a proxy for long-run neutral rate + term premium expectations) has moved from ~2.0–2.5% in 2019 to ~3.5–4.0% in 2026. Decomposing this:

- **Higher neutral rate expectations**: ~20–30bp. Growth expectations modestly revised higher due to AI productivity narrative and fiscal activism.
- **Higher long-run inflation expectations**: ~15–25bp. 5y5y inflation breakevens ~10–15bp above pre-2020 levels.
- **Higher term premium floor**: ~40–60bp. This is the balance sheet normalization component. Markets price that the next QE episode requires a much larger shock to trigger, meaning the steady-state balance sheet is smaller, and the steady-state term premium is higher.

This claim is supported by the fact that even as the Fed has cut rates in 2024–2025, 5y5y forwards have not retraced. The market is embedding a regime-shift premium.

### Claim 6: Supply Absorption Capacity Deteriorating

The demand side of Treasury markets has fundamentally shifted:

- **Fed**: Net seller at $25B/month. Was the largest buyer during QE.
- **Foreign official**: Holdings ~$3.3T, roughly flat since 2014. China has actively reduced (~$200B decline over 3 years). Japan stable but at repatriation risk (see Claim 10).
- **Domestic banks**: Constrained by unrealized losses on existing bond portfolios (post-SVB mark-to-market awareness) and regulatory capital requirements.
- **Hedge funds (basis trade)**: ~$800B–$1T notional. Growing but fragile (see Claim 7).
- **Households/retail**: Growing share through money market funds → T-bills, but concentrated in short duration.

The implication: $2T+ annual net issuance must be absorbed by a buyer base that is more price-sensitive than at any point since pre-QE era. This creates a structural bid for higher term premium, particularly at the long end where supply is most concentrated (Treasury has been relying on T-bill issuance, but WAM extension is inevitable for debt sustainability).

### Claim 7: Basis Trade as Synthetic QE (Fragile)

The Treasury cash-futures basis trade works by:
1. Buying Treasury cash bonds
2. Selling Treasury futures against them
3. Financing the cash position in repo
4. Earning the basis (futures rich to cash) net of carry

This economically replicates what QE does—absorbing cash Treasury duration from the market. At ~$800B–$1T, it is comparable in scale to a medium-sized QE program. However:

- It is leverage-dependent (50–100x), meaning it unwinds when repo funding costs spike or margins increase.
- It unwinds pro-cyclically: precisely when Treasury markets stress (March 2020, October 2023), basis traders are forced sellers.
- It creates a false calm—term premium appears lower than supply fundamentals warrant because basis traders are absorbing duration. But this liquidity is borrowed from future stress episodes.

The implication for curve strategy: the term premium is understated by 20–40bp relative to what pure supply-demand would imply. Any basis trade unwind event would produce a rapid term premium repricing, concentrated in the belly-to-long end of the curve (7–20 year sector where basis trade activity is heaviest).

### Claim 8: Term Premium Steepener Regime

Yield curve decomposition using ACM model (as of early 2026):

- **2-year yield (~4.0%)**: ~3.7% expected path + ~0.3% term premium
- **10-year yield (~4.5%)**: ~3.5% expected path + ~1.0% term premium
- **2s10s slope (~50bp)**: -20bp from expectations (market expects lower rates) + ~70bp from term premium differential

This means the curve is steep *despite* market expectations of lower rates. Historically, a positively sloped curve signaled economic expansion. In the current regime, it signals fiscal supply stress and duration risk aversion. This is a critical distinction for anyone using the curve as a macro signal:

- The 3m10y spread (a canonical recession indicator) is also positive, but for term premium reasons rather than expectations reasons. Its predictive power for recession is likely diminished in this regime.
- The signal for other asset classes: a term premium steepener is equity-negative (higher discount rates without growth offset) and credit-negative (wider risk-free component raises all-in borrowing costs). This is the "bad steepening" scenario.

### Claim 9: ECB Normalization and BTP-Bund Spreads

The ECB's balance sheet reduction has particular implications for peripheral sovereign spreads:

- Under APP/PEPP, the ECB accumulated ~€750B in Italian sovereign debt, representing roughly 25% of outstanding BTPs. This buying suppressed BTP-Bund spreads from fundamental equilibrium.
- PEPP reinvestment flexibility (the ability to redirect maturing proceeds to periphery) was a powerful spread compression tool. Its wind-down removes this valve.
- TPI is a backstop, not a standing facility. It requires conditions (compliance with EU fiscal rules, no excessive macro imbalances) and has never been activated. Markets cannot price it as a continuous put.
- The equilibrium BTP-Bund spread without ECB flow support is likely 180–250bp, versus the current ~130–150bp. This represents 30–100bp of spread tightness that is a legacy of balance sheet accommodation.

### Claim 10: BOJ Normalization and Global Duration Reallocation

Japan's external bond portfolio is the largest single-country source of cross-border fixed income demand:

- Japanese life insurers: ~$600B in foreign bonds (primarily USD, EUR-denominated).
- Japanese pension funds (GPIF + corporate): ~$400B in foreign bonds.
- Japanese banks: ~$300B in foreign bonds.

As BOJ normalization raises JGB yields toward 1.5–2.0% (from current ~1.0–1.3%), the hedging calculus changes:
- Hedged UST yields (UST yield minus FX hedge cost) have been negative or near-zero for Japanese investors since 2022. Higher JGB yields make unhedged domestic allocation increasingly attractive.
- Even a 10–15% reallocation of Japanese foreign bond holdings toward domestic = $130–200B in selling pressure on USTs and European sovereigns.
- This flow effect would add 15–30bp to UST term premium, concentrated in the 10–30 year sector where Japanese life insurers are the most active.

The timing is the key uncertainty: BOJ is proceeding cautiously, and Japanese institutions move slowly. But the direction is clear, and the flow effects are large enough to matter for global curve strategy.

## Confidence Assessment

| Claim | Confidence (1–10) | Justification |
|---|---|---|
| 1. QT transmits through term premium | **8** | Strong theoretical and empirical foundation. Portfolio balance models well-established. Remaining uncertainty is around magnitude, not mechanism. |
| 2. Reserve scarcity nonlinearity | **8** | 2019 repo spike is definitive evidence. Post-SVB reserve concentration well-documented. The unknowable threshold is itself a high-confidence assertion. |
| 3. RRP buffer exhaustion | **9** | This is largely mechanical accounting. RRP levels are observable. The implication for QT transmission is direct. Highest confidence claim. |
| 4. Asynchronous global normalization | **8** | Balance sheet levels and policy announcements are publicly observable. The exploitable implication for relative value is well-supported by historical precedent. |
| 5. Structural 5y5y repricing | **6** | Decomposition between neutral rate, inflation expectations, and term premium is model-dependent. The total repricing is observable, but attribution across components has wide confidence intervals. |
| 6. Supply absorption deterioration | **7** | Issuance numbers and demand composition are observable. The term premium implication depends on elasticity estimates that vary across models. But directional confidence is high. |
| 7. Basis trade as fragile synthetic QE | **7** | Notional estimates vary ($600B–$1T). Pro-cyclical unwind is empirically validated (March 2020). Quantifying the term premium suppression effect (20–40bp) is less certain. |
| 8. Term premium steepener regime | **7** | ACM and Kim-Wright broadly agree on the direction. Exact decomposition varies by 15–20bp across models. The macro signal interpretation follows logically from the decomposition. |
| 9. ECB normalization → BTP-Bund | **6** | The direction is high-conviction, but the equilibrium spread without ECB support is genuinely uncertain. TPI's effectiveness as a backstop is untested. Political dynamics add uncertainty. |
| 10. BOJ → global duration reallocation | **5** | The potential flow is well-documented. The timing, pace, and whether institutional reallocation actually materializes are highly uncertain. Japanese institutions have historically been slow to adjust. This is a 2–3 year thematic, not an imminent trade. |

## Connections to Other Topics

### Monetary Policy (credit_and_rates)
Balance sheet normalization is the "other half" of monetary policy tightening that operates through quantity (reserves, duration) rather than price (fed funds rate). The interaction between rate policy and balance sheet policy creates a two-dimensional policy space that is more complex than either alone. The Fed's decision to slow QT while maintaining rates signals that these instruments are partially independent.

### Fiscal Policy & Debt Sustainability (structural_themes: fiscal_dominance)
The single most important connection. Central bank balance sheet shrinkage is occurring simultaneously with fiscal expansion, creating a "supply pincer"—more issuance from Treasury, less absorption from the Fed. This is the mechanism through which fiscal dominance manifests in rates markets. The deficit-term premium doom loop (already in KB) is amplified by QT. If fiscal trajectories are unsustainable, central banks may eventually be forced to restart QE not for monetary policy reasons but for fiscal reasons—the definition of fiscal dominance.

### Volatility Regimes (asset_class_dynamics)
QT creates a structural bid for higher rates volatility through two channels: (1) reserve scarcity introduces jump risk in funding markets, and (2) the absence of central bank buying removes a volatility dampener from sovereign bond markets. The transition from QE (vol suppression) to QT (vol amplification) is a regime change that affects cross-asset volatility correlations, particularly the rates-equity vol relationship.

### Credit Cycles (credit_and_rates)
Term premium driven by balance sheet normalization raises the risk-free component of all-in borrowing costs, tightening credit conditions independently of the policy rate. This is particularly impactful for long-duration credit (IG 10+ year, infrastructure, project finance) where the term premium component is a larger share of total yield. The basis trade fragility connection also creates a channel from Treasury market stress to credit market contagion via dealer balance sheet constraints.

### FX Regimes & Carry (asset_class_dynamics: fx_regimes)
The asynchronous pace of global balance sheet normalization is a primary driver of rate differentials and hence FX carry attractiveness. Fed QT slowing while ECB normalizes aggressively compresses the UST-Bund rate differential, which is EUR-supportive. BOJ balance sheet expansion (still ongoing) keeps JGB yields artificially low, supporting the yen carry trade—but creating cliff risk when normalization eventually begins.

### Commodity-Inflation Nexus (cross_asset)
Central bank balance sheet size interacts with inflation expectations through the "monetization" channel. Large balance sheets can be perceived as inflationary if markets believe they represent permanent money creation (fiscal-monetary cooperation). Balance sheet reduction signals commitment to price stability, anchoring inflation expectations. The credibility of balance sheet normalization is a key input to long-run inflation breakevens and hence to commodity inflation hedging demand.

### Risk Appetite Regimes (cross_asset)
The "central bank put" is directly tied to balance sheet willingness. QE represented an unlimited backstop (March 2020: $1.6T in emergency purchases). QT represents the removal of this put. Markets have not fully repriced the risk premium associated with operating without a guaranteed central bank backstop, partly because memory of 2020 interventions creates moral hazard. The question of when the Fed would restart QE (the "Fed put strike price") is the most important unobservable in rates markets.

## Open Questions

1. **Where exactly is the reserve scarcity threshold?** Fed estimates vary from $2.5T to $3.5T. The distributional dimension (which banks hold reserves) matters as much as the aggregate level. Without a stress test that reveals the binding constraint, this remains unknowable—and is the most consequential unknown for rates market structure.

2. **Will the Fed end QT in 2026, and at what balance sheet level?** The Fed has signaled sensitivity to reserve indicators but has not committed to a terminal balance sheet size. The difference between $6T and $6.5T in terminal holdings is ~50bp in long-end term premium. Forward guidance on QT end date would itself be a significant market event.

3. **How will Treasury respond to the absorption challenge—duration extension or more T-bills?** TBAC (Treasury Borrowing Advisory Committee) guidance has favored T-bill share increases to ease absorption. But T-bill-heavy issuance creates rollover risk and does not address the long-end supply problem. A shift to coupon-heavy issuance would directly impact 10–30y term premium.

4. **What triggers BOJ balance sheet reduction (not just rate hikes)?** BOJ has exited YCC and raised rates, but its balance sheet continues to grow through reinvestment. Actual balance sheet reduction is a separate, politically more difficult decision. The timing and pace of this transition will determine the magnitude of global duration reallocation flows.

5. **Is the basis trade self-limiting, or does it grow until it breaks?** Regulatory proposals (SEC Rule 10c-1a, potential CFTC margin requirements) could constrain basis trade growth. But without regulation, the trade's profitability attracts more capital, increasing systemic fragility. The question is whether the trade collapses under its own weight before regulators act.

6. **How does TPI credibility evolve under actual fiscal stress in Italy or other periphery?** TPI has never been activated. Its conditionality requirements could make it unavailable precisely when needed (if a country is in fiscal stress, it may not meet the conditions). The ECB may face a choice between activating TPI without conditions (undermining credibility) or not activating it (allowing spread contagion).

7. **What is the interaction between QT and financial stability events?** The Fed paused QT effectively during March 2023 (SVB) but did not formally stop it. Would a future financial stress event trigger QT pause, QT end, or QE restart? The sequence and speed of this reaction function matters enormously for rates positioning—and it is deliberately ambiguous, as the Fed wants to preserve optionality while avoiding moral hazard.

8. **Can the standing repo facility (SRF) substitute for ample reserves?** The SRF was designed to prevent repo rate spikes by providing a lending facility. But it is untested under genuine stress, counterparty stigma may limit its use, and its rate (currently IORB + 10bp) may not be low enough to prevent dislocations. If the SRF works, the Fed can run a smaller balance sheet; if it doesn't, reserve scarcity arrives sooner and harder than expected.
