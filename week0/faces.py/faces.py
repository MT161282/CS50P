def main():
    text = input()
    print(convert(text))


def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


main()
