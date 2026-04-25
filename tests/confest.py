import pytest
from core.database import db, create_tables
from peewee import SqliteDatabase

db = SqliteDatabase(None)
@pytest.fixture(autouse=True)
def setup_db():
    db.init(':memory:')
    db.connect()
    create_tables()
    yield
    db.drop_tables(db.get_tables())
    db.close()