# Day 10 — n8n Data and Expressions

Practice using expressions, pinned test data, workflow exports, and execution history.

## Workflow

Manual Trigger → Get Live Weather → Extract Temperature → Check Warm Threshold → Warm or Cool Message

The workflow requests weather data from Open-Meteo for Las Palmas and compares the temperature against a threshold of 25°C.

## Expressions

- `{{ $json.current.temperature_2m }}` reads the temperature from the API response.
- `{{ $json.temperature }}` reads the simplified field used by later nodes.
- Message expressions combine fixed text with the incoming temperature.

## Testing completed

- Pinned the temperature output to `30`.
- Confirmed that `30` followed the True branch for temperature ≥ 25.
- Removed pinned data and restored live API data.
- Exported the workflow and imported a practice copy.
- Executed the imported workflow successfully.
- Inspected a saved execution showing 23.2°C.

Pinned data is used for manual testing. Execution history preserves the data recorded during each saved run.

## How to run

1. Import `day-10-data-and-expressions.json` into a blank n8n workflow.
2. Ensure no test data is pinned.
3. Click **Execute workflow**.
4. Inspect the message on the branch that ran.

The exported workflow retains its original Day 9 name because it was reused for this lesson. It requires internet access but no API key.