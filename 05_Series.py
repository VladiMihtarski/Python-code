budget = float(input())
num_series = int(input())

total_cost = 0

for _ in range(num_series):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        series_price -= series_price * 0.50

    elif series_name == "Lucifer":
        series_price -= series_price * 0.40

    elif series_name == "Protector":
        series_price -= series_price * 0.30

    elif series_name == "TotalDrama":
        series_price -= series_price * 0.20

    elif series_name == "Area":
        series_price -= series_price * 0.10

    total_cost += series_price

if budget >= total_cost:
    remaining_money = budget - total_cost
    print(f"You bought all the series and left with {remaining_money:.2f} lv.")
else:
    needed_money = total_cost - budget
    print(f"You need {needed_money:.2f} lv. more to buy the series!")
