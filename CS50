import inflect
p = inflect.engine()


def main():
    list_name = get_names()
    # p.join(list_name)
    print(f"Adieu, adieu, to {p.join(list_name)}")

def get_names():
    names = []
    while True:
        try:
            name = input("Name: ")
            names += [name]

        except (ValueError, EOFError):
            return names



if __name__ == "__main__":
    main()
