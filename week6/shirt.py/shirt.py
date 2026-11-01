import sys

from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

input_extension = input_file.lower().split(".")[-1]
output_extension = output_file.lower().split(".")[-1]

valid_extensions = ["jpg", "jpeg", "png"]

if input_extension not in valid_extensions:
    sys.exit("Invalid input")

if output_extension not in valid_extensions:
    sys.exit("Invalid output")

if input_extension != output_extension:
    sys.exit("Input and output have different extensions")

try:
    image = Image.open(input_file)
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")

image = ImageOps.fit(image, shirt.size)
image.paste(shirt, (0, 0), shirt)
image.save(output_file)

image.close()
shirt.close()

