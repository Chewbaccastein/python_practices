
due = 50

while due > 0:
    coin_received = input("Insert Coin: ")
    coin_received = int(coin_received)
    if coin_received == 5 or coin_received == 25 or coin_received == 10:
        due -= coin_received
    if due < 1:
        print(f"Change Owed: {abs(due)}")
    else:
        print(f"Amount Due: {due}")


