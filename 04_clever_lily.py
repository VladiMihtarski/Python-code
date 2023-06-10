age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_count = 0
money_saved = 0
even_birthdays_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        even_birthdays_money += 10
        money_saved += even_birthdays_money - 1
    else:
        toys_count += 1

money_from_toys = toys_count * toy_price
money_saved += money_from_toys

if money_saved >= washing_machine_price:
    remaining_money = money_saved - washing_machine_price
    print(f"Yes! {remaining_money:.2f}")
else:
    needed_money = washing_machine_price - money_saved
    print(f"No! {needed_money:.2f}")
