width = int(input())
length = int(input())

cake_size = width * length  # общият размер на тортата в квадратни сантиметри
has_cake = True  # флаг, който показва дали има останали парчета

while has_cake:
    command = input()
    if command == "STOP":
        break
    else:
        pieces_taken = int(command)
        cake_size -= pieces_taken
        if cake_size <= 0:
            has_cake = False

if has_cake:
    print(f"{cake_size} pieces are left.")
else:
    print(f"No more cake left! You need {-cake_size} pieces more.")
