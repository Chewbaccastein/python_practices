import sys

try:
    file = open("invalid_extension.txt", "a")
    invalid_extension = sys.argv[1].strip().lower().split(".")
    file.write(invalid_extension[1])
    file.close()
except IndexError:
    sys.exit("Too few command-line arguments")


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].lower().strip() == "invalid_extension.txt":
    sys.exit("Not a python file")


with open(sys.argv[1], "r") as file:
    try:
        lines = file.readlines()
        counter = 0
        for line in lines:
            line = line.strip()
            if line.startswith("#"):
                counter += 0
            elif line.strip() == "":
                counter += 0
            else:
                counter += 1
        print(counter)
    except FileNotFoundError:
        sys.exit("File not found")


