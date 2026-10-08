import pytest
from src.book import Book
from src.library import Library


@pytest.fixture
def bibliotheque():
    return Library()


@pytest.fixture
def petit_prince():
    return Book("Le Petit Prince", "Antoine de Saint-Exupery", "9782070612758")