import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(filename) as file:
        number_of_lines = 0

        for line in file:
            if line.strip() and not line.lstrip().startswith("#"):
                number_of_lines += 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(number_of_lines)
