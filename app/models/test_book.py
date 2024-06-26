import pytest
from app.models.book import Book

def test_book_to_dict():
    book = Book(id=1, title="Test Book", description="This is a test book")
    expected_dict = {
        'id': 1,
        'title': 'Test Book',
        'description': 'This is a test book'
    }
    assert book.to_dict() == expected_dict

def test_book_from_dict():
    data = {
        'title': 'Test Book',
        'description': 'This is a test book'
    }
    book = Book.from_dict(data)
    assert book.title == 'Test Book'
    assert book.description == 'This is a test book'

def test_book_from_dict_missing_fields():
    data = {
        'title': 'Test Book'
    }
    with pytest.raises(ValueError):
        Book.from_dict(data)
        def test_book_from_dict_missing_description():
            data = {
                'title': 'Test Book'
            }
            with pytest.raises(ValueError):
                Book.from_dict(data)

        def test_book_from_dict_missing_title():
            data = {
                'description': 'This is a test book'
            }
            with pytest.raises(ValueError):
                Book.from_dict(data)