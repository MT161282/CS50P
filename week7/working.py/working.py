import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = (
        r"([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to "
        r"([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)"
    )

    matches = re.fullmatch(pattern, s)

    if not matches:
        raise ValueError

    start_hour = to_24_hour(int(matches.group(1)), matches.group(3))
    start_minute = matches.group(2) or "00"

    end_hour = to_24_hour(int(matches.group(4)), matches.group(6))
    end_minute = matches.group(5) or "00"

    return f"{start_hour:02}:{start_minute} to {end_hour:02}:{end_minute}"


def to_24_hour(hour, period):
    if period == "AM":
        if hour == 12:
            return 0
        return hour

    if hour == 12:
        return 12

    return hour + 12


if __name__ == "__main__":
    main()
