from um import count


def test_one_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um!") == 1


def test_multiple_ums():
    assert count("Um, thanks, um...") == 2
    assert count("um um UM") == 3


def test_inside_words():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0


def test_no_um():
    assert count("hello, world") == 0

