special_numbers = int(input())

for number in range(1111, 10000):
    is_special = True
    temp = number

    while temp > 0:
        digit = temp % 10

        if digit == 0 or special_numbers % digit != 0:
            is_special = False
            break

        temp = temp // 10

    if is_special:
        print(number, end=" ")
