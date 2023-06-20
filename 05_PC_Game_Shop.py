games_sold = int(input())

hearthstone_sales = 0
fortnite_sales = 0
overwatch_sales = 0
others_sales = 0

for _ in range(games_sold):
    game_name = input()

    if game_name == "Hearthstone":
        hearthstone_sales += 1
    elif game_name == "Fornite":
        fortnite_sales += 1
    elif game_name == "Overwatch":
        overwatch_sales += 1
    else:
        others_sales += 1

total_sales = hearthstone_sales + fortnite_sales + overwatch_sales + others_sales

hearthstone_percentage = (hearthstone_sales / total_sales) * 100
fortnite_percentage = (fortnite_sales / total_sales) * 100
overwatch_percentage = (overwatch_sales / total_sales) * 100
others_percentage = (others_sales / total_sales) * 100

print(f"Hearthstone - {hearthstone_percentage:.2f}%")
print(f"Fornite - {fortnite_percentage:.2f}%")
print(f"Overwatch - {overwatch_percentage:.2f}%")
print(f"Others - {others_percentage:.2f}%")
