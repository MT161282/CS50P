from numb3rs import validate


def test_valid_addresses():
    assert validate("0.0.0.0") is True
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True


def test_out_of_range():
    assert validate("256.0.0.1") is False
    assert validate("1.256.3.4") is False
    assert validate("1.2.256.4") is False
    assert validate("1.2.3.256") is False


def test_invalid_formats():
    assert validate("1.2.3") is False
    assert validate("1.2.3.4.5") is False
    assert validate("cat") is False


def test_leading_zeros():
    assert validate("192.168.001.1") is False
    assert validate("01.2.3.4") is False
