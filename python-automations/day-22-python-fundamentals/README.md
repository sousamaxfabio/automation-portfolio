# Day 22 - Python Fundamentals: Invoice Processing

> Rebuilding my n8n invoice validation workflow in pure Python.

This project is part of my 30-day Automation Portfolio challenge. Goal: translate no-code automation logic (n8n) into Python fundamentals.

## 📋 Overview

A Python script that simulates the core logic of an automated invoice processing pipeline:
- Parses invoice filenames
- Calculates VAT
- Validates documents against business rules
- Simulates Airtable storage and retry logic
- Encapsulates logic into reusable functions (like n8n nodes)

## 🧠 What I Learned

### 1. Variables
Invoice metadata as variables - `invoice_file`, `vendor_name`, `amount`.

### 2. Strings & Numbers
```python
invoice_number = invoice_file.replace("valid-invoice-", "").replace(".pdf", "")
total = amount * 1.21 # 21% VAT