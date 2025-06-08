import sys
import os
from PIL import Image, ImageOps

valid_extension = (".jpg", ".jpeg", ".png")

input = sys.argv[1]
output = sys.argv[2]

_, extension1 = os.path.splitext(input)
_, extension2 = os.path.splitext(output)


try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not input.lower().endswith(valid_extension):
        sys.exit("Invalid input")
    elif not output.lower().endswith(valid_extension):
        sys.exit("Invalid output")
    elif extension1 != extension2:
        sys.exit("Input and ouput have different extensions")
    # _, extension1 = sys.argv[1].rsplit(".", 1)
    # _, extension2 = sys.argv[2].rsplit(".", 1)
    # if extension1.lower() != extension2.lower():
    #     sys.exit("Input and output have different extensions")

    shirt = Image.open("shirt.png")


    with Image.open(input) as muppet:
    # size = shirt.size
    # print(size) # output = (600,600)
    # muppet_size = muppet.size
    # print(muppet_size) # output = (1200, 1600)
        muppet = ImageOps.fit(muppet, (600, 600))
        muppet.paste(shirt, shirt)
        muppet.save(output)



except FileNotFoundError:
    sys.exit("File does not exit")


