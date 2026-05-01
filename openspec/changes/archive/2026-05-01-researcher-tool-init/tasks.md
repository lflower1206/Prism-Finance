## 1. Project Scaffolding & Dependencies

- [x] 1.1 Create directory structure: `engine/`, `components/`, `data/`
- [x] 1.2 Initialize `pyproject.toml` with dependencies: `streamlit`, `pandas`, `plotly`, `yfinance`, `pyarrow` (for Parquet)

## 2. Data Ingestion Layer

- [x] 2.1 Implement `engine/data.py` with symbol normalization (e.g., numeric to `.TW`)
- [x] 2.2 Implement yfinance wrapper to fetch daily OHLCV data
- [x] 2.3 Implement local Parquet caching logic to speed up repeated fetches

## 3. Backtesting Engine

- [x] 3.1 Implement `engine/strategy.py` with vectorized indicator calculations (e.g., SMA, EMA)
- [x] 3.2 Implement `engine/backtest.py` for signal generation (crossovers) and return calculation
- [x] 3.3 Implement risk metric functions (Total Return, Max Drawdown)

## 4. UI Development (Streamlit)

- [x] 4.1 Create `main.py` entry point with basic Streamlit page config
- [x] 4.2 Implement sidebar controls for symbol input, date range, and strategy parameters
- [x] 4.3 Create `components/charts.py` for Plotly candlestick and equity curve rendering
- [x] 4.4 Integrate UI with engine to create the full "Researcher" loop

## 5. Verification & Polishing

- [x] 5.1 Verify US stock data (e.g., AAPL) displays and backtests correctly
- [x] 5.2 Verify TW stock data (e.g., 2330) displays and backtests correctly
- [x] 5.3 Add error handling for invalid symbols or connection issues
