# Capability: interactive-charting

## Purpose
Interactive visualization of price data and technical indicators.

## Requirements

### Requirement: Interactive Candlestick Visualization
The system SHALL render an interactive candlestick chart displaying the fetched price data.

#### Scenario: Render Candlesticks
- **WHEN** price data is successfully loaded
- **THEN** the system displays a Plotly candlestick chart with zoom and pan capabilities

### Requirement: Dynamic Technical Indicators
The system SHALL allow users to overlay technical indicators (e.g., Moving Averages) on the price chart.

#### Scenario: Overlay Moving Average
- **WHEN** the user enables a Moving Average in the UI
- **THEN** the system calculates the MA using Pandas and plots it as a line on the candlestick chart
