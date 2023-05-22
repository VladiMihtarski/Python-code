premiere = 12.00
normal = 7.50
discount = 5.00

projection_type = input()
number_of_row = int(input())
number_of_columns = int(input())

ticket_price = 0.0

if projection_type == "Premiere":
    ticket_price = premiere
elif projection_type == "Normal":
    ticket_price = normal
elif projection_type == "Discount":
    ticket_price = discount

total_seats = number_of_row * number_of_columns
total_revenue = ticket_price * total_seats

print(f"{total_revenue:.2f} leva")
