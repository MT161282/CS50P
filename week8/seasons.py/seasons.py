import sys
from datetime import date

import inflect


def main():
    birthdate = input("Date of Birth: ")

    try:
        birthday = date.fromisoformat(birthdate)
    except ValueError:
        sys.exit("Invalid date")

    if birthday.isoformat() != birthdate:
        sys.exit("Invalid date")

    difference = date.today() - birthday
    minutes = difference.days * 24 * 60

    print(convert(minutes))


def convert(minutes):
    engine = inflect.engine()
    words = engine.number_to_words(minutes, andword="")

    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
