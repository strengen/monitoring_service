# Monitoring Service

Backend service for tracking and analyzing price changes of books from https://books.toscrape.com.

The system collects data over time, stores historical records, and allows analysis of price dynamics.

---

## Features

- Web scraping of product data (price tracking)
- Historical data storage in database
- REST API for accessing collected data
- Data analysis and visualization
- Containerized deployment with Docker
- Automated testing and CI pipeline (GitHub Actions)

---

## Tech Stack

- Python
- Flask
- SQL (SQLite / PostgreSQL)
- Docker & Docker Compose
- BeautifulSoup (web scraping)
- GitHub Actions (CI/CD)
- Pytest (testing)

---

## Architecture Overview

The system consists of:

- Scraper module — collects data from target website
- Database layer — stores historical price data
- API layer — provides access to stored information
- Analysis module — processes and visualizes trends

---

## Usage

```bash
git clone <repo>
cd <repo>
```
Run locally:
```bash
pip install -r requirements.txt
python main.py
```

Run with Docker:

```bash
docker compose up --build
```
