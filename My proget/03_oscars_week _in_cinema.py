movie_name = input()
hall_type = input()
number_tickets = int(input())

ticket_prices = {
    "A Star Is Born": [7.5, 10.5, 13.5],
    "Bohemian Rhapsody": [7.35, 9.45, 12.75],
    "Green Book": [8.15, 10.25, 13.25],
    "The Favourite": [8.75, 11.55, 13.95]
}

price_index = {"normal": 0, "luxury": 1, "ultra luxury": 2}
ticket_price = ticket_prices[movie_name][price_index[hall_type]]

revenue = ticket_price * number_tickets

print(f"{movie_name} -> {revenue:.2f} lv.")

# movie_name = input()
# theater_type = input()
# num_tickets = int(input())
#
# ticket_prices = {
#     "A Star Is Born": [7.5, 10.5, 13.5],
#     "Bohemian Rhapsody": [7.35, 9.45, 12.75],
#     "Green Book": [8.15, 10.25, 13.25],
#     "The Favourite": [8.75, 11.55, 13.95]
# }
#
# price_index = {"normal": 0, "luxury": 1, "ultra luxury": 2}
# ticket_price = ticket_prices[movie_name][price_index[theater_type]]
#
# revenue = round(ticket_price * num_tickets, 2)
#
# print(f"{movie_name} -> {revenue} lv.")