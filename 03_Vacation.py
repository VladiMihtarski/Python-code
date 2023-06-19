money_needed = float(input())
available_money = float(input())
days = 0
spend_days = 0
can_save = True

while available_money < money_needed and spend_days < 5 and can_save:
    action = input()
    amount = float(input())

    if action == "spend":
        if amount > available_money:
            amount = available_money
            available_money = 0
        else:
            available_money -= amount
        spend_days += 1
    elif action == "save":
        available_money += amount
        spend_days = 0

    days += 1

