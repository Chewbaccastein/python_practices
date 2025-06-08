import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    um = re.findall(r"\bum\b", s, re.IGNORECASE)
    for _ in um:
        count += 1
    return count







if __name__ == "__main__":
    main()
