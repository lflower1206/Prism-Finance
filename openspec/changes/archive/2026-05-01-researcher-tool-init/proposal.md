## Why

Users need a tool to explore TW and US stock market data interactively and test simple strategies using Python and Pandas. Currently, there is no integrated environment in this project that provides both visualization and vectorized backtesting capabilities for these two markets.

## What Changes

- **Interactive Dashboard**: Implementation of a Streamlit-based web application for stock exploration.
- **Unified Data Loading**: Support for fetching EOD data for both US (via yfinance) and TW (via yfinance/FinMind) markets with symbol normalization.
- **Live Indicator Lab**: Capability to adjust technical indicator parameters (e.g., MA periods) via UI sliders with instant chart updates.
- **Interactive Charting**: Integration of Plotly candlestick charts for detailed price action analysis.
- **Vectorized Backtesting Core**: A Python/Pandas engine to calculate trade signals and equity curves based on user-defined parameters.

## Capabilities

### New Capabilities

- `data-ingestion`: Fetching and normalizing EOD stock data from US and TW sources.
- `interactive-charting`: Visualizing price action and technical indicators using interactive Plotly charts.
- `backtest-engine`: Vectorized calculation of strategy signals, equity curves, and performance metrics (Sharpe, Drawdown).
- `researcher-ui`: Streamlit-based interface for parameter adjustment and dashboard layout.

### Modified Capabilities

(None)

## Impact

- **New Dependencies**: `streamlit`, `pandas`, `plotly`, `yfinance`.
- **Project Structure**: Addition of `engine/`, `components/`, and `data/` directories to organize the application logic and cache.
- **Workflow**: Provides a new entry point (`main.py`) for the interactive researcher tool.
