"""To run the test call: python -m pytest --disable-pytest-warnings some_test.py"""
from add import total

def test_total_empty() -> None:
    assert total([]) == 0.0
    
def test_total_single_item() -> None:
    assert total([7.0]) == 7.0

def test_total_many_items() -> None:
    assert total([1,2,3.0]) == 6.0


