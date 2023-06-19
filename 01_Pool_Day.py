from math import ceil

number_of_people = int(input())
entrance_fee = float(input())
price_one_per_sun_lounger = float(input())
one_umbrella_price = float(input())

money_needed = (number_of_people * entrance_fee)\
               + (ceil(number_of_people * 0.75) * price_one_per_sun_lounger)\
               + (ceil(number_of_people * 0.50) * one_umbrella_price)

print(f"{money_needed:.2f} lv.")