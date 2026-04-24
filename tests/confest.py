import pytest
from core.database import db, create_tables

@pytest.fixture(autouse=True)
def setup_db():
    db.connect()
    create_tables()
    yield
    db.drop_tables(db.get_tables())
    db.close()