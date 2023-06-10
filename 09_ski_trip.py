days = int(input())
room_type = input()
rating = input()

price_per_night = 0
discount = 0

if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

total_price = (days - 1) * price_per_night  # Изчисляваме цената без намаления за пълен престой

if days < 10:
    if room_type == "apartment":
        discount = total_price * 0.3
    elif room_type == "president apartment":
        discount = total_price * 0.1
elif 10 <= days <= 15:
    if room_type == "apartment":
        discount = total_price * 0.35
    elif room_type == "president apartment":
        discount = total_price * 0.15
elif days > 15:
    if room_type == "apartment":
        discount = total_price * 0.5
    elif room_type == "president apartment":
        discount = total_price * 0.2

total_price -= discount

if rating == "positive":
    total_price += total_price * 0.25
elif rating == "negative":
    total_price -= total_price * 0.1

print(f"{total_price:.2f}")
