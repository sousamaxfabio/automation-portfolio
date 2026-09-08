\# Day 25 — Project 3 Part 1: CSV → Validation → OpenAI API Classification



\## What it does

\- Reads `input.csv`

\- Validates required fields (`name`, `description`)

\- Sends each row to OpenAI `gpt-4o-mini` for classification

\- Parses JSON response `{category, confidence}`

\- Saves `results.csv` with category + status



\## Flow

input.csv → validate → OpenAI API → JSON → results.csv



\## Setup

```bash

pip install openai python-dotenv

OPENAI\_API\_KEY=sk-proj-...

OPENAI\_MODEL=gpt-4o-mini

