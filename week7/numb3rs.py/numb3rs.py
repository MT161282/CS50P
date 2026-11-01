import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = (
        r"(0|[1-9][0-9]{0,2})\."
        r"(0|[1-9][0-9]{0,2})\."
        r"(0|[1-9][0-9]{0,2})\."
        r"(0|[1-9][0-9]{0,2})"
    )

    matches = re.fullmatch(pattern, ip)

    if not matches:
        return False

    for number in matches.groups():
        if int(number) > 255:
            return False

    return True


if __name__ == "__main__":
    main()
