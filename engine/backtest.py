from typing import TypedDict

import pandas as pd


class StrategyMetrics(TypedDict):
    """Dictionary containing strategy performance metrics."""

    total_return_pct: float
    max_drawdown_pct: float


def run_crossover_strategy(
    df: pd.DataFrame, fast_period: int, slow_period: int
) -> pd.DataFrame:
    """Run a vectorized MA crossover strategy.

    Args:
        df: DataFrame with at least a 'Close' column.
        fast_period: Window size for the fast moving average.
        slow_period: Window size for the slow moving average.

    Returns:
        DataFrame with strategy columns (MA_Fast, MA_Slow, Signal, Strategy_Return, Equity_Curve).
    """
    results = df.copy()

    # Calculate indicators
    results["MA_Fast"] = results["Close"].rolling(window=fast_period).mean()
    results["MA_Slow"] = results["Close"].rolling(window=slow_period).mean()

    # Generate signals: 1 for Buy, 0 for None
    # We buy when Fast > Slow
    results["Signal"] = 0
    results.loc[results["MA_Fast"] > results["MA_Slow"], "Signal"] = 1

    # Calculate daily returns
    results["Daily_Return"] = results["Close"].pct_change()

    # Strategy returns: we get the return of the NEXT day if we have a signal today
    # Or more simply, if we are 'in' the market (Signal=1), we get the return
    results["Strategy_Return"] = results["Signal"].shift(1) * results["Daily_Return"]

    # Calculate Equity Curve
    results["Equity_Curve"] = (1 + results["Strategy_Return"].fillna(0)).cumprod()

    return results


def calculate_metrics(results: pd.DataFrame) -> StrategyMetrics:
    """Calculate key performance metrics.

    Args:
        results: DataFrame containing an 'Equity_Curve' column.

    Returns:
        A StrategyMetrics dictionary containing 'total_return_pct' and 'max_drawdown_pct'.
    """
    if results.empty or "Equity_Curve" not in results:
        return {"total_return_pct": 0.0, "max_drawdown_pct": 0.0}

    equity: pd.Series[float] = results["Equity_Curve"]

    total_return = (equity.iloc[-1] - 1) * 100

    # Max Drawdown
    running_max = equity.cummax()
    drawdown = (equity - running_max) / running_max
    max_drawdown = drawdown.min() * 100

    return {
        "total_return_pct": round(float(total_return), 2),
        "max_drawdown_pct": round(float(max_drawdown), 2),
    }
