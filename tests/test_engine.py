import pandas as pd

from engine.backtest import calculate_metrics, run_crossover_strategy
from engine.data import normalize_symbol
from engine.strategy import calculate_ema, calculate_sma


def test_normalize_symbol() -> None:
    """Test symbol normalization logic."""
    assert normalize_symbol("aapl") == "AAPL"
    assert normalize_symbol("2330") == "2330.TW"
    assert normalize_symbol("  msft  ") == "MSFT"


def test_calculate_sma() -> None:
    """Test SMA calculation."""
    data = pd.DataFrame({"Close": [10.0, 20.0, 30.0, 40.0, 50.0]})
    sma = calculate_sma(data, 3)
    expected_sma_2 = 20.0
    expected_sma_4 = 40.0
    assert pd.isna(sma[0])
    assert pd.isna(sma[1])
    assert sma[2] == expected_sma_2
    assert sma[4] == expected_sma_4


def test_calculate_ema() -> None:
    """Test EMA calculation."""
    data = pd.DataFrame({"Close": [10.0, 20.0, 30.0, 40.0, 50.0]})
    ema = calculate_ema(data, 3)
    expected_ema_0 = 10.0
    expected_ema_1 = 15.0
    assert ema[0] == expected_ema_0
    # EMA formula: (Close - PrevEMA) * (2 / (N+1)) + PrevEMA
    # EMA[1] = (20 - 10) * (2/4) + 10 = 15.0
    assert ema[1] == expected_ema_1


def test_run_crossover_strategy() -> None:
    """Test strategy signal generation."""
    # Create data where Fast crosses Slow
    # Fast (2), Slow (4)
    data = pd.DataFrame({"Close": [10, 11, 12, 13, 14, 15, 14, 13, 12, 11]})
    results = run_crossover_strategy(data, 2, 4)

    assert "MA_Fast" in results.columns
    assert "MA_Slow" in results.columns
    assert "Signal" in results.columns
    assert "Equity_Curve" in results.columns


def test_calculate_metrics() -> None:
    """Test metrics calculation."""
    results = pd.DataFrame({"Equity_Curve": [1.0, 1.1, 1.05, 1.2, 0.9]})
    metrics = calculate_metrics(results)

    expected_total_return = -10.0
    expected_max_drawdown = -25.0

    # Total Return: (0.9 - 1.0) / 1.0 = -10%
    assert metrics["total_return_pct"] == expected_total_return

    # Max Drawdown:
    # Maxes: 1.0, 1.1, 1.1, 1.2, 1.2
    # DDs: 0, 0, (1.05-1.1)/1.1 = -4.5%, 0, (0.9-1.2)/1.2 = -25%
    assert metrics["max_drawdown_pct"] == expected_max_drawdown


def test_calculate_metrics_empty() -> None:
    """Test metrics with empty data."""
    metrics = calculate_metrics(pd.DataFrame())
    assert metrics["total_return_pct"] == 0.0
    assert metrics["max_drawdown_pct"] == 0.0
