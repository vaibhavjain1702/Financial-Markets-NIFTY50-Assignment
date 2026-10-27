# Financial Markets Assignment: NIFTY 50 Analysis (2009-2013)

Analysis of NIFTY 50 constituents (July 2011 mid-point snapshot) using Python and yfinance: price trends, log returns, full-period and rolling correlation, and identification of crash/critical epochs from correlation spikes.

## Contents

| File | Description |
|---|---|
| `FinMarkets_NIFTY50_Assignment.ipynb` | Main notebook (data download, cleaning, analysis, plots) |
| `FIN_Assignment_Q3_NIFTY50.txt` | Plain-text export of the Question 3 code |
| `NIFTY50_Analysis_Inferences.md` | Step-by-step interpretation of the results |
| `NIFTY50_Complete_Analysis_with_Graphs.docx` | Written report with embedded graphs |
| `build_docx.py` | Script that assembles the report from the graphs |
| `graphs/` | Generated figures (prices, log returns, correlation, rolling windows, crashes) |

## Running

```bash
pip install yfinance pandas numpy matplotlib seaborn
jupyter notebook FinMarkets_NIFTY50_Assignment.ipynb
```

Data is downloaded live from Yahoo Finance; results may differ slightly if adjusted prices change.
