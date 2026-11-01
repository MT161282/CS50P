import csv
import sys

from tabulate import tabulate


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.lower().endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(filename) as file:
        reader = csv.reader(file)
        table = list(reader)

except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(table, headers="firstrow", tablefmt="grid"))

