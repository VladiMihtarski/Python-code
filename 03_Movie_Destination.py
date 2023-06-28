budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

daily_cost = 0

if season == "Winter":
    if destination == "Dubai":
        daily_cost = 45000
    elif destination == "Sofia":
        daily_cost = 17000
    elif destination == "London":
        daily_cost = 24000
elif season == "Summer":
    if destination == "Dubai":
        daily_cost = 40000
    elif destination == "Sofia":
        daily_cost = 12500
    elif destination == "London":
        daily_cost = 20250

total_cost = daily_cost * number_of_days

if destination == "Dubai":
    total_cost *= 0.7  # 30% отстъпка
elif destination == "Sofia":
    total_cost *= 1.25  # увеличение с 25%

difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
