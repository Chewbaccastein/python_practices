


while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        fraction = x / y * 100
        fraction = round(fraction)
        if fraction > 100:
            continue
        elif fraction >= 90:
            print("F")
        elif fraction <= 1:
            print("E")
        else:
            print(f"{fraction}%")
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break




