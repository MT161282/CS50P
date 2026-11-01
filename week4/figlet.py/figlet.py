import random
import sys

from pyfiglet import Figlet


fonts = Figlet().getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)
elif (
    len(sys.argv) == 3
    and sys.argv[1] in ["-f", "--font"]
    and sys.argv[2] in fonts
):
    font = sys.argv[2]
else:
    sys.exit("Invalid usage")

figlet = Figlet(font=font)

text = input("Input: ")

print("Output:")
print(figlet.renderText(text))

