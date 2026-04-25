import pytest
from peewee import SqliteDatabase
from core.database import db, Book, PriceHistory

MODELS = [Book, PriceHistory]

@pytest.fixture(autouse=True)
def setup_db():
    test_db = SqliteDatabase(":memory:")
    with test_db.bind_ctx(MODELS):
        test_db.create_tables(MODELS)
        yield
        test_db.drop_tables(MODELS)