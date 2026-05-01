## Context

Prism Finance is currently a blank project (as per the file tree) intended for financial analysis. The goal is to build a "Researcher Tool" that allows interactive exploration of US and TW stock markets. The user has specified a preference for Python, Pandas, Streamlit, and Plotly, with a focus on EOD (End of Day) data and vectorized backtesting.

## Goals / Non-Goals

**Goals:**
- Provide a responsive Streamlit UI for stock data visualization.
- Implement a robust data ingestion layer supporting both US and TW markets.
- Build a vectorized backtesting engine using Pandas for high-speed computation.
- Enable interactive parameter tuning via sidebar sliders.
- Integrate Plotly for professional-grade interactive charts.

**Non-Goals:**
- Real-time data streaming (EOD data is sufficient).
- Complex event-driven backtesting (vectorized is preferred for speed and simplicity).
- Full trade execution/broker integration.
- Advanced machine learning models for prediction.

## Decisions

### 1. Framework: Streamlit
- **Rationale**: Streamlit allows for rapid development of data-centric web applications in pure Python. It handles the UI state and reactivity automatically, which is ideal for a "Researcher Tool."
- **Alternative**: React/FastAPI. While more flexible, it requires significantly more boilerplate and frontend knowledge (TypeScript/CSS), which doesn't align with the rapid prototyping goal.

### 2. Visualization: Plotly
- **Rationale**: Plotly provides out-of-the-box interactive features (zoom, pan, hover) that are essential for analyzing stock charts. It integrates seamlessly with Streamlit.
- **Alternative**: Matplotlib/Seaborn. These produce static images, which would break the "interactive" requirement.

### 3. Backtesting Engine: Vectorized Pandas
- **Rationale**: Vectorized backtesting (applying operations across entire DataFrames) is much faster and simpler to implement than looping through days (event-driven). It is perfect for EOD data and basic technical strategies.
- **Alternative**: Backtrader or Zipline. These are powerful but have steep learning curves and may be overkill for a researcher-focused tool.

### 4. Data Format: Parquet for Caching
- **Rationale**: Storing fetched data in Parquet format provides high compression and extremely fast read/write speeds for Pandas.
- **Alternative**: CSV. CSVs are slower to parse and don't preserve data types (like Datetime) as effectively as Parquet.

## Risks / Trade-offs

- **[Risk] yfinance Flakiness for TW Market** → **Mitigation**: Implement symbol normalization and provide a fallback logic or error message if a symbol isn't found.
- **[Risk] Streamlit "State" Reset on Rerun** → **Mitigation**: Use `st.session_state` to cache data and prevent redundant API calls on every slider move.
- **[Risk] Large Data Volume** → **Mitigation**: Limit default data range to 5-10 years and use efficient column operations.
