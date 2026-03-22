# FX-Rates Divergence & Carry Dynamics — Tail Risk & Crisis Mechanics Specialist Analysis

## Key Claims

1. **The carry trade ecosystem constitutes a system-level short-volatility position of ~$4-6T notional equivalent, and the current configuration satisfies all four VTA (Vulnerability-Trigger-Amplification) prerequisites — leverage, maturity mismatch, concentration, and opacity — placing it in the historically validated pre-crisis zone, albeit with genuinely uncertain timing.**

2. **The swap line architecture is structurally undersized relative to the carry-driven dollar funding demand it would face in a synchronized unwind: authorized capacity of ~$600B against potential acute demand of $3-5T, creating a credibility gap that itself could become an amplification mechanism once market participants perform the same arithmetic.**

3. **The Treasury basis trade (~$800B-$1T) and FX carry trade (~$4-6T notional) share a common vulnerability to dollar funding stress, creating a dual-fragility corridor where dislocation in either market can cascade to the other through repo and cross-currency swap channels within 24-72 hours.**

4. **Crisis amplification in the current FX-carry configuration would propagate through three distinct but interacting channels — margin/collateral spirals, redemption cascades, and counterparty opacity — with the margin channel now operating 3-5x faster than in 2008 due to automated margin calls and algorithmic deleveraging, compressing the policy response window from weeks to days.**

5. **The vol regime transition zone (8.5-10.5% realized G10 FX vol) exhibits maximum vol-of-vol — not maximum vol itself — creating a hedging paradox where options are cheapest precisely when the probability distribution is most uncertain, and most expensive after the regime has already shifted.**

6. **The BoJ normalization pathway represents a compound tail risk where each incremental step (estimated 4-6 remaining to reach ~1.0%+) produces selection bias in surviving carry positions — the weakest hands exit first, leaving a residual position set that is more leveraged, more concentrated, and more likely to unwind violently on subsequent steps.**

7. **Agricultural supply shock represents a previously under-integrated amplification channel for carry crises: a food price spike in the current thin-buffer environment (corn stocks-to-use ex-China <15%) could simultaneously widen EM rate differentials (via food-inflation policy floors) while triggering EM capital outflows, creating a reflexive loop that standard FX risk models do not capture.**

8. **The August 2024 JPY carry unwind provides a partial out-of-sample validation of the VTA framework with critical lessons: the speed of propagation (3 trading days from trigger to peak stress), the role of vol-targeting strategies as amplifiers, and — importantly — the containment factors (BoJ dovish pivot, carry positions below extremes) that prevented the foreshock from becoming systemic.**

## Evidence & Reasoning

### Claim 1: VTA Prerequisites Currently Satisfied

**Vulnerability Map (as of March 2026):**

- **Leverage:** Carry positioning has rebuilt since the August 2024 unwind. CFTC net speculative positioning in JPY and CHF shorts has recovered to ~65-75th percentile of the post-GFC range. The critical issue is not the visible exchange-traded positioning but the OTC and offshore components (primarily structured products, dual-currency deposits in Asia, liability-driven FX overlays) that are unmeasured. Estimate: exchange-traded represents ~15-25% of total carry exposure, implying total notional of $4-6T. This is not a new claim — it was validated in iter_0008 and not contested by any agent.

- **Maturity mismatch:** Carry is inherently a maturity mismatch trade — borrowing short-term in funding currencies (JPY, CHF, EUR) to invest in longer-duration higher-yielding assets. The critical refinement from iter_0008: the mismatch has *elongated* since 2022 because DM rate divergence has persisted longer than any cycle in the past 30 years, encouraging carry traders to extend duration to capture term premium in addition to cross-currency differential. This means unwind would require liquidation of longer-dated positions in less liquid tenors, increasing market impact per unit of notional.

- **Concentration:** Three funding currencies (JPY, CHF, EUR) account for an estimated 70-80% of G10 carry funding. On the investment side, USD, AUD, and MXN/BRL dominate. The PCA collapse during stress (H6 from iter_0008: eigenvalue ratio from ~3:1 to ~8:1+) demonstrates that diversification across carry pairs is illusory — they become a single factor in crisis.

- **Opacity:** The most underappreciated prerequisite. No regulatory body publishes comprehensive data on aggregate FX carry positioning. CFTC futures data captures a fraction. BIS triennial survey (last: April 2022, next due 2025 but delayed) provides periodic snapshots with 18-month lag. Dual-currency deposit structures in Japan and Korea are reported with variable quality. The gap between observable and total exposure means that neither regulators nor market participants can assess the system-level short-vol position in real time. This opacity was a critical feature of every prior crisis — participants cannot price counterparty risk when they cannot observe counterparty positioning.

**Historical validation:** Every major carry unwind in the database (1998 LTCM, 2007-08 GFC, 2015 CHF floor removal, 2020 March, 2024 August) occurred when at least three of four VTA prerequisites were present. The current configuration satisfies all four. This is a necessary but not sufficient condition — the timing depends on triggers, which are by definition unpredictable.

### Claim 2: Swap Line Capacity Gap

The Federal Reserve maintains standing dollar swap lines with five central banks (ECB, BoJ, BoE, SNB, BoC) and temporary arrangements with ~9 others. The authorized aggregate ceiling is approximately $600B, though the standing lines are technically unlimited on the Fed's side (the constraint is on the borrowing central bank's willingness to take credit risk on domestic counterparties).

However, "unlimited" in theory faces political and operational constraints in practice:

- **Political constraint:** Drawing $2T+ on swap lines during a crisis would require the Fed to absorb enormous credit risk to foreign central banks, creating political backlash domestically. The 2008-09 experience (peak usage ~$580B) generated Congressional scrutiny despite being a fraction of what a carry unwind would require.

- **Operational constraint:** Swap line draws are overnight or short-term (typically 7-84 day tenors). A carry unwind requiring multi-month funding would need repeated rollovers, creating cliff risk at each maturity and requiring ongoing Congressional tolerance.

- **Moral hazard feedback:** The existence of swap lines suppresses FX vol (market participants price in the backstop), which encourages more carry positioning, which increases the eventual demand on swap lines. This is a textbook Minsky cycle. The gap between capacity and potential demand widened in iter_0008's analysis and has not narrowed.

The arithmetic: if 10-20% of the $4-6T carry notional needs to be unwound through official channels (because private dollar funding markets seize), demand is $400B-$1.2T — already at or beyond the 2008 peak on a *partial* unwind. A synchronized unwind of 30-50% of notional implies $1.2-3.0T in demand. The Fed can meet this demand in principle but the speed of deployment, the credit risk absorption, and the political economy constraints create a credibility gap.

**Key refinement from iter_0008 panel feedback:** I accept the panel's characterization that this arithmetic "deserves a dedicated claim rather than being buried." The swap line capacity gap is not merely a technical footnote — it is the single most important structural vulnerability in the crisis response architecture for FX carry. If the market reprices the Fed put on dollar funding from "unlimited and immediate" to "large but potentially delayed and conditional," the vol regime shift occurs before the actual liquidity crunch.

### Claim 3: Treasury-FX Dual Fragility Corridor

The Treasury basis trade and FX carry trade are connected through dollar funding markets:

- **Shared vulnerability:** Both trades require continuous access to short-term dollar funding (repo for basis trade, FX swap/cross-currency basis for carry). A spike in dollar funding costs propagates to both simultaneously.

- **Transmission mechanics:** (a) Basis trade stress → forced UST selling → UST volatility spike → MOVE index elevation → cross-asset vol spillover to FX; (b) FX carry unwind → demand for dollar liquidity → repo rate spike → basis trade margin calls → UST selling → recursive loop. Either market can be the entry point.

- **Speed of transmission:** The March 2020 episode demonstrated that UST-FX contagion operates in 24-72 hours. The October 2023 UST selloff caused measurable FX vol spillover within one trading session. The September 2022 UK LDI crisis transmitted from gilt market to GBP within hours.

- **Scale interaction:** The basis trade (~$800B-$1T, per OFR and Fed estimates) and FX carry ($4-6T notional) overlap in funding markets. A 1-standard-deviation funding cost shock that is manageable for either trade in isolation may be unmanageable when both need to refinance simultaneously. This is a correlation-of-correlations problem that standard VaR models miss because they estimate each trade's risk independently.

**The corridor creates non-linearity:** Small funding shocks are absorbed (normal functioning). Medium shocks affect the weaker of the two trades but are contained. Large shocks activate the feedback loop and produce outsized moves. The distribution of outcomes is bimodal — either contained or systemic — with very little probability mass in between. This is the signature of a fragile system.

### Claim 4: Amplification Channel Speed

**Margin/collateral spiral (Channel 1):** Modern clearing and margining operates in real-time. Variation margin on exchange-traded FX futures is called intraday. OTC CSAs typically require next-day settlement (some same-day). Automated risk systems at banks and prime brokers issue margin calls with minimal human intervention. The 2024 August carry unwind saw margin-driven liquidation begin within hours of the BoJ announcement. Contrast with 2007-08, where the mortgage credit unwind took weeks to produce margin-driven selling.

Speed multiplier relative to 2008: **3-5x** for the initial margin cascade. The endgame (resolution) may be similar in duration because it depends on policy response, which is human-speed.

**Redemption cascade (Channel 2):** FX carry is embedded in multi-asset hedge funds, EM local currency bond funds, and structured products. Redemption requests triggered by carry losses propagate with a lag (monthly/quarterly liquidity terms) but create a predictable second wave of selling 30-90 days after the initial shock. The August 2024 episode was contained partly because it occurred at the start of a month, limiting redemption-driven amplification.

**Counterparty opacity (Channel 3):** Who is on the other side of the carry trade? During stress, this question becomes unanswerable because OTC positioning data is lagged and incomplete. Banks reduce prime brokerage credit lines preemptively, not knowing whether their counterparties have concentrated carry exposure. This credit line withdrawal is itself an amplification mechanism — it forces deleveraging by those who still have capacity to trade, not just those experiencing losses. The dynamic was documented in granular detail during the 2008 Lehman aftermath and the 2023 Credit Suisse failure.

**Policy response window compression:** If the margin cascade operates in hours-to-days rather than days-to-weeks, central bank emergency meetings, swap line activations, and coordinated statements must also compress. The BoJ's August 2024 rapid response (Deputy Governor Uchida's dovish remarks within 2 days) showed this is possible but requires pre-positioned playbooks. The risk: a weekend or holiday-period trigger where policy machinery operates slowly while automated margin calls do not.

### Claim 5: Vol Regime Transition Zone Dynamics

Prior iterations established the ~9-10% realized G10 FX vol threshold separating regimes. The iter_0008 panel correctly identified the endogeneity problem (carry drawdowns mechanically produce elevated vol, inflating the threshold's apparent predictive power) and reduced confidence on the specific number to 6.5/10.

I accept this critique but extend the analysis to the *transition zone* behavior, which is the decision-relevant feature for hedging:

- **Vol-of-vol peaks near, not at, the threshold:** In the 8.5-10.5% range, realized vol oscillates between regimes. Some days/weeks it dips below 9%, others it spikes to 11%. This oscillation creates maximum *uncertainty about which regime the system is in*. The vol-of-vol (variance of rolling realized vol estimates) peaks in this zone, not in either stable regime.

- **Hedging paradox:** FX options are priced off implied vol, which in the low-vol regime (current: 7-9% G10 implied) is cheap. But the *probability of a regime shift* is highest when realized vol is approaching the transition zone from below — precisely the moment when implied vol begins to price higher but hasn't yet jumped. Once the regime shifts (realized vol >10.5%), implied vol reprices sharply and options become expensive. The hedging window is narrowest when the risk is highest and widest when the risk is lowest.

- **Practical implication:** The optimal hedging strategy involves pre-positioned, long-dated option structures bought during the low-vol regime (current), not reactive purchases during transition. This means accepting carry cost (negative theta) for an uncertain duration in exchange for convex exposure at the regime shift. The cost: 1-3% annualized drag on an FX carry portfolio (depending on strike selection and tenor). The benefit: protection against the 10-30% drawdowns that occur at regime shifts (iter_0008 H7: 20%+ G10 pair moves at elevated conditional probability, with wide CI).

### Claim 6: BoJ Normalization as Compound Risk

Building on iter_0008's M2 (cumulative dislocation probability):

- Each BoJ normalization step (estimated 15-25bp increments to reach ~1.0%+ from the current ~0.5%) creates a selection filter on surviving carry positions. The weakest-hands (smallest margin buffers, tightest stop-losses, highest leverage) exit at each step. What remains is a population of positions with either: (a) very deep pockets and long horizons (institutional, GPIF-adjacent), or (b) high leverage with stops placed beyond the next expected BoJ move (concentrated risk).

- **The paradox of partial normalization:** Each step that does *not* produce a carry crisis reinforces the belief that normalization is "priced in" and carry is safe. This behavioral pattern (the turkey problem — every day of feeding confirms safety until Thanksgiving) increases positioning between steps. The August 2024 episode partially reset this cycle, but the subsequent carry rebuild over 18+ months has restored it.

- **Serial correlation in BoJ actions:** If the BoJ moves once and markets stabilize, the probability of a second move within 3-6 months increases (revealed preference for normalization). But carry traders' risk budgets have been consumed by the first move, reducing their capacity to absorb the second. The combination of increased policy probability and reduced market absorption capacity creates a compounding risk that a simple per-action base rate (iter_0008: 10-15%, CI [2%, 35%]) fails to capture.

- **The 2006-07 analogue remains the only template:** Foreshock (July 2006 BoJ rate hike) → carry positions rebuild → main event (August 2007, triggered by BNP Paribas credit freeze). 13-month interval. If the August 2024 event was a foreshock, the analogue window for a main event extends through late 2025 and into 2026. We are now within or just past this window. The analogue is not predictive (n=1), but it provides the only historical framework for how BoJ normalization and carry fragility interact over multi-step sequences.

### Claim 7: Agricultural Amplification Channel

Prior iterations (iter_0007, iter_0008) established the agricultural supply-inflation-rate differential transmission chain through the commodities analysts. I integrate this into the VTA crisis mechanics framework:

- **The reflexive loop:** Food price spike → EM central banks unable to cut (30-50% food CPI weight in many EMs) → EM rate differentials widen → carry traders increase EM carry positions (higher spread) → EM currencies appreciate (masking underlying vulnerability) → EM current account deterioration (capital inflow substituting for trade surplus) → sudden reversal when food prices moderate or a second shock hits → EM currency depreciation + carry unwind simultaneously.

- **Why standard models miss this:** FX risk models treat rate differentials as exogenous inputs and agricultural commodity prices as unrelated to FX risk. The reflexive loop makes rate differentials endogenous to commodity dynamics, which are endogenous to weather events with fat-tailed distributions. The resulting compound distribution has much fatter tails than the individual marginal distributions suggest.

- **Current vulnerability:** Corn stocks-to-use ex-China <15% (iter_0008 M13), placing the system on the convex portion of the price-stocks curve. A single major growing season failure (US Midwest drought, Brazilian safrinha disruption) could trigger the cascade. The El Nino/La Nina transition cycle, combined with climate trend increasing weather variance, elevates the base rate of such events above historical norms.

- **Amplification interaction with BoJ risk:** A food price spike coinciding with BoJ normalization would create a two-front carry stress: EM leg (widening differentials attracting more carry, then reversing) and G10 leg (JPY funding cost increase). The joint probability is low (~2-5% within 12 months) but the impact would be outsized because the carry positions exposed to each risk partially overlap.

### Claim 8: August 2024 As Partial Out-of-Sample Test

The August 5, 2024 JPY carry unwind provides the most recent real-world test of the VTA framework:

**What the VTA framework predicted correctly:**
- The trigger (BoJ rate hike + weak US payrolls) was exogenous to carry positioning — consistent with the framework's emphasis on triggers being unpredictable.
- Amplification operated through margin/collateral calls and vol-targeting strategy deleveraging — the two fastest channels.
- PCA dimensionality collapsed (consistent with H6 from iter_0008).
- Cross-currency basis widened (consistent with H10, though not with sufficient lead time to be an "early warning").
- Speed was extreme: 3 trading days from trigger to peak Nikkei drawdown of ~12%.

**What the framework did not predict (containment factors):**
- The BoJ's rapid communication (Deputy Governor Uchida's dovish remarks on August 7) arrested the unwind. Policy response speed matched the crisis speed — this may not recur if the trigger is more ambiguous.
- Carry positioning was at moderate levels (~65th percentile by CFTC data), not at extremes. A trigger hitting when positioning is at 85th+ percentile would face less absorption capacity.
- Credit conditions were benign — HY spreads were tight, bank funding markets were calm. The iter_0008 panel correctly noted (H9) that credit cycle conditions amplify severity but the August 2024 episode lacked this amplifier.
- Vol-targeting and risk-parity strategy deleveraging was sharp but quickly reversed as vol mean-reverted, preventing the second-wave redemption cascade.

**Lessons for the current configuration (March 2026):**
- Carry positions have rebuilt beyond August 2024 pre-shock levels.
- The BoJ has continued normalizing (current rate ~0.5%), with further hikes expected. Each hike is a potential trigger.
- Credit conditions have tightened modestly (maturity wall approaching 2026-2028, CRE stress ongoing in some regions), adding a partial amplifier that was absent in August 2024.
- The containment playbook (BoJ dovish communication) has been revealed, which paradoxically may reduce its future effectiveness — market participants may front-run the expected BoJ retreat, and the BoJ may feel constrained to "not be seen as caving to markets" on subsequent occasions.

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1. VTA prerequisites satisfied | **8/10** | Empirically grounded in observable data (positioning, maturity mismatch, concentration, opacity). The framework correctly identified vulnerability in August 2024. Limitation: necessary but not sufficient — timing remains unpredictable. Reduced from 8.5 in iter_0008 to reflect the panel's valid point that individual base rate CIs are wide and the framework provides directional, not probabilistic, guidance. |
| 2. Swap line capacity gap | **7.5/10** | The arithmetic is straightforward and the political/operational constraints are documented from 2008-09 Congressional hearings. Confidence limited by: the Fed could theoretically commit unlimited resources, and the historical peak ($580B) was never tested against the ceiling. The gap is about *speed of deployment and political willingness*, not absolute capacity. |
| 3. Treasury-FX dual fragility | **7/10** | Mechanistically sound and partially validated by March 2020 and October 2023 episodes. Confidence limited by: the basis trade size is estimated, not precisely known; the degree of overlap in funding markets is approximate; and central bank intervention (e.g., SRF, standing repo facility) provides a partial circuit breaker not present in 2020. |
| 4. Amplification speed increase | **7.5/10** | The 3-5x speed multiplier for margin cascades is directionally validated by August 2024 (3 trading days vs. weeks in prior episodes). Confidence limited by: the speed of containment also increased (BoJ responded in 2 days), so the net effect on crisis severity is ambiguous. The margin channel speed is observable; the policy response speed is less predictable. |
| 5. Vol regime transition dynamics | **7/10** | The vol-of-vol peak in the transition zone is consistent with regime-switching model theory and observable in historical data. The hedging paradox is a logical consequence. Confidence limited by: the specific transition zone boundaries (8.5-10.5%) are approximate and may shift with market structure; the endogeneity critique from iter_0008 reduces confidence in any specific threshold. |
| 6. BoJ compound risk | **6.5/10** | The selection bias mechanism (weakest hands exit first, residual positions more fragile) is logically sound. Confidence limited by: n=1 for the 2006-07 analogue; the per-step base rate CI is extremely wide ([2%, 35%]); the BoJ has been the "graveyard of hawkish forecasts" for 30 years (challenger_02's valid critique from iter_0008). The direction of risk (compounding) is more reliable than the magnitude. |
| 7. Agricultural amplification channel | **6/10** | The reflexive loop is mechanistically plausible and each component link has supporting evidence. Confidence limited by: the full loop has never been observed in isolation (prior episodes involved multiple simultaneous triggers); the food-inflation-rate channel operates on 3-12 month lags, which may allow policy response before carry stress materializes; the quantitative contribution of the agricultural channel vs. other amplifiers is unestimated. |
| 8. August 2024 VTA validation | **8.5/10** | This is a retrospective assessment of a documented event, which is inherently more confident than forward-looking claims. The framework's predictions about speed, channels, and PCA collapse were confirmed. The containment factors provide specific, testable conditions for when a future episode might not be contained. |

## Connections to Other Topics

**Monetary Policy & Central Bank Frameworks:** The BoJ normalization trigger directly connects to the monetary policy divergence that drives rate differentials. The swap line architecture is a monetary policy tool. The vol regime that governs carry behavior is itself a function of central bank forward guidance and balance sheet policy. The "central bank put" on vol suppression is the deepest connection — every crisis in the VTA framework ultimately tests whether central banks can backstop faster than markets can unwind.

**Credit-Equity Linkage & Contagion Channels:** The dual fragility corridor (Treasury basis trade <-> FX carry) is a specific instance of credit-equity-FX contagion. The credit cycle's role as severity amplifier (iter_0008 H9) directly connects carry dynamics to credit spreads. The 2026-2028 maturity wall creates a time-bound window where credit stress and carry stress could coincide, the joint probability of which is far more dangerous than either marginal probability.

**Commodity Price -> Inflation Transmission Mechanisms:** The agricultural amplification channel (Claim 7) is a direct extension of the commodity-inflation work. The energy channel (oil surplus weakening the BoP amplifier per commodities_analyst_01) and the agricultural channel (food prices creating rate floors per commodities_analyst_02) have opposite directional implications for carry vulnerability, creating a within-topic tension that requires integration.

**Volatility Regimes:** The vol regime transition zone (Claim 5) is the primary connection. The carry trade is effectively a short-vol position, so carry dynamics *are* volatility regime dynamics viewed through the FX lens. The correlation amplification during stress (carry-equity from 0.3 to 0.8; carry-momentum from -0.2 to +0.7) is a direct manifestation of the vol regime shift.

**Risk Appetite Regimes:** Carry is a risk appetite proxy — carry returns track VIX inversion, high-yield spreads, and equity risk premium compression. A shift in the risk appetite regime would reprice carry before the fundamental drivers (rate differentials) change. The carry-to-vol ratio at 90th+ percentile (iter_0008 H12) is itself a risk appetite indicator suggesting complacency.

**Sovereign Debt Dynamics:** Dollar cycle analysis (iter_0008 L7) connects carry to the structural dollar overvaluation and twin deficit dynamics. A carry crisis that produces sharp dollar appreciation would tighten financial conditions globally via the dollar as "risk factor," transmitting FX stress to sovereign debt sustainability for dollar-denominated borrowers.

## Open Questions

1. **Positioning reconstruction quality:** How much carry was rebuilt between August 2024 and March 2026? CFTC data shows partial recovery, but the critical OTC and offshore components remain unobservable. Without a better positioning estimate, the VTA leverage assessment is calibrated to within +/-30-40% — enough for directional analysis but insufficient for threshold-based trigger identification.

2. **Vol-of-vol dynamics in the transition zone — is the peak shifting?** Post-2020 changes in market structure (more systematic strategies, faster margin calls, standing repo facility) may have altered the transition zone boundaries. Has the peak vol-of-vol band shifted from 8.5-10.5% to a different range? This requires updated rolling estimation that cannot be performed from first principles alone.

3. **Swap line political economy in 2026:** The political environment for Fed swap line deployment has changed since 2008-09. Would the current administration support $1T+ in swap line deployment to foreign central banks during a carry crisis? The political constraint may be tighter than the operational one, but quantifying political willingness ex ante is speculative.

4. **How does the standing repo facility (SRF) change the Treasury-FX dual fragility?** The SRF was specifically designed to prevent March 2020-style Treasury market dysfunction. If it works as intended, one leg of the dual fragility corridor is reinforced, potentially preventing the feedback loop. But the SRF has not been tested under genuine stress, and its counterparty eligibility (primary dealers only) means non-bank holders of the basis trade cannot access it directly.

5. **Joint probability estimation:** The VTA framework identifies four prerequisites and multiple triggers. The relevant risk metric is the joint probability of trigger activation *conditional on* all prerequisites being satisfied. This joint distribution is not estimable from data (sample size of crisis episodes is ~5-8) and structural assumptions about independence are demonstrably wrong (triggers and vulnerabilities co-evolve). Is there a principled way to bound the joint probability beyond "elevated relative to unconditional base rate"?

6. **Does the August 2024 containment playbook degrade with reuse?** The BoJ's dovish pivot arrested the carry unwind in 2024. If this playbook is reused on the next BoJ-triggered carry stress, does its effectiveness decline (market participants front-run the dovish pivot, reducing the unwind before the statement, but also reducing the BoJ's credibility on normalization)? Or does it remain effective because the carry community has a revealed preference for believing dovish guidance? The behavioral dynamics of repeated policy intervention during carry stress are theoretically ambiguous.

7. **What is the minimum shock size required to shift from the contained (August 2024) to the systemic (2008) regime?** The containment factors identified in Claim 8 — moderate positioning, benign credit, rapid policy response — provide a partial answer, but the functional form of the relationship between these factors and crisis severity is unknown. Is it continuous (gradually worse as conditions deteriorate) or threshold (contained until a tipping point, then sudden phase transition)? The historical record supports the threshold interpretation, but the sample is too small to be confident.

8. **How does the dedollarization trend, even if slow, interact with swap line credibility over a 3-5 year horizon?** If non-dollar settlement of commodity trade increases from the current ~5-8pp shift, does this structurally reduce the demand for dollar liquidity during carry crises (fewer dollar-denominated obligations to refinance), or does it reduce the *supply* of dollars in normal times (fewer petrodollar recycling flows), making the system *more* fragile when a dollar squeeze occurs? The net effect is ambiguous and depends on whether the reduction is in gross or net dollar flows.
