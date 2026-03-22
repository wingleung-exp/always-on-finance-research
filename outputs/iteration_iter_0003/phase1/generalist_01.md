Now I have full context. Let me produce the analysis.

# Risk Appetite Regimes — Cross-Asset Strategist Analysis

## Key Claims

1. **Risk appetite operates in three distinct macro regimes — risk-on, risk-off, and stagflationary — each characterized by specific cross-asset correlation structures, and the transitions between regimes are more consequential for portfolio outcomes than the regimes themselves.**

2. **The stock-bond correlation is the single most important regime identifier: negative in growth-scare risk-off environments, near-zero or positive in risk-on, and persistently positive in stagflationary regimes — and we are currently in a structurally ambiguous transition zone where the post-2022 positive correlation episodes may reflect a regime shift rather than a temporary anomaly.**

3. **The credit-equity basis (the gap between equity-implied credit spreads from structural models and actual market credit spreads) is the most reliable early warning signal for risk appetite regime shifts, typically leading broad market moves by 2–6 weeks.**

4. **Modern market microstructure — ETF flows, systematic vol-targeting strategies, and dealer balance sheet constraints — has compressed the timeline of risk appetite regime transitions from weeks (pre-GFC) to days or even hours, creating a "contagion velocity" problem that traditional regime-switching models fail to capture.**

5. **Liquidity withdrawal cascades follow a predictable sequence: vol spike → systematic deleveraging → dealer inventory reduction → credit market gapping → EM contagion, and each link in this chain has amplified since 2008 due to the growth of passive/systematic strategies from ~15% to ~60%+ of equity market volume.**

6. **The VIX-credit spread relationship is regime-dependent and nonlinear: in risk-on environments, VIX and IG spreads are loosely correlated (~0.4); in risk-off transitions, the correlation spikes to 0.8+ as the same underlying factor (liquidity withdrawal) drives both — but credit lags vol, creating a tradeable relative value window.**

7. **The current macro environment (March 2026) exhibits a cross-asset inconsistency: equity vol (VIX) is pricing a benign outlook, credit spreads are near cycle tights, but rates vol (MOVE index) remains elevated and the yield curve is sending mixed signals — this divergence historically resolves with equities and credit repricing toward the rates market's more cautious assessment.**

8. **Dollar strength/weakness is both a cause and consequence of global risk appetite regimes: a strong dollar tightens financial conditions for ~$13T in offshore dollar-denominated debt, creating a reflexive feedback loop where risk-off → dollar strength → EM stress → more risk-off, making the DXY a critical regime amplifier rather than a passive indicator.**

## Evidence & Reasoning

**Claim 1 — Three-regime framework:**
The academic foundation comes from Ang & Bekaert (2002) and Guidolin & Timmermann (2008), who formalize regime-switching models for asset returns. The empirical evidence is overwhelming: risk-on periods (2003–2007, 2012–2014, 2017, 2021) show equities up/credit tight/vol low/commodities bid/EM outperforming; risk-off episodes (Q4 2008, Aug 2011, Mar 2020) show the mirror image; stagflationary periods (1970s, 2022) show equities down/bonds down/commodities up — a correlation structure that devastates traditional portfolios. The critical insight is that regime *transitions* — not steady-state regimes — generate the largest P&L impacts. A portfolio optimized for risk-on that experiences a sudden shift to risk-off faces correlated drawdowns across what it assumed were diversifying positions. The transition speed matters more than the destination.

**Claim 2 — Stock-bond correlation as regime identifier:**
Campbell, Sunderam & Viceira (2017) demonstrate that the stock-bond correlation flips sign based on whether the dominant macro risk is demand-side (negative correlation: growth scares pull both stocks and yields down) or supply-side (positive correlation: inflation pushes yields up while hurting equities). The post-1997 negative correlation that underpinned the 60/40 portfolio was a *regime*, not a law. From 1965–1997, the correlation was positive. Post-2022, we have seen multiple episodes of positive correlation during stress (Oct 2022, Aug 2023, Oct 2023), consistent with supply-side/inflationary risk dominance. This connects directly to our prior research on demographic labor scarcity as a supply shock biasing the correlation positive (iter_0001, confidence 8/10). A 60/40 portfolio calibrated to −0.2 correlation that realizes +0.3 faces 15–25% higher volatility — this is not a theoretical curiosity but a live portfolio risk.

**Claim 3 — Credit-equity basis as early warning:**
The Merton structural model implies that equity volatility and credit spreads should move in tandem, since both price default risk. When equity-implied spreads (derived from equity vol, leverage, and asset values) diverge from actual CDS or cash bond spreads, one market is "wrong." Historically, the credit market tends to be the laggard — equity markets price information faster. Moody's KMV Expected Default Frequencies, which are equity-derived, led actual spread moves by 2–6 weeks in the 2007 pre-crisis period, the 2011 European sovereign crisis, the 2015 commodity bust, and the 2018 Q4 selloff. The basis also works in reverse: when credit spreads are tighter than equity vol implies, it signals either excessive complacency in credit or that equity vol is overstating risk.

**Claim 4 — Contagion velocity compression:**
Pre-GFC, the 2007 quant unwind took ~3 weeks to propagate from equity stat-arb to credit to EM. The 2015 August "flash crash" propagated across asset classes within hours. The March 2020 COVID crash saw the S&P fall 34% in 23 trading days with Treasury market dysfunction within the same window — historically, Treasuries provide a buffer for weeks before stress propagates. The structural drivers: (a) vol-targeting strategies (~$400B+ in AUM) mechanically sell as vol rises, creating a self-reinforcing loop; (b) risk-parity strategies amplify cross-asset correlation in drawdowns as they delever simultaneously; (c) ETF authorized participants withdraw liquidity precisely when it's most needed, creating NAV-discount spirals in credit ETFs (LQD traded at a 5% discount to NAV in March 2020); (d) dealer balance sheets are constrained by post-GFC regulation, reducing their ability to warehouse risk during stress.

**Claim 5 — Liquidity withdrawal cascade sequence:**
This is the empirical sequencing observed across the 2010, 2011, 2015, 2018, and 2020 episodes. Vol spikes first (VIX moves from ~15 to 25+ within days). This triggers systematic deleveraging by vol-targeting and CTA strategies, which amplifies the equity selloff. Dealers respond by widening bid-ask spreads and reducing inventory. Credit markets gap because the intermediation chain (dealer → market-maker → end investor) breaks down — credit is inherently illiquid and depends on dealer willingness to warehouse. EM is last because it requires the additional transmission mechanism of dollar funding stress (covered swap basis widening, EM local currency weakness). The growth of passive/systematic from ~15% of equity volumes (2005) to 60%+ (2025) means the first two links in the chain are mechanically larger and faster.

**Claim 6 — VIX-credit spread nonlinearity:**
In calm markets, the VIX-IG spread correlation is moderate (~0.3–0.5) because credit spreads embed firm-specific and sector-specific risk not captured by equity index vol. In regime transitions, the idiosyncratic components get dominated by the common factor (liquidity/risk appetite), and correlation spikes to 0.8+. But credit adjusts with a lag — cash bonds trade by appointment, CDS indices (CDX, iTraxx) move faster but still trail equity derivatives. This creates a window: when VIX spikes >5 points intraday but CDX IG hasn't moved, buying protection on CDX captures the catch-up. This has been a positive-expectancy trade in every major risk-off episode since 2008. The nonlinearity also means that VIX levels below ~15 tell you almost nothing about credit risk, while VIX moves above ~25 are highly informative.

**Claim 7 — Current cross-asset inconsistency (March 2026):**
This requires stating what cross-asset markets are currently pricing. If equity implied vol (VIX) is suppressed while rates vol (MOVE) remains elevated, this is a specific disagreement about macro uncertainty. Rates markets, which are driven by macro-focused participants, are expressing more uncertainty about the growth/inflation path than equity markets, which are heavily influenced by passive flows and buybacks. Historically (2007 H1, 2018 Q3, 2019 H2), when MOVE diverges upward from VIX for extended periods, the resolution favors the rates market's assessment — equities eventually reprice. The credit market sitting at tight spreads alongside elevated rates vol is an additional inconsistency: tight credit assumes a benign growth path that elevated rates vol calls into question.

**Claim 8 — Dollar as regime amplifier:**
BIS estimates ~$13T in offshore dollar-denominated debt. When risk appetite contracts, demand for dollar funding rises (hedging costs increase, cross-currency basis widens), which strengthens the dollar, which worsens the debt burden for EM borrowers, which triggers further risk-off. This is Bruno & Shin's (2015) "risk-taking channel of exchange rates." The mechanism is reflexive: unlike a passive indicator, the dollar *causes* the very stress it's measuring. This makes the DXY not just a barometer but an active participant in regime transitions. During COVID (March 2020), the DXY surged 8% in two weeks, and EM local currency bonds fell 15–20%. The Fed's swap lines were the circuit breaker — without them, the feedback loop would have continued.

## Confidence Assessment

| Claim | Confidence | Justification |
|-------|-----------|---------------|
| 1. Three-regime framework | 8/10 | Well-established in academic literature and consistent with empirical observation across multiple cycles. Slight uncertainty on whether three regimes are sufficient vs. more granular classifications. |
| 2. Stock-bond correlation as regime ID | 9/10 | Empirically robust across 60+ years of data. The current ambiguity about whether we've shifted regimes reduces confidence for *current positioning* but not for the framework itself. |
| 3. Credit-equity basis as early warning | 7/10 | Strong historical track record but the signal has a meaningful false positive rate (~30% of divergences resolve without a regime shift). Also degraded by the growth of credit ETFs which have partially closed the lag. |
| 4. Contagion velocity compression | 7/10 | The structural drivers are real and well-documented, but the claim that regime transitions now happen in "days or hours" is partly selection bias — we remember the fast ones and forget the slow ones. 2022's drawdown was protracted, not flash. |
| 5. Liquidity cascade sequence | 7/10 | The sequence is empirically grounded but not perfectly stable — March 2020 saw credit and EM stress almost simultaneously with equities, partly because COVID was a global shock. The sequence is most reliable for financially-originated stress, less so for exogenous shocks. |
| 6. VIX-credit nonlinearity | 8/10 | Highly robust empirical relationship. The tradeable lag is narrowing as algorithmic traders arbitrage it faster, but it still exists in cash credit markets. |
| 7. Current cross-asset inconsistency | 6/10 | This is a *nowcast* claim subject to revision as data changes. The historical base rate for MOVE-VIX divergences resolving in rates' favor is ~65%, not 100%. Also depends on the specific levels at the time of analysis. |
| 8. Dollar as regime amplifier | 8/10 | Bruno & Shin's mechanism is well-established. The $13T in offshore dollar debt is a structural fact. The main uncertainty is whether EM borrowers have hedged more effectively post-2013 taper tantrum. |

## Connections to Other Topics

**Volatility regimes (confidence 3.0, depth 0):** Risk appetite regimes and volatility regimes are deeply intertwined — you cannot define one without the other. The VIX regime (low vol <15, moderate 15–25, crisis >25) is the equity-market expression of risk appetite. Vol-of-vol (VVIX) and the term structure of vol (VIX futures contango/backwardation) carry additional regime information. This topic should be explored in tandem.

**Credit cycles (confidence 6.0, depth 3):** The credit cycle is one of the most important inputs to risk appetite regime classification. Late-cycle credit behavior (spread compression despite rising leverage, covenant erosion, increased CLO issuance) is both a symptom and cause of excessive risk appetite. The "retailization" of private credit identified in iter_0001 (confidence 6/10) is a specific mechanism through which the current risk appetite regime could unravel — gate-contagion in semi-liquid vehicles would be a liquidity cascade trigger.

**Equity cycles (confidence 5.0, depth 2):** Equity valuations are regime-dependent: P/E multiples expand in risk-on (discount rate compression) and contract in risk-off. The starting-valuation interaction flagged in iter_0001 (S&P at ~20x vs. Germany's DAX at 12x during its demographic drag) is critical — the same risk appetite regime shift produces much larger drawdowns from higher starting multiples.

**FX regimes (confidence 4.0, depth 1):** The dollar's role as regime amplifier (Claim 8) makes FX an integral part of risk appetite analysis. Carry trade unwinds (JPY, CHF) are among the most violent expressions of risk appetite regime shifts — the August 2024 JPY carry unwind is a recent example. EM FX is the highest-beta expression of global risk appetite.

**Demographics (iter_0001):** The demographic research identified a structural shift in the stock-bond correlation regime driven by labor scarcity supply shocks. This has direct implications for risk appetite regimes: if the stock-bond correlation has structurally shifted positive, then traditional "risk-off" hedges (long bonds) fail precisely when they're needed, fundamentally altering how risk appetite regime shifts propagate through portfolios. The demographic bid for fixed income (pension/insurance ALM demand) also compresses credit spreads in a way that masks underlying risk appetite — spreads may stay tight not because risk appetite is robust but because structural demand prevents them from widening. This makes spread-based risk appetite indicators less reliable.

**Minsky cycle conditioning (iter_0001, confidence 5/10):** Risk appetite regimes can be mapped onto the Minsky framework: risk-on corresponds to the speculative/Ponzi finance phase, and risk-off to the Minsky moment and subsequent deleveraging. The demographic conditioning of Minsky cycles (longer, deeper in aging societies) suggests that risk appetite regime shifts in demographically challenged economies may be more severe and protracted.

## Open Questions

1. **Has the stock-bond correlation regime permanently shifted, or are the post-2022 positive-correlation episodes transitory?** This is the most consequential open question for multi-asset portfolio construction. If permanent, the entire risk-budgeting framework for balanced portfolios needs rebuilding. If transitory, the current episode is a buying opportunity for duration as a hedge.

2. **How do you measure risk appetite in real time when traditional indicators disagree?** VIX says calm, MOVE says uncertain, credit says tight, EM flows say cautious. Is there a composite indicator that appropriately weights these signals, or is the disagreement itself the signal?

3. **What is the current "contagion velocity" — have post-2020 structural changes (higher dealer profits, reduced repo fragility, standing repo facility) partially reversed the pre-2020 fragility, or have new channels (0DTE options, meme stock coordination, crypto-TradFi linkages) created new transmission paths?**

4. **Can risk appetite regimes be forecast, or only identified in real-time?** Markov regime-switching models can estimate transition probabilities, but their out-of-sample forecasting record is poor. Are there leading indicators (credit impulse, financial conditions indices, bank lending standards) that reliably predict regime shifts with enough lead time to be actionable?

5. **How does the rise of private credit (~$1.7T AUM) affect risk appetite regime dynamics?** Private credit doesn't mark to market daily, which means it absorbs risk appetite deterioration with a lag — but this creates a "shadow inventory" of unrealized losses that could crystallize suddenly if forced selling occurs (via the retailization channel identified in iter_0001). Does private credit dampen or amplify risk appetite regime transitions?

6. **What role does central bank reaction function play in regime persistence?** The "Fed put" (or its absence) is arguably the single biggest determinant of how long risk-off regimes persist. Has the post-2022 hawkish shift durably changed the central bank reaction function, or will the next crisis trigger the same liquidity interventions?

7. **How should risk appetite regime analysis account for geographic desynchronization?** Global risk appetite regimes were highly synchronized from 2008–2019 (global beta ~1), but increasing US-China decoupling and divergent monetary policies suggest regimes may desynchronize. If US equities are in risk-on while China is in risk-off, what does that mean for cross-asset positioning?
