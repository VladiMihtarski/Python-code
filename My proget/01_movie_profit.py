# You have been hired by "SoftUni Studios" to write a program that calculates the potential profit from
# the sale of movie tickets. The film runs for a predetermined number of days, with a certain number of tickets sold each day.
# The price of 1 ticket is determined by the studio. For broadcast production, a certain percentage of the total revenue remains for the cinema.
# Login
# 5 lines are read from the console:
# 1. Movie name - text
# 2. Number of days - an integer in the range [1… 90]
# 3. Number of tickets - an integer in the range [100… 100000]
# 4. Ticket price - real number in the range [5.0… 25.0]
# 5. Percentage for cinema - an integer in the range [5... 35]
# Exit
# To print the sales revenue on the console, in the following format:
# • "The profit from the movie {movie name} is {studio income} lv."
# The price of the revenue to be formatted to the second digit after the decimal point.

movie_name = input()
number_days = int(input())
number_tickets = int(input())
ticket_price = float(input())
percentage_cinema = int(input())

total_price_tickets = number_tickets * ticket_price
all_period = number_days * total_price_tickets
procent = all_period * percentage_cinema / 100
income_money = all_period - procent

print(f'The profit from the movie {movie_name} is {income_money:.2f} lv.')