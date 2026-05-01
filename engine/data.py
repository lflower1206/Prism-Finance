import os

import pandas as pd
import yfinance as yf

CACHE_DIR = "data"
TW_SYMBOL_LENGTH = 4


def normalize_symbol(symbol: str) -> str:
    """Normalize symbol to yfinance format.

    Args:
        symbol: The stock symbol to normalize (e.g., 'AAPL' or '2330').

    Returns:
        The normalized symbol (e.g., 'AAPL' or '2330.TW').
    """
    symbol = symbol.strip().upper()
    # If it's a 4-digit number, assume it's a TW stock and append .TW
    if symbol.isdigit() and len(symbol) == TW_SYMBOL_LENGTH:
        return f"{symbol}.TW"
    return symbol


def get_stock_data(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    """Fetch stock data with local Parquet caching.

    Args:
        symbol: Stock symbol.
        start_date: Start date string (YYYY-MM-DD).
        end_date: End date string (YYYY-MM-DD).

    Returns:
        DataFrame with OHLCV data. Returns empty DataFrame on error.
    """
    norm_symbol = normalize_symbol(symbol)
    cache_path = os.path.join(
        CACHE_DIR, f"{norm_symbol}_{start_date}_{end_date}.parquet"
    )

    if os.path.exists(cache_path):
        return pd.read_parquet(cache_path)

    try:
        df = yf.download(norm_symbol, start=start_date, end=end_date)
        if df.empty:
            return pd.DataFrame()

        # Ensure directory exists
        os.makedirs(CACHE_DIR, exist_ok=True)
        df.to_parquet(cache_path)
        return df  # type: ignore[no-any-return]
    except Exception as e:
        print(f"Error fetching data for {norm_symbol}: {e}")
        return pd.DataFrame()
