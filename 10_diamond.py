n = int(input())

leftRight = (n - 1) // 2

# Горна част на диаманта
for row in range(leftRight + 1):
    dashes = leftRight - row
    stars = n - 2 * dashes - 2

    if stars >= 0:
        line = '-' * dashes + '*' + '-' * stars + '*' + '-' * dashes
    else:
        line = '-' * dashes + '*' + '-' * dashes

    print(line)

# Долната част на диаманта
for row in range(leftRight, 0, -1):
    dashes = leftRight - row + 1
    stars = n - 2 * dashes - 2

    if stars >= 0:
        line = '-' * dashes + '*' + '-' * stars + '*' + '-' * dashes
    else:
        line = '-' * dashes + '*' + '-' * dashes

    print(line)
