# money_movie = float(input())
# extras_number = int(input())
# clothing_price = float(input())
#
# set_cost = money_movie * 0.1
# if extras_number > 150:
#     clothing_cost = extras_number * clothing_price * 0.9
# else:
#     clothing_cost = extras_number * clothing_price
#
# total_cost = set_cost + clothing_cost
#
# if total_cost > money_movie:
#     money_short = total_cost - money_movie
#     print("Not enough money!")
#     print(f"Wingard needs {money_short:.2f} leva more.")
# else:
#     remaining_money = money_movie - total_cost
#     print("Action!")
#     print(f"Wingard starts filming with {remaining_money:.2f} leva left.")

money_movie = float(input())
extras_number = int(input())
clothing_price = float(input())

set_cost = money_movie * 0.1
clothing_cost = extras_number * clothing_price * 0.9 if extras_number > 150 else extras_number * clothing_price
total_cost = set_cost + clothing_cost

if total_cost > money_movie:
    money_short = total_cost - money_movie
    print("Not enough money!")
    print(f"Wingard needs {money_short:.2f} leva more.")
else:
    remaining_money = money_movie - total_cost
    print("Action!")
    print(f"Wingard starts filming with {remaining_money:.2f} leva left.")