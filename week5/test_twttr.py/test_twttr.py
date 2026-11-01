
from twttr import shorten


def test_lowercase_vowels():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_uppercase_vowels():
    assert shorten("AEIOU") == ""
    assert shorten("PYTHON") == "PYTHN"


def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("12345") == "12345"


def test_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("!?.,") == "!?.,"
