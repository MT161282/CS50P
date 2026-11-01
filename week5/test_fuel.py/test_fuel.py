import pytest

from fuel import convert, gauge


def test_convert():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("2/3") == 67
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_convert_returns_integer():
    assert type(convert("1/2")) is int


def test_value_error():
    with pytest.raises(ValueError):
        convert("cat")

    with pytest.raises(ValueError):
        convert("1.5/3")

    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ValueError):
        convert("-1/4")

    with pytest.raises(ValueError):
        convert("1/-4")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

