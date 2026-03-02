# Sentiment_API

A **Python API** for sentiment analysis using **FastAPI** and **Hugging Face Transformers**.  
It allows batch analysis of comments, classifies them as **POSITIVE**, **NEUTRAL**, or **NEGATIVE**, generates statistics, and stores results in a **SQLite database**.

---

## Features

- Batch comment analysis
- Sentiment classification: **POSITIVE / NEUTRAL / NEGATIVE**
- Summary statistics
- Data persistence with **SQLite**
- Professional modular structure with FastAPI:
  - `main.py`
  - `database.py`
  - `models.py`
  - `schemas.py`
  - `services.py`
  - `sentiment_routes.py`
- Public endpoints (no login required)



----------

## 📜 History & Search

The API includes a **History endpoint** (`/history`) that allows users to retrieve all previously analyzed comments. 
This endpoint is useful for tracking past analyses, generating reports, or building dashboards.

### Features

- Retrieve **all analyzed comments**
- Filter by **sentiment**: POSITIVE, NEUTRAL, NEGATIVE
- Filter by **date range**: e.g., last 7 days or specific period
- Pagination support with `limit` and `offset` parameters

---

## Installation

1. Clone the repository:

git clone https://github.com/enishi2/Sentiment_API.git
cd Sentiment_API
