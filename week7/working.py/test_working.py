import pytest

from working import convert


def test_am_to_pm():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_mixed_minutes():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 PM to 12:45 AM") == "12:30 to 00:45"


def test_invalid_times():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")


def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM to 5:00 PM")

