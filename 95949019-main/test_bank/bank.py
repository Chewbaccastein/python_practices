def main():
    greeting = input("Greeting: ").strip().lower()
    money_counter = value(greeting)
    print(f"${money_counter}")



def value(greeting):
    money_counter = 0
    greeting = str(greeting)
    if greeting == "hello" or greeting == "Hello":
        money_counter += 0
        return money_counter
    elif greeting[0] == "h" or greeting[0] == "H":
        money_counter += 20
        return money_counter
    else:
        money_counter += 100
        return money_counter



if __name__ == "__main__":
    main()








# money_counter = 0

# response = input("Greeting: ").strip().lower()

# if "hello" in  response:
#     money_counter += 0
# elif response[0] == "h" and "hello" not in response:
#     money_counter += 20
# else:
#     money_counter += 100

# print(f"${money_counter}")


