from datetime import datetime
import os
from peewee import(
    CharField, 
    FloatField,
    Model,
    SqliteDatabase, 
    ForeignKeyField,
    DateTimeField,
    fn
)


db = SqliteDatabase('./data/books.db')
os.makedirs("./data", exist_ok=True)
DATE_FORMAT = '%d-%m-%Y %H:%M:%S'

class BaseModel(Model):
    class Meta:
        database = db

class Book(BaseModel):
    title = CharField(unique=True)
    price = FloatField()
    last_updated = DateTimeField(default=lambda: datetime.now().strftime(DATE_FORMAT))

class PriceHistory(BaseModel):
    book = ForeignKeyField(Book, backref='history', on_delete='CASCADE')
    price = FloatField()
    created_at = DateTimeField(default=lambda: datetime.now().strftime(DATE_FORMAT))

def get_book(item: str) -> Book:
    try:
        return Book.get(fn.LOWER(Book.title) == item.lower())
    except Book.DoesNotExist:
        return
    
def create_instances():
    db.create_tables([Book, PriceHistory])