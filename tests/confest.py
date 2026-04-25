import pytest
from core.database import db_proxy
from peewee import SqliteDatabase

@pytest.fixture(autouse=True)
def setup_db():
    db = SqliteDatabase(':memory:')
    db.connect()
    db.create_tables(['Book', 'PriceHistory'])
    yield
    db.drop_tables(db.get_tables())
    db.close()