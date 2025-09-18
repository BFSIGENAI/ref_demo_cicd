from src import add, greet
from src.core.math_operations import subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_greet():
    assert greet("Malay") == 2
