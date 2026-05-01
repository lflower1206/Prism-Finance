import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_stock_and_strategy(df: pd.DataFrame, symbol: str) -> go.Figure:
    """Create a subplot with Candlestick chart and Equity Curve.

    Args:
        df: DataFrame containing OHLC data and strategy results.
        symbol: The stock symbol for the title.

    Returns:
        A Plotly Figure object.
    """
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        subplot_titles=(f"{symbol} Price & Indicators", "Strategy Equity Curve"),
        row_heights=[0.7, 0.3],
    )

    # 1. Candlestick Chart
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="OHLC",
        ),
        row=1,
        col=1,
    )

    # Add Moving Averages if they exist
    if "MA_Fast" in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["MA_Fast"],
                name="MA Fast",
                line=dict(color="orange", width=1.5),
            ),
            row=1,
            col=1,
        )
    if "MA_Slow" in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["MA_Slow"],
                name="MA Slow",
                line=dict(color="blue", width=1.5),
            ),
            row=1,
            col=1,
        )

    # 2. Equity Curve
    if "Equity_Curve" in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["Equity_Curve"],
                name="Equity Curve",
                line=dict(color="green"),
            ),
            row=2,
            col=1,
        )

    fig.update_layout(
        height=800,
        template="plotly_dark",
        showlegend=True,
        xaxis_rangeslider_visible=False,
    )

    return fig
