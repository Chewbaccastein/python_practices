

def main():
    grocerylist = []
    grocerylist = list_of_grocery()
    total_items = len(grocerylist)
    sorted_list = []
    count = 0
    for _ in range(total_items):
        count = grocerylist.count(grocerylist[_])
        sorted_list.append(f"{count} {grocerylist[_]}")
        count = 0
    sorted_list = set(sorted_list)
    for item in sorted_list:
        print(item)







def list_of_grocery():
    to_buy = []
    while True:
        try:
            grocery = input("").upper()
            to_buy.append(grocery)
        except (ValueError, EOFError):
            break
    return to_buy




main()
