# Capability: researcher-ui

## Purpose
Streamlit-based user interface for adjusting parameters and viewing the dashboard.

## Requirements

### Requirement: Sidebar Parameter Controls
The system SHALL provide a sidebar containing input fields and sliders for strategy parameters.

#### Scenario: Adjust MA Period
- **WHEN** the user moves the "MA Period" slider
- **THEN** the Streamlit application triggers a rerun and updates the charts with the new parameter

### Requirement: Dashboard Layout
The system SHALL organize the interface into distinct sections for controls, price charts, and performance metrics.

#### Scenario: View Dashboard
- **WHEN** the application is launched
- **THEN** the user sees a sidebar for inputs and a main area for the interactive charts and metrics
