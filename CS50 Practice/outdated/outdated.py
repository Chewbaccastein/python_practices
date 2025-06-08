months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]




while True:
    try:
        date = input("Date: ").title().strip()

        date_seperator = [0, 0, 0]

        if "/" in date:
            date_seperator = date.split("/")
            if date_seperator[0].isalpha():
                continue
        elif "/" not in date and "," not in date:
            continue
        elif "," in date: # if May 1, 2020 ->
            first_split = [word.strip() for word in date.split(",")]  # may 1, 2020
            second_split = list(first_split[0].split(" ")) # may, 1
            second_split.append(first_split[1])  # may, 1, 2020
            date_seperator = second_split
        mm, dd, yyyy = date_seperator
        if date_seperator[0] in months:
            mm = months.index(mm) + 1

        mm = int(mm)
        if mm > 12:
            continue

        dd = int(dd)
        if dd > 31:
            continue

        new_format = (f"{yyyy}-{mm:02}-{dd:02}")
        print(new_format)
        break

    except ValueError:
        pass




# def main():
#     while True:
#         try:
#             date = input("Date: ").title().strip()
#             iso_format = date_converter(date)
#         except ValueError:
#             pass
#         else:
#             break

#     iso_format = str(iso_format)
#     print(iso_format)



# def date_converter(date):
#     mm, dd, yyyy = [0, 0, 0]
#     date_seperator = [0, 0, 0]
#     if "/" in date:
#         date_seperator = date.split("/")
#     elif "," in date: # if May 1, 2020 ->
#         first_split = [word.strip() for word in date.split(",")]  # may 1, 2020
#         second_split = list(first_split[0].split(" ")) # may, 1
#         date_seperator = second_split.append(first_split[1])  # may, 1, 2020


#     # if 0 > mm > 12:
#     #     continue
#     # elif 0 > dd > 31:
#     #     continue
#     if date_seperator[0] in months:
#         mm = months.index(mm) + 1
#     mm = int(mm)
#     dd = date_seperator[1]
#     dd = int(dd)
#     yyyy = date_seperator[2]
#     new_format = (f"{yyyy}-{mm:02}-{dd:02}")
#     return new_format




# if __name__== "__main__":
#     main()

