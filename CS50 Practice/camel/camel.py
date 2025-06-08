ask_name = input("camelCase: ")
snake_name = ""
for letter in ask_name:
    if letter.isupper():
        snake_name += "_"
    snake_name += letter.lower()
print(snake_name)


