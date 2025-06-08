import random


def main():
    level = get_level()


    counter = 0
    wrong = 0
    score = 0

    while counter < 10:
        try:
            x = generate_integer(level)
            y = generate_integer(level)
            answer = input(f"{x} + {y} = ")
            answer = int(answer)
            while answer != x +y:
                print("EEE")
                wrong += 1
                if wrong == 3:
                    counter+= 1
                    wrong = 0
                    print(f"{x} + {y} = {x + y}")
                    break
                else:
                    answer = input(f"{x} + {y} = ")
                    answer = int(answer)
                    continue



            # if answer != x + y:
            #     print("EEE")
            #     wrong += 1

            #     if wrong == 3:
            #         counter += 1
            #         wrong = 0
            #         print(f"{x} + {y} = {x + y}")
            #         continue

            if answer == x + y:
                counter += 1
                score += 1
                wrong = 0

        except ValueError:
            pass

    print(score)




def get_level():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if level not in [1, 2, 3]:
                continue
            else:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    else:
        n = random.randint(100, 999)

    return n


if __name__ == "__main__":
    main()


