from math_series import __version__
from math_series.math_series import fibonacci, lucas, sum_series

def test_version():
    assert __version__ == '0.1.0'

# Fibonacci tests
def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


# Lucas tests
def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected


#Sum Series

## sum_series fib implicit tests
def test_sum_series_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_series_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_series_five():
    actual = sum_series(5)
    expected = 5
    assert actual == expected

## sum_series fib explicit tests
def test_sum_series_zero_zero_one():
    actual = sum_series(0, 0, 1)
    expected = 0
    assert actual == expected

def test_sum_series_one_zero_one():
    actual = sum_series(1, 0, 1)
    expected = 1
    assert actual == expected

def test_sum_series_two_zero_one():
    actual = sum_series(2, 0, 1)
    expected = 1
    assert actual == expected

def test_sum_series_five_zero_one():
    actual = sum_series(5, 0, 1)
    expected = 5
    assert actual == expected

# sum_series lucas explicit tests
def test_sum_series_zero_two_one():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

def test_sum_series_one_two_one():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected

def test_sum_series_two_two_one():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

def test_sum_series_five_two_one():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected

# Other starter nums
def test_sum_series_zero_three():
    actual = sum_series(0, 3)
    expected = 3
    assert actual == expected

def test_sum_series_one_three_two():
    actual = sum_series(1, 3, 2)
    expected = 2
    assert actual == expected

def test_sum_series_three_three_two():
    actual = sum_series(3, 3, 2)
    expected = 7
    assert actual == expected