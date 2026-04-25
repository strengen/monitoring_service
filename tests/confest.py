import pytest
from core.database import db, Book, PriceHistory

@pytest.fixture(autouse=True)
def setup_db():
    db.connect()
    db.create_tables([Book, PriceHistory])

    yield

    db.drop_tables([Book, PriceHistory])
    db.close()