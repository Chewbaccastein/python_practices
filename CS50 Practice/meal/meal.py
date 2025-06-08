def main():
    meal_time = input("What time is it? ").strip().lower()
    hungry = convert(meal_time)
    if 7 <= hungry <= 8:
        print("breakfast time")
    elif 12 <= hungry <= 13:
        print("lunch time")
    elif 18 <= hungry <= 19:
        print("dinner time")
    else:
        return None



def convert(time):
    if time.endswith("p.m."):
        counter = 12
    else:
        counter = 0

    hour, minute = time.rstrip('amAMpmPM.').split(":")
    hour = int(hour)
    minute = int(minute)
    hour_24 = hour + counter
    minute_to_hour = minute / 60
    total_hour = hour_24 + minute_to_hour
    total_hour = float(total_hour)
    return total_hour





if __name__ == "__main__":
    main()
