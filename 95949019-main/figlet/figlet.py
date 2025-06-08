import sys
import random
from pyfiglet import Figlet



# def main():
#     get_font()
#     user_input = input("Input: ")
#     print(user_input)



# def get_font():
#     if len(sys.argv) == 1:
#         figlet = Figlet()
#         f = figlet.getFonts(random)
#         return f



figlet = Figlet()

if len(sys.argv) == 1:
    user = input("Input: ")
    rand_font = random.choice(figlet.getFonts())
    figlet.setFont(font=rand_font)
    print(figlet.renderText(user))

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    elif sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    else:
        user = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(user))
else:
    sys.exit("Invalid usage")


