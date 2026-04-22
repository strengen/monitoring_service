from core import (
    add_one_element,
    get_book,
    update_data,
    delete_element
)

def test_add_one_element():
    add_one_element("TestBook", 10.0)

    book = get_book("TestBook")
    assert book is not None
    assert book.price == 10.0


def test_update_data():
    update_data(["BookA"], [20.0])

    book = get_book("BookA")
    assert book is not None
    assert book.price == 20.0


def test_delete_element():
    add_one_element("ToDelete", 5.0)
    delete_element("ToDelete")

    assert get_book("ToDelete") is None