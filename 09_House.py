n = int(input())

for i in range((n + 1) // 2):
    roof = "-" * ((n - 1 - 2 * i) // 2)
    stars = "*" * (n - 2 * ((n - 1 - 2 * i) // 2))
    print(roof + stars + roof)

for _ in range(n // 2):
    print("|" + "*" * (n - 2) + "|")
