from bs4 import BeautifulSoup
from typing import Tuple, List
import requests
import re

session = requests.Session()
def get_items() -> Tuple[List[str], List[str]]:
    """ Get prices and books. This function parses all 50 pages of the website, 
    be prepared for a slightly big latency."""
    books = []
    prices = []
    for page in range(1,51):
        html_doc = session.get(f'https://books.toscrape.com/catalogue/page-{page}.html').text
        soup = BeautifulSoup(html_doc, 'lxml')
        books.extend([book.a['title'] for book in soup.find_all('h3')])
        prices.extend([float(re.findall(r'\d+\.\d+', elem.string)[0]) for elem in soup.find_all('p', class_='price_color')])
    return books, prices
