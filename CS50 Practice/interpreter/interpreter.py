(x, y, z) = input("Expression: ").split()
answer = 0
x = int(x)
z = int(z)
if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*":
    answer = x * z
elif y == "/":
    answer = x / z




print(float(answer))
