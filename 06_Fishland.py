mackerel_price_kg = float(input())
sprinkle_price_kg = float(input())
bonito_kg = float(input())
saffron_kg = float(input())
mussels_kg = float(input())

bonito_price = mackerel_price_kg + mackerel_price_kg * 0.60
saffron_price = sprinkle_price_kg + sprinkle_price_kg * 0.80
mussels_price = mussels_kg * 7.50

total_price = (bonito_price * bonito_kg) + (saffron_price * saffron_kg) + mussels_price

print(f"{total_price:.2f}")
