text = input("Input: ")

print("Output: ", end="")

for character in text:
    if character.lower() not in ["a", "e", "i", "o", "u"]:
        print(character, end="")

print()
