import re


def main():

            print(convert(input("Hours: ")))



def convert(s):
    # while True:
        # # try:
        #     s = input("Hours: ")
            hours = re.match(r"^([0-1]?[0-9])(:([0-5]?[0-9]))? (AM|PM) to ([0-1]?[0-9])(:([0-5]?[0-9]))? (AM|PM)", s)
            if not hours:
                raise ValueError
            start_hour = int(hours.group(1))
            start_minute = hours.group(3)
            start_ampm = hours.group(4)
            end_hour = int(hours.group(5))
            end_minute = hours.group(7)
            end_ampm = hours.group(8)

            if start_ampm == "PM":
                start_hour += 12
                if start_hour > 24:
                    raise ValueError
                elif start_hour == 24:
                        start_hour = 12
            elif start_ampm == "AM" and start_hour == 12:
                    start_hour = 00

            if start_minute == None:
                start_minute = "00"
            elif int(start_minute) > 60:
                    raise ValueError

            start_time = f"{start_hour:02}:{start_minute:02}"

            if end_ampm == "PM":
                end_hour += 12
                if end_hour > 24:
                    raise ValueError
                elif end_hour == 24:
                        end_hour = 12
            elif end_ampm == "AM" and end_hour == 12:
                    end_hour = 00

            if end_minute == None:
                end_minute = "00"
            elif int(end_minute) > 60:
                    raise ValueError

            end_time = f"{end_hour:02}:{end_minute:02}"

            working = f"{start_time:} to {end_time:}"

            return working

        # except ValueError:
        #     break

if __name__ == "__main__":
    main()

