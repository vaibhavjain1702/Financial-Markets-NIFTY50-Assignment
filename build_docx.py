from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document()

# --- Styles ---
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)

def add_title(text):
    p = doc.add_heading(text, level=1)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

def add_section(text):
    doc.add_heading(text, level=2)

def add_sub(text):
    doc.add_heading(text, level=3)

def add_para(text, bold=False):
    p = doc.add_paragraph(text)
    if bold:
        for run in p.runs:
            run.bold = True

def add_bullet(text):
    doc.add_paragraph(text, style='List Bullet')

def add_img(path, width=6.0):
    if os.path.exists(path):
        doc.add_picture(path, width=Inches(width))
        last = doc.paragraphs[-1]
        last.alignment = WD_ALIGN_PARAGRAPH.CENTER

def add_break():
    doc.add_page_break()

G = "graphs/"

# ============================================================
# TITLE PAGE
# ============================================================
doc.add_paragraph("")
doc.add_paragraph("")
add_title("NIFTY 50 Historical Stock Price Analysis")
add_title("Comprehensive Graph-by-Graph Interpretation")
doc.add_paragraph("")
p = doc.add_paragraph("Course: Financial Markets – From Fundamentals to AI-Driven Analytics")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p = doc.add_paragraph("Analysis Period: January 2009 – December 2013")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p = doc.add_paragraph("Index: NIFTY 50 (National Stock Exchange of India)")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p = doc.add_paragraph("Question 3 – 10 Marks")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
add_break()

# ============================================================
# 1. CLOSING PRICE GRAPHS (5 graphs)
# ============================================================
add_section("1. Closing Price Time Series (Groups 1–5)")

add_para("These 5 plots show the daily adjusted closing prices (in INR) for all ~49 NIFTY 50 stocks over the 5-year period (2009–2013). Each plot contains approximately 10 stocks for readability.")

add_sub("What does a Closing Price graph signify?")
add_bullet("The closing price is the last traded price of a stock on a given trading day. It is the single most important price point because mutual funds, index values, and portfolio NAVs are all calculated using it.")
add_bullet("An upward trend means the company is growing in value (investors are willing to pay more). A downward trend means the company is losing market confidence.")
add_bullet("When multiple stock lines move together (up or down), it shows that the entire market is being driven by a common macro factor rather than individual company performance.")

add_sub("Key observations across all 5 plots:")
add_bullet("Starting Point (Jan 2009): All stocks start at their lowest levels because this is the tail-end of the 2008 Global Financial Crisis. The market had crashed ~60% from its 2008 peak.")
add_bullet("Sharp V-shaped Recovery (Mar 2009 – Dec 2010): After March 2009, almost every stock rallied sharply. This was driven by global stimulus packages, RBI rate cuts, and renewed FII (Foreign Institutional Investor) inflows into India.")
add_bullet("Mid-period Plateau & Dip (2011): Stocks flattened or dipped during mid-2011 due to the European Sovereign Debt Crisis and the US Debt Ceiling standoff. Indian markets were hit by capital outflows.")
add_bullet("Divergence (2012–2013): After the 2011 crisis, stocks began to diverge. Defensive sectors (FMCG like HUL, ITC; Pharma like Sun Pharma, Dr. Reddy's) kept climbing, while cyclical sectors (Metals like Tata Steel, Hindalco; Infrastructure like DLF, Reliance Infra) stayed flat or declined.")

for i in range(1, 6):
    add_sub(f"Group {i}")
    add_img(f"{G}graph_{i:02d}_plot-prices.png")
    doc.add_paragraph("")

add_sub("Winners & Losers of the Period:")
add_bullet("Best Performers: Asian Paints, TCS, HCL Tech, HDFC Bank, Bajaj Auto – these stocks saw 3x to 5x growth from 2009 to 2013. They benefited from India's consumption boom and IT export growth.")
add_bullet("Worst Performers: DLF, Reliance Infrastructure, Reliance Power – these infrastructure/real estate stocks never recovered to their 2008 highs due to regulatory issues, debt problems, and slowing construction activity.")
add_bullet("Steady Growers: ITC, Hindustan Unilever, Infosys – these 'blue chips' showed consistent upward trends with lower volatility, making them 'safe haven' stocks.")

add_break()

# ============================================================
# 2. LOG RETURNS GRAPHS (5 graphs)
# ============================================================
add_section("2. Log Returns Time Series (Groups 1–5)")

add_sub("What are Log Returns and why do we use them?")
add_bullet("Log Return = ln(P_t / P_{t-1}), where P_t is today's price and P_{t-1} is yesterday's price.")
add_bullet("Unlike simple percentage returns, log returns are time-additive (you can sum daily log returns to get weekly/monthly returns) and they are approximately normally distributed, which makes them ideal for statistical analysis like correlation matrices.")
add_bullet("A value of 0 means no change. Positive values mean the stock went up. Negative values mean it went down. A value of +0.05 means roughly a +5% daily gain.")

add_sub("What does a Log Returns graph signify?")
add_bullet("The 'thickness' or 'spread' of the band around zero represents VOLATILITY. A thin, tight band means the stock is calm and predictable. A wide, spiky band means the stock is highly volatile and risky.")
add_bullet("Sudden large spikes (both positive and negative) represent 'shock events' – earnings surprises, policy announcements, or global crises.")
add_bullet("When ALL stocks show wide bands simultaneously, it means the entire market is in a state of panic or euphoria.")

add_sub("Key observations across all 5 plots:")
add_bullet("Early 2009 (Widest Bands): The log return bands are at their widest here. Daily swings of ±5% to ±10% were common. This is the 'fear zone' at the bottom of the GFC.")
add_bullet("2010–2012 (Moderate Bands): Volatility settled down as the recovery matured. Occasional spikes appear around May 2010 (Flash Crash) and Aug 2011 (EU Crisis).")
add_bullet("2013 (Calm then Spike): Most of 2013 was relatively calm, but a sharp spike appears in May–June 2013 (Taper Tantrum) when the US Fed signaled it would reduce stimulus.")
add_bullet("The horizontal dashed line at y=0 is the 'zero return' baseline. Stocks spending more time above this line are in an uptrend; stocks hovering around it are stagnant.")

for i in range(6, 11):
    add_sub(f"Group {i-5}")
    add_img(f"{G}graph_{i:02d}_plot-log-returns.png")
    doc.add_paragraph("")

add_break()

# ============================================================
# 3. FULL-PERIOD CORRELATION MATRIX
# ============================================================
add_section("3. Full-Period Correlation Matrix (Heatmap)")

add_img(f"{G}graph_11_corr-matrix.png", 6.5)
doc.add_paragraph("")

add_sub("What is this matrix?")
add_bullet("This is a 49×49 grid where each cell shows the Pearson correlation coefficient between the log returns of two stocks over the entire 5-year period.")
add_bullet("Correlation ranges from -1 (perfectly opposite movement) to +1 (perfectly identical movement). A value of 0 means no relationship.")
add_bullet("The diagonal is always 1.0 (every stock is perfectly correlated with itself).")

add_sub("How to read the colors:")
add_bullet("Dark Green (0.6 to 1.0): These stock pairs move very closely together. They are in the same sector or respond to the same economic drivers. Holding both gives you almost no diversification benefit.")
add_bullet("Light Green / Yellow (0.2 to 0.5): Moderate correlation. These stocks are somewhat related but have enough independence to provide some diversification.")
add_bullet("Red / Orange (below 0.1 or negative): These pairs move independently or in opposite directions. They are the BEST pairs for diversification.")

add_sub("Key observations:")
add_bullet("Banking Cluster: HDFC Bank, ICICI Bank, Axis Bank, SBI, Kotak Bank, PNB all show high mutual correlations (0.5–0.8). This makes sense – all banks respond to RBI policy rates, credit growth, and NPA fears.")
add_bullet("IT Cluster: TCS, Infosys, Wipro, HCL Tech show moderate-to-high correlations with each other (0.4–0.7) but LOWER correlation with banks and metals. This is because IT revenue comes from US/Europe, not India.")
add_bullet("Metals Cluster: Tata Steel, Hindalco, JSW Steel, SAIL, Jindal Steel correlate highly (0.5–0.7) because they all depend on global commodity prices and Chinese demand.")
add_bullet("Defensive vs Cyclical: FMCG stocks (HUL, ITC) show the LOWEST correlation with metals and infrastructure stocks. This is the core principle of diversification – pair defensive stocks with cyclical ones.")
add_bullet("Mean Correlation (~0.35): The overall average is positive because all 49 stocks belong to the same Indian economy and are influenced by the same macro factors (GDP growth, monsoon, RBI policy, FII flows).")

add_break()

# ============================================================
# 4. ROLLING CORRELATION HEATMAPS
# ============================================================
add_section("4. Rolling Correlation Heatmaps (3 Sample Epochs)")

add_img(f"{G}graph_12_plot-sample-rolling.png", 6.5)
doc.add_paragraph("")

add_sub("What are these 3 heatmaps?")
add_bullet("These are 3 'snapshots' of the correlation matrix at different points in time – Early (2009), Mid (~2011), and Late (2013).")
add_bullet("Each snapshot uses only 20 trading days of data (the 'epoch window'), giving a short-term view of how stocks were related during that specific month.")

add_sub("Key observations:")
add_bullet("Early Period (2009): The heatmap is overwhelmingly GREEN/YELLOW. Almost every pair has high correlation (0.4–0.8). This is the 'Crisis Correlation' effect – during the GFC bottom, ALL stocks were crashing together. Diversification was useless.")
add_bullet("Mid Period (~2011): The heatmap shows a MIX of green and yellow with some lighter patches. Correlations have eased from the crisis peak, but remain elevated during the EU Debt Crisis period.")
add_bullet("Late Period (2013): More COLOR VARIATION appears. Some pairs are green (correlated), some are yellow/orange (less correlated). This indicates the market has 'normalized' – individual stock fundamentals matter more than macro panic.")
add_bullet("The Key Takeaway: Correlation is NOT a fixed number. It changes dramatically based on market conditions. Risk models that assume fixed correlations (like basic Modern Portfolio Theory) will FAIL during crises.")

add_break()

# ============================================================
# 5. CRASH EPOCH DETECTION PLOT
# ============================================================
add_section("5. Mean Rolling Correlation with Crash Epoch Markers")

add_img(f"{G}graph_13_plot-crash.png", 6.5)
doc.add_paragraph("")

add_sub("What does this graph show?")
add_bullet("The BLUE LINE traces the mean pairwise correlation across all ~49 stocks over time. Each point represents one 20-day rolling window (epoch).")
add_bullet("The GRAY DOTTED LINE is the overall average mean correlation across the entire 5 years. It serves as a 'normal' baseline.")
add_bullet("The RED DASHED LINE is the 'Crash Threshold' = Mean + 1.5 × Standard Deviation. Any epoch where correlation exceeds this line indicates abnormally high market synchronization – a potential crash or stress event.")
add_bullet("The RED DOTS are the specific epochs that breached the crash threshold.")

add_sub("What each annotated event means:")
add_bullet("GFC Bottom (Mar 2009): The correlation spike here shows the final wave of panic selling from the 2008 crisis. Every stock was being sold indiscriminately. The market bottomed on March 9, 2009 – after which the recovery began.")
add_bullet("Flash Crash (May 2010): On May 6, 2010, the US Dow Jones plunged ~1000 points in minutes due to algorithmic trading errors. This panic briefly spread to Indian markets, causing a correlation spike.")
add_bullet("US Debt / EU Crisis (Aug 2011): This is the BIGGEST spike. In August 2011, S&P downgraded US debt for the first time in history, AND the European debt crisis (Greece, Italy, Spain) escalated. Indian markets saw massive FII selling, and ALL stocks dropped together.")
add_bullet("Taper Tantrum (Jun 2013): When Fed Chairman Bernanke hinted that the US would reduce its bond-buying program (QE3), emerging market currencies crashed. The Indian Rupee fell from ₹55 to ₹68 per dollar in weeks, and NIFTY dropped ~10%.")

add_sub("Why is this graph important?")
add_bullet("It proves that 'correlation spikes = market stress.' By monitoring this single metric (mean rolling correlation), a fund manager could have detected every major crisis in this 5-year period.")

add_break()

# ============================================================
# 6. MEAN PAIRWISE CORRELATION OVER TIME
# ============================================================
add_section("6. Mean Pairwise Correlation Over Time (Smoothed)")

add_img(f"{G}graph_14_mean-corr-plot.png", 6.5)
doc.add_paragraph("")

add_sub("What does this graph show?")
add_bullet("The LIGHT BLUE SHADED AREA shows the raw mean correlation at each epoch. The spikiness reflects the 'noise' in short 20-day windows.")
add_bullet("The DARK NAVY LINE is a smoothed version (5-epoch moving average) that filters out noise and reveals the underlying trend.")
add_bullet("VERTICAL GRAY DOTTED LINES mark the start of each calendar year (2009–2013) for easy reference.")

add_sub("Year-by-year interpretation:")
add_bullet("2009: Correlation starts VERY HIGH (~0.5–0.6) because of the GFC aftermath. It gradually drops as markets recover and sectors start diverging.")
add_bullet("2010: Correlation is at its LOWEST and most stable (~0.25–0.35). This was the 'Goldilocks' period – strong recovery, moderate inflation, no major crises. Diversification was most effective here.")
add_bullet("2011: A SHARP SPIKE back up to ~0.5+ during the EU Crisis. The smoothed line clearly shows the market entering a 'stress regime' from mid-2011.")
add_bullet("2012: Correlation eases back to normal levels as the ECB's 'whatever it takes' pledge calmed European fears and Indian markets stabilized.")
add_bullet("2013: A BRIEF SPIKE during the Taper Tantrum (May–Jun), but the market quickly normalized. Overall, 2013 correlation was moderate.")

add_sub("Key Insight:")
add_bullet("The smoothed line reveals a 'W-shaped' pattern: High (2009) → Low (2010) → High (2011) → Low (2012) → Brief spike (2013). Each peak corresponds to a global crisis that temporarily destroyed diversification in Indian markets.")

add_break()

# ============================================================
# 7. CRITICAL STATE IDENTIFICATION (3 PANELS)
# ============================================================
add_section("7. Critical State Identification (3-Panel Analysis)")

add_img(f"{G}graph_15_plot-critical.png", 6.5)
doc.add_paragraph("")

add_sub("Panel 1: Mean Pairwise Correlation with Critical State Zones")
add_bullet("The BLUE LINE is the same mean correlation series from before.")
add_bullet("The ORANGE DASHED LINE is the 'Critical Threshold' set at the 90th percentile of all correlation values. Only the top 10% of epochs breach this line.")
add_bullet("The RED SHADED AREAS are the 'Critical State Zones' – periods where correlation exceeded the 90th percentile threshold.")
add_bullet("These red zones cluster around: early 2009 (GFC), mid-2011 (EU Crisis), and mid-2013 (Taper Tantrum). These are the periods of maximum systemic risk.")
add_bullet("During red zones, ALL stocks move as ONE. An investor holding 49 different stocks would have experienced nearly the same loss as holding just 1 stock. Diversification completely breaks down.")

add_sub("Panel 2: Rate of Change of Mean Correlation (Δ Correlation)")
add_bullet("Each BAR represents the epoch-to-epoch change in mean correlation. Positive bars = correlation is increasing (market synchronizing). Negative bars = correlation is decreasing (market normalizing).")
add_bullet("RED BARS are those exceeding the 90th percentile threshold for rate of change. These represent 'sudden surges' in correlation – the market snapping into crisis mode.")
add_bullet("The ORANGE DASHED LINE is the high-change threshold.")
add_bullet("Key Observation – Asymmetry: The red bars (surges UP) are much taller and sharper than the blue bars (recoveries DOWN). This means: Markets crash FAST (panic spreads instantly) but recover SLOWLY (confidence rebuilds gradually). This is called 'Asymmetric Contagion.'")

add_sub("Panel 3: Market Volatility Over Time")
add_bullet("The PURPLE LINE shows the average volatility (standard deviation of log returns) across all stocks for each epoch.")
add_bullet("The PURPLE SHADED AREA emphasizes the magnitude of volatility.")
add_bullet("Early 2009 has the HIGHEST volatility (daily swings of 3–5% were common). This gradually decreases as the market stabilizes.")
add_bullet("Volatility spikes align perfectly with the correlation spikes in Panel 1. This confirms: High correlation + High volatility = Critical State (maximum systemic risk).")
add_bullet("When volatility is LOW and correlation is LOW (e.g., mid-2010, mid-2012), the market is in its healthiest, most 'normal' state.")

add_break()

# ============================================================
# 8. OVERALL CONCLUSIONS
# ============================================================
add_section("8. Overall Conclusions – What Did We Learn About 2009–2013?")

add_sub("The Big Picture")
add_bullet("The 2009–2013 period was one of the most eventful in Indian stock market history. It began in the depths of the worst financial crisis since 1929 and ended with India as one of the fastest-growing large economies.")
add_bullet("The NIFTY 50 more than doubled from its March 2009 low to its 2013 close, but this recovery was uneven across sectors.")

add_sub("Which stocks performed best?")
add_bullet("IT Sector (TCS, Infosys, HCL Tech): Benefited from Rupee depreciation (cheaper exports) and growing global IT spending. TCS went from ~₹85 to ~₹2000+.")
add_bullet("FMCG (HUL, ITC, Asian Paints): India's consumption story. Rising middle class, rural demand, and pricing power made these 'compounders.'")
add_bullet("Private Banks (HDFC Bank, Kotak Bank): Gained market share from weak public-sector banks. Superior asset quality and digital adoption.")

add_sub("Which stocks struggled?")
add_bullet("Infrastructure/Real Estate (DLF, Reliance Infra, Reliance Power): Over-leveraged balance sheets, regulatory delays, and slowing construction activity. These stocks never recovered their 2008 peaks.")
add_bullet("Public Sector Banks (PNB, SBI): Rising Non-Performing Assets (NPAs) from aggressive lending during 2007–2008 started showing up, hurting profitability.")
add_bullet("Metals (SAIL, Jindal Steel): Global commodity price slump after China's growth slowed from 10%+ to ~7%.")

add_sub("Key Events Worth Noticing")
add_bullet("March 2009: NIFTY hit its crisis low (~2600). This was the single best buying opportunity in a generation.")
add_bullet("November 2010: Coal India IPO – the largest IPO in Indian history at that time.")
add_bullet("August 2011: S&P downgraded US debt; NIFTY fell ~25% in 3 months.")
add_bullet("September 2012: Government announced FDI reforms (retail, aviation, broadcasting), sparking a rally.")
add_bullet("May 2013: Taper Tantrum caused Rupee to crash; RBI raised rates sharply.")

add_sub("The Critical Insight for Finance Students")
add_bullet("During a crisis, the ONLY thing that matters is CORRELATION. When all stocks move together, no amount of diversification can save a portfolio.")
add_bullet("Monitoring the mean rolling correlation is an 'early warning system' for systemic risk. Every major crash in this period was preceded or accompanied by a correlation spike.")
add_bullet("The market operates in two 'regimes': a Normal Regime (low correlation, effective diversification) and a Crisis Regime (high correlation, no diversification). Recognizing which regime the market is in is the most important skill in risk management.")

# Save
out_path = "NIFTY50_Complete_Analysis_with_Graphs.docx"
doc.save(out_path)
print(f"DOCX saved: {out_path}")
