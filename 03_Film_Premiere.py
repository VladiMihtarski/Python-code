projection = input()
movie_pack = input()
number_of_tickets = int(input())

if projection == "John Wick":
    if movie_pack == "Drink":
        total_price = number_of_tickets * 12
    elif movie_pack == "Popcorn":
        total_price = number_of_tickets * 15
    elif movie_pack == "Menu":
        total_price = number_of_tickets * 19
elif projection == "Star Wars":
    if movie_pack == "Drink":
        total_price = number_of_tickets * 18
    elif movie_pack == "Popcorn":
        total_price = number_of_tickets * 25
    elif movie_pack == "Menu":
        total_price = number_of_tickets * 30
elif projection == "Jumanji":
    if movie_pack == "Drink":
        total_price = number_of_tickets * 9
    elif movie_pack == "Popcorn":
        total_price = number_of_tickets * 11
    elif movie_pack == "Menu":
        total_price = number_of_tickets * 14

if projection == "Star Wars" and number_of_tickets >= 4:
    total_price *= 0.7
elif projection == "Jumanji" and number_of_tickets == 2:
    total_price *= 0.85

formatted_price = "{:.2f}".format(total_price) # print(f"Your bill is {total_price:.2f} leva.")
print(f"Your bill is {formatted_price} leva.")

