import pandas as pd


def calculate_sma(df: pd.DataFrame, period: int) -> pd.Series[float]:
    """Calculate Simple Moving Average.

    Args:
        df: DataFrame containing a 'Close' column.
        period: Number of periods for the rolling average.

    Returns:
        A Series containing the calculated SMA.
    """
    return df["Close"].rolling(window=period).mean()


def calculate_ema(df: pd.DataFrame, period: int) -> pd.Series[float]:
    """Calculate Exponential Moving Average.

    Args:
        df: DataFrame containing a 'Close' column.
        period: Number of periods for the EWM.

    Returns:
        A Series containing the calculated EMA.
    """
    return df["Close"].ewm(span=period, adjust=False).mean()
