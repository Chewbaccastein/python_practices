def main():

    fraction = input("Fraction: ")
    percentage = convert(fraction)

    answer = gauge(percentage)
    print(answer)


def convert(fraction):
        fraction = str(fraction)
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
             raise ZeroDivisionError
        elif x > y:
             raise ValueError
        else:
            percentage = x / y * 100
            percentage = round(percentage)
            return percentage



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        new_percentage = f"{percentage}%"
        return new_percentage



if __name__ == "__main__":
    main()




# while True:
#     try:
#         x, y = input("Fraction: ").split("/")
#         x = int(x)
#         y = int(y)
#         fraction = x / y * 100
#         fraction = round(fraction)
#         if fraction > 100:
#             continue
#         elif fraction >= 90:
#             print("F")
#         elif fraction <= 1:
#             print("E")
#         else:
#             print(f"{fraction}%")
#     except (ValueError, ZeroDivisionError):
#         pass
#     else:
#         break




