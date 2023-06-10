month = input()
nights = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if nights > 14:
        studio_price *= 0.7  # 30% discount for more than 14 nights
        apartment_price *= 0.9  # 10% discount for more than 14 nights
    elif nights > 7:
        studio_price *= 0.95  # 5% discount for more than 7 nights
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price *= 0.8  # 20% discount for more than 14 nights
        apartment_price *= 0.9  # 10% discount for more than 14 nights
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if nights > 14:
        apartment_price *= 0.9  # 10% discount for more than 14 nights

studio_total_price = studio_price * nights
apartment_total_price = apartment_price * nights

print(f"Apartment: {apartment_total_price:.2f} lv.")
print(f"Studio: {studio_total_price:.2f} lv.")
