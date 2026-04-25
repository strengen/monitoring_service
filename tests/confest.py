import pytest
from peewee import SqliteDatabase
import os

@pytest.fixture(autouse=True)
def setup_db():
    os.makedirs('./data', exist_ok=True)

    from core.database import Book, PriceHistory, db
    db.create_tables([Book, PriceHistory])
    
    yield
    
    db.drop_tables(db.get_tables())
    db.close()