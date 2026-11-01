from plates import is_valid


def test_length():
    assert is_valid("CS") is True
    assert is_valid("ABCDEF") is True
    assert is_valid("H") is False
    assert is_valid("OUTATIME") is False


def test_starts_with_two_letters():
    assert is_valid("CS50") is True
    assert is_valid("1A") is False
    assert is_valid("A1") is False


def test_characters():
    assert is_valid("HELLO") is True
    assert is_valid("PI3.14") is False
    assert is_valid("HELLO!") is False
    assert is_valid("AB CD") is False


def test_number_position():
    assert is_valid("AAA222") is True
    assert is_valid("CS50P") is False
    assert is_valid("AAA2B2") is False


def test_first_number():
    assert is_valid("CS50") is True
    assert is_valid("CS05") is False
    assert is_valid("AB0") is False

