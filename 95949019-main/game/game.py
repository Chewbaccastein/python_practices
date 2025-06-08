import random
import sys

number = 0
while True:
    try:
        number = input("Level: ")
        number = int(number)

        if number < 1:
            continue
        elif type(number) != int:
            continue
        else:
            rand_int = random.randint(1 , number)

        while True:
            try:
                guess = input("Guess: ")
                guess = int(guess)
                if guess == rand_int:
                    print("Just right!")
                    sys.exit()
                elif guess < rand_int:
                    print("Too small!")
                    continue
                elif guess > rand_int:
                    print("Too large!")
                    continue
            except ValueError:
                pass

    except ValueError:
        pass



