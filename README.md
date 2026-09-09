# 🤖 Automation Portfolio — Fabio Sousa

> Documenting my journey to become an Automation Engineer — Week by Week

![GitHub last commit](https://img.shields.io/github/last-commit/sousamaxfabio/automation-portfolio)
![GitHub repo size](https://img.shields.io/github/repo-size/sousamaxfabio/automation-portfolio)

## 📌 About Me
I am building real automation systems with Python, n8n, and Make. This repo is my public lab.

**Current Focus:** n8n Automations + API Integrations
**Location:** Canary Islands, Spain
**Goal:** Junior Automation Engineer role

## 🗂️ Portfolio Structure
- `projects/` — Full case studies
- `python-automations/` — Python scripts
- `n8n-workflows/` — n8n JSON exports
- `docs/` — Notes and learning docs

## ✅ Progress Tracker

- Days 1–4: Git, GitHub, and repository foundations
- Day 5: API fundamentals
- Day 6: Python mini integration
- Day 9: n8n data mapping and live weather API
- Day 10: n8n data and expressions
- Day 11: Webhooks and input validation
- Day 12: Scheduling, Google Sheets, Gmail, Slack, OpenAI, and Airtable
- Day 13: Human approval with Gmail and conditional routing
- Day 14: AI service request classifier
- Day 15: Make fundamentals
- Day 17: AI invoice processing, validation, approval, and Airtable
- Day 18: Invoice processing audit logs and failure handling
- Day 19: Invoice production hardening, notifications, and validation testing
- Day 20: Publish Project 2 — Invoice Processing final docs and sample invoices

## 🚀 Recent n8n Projects

- [Day 19 — Invoice Processing Production Improvements](day-19-production-improvements/README.md)
- [Day 18 — Invoice Processing, Part 2](day-18-invoice-processing-part-2/README.md)
- [Day 17 — Invoice Processing, Part 1](day-17-invoice-processing-part-1/README.md)
- [Day 14 — AI Service Request Classifier](day-14-ai-service-request-classifier/README.md)
- [Day 13 — Human Approval](day-13-human-approval/README.md)
- [Day 12 — Scheduled Weather Check](day-12-scheduled-weather-check/README.md)
- [Day 12 — Essential Integrations](day-12-essential-integrations/README.md)
- [Day 11 — Webhook Practice](day-11-webhook-practice/README.md)
- [Day 10 — Data and Expressions](day-10-data-and-expressions/README.md)
- [Day 9 — Live Weather Check](day-9-live-weather-check/README.md)

## 🛠️ Tech Stack
- **Languages:** Python, Markdown
- **Tools:** Git, GitHub, VS Code, Docker
- **Platforms:** n8n, Google Cloud, Gmail, Google Sheets, Slack, OpenAI, Airtable

## 📫 How to Reach Me
- GitHub: [@sousamaxfabio](https://github.com/sousamaxfabio)
- LinkedIn: (add your link here)

### Project 3 — Part 2 (Day 26) — Production Refactor
- Refactored Day 25 prototype into 6 functions
- Added `validate_row()` → filtered 2 invalid rows (id=11 missing name, id=12 missing description)
- Added retry logic (3x) + structured logging to `app.log`
- Result: `results.csv` → 16 classified with category + confidence
- Tech: `openai`, `python-dotenv`, logging