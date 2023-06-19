desired_profit = float(input())
total_income = 0

while True:
    cocktail_name = input()
    if cocktail_name == "Party!":
        break

    quantity = int(input())
    cocktail_price = len(cocktail_name)

    order_price = quantity * cocktail_price
    if order_price % 2 != 0:
        order_price -= order_price * 0.25

    total_income += order_price

    if total_income >= desired_profit:
        break

if total_income >= desired_profit:
    print("Target acquired.")
else:
    needed_money = desired_profit - total_income
    print(f"We need {needed_money:.2f} leva more.")

print(f"Club income - {total_income:.2f} leva.")