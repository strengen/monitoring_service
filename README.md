# Book Price Monitoring Service

A Python service that tracks book prices from [books.toscrape.com](https://books.toscrape.com), stores historical data, and provides both a CLI and a web interface for analysis.

## Tech Stack

- **Python**: core language
- **BeautifulSoup4 + requests**: web scraping
- **Peewee**: SQLite ORM
- **Flask**: web interface
- **Matplotlib**: price charts
- **Docker**: containerization  

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
