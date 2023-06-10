total_amount = 0
is_finished = False

while not is_finished:
    command = input()

    if command == "NoMoreMoney":
        is_finished = True
    else:
        amount = float(command)

        if amount < 0:
            print("Invalid operation!")
            is_finished = True
        else:
            total_amount += amount
            print("Increase: {:.2f}".format(amount))

print("Total: {:.2f}".format(total_amount))