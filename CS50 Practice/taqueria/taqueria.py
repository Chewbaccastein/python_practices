import sys

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

total = 0
while True:
    try:
       order = input("Item: ").title()
       if order in menu:
           total += menu[order]
           print(f"Total: ${total:.2f}")
    except (ValueError, EOFError):   # I couldn't figure out EOF error. I found this solution in Reddit. Please let me know if there is more elegant way
        sys.exit()





# order = input("Item: ").title()

# if order in menu:
#     total += menu[order]




# total = 0


# def main():
#     while True:
#         total_order = total()
#         print(f"Total: ${total_order:.2f}")



# def total():
#     total_order = 0
#     while True:
#         try:
#             order = input("Item: ").title()
#             if order in menu:
#                 total_order += menu[order]
#                 return total_order
#         except ValueError:
#             pass

# if __name__ == "__main__":
#     main()


