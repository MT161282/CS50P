from seasons import convert


def test_one_day():
    assert convert(1440) == "One thousand, four hundred forty minutes"


def test_one_year():
    assert convert(525600) == (
        "Five hundred twenty-five thousand, six hundred minutes"
    )


def test_two_years():
    assert convert(1051200) == (
        "One million, fifty-one thousand, two hundred minutes"
    )

