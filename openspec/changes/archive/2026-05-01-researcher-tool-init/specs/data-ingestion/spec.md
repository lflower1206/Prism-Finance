## ADDED Requirements

### Requirement: Multi-market Data Fetching
The system SHALL support fetching daily OHLCV (Open, High, High, Low, Close, Volume) data for both US and Taiwan (TW) stock markets.

#### Scenario: Fetch US Stock Data
- **WHEN** the user enters a US ticker symbol (e.g., "AAPL")
- **THEN** the system fetches EOD data using the yfinance library

#### Scenario: Fetch TW Stock Data
- **WHEN** the user enters a TW ticker symbol (e.g., "2330")
- **THEN** the system normalizes the symbol (e.g., to "2330.TW") and fetches EOD data

### Requirement: Symbol Normalization
The system SHALL automatically detect and normalize stock symbols to ensure compatibility with data providers.

#### Scenario: Normalize TW Numeric Symbol
- **WHEN** a 4-digit numeric string is provided
- **THEN** the system appends ".TW" before fetching data
