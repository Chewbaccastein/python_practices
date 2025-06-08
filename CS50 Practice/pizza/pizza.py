import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1].strip().lower()
if not file_name.endswith(".csv"):
    sys.exit("Not a CSV file")

rows = []
table = []
headers = []

try:
    with open(file_name) as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
        headers = rows[0]
        table = rows[1:]
        print(tabulate(table, headers, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
