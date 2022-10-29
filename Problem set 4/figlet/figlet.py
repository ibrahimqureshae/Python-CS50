import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
font_list = figlet.getFonts()


# Zero or 2 command-line arguments expected
if len(sys.argv) == 1:
        random_font = random.choice(font_list)
        figlet.setFont(font=random_font)
        sentence = input("input: ").strip()
        print(figlet.renderText(sentence))
        sys.exit()

# Prompt user for a str


# if Zero arguments - Random font is displayed

if len(sys.argv) == 3 and sys.argv[1] in ["-f" , "--f"] and sys.argv[2] in font_list:
        figlet.setFont(font=sys.argv[2])
        sentence = input("input: ").strip()
        print(figlet.renderText(sentence))
else:
        sys.exit("arguments Invalid")

# Output the font
