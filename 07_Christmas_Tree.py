n = int(input("Въведете число: "))

print((n) * " " + " | ")
for i in range(n):
    print(" " * (n - i - 1) + "*" * (i + 1) + " | ", end="")
    print("*" * (i + 1))



