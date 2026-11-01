from bank import value


def test_hello():
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, Newman") == 0


def test_starts_with_h():
    assert value("Hi") == 20
    assert value("Hey") == 20
    assert value("How are you?") == 20


def test_other_greetings():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("Welcome") == 100
