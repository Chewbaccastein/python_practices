import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]
students = []


try:
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            last, first = row["name"].split(",")
            first = first.strip()
            last = last.strip()
            students.append({"first": first, "last": last, "house":row["house"].strip()})


except FileNotFoundError:
    sys.exit(f"Could not read {filename}")


# for student in students:  # test if reader is working
#     print(f"{student['name']} is from {student['house']}")

# for name in names:
#     name = str(name)
#     last, first = name.split(",")
#     last = last.strip()
#     first = first.strip()

new_file = sys.argv[2]

with open(new_file, "w", newline="") as csvfile2:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow(student)



    # for row in students:
    #     for name in names:
    #         name = str(name)
    #         last, first = name.split(",")
    #         last = last.strip()
    #         first = first.strip()
    #     writer.writerow({'first': first, 'last':last, 'house':row["house"]})










