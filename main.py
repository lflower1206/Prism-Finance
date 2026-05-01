from datetime import datetime, timedelta

import pandas as pd
import streamlit as st

from components.charts import plot_stock_and_strategy
from engine.backtest import calculate_metrics, run_crossover_strategy
from engine.data import get_stock_data, normalize_symbol

# Constants
DATE_RANGE_LEN = 2

# Page Config
st.set_page_config(page_title="Prism Finance Researcher", layout="wide")

st.title("📊 Prism Finance: Strategy Researcher")

# --- Sidebar Controls ---
st.sidebar.header("Strategy Parameters")

symbol = st.sidebar.text_input("Stock Symbol (e.g., AAPL, 2330)", value="AAPL")
date_range = st.sidebar.date_input(
    "Date Range", value=[datetime.now() - timedelta(days=365 * 2), datetime.now()]
)

st.sidebar.markdown("---")
st.sidebar.subheader("MA Crossover Settings")
fast_ma = st.sidebar.slider("Fast MA Period", min_value=5, max_value=50, value=20)
slow_ma = st.sidebar.slider("Slow MA Period", min_value=10, max_value=200, value=50)

# --- Data Loading ---
if isinstance(date_range, list) and len(date_range) == DATE_RANGE_LEN:
    start_date, end_date = date_range
    if start_date >= end_date:
        st.error("Error: Start date must be before end_date.")
    else:
        with st.spinner(f"Loading data for {symbol}..."):
            try:
                df = get_stock_data(
                    symbol,
                    start_date.strftime("%Y-%m-%d"),
                    end_date.strftime("%Y-%m-%d"),
                )
            except Exception as e:
                st.error(f"Critical error fetching data: {e}")
                df = pd.DataFrame()

        if not df.empty:
            # --- Run Backtest ---
            try:
                results = run_crossover_strategy(df, fast_ma, slow_ma)
                metrics = calculate_metrics(results)

                # --- Display Metrics ---
                col1, col2 = st.columns(2)
                col1.metric("Total Return (%)", f"{metrics['total_return_pct']}%")
                col2.metric("Max Drawdown (%)", f"{metrics['max_drawdown_pct']}%")

                # --- Display Charts ---
                fig = plot_stock_and_strategy(results, normalize_symbol(symbol))
                st.plotly_chart(fig, use_container_width=True)

                # --- Data Table ---
                with st.expander("View Raw Data"):
                    st.dataframe(results.tail(100))
            except Exception as e:
                st.error(f"Error during backtest calculation: {e}")
        else:
            error_msg = (
                f"No data found for symbol: '{symbol}'. "
                "Please check the symbol (e.g., 'AAPL' or '2330') and ensure "
                "the date range is valid."
            )
            st.error(error_msg)
else:
    st.warning("Please select a valid date range (Start and End date).")
