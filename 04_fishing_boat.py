budget = int(input())
season = input()
fishermen_count = int(input())

spring_price = 3000
summer_autumn_price = 4200
winter_price = 2600

if season == "Spring":
    boat_rental_price = spring_price
elif season == "Summer" or season == "Autumn":
    boat_rental_price = summer_autumn_price
else:
    boat_rental_price = winter_price

if fishermen_count <= 6:
    boat_rental_price *= 0.9
elif 7 <= fishermen_count <= 11:
    boat_rental_price *= 0.85
else:
    boat_rental_price *= 0.75

if fishermen_count % 2 == 0 and season != "Autumn":
    boat_rental_price *= 0.95

if budget >= boat_rental_price:
    money_left = budget - boat_rental_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = boat_rental_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")