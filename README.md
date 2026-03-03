# Sentiment_API

A Python API for sentiment analysis using FastAPI and Hugging Face Inference API.
It supports batch analysis of comments, classifies them as POSITIVE, NEUTRAL, or NEGATIVE, generates statistics, and stores results in a SQLite database.

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

## 🟢 Try the API Online

The Sentiment API is deployed and publicly accessible! You can test it directly in your browser or via HTTP requests:

🔗 **Live Demo:** [https://sentiment-analysis-7wj5.onrender.com/](https://sentiment-analysis-7wj5.onrender.com/)

No login or setup is required. Just send your comments and see the sentiment analysis results instantly.

Notes

The API no longer requires local Transformers models, reducing memory usage.
Supports multilingual sentiment analysis via Hugging Face Inference API.
SQLite database stores all analyzed comments, enabling history and analytics.
