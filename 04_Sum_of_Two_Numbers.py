start = int(input())
end = int(input())
magic_number = int(input())

combinations = 0
found_combination = False

for x1 in range(start, end + 1):
    for x2 in range(start, end + 1):
        combinations += 1
        if x1 + x2 == magic_number:
            print(f"Combination N:{combinations} ({x1} + {x2} = {magic_number})")
            found_combination = True
            break

    if found_combination:
        break

if not found_combination:
    print(f"{combinations} combinations - neither equals {magic_number}")
