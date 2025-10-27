import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
])
def test_positive_add(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 2, 3.0),
    (10, 5, 2.0),
    (-8, 2, -4.0),
    (5, 2, 2.5),
])
def test_positive_divide(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected

def test_negative_zero(calculator):
    with pytest.raises(ValueError, match="дырка от бублика"):
        calculator.divide(10, 0)

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (25, False),
    (0, False),
    (1, False),
])
def test_positive_prime_number(calculator, n, expected):
    assert calculator.is_prime_number(n) == expected

def test_negative_prime_number(calculator):
    with pytest.raises(TypeError, match="нужно число целое"):
        calculator.is_prime_number(3.5)