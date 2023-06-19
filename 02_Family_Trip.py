budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
additional_costs_percent = int(input())

if number_of_nights > 7:
    price_per_night -= price_per_night * 0.05

total_expenses = number_of_nights * price_per_night
additional_expenses = budget * (additional_costs_percent / 100)

if budget >= total_expenses + additional_expenses:
    left_money = budget - (total_expenses + additional_expenses)
    print (f"Ivanovi will be left with {left_money:.2f} leva after vacation.")
else:
    needed_money = (total_expenses + additional_expenses) - budget
    print(f"{needed_money:.2f} leva needed.")