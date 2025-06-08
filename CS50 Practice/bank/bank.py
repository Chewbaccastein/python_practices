money_counter = 0

response = input("Greeting: ").strip().lower()

if "hello" in  response:
    money_counter += 0
elif response[0] == "h" and "hello" not in response:
    money_counter += 20
else:
    money_counter += 100

print(f"${money_counter}")


