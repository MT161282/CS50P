import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = (
        r'<iframe[^>]*\ssrc="'
        r'https?://(?:www\.)?youtube\.com/embed/([^"]+)"'
    )

    matches = re.search(pattern, s)

    if matches:
        return f"https://youtu.be/{matches.group(1)}"

    return None


if __name__ == "__main__":
    main()
