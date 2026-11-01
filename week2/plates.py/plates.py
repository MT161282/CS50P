def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    if not s.isalnum():
        return False

    number_found = False

    for character in s:
        if character.isdigit():
            if not number_found:
                if character == "0":
                    return False
                number_found = True
        elif number_found:
            return False

    return True


main()
