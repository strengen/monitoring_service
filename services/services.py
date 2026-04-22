from parser import get_items
from database import Book, PriceHistory, get_book, DATE_FORMAT
from typing import List
from datetime import datetime, time
from peewee import fn
import logging
import matplotlib.pyplot as plt
import random
import time 

logger = logging.getLogger(__name__)

def update_data(items: List[str] | None = None, 
                  prices: List[float] | None = None) -> None:
    """ Save all parsed data to the database """
    logging.info('Saving data to the database...')
    if items is None or prices is None:
        items, prices = get_items()
    for item, price in zip(items, prices):
        book, created = Book.get_or_create(title=item, defaults={'price': price})
        book.last_updated = datetime.now().strftime(DATE_FORMAT)
        if not created and book.price != price:
            PriceHistory.create(book=book, price=price)
            book.price = price
        book.save()
    logging.info('Data saved successfully.')
    
def add_one_element(item: str, price: float) -> None:
    """ Save one particular element to the database """
    logger.info(f'Saving \"{item}\" to the database...')
    Book.get_or_create(title=item, defaults={'price': price})
    logger.info(f'\"{item}\" saved successfully.')

def get_price_history(item: str) -> None:
    """ Get price history of a particular book """
    logger.info(f'Getting price history for \"{item}\"...')
    book = get_book(item)
    if not book:
        raise AttributeError(f'No such book in the database')
    print(book.title + ':')
    for price_h in book.history.order_by(PriceHistory.created_at):
        print(f'\t{price_h.price}$ — {price_h.created_at}')
    logger.info(f'Price history for \"{item}\" retrieved successfully.')

def get_analytics(item: str) -> None:
    """ Get analytics of a particular book """
    logger.info(f'Getting analytics for \"{item}\"...')
    book = get_book(item)
    if not book:
        raise AttributeError('No such book in the database')
    result = (PriceHistory
        .select(fn.Min(PriceHistory.price), fn.Max(PriceHistory.price), fn.Avg(PriceHistory.price))
        .where(PriceHistory.book == book).tuples().get())
    min_price, max_price, avg_price = result
    print(f'Min price of \"{book.title}\" - {min_price}$')
    print(f'Max price of \"{book.title}\" - {max_price}$')
    print(f'Average price of \"{book.title}\" - {avg_price}$')
    print(f'Current price of \"{book.title}\" - {book.price}$')
    logger.info(f'Analytics for \"{item}\" retrieved successfully.')

def delete_element(item: str) -> None:
    """ Delete book from the database """
    logger.info(f'Deleting \"{item}\" from the database')
    book = get_book(item)
    if not book:
        raise AttributeError('No such book in the database')
    book.delete_instance(recursive=True)
    logger.info(f'\"{item}\" successfully deleted from the database')


def work_state() -> None:
    """ This function is for testing purposes. It simulates the work of the service, 
    updating prices in the database every hour. """
    while True:
        time.sleep(3600)
        update_data()


# Testing function to randomly change prices.
# def change_price() -> None:
#     books = [book for book in Book.select()]
#     for book in books:
#         new_price = round(random.uniform(10, 50), 2)
#         if book.price != new_price:
#             PriceHistory.create(book=book, price=new_price)
#             book.price = new_price
#             book.last_updated = datetime.now().strftime(DATE_FORMAT)
#             book.save()
