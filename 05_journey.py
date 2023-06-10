budget = float(input())
season = input()

destination = ""
accommodation = ""
expenses = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        expenses = budget * 0.3
    elif season == "winter":
        accommodation = "Hotel"
        expenses = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        expenses = budget * 0.4
    elif season == "winter":
        accommodation = "Hotel"
        expenses = budget * 0.8
else:
    destination = "Europe"
    accommodation = "Hotel"
    expenses = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{accommodation} - {expenses:.2f}")