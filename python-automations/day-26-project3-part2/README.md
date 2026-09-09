# AI CSV Classification Pipeline

A Python automation project that reads structured CSV data, validates required fields, classifies products using the OpenAI API, and writes the processed results to a new CSV file.

## What It Does

- Reads product data from `input.csv`
- Validates required fields before processing
- Sends valid records to the OpenAI API
- Classifies each product into a defined category
- Returns a confidence score
- Retries failed API requests up to 3 times
- Logs execution details to `app.log`
- Writes final results to `results.csv`

## Reliability Features

- Input validation
- Retry handling
- Exception handling
- Structured logging
- Environment variables for API credentials

## Tech Stack

- Python
- OpenAI API
- CSV
- `python-dotenv`
- Python logging

## Project Files

- `main.py` — main automation pipeline
- `input.csv` — sample input data
- `results.csv` — processed output
- `requirements.txt` — Python dependencies
- `.env.example` — example environment configuration
- `screenshots/` — execution and output evidence

## Example Result

The pipeline processes valid product records and returns:

- product category
- confidence score
- processing status

Invalid rows are skipped and logged instead of stopping the full workflow.

## Skills Demonstrated

- Python automation
- API integration
- Data validation
- Error handling
- Retry logic
- Logging
- Structured data processing
# AI CSV Classification Pipeline

A Python automation project that reads structured CSV data, validates required fields, classifies products using the OpenAI API, and writes the processed results to a new CSV file.

## What It Does

- Reads product data from `input.csv`
- Validates required fields before processing
- Sends valid records to the OpenAI API
- Classifies each product into a defined category
- Returns a confidence score
- Retries failed API requests up to 3 times
- Logs execution details to `app.log`
- Writes final results to `results.csv`

## Reliability Features

- Input validation
- Retry handling
- Exception handling
- Structured logging
- Environment variables for API credentials

## Tech Stack

- Python
- OpenAI API
- CSV
- `python-dotenv`
- Python logging

## Project Files

- `main.py` — main automation pipeline
- `input.csv` — sample input data
- `results.csv` — processed output
- `requirements.txt` — Python dependencies
- `.env.example` — example environment configuration
- `screenshots/` — execution and output evidence

## Example Result

The pipeline processes valid product records and returns:

- product category
- confidence score
- processing status

Invalid rows are skipped and logged instead of stopping the full workflow.

## Skills Demonstrated

- Python automation
- API integration
- Data validation
- Error handling
- Retry logic
- Logging
- Structured data processing