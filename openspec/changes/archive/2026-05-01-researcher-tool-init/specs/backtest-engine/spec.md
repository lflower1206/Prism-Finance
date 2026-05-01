## ADDED Requirements

### Requirement: Vectorized Signal Generation
The system SHALL calculate buy and sell signals based on technical indicator crossovers using vectorized Pandas operations.

#### Scenario: MA Crossover Signal
- **WHEN** the Fast MA crosses above the Slow MA
- **THEN** the system marks a "Buy" signal for that date in the results DataFrame

### Requirement: Equity Curve Calculation
The system SHALL compute the cumulative return (equity curve) of the strategy based on generated signals.

#### Scenario: Calculate Total Return
- **WHEN** signals are generated
- **THEN** the system calculates daily strategy returns and displays a cumulative equity chart

### Requirement: Risk Metric Reporting
The system SHALL report key performance metrics including Total Return and Max Drawdown.

#### Scenario: Display Metrics
- **WHEN** a backtest is completed
- **THEN** the system displays the calculated Total Return % and Max Drawdown % in the UI
