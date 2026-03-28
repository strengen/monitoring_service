# Book Price Monitoring Service

A Python service that tracks book prices from [books.toscrape.com](https://books.toscrape.com), stores historical data, and provides both a CLI and a web interface for analysis.

## Features

- Scrapes all 1000 books across 50 pages
- Tracks price changes over time
- CLI for manual control
- Flask web interface with price history and analytics charts
- Automated price updates via systemd timer

## Tech Stack

- **Python** — core language
- **BeautifulSoup4 + requests** — web scraping
- **Peewee** — SQLite ORM
- **Flask** — web interface
- **Matplotlib** — price charts

## Installation

```bash
git clone <repo-url>
cd monitoring_service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Web interface
```bash
python main.py
```


### CLI
```bash
python main.py update              # Scrape and update all prices
python main.py history "Book Title" # Show price history
python main.py analytics "Book Title" # Show analytics
```

### Automated updates (systemd)
```bash
sudo systemctl enable --now monitoring.timer   # Enable
sudo systemctl disable --now monitoring.timer  # Disable
```

## Project Structure

```
monitoring_service/
├── main.py            # Entry point
├── parser.py          # Web scraper
├── database.py        # DB models (Peewee + SQLite)
├── services.py        # Business logic
├── cli.py             # CLI interface
├── flask_app.py       # Web interface
├── update_prices.py   # Script for systemd timer
└── templates/         # HTML templates
```
