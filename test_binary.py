import pytest
from main import binary_search


def test_binary_search():
    assert binary_search([1, 2, 62, 87, 92, 9, 22], 1) == True, "Binary search function Failed"
    assert binary_search([2, 4, 78, 65, 89, 99], 1) == False, "Binary search function failed"
