import re
# import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    iframe = re.search(r"iframe", s, re.IGNORECASE)
    if not iframe:
        return None

    address = re.search(r"src=\"https?:\/\/(www\.)?youtube\.com\/embed\/(\w+)", s, re.IGNORECASE)
    if address:
        address_id = address.group(2)
        abr_address = "https://youtu.be/" + address_id
        return abr_address
    else:
        return None





if __name__ == "__main__":
    main()
