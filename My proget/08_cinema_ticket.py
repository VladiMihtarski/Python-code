# day_of_week = input()
#
# if day_of_week == 'Monday' or day_of_week == 'Tuesday':
#     ticket_price = 12
# elif day_of_week == 'Wednesday' or day_of_week == 'Thursday':
#     ticket_price = 14
# elif day_of_week == 'Friday':
#     ticket_price = 12
# elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
#     ticket_price = 16
# else:
#     print("Invalid input")
#     exit()
#
# print(f"The ticket price for {day_of_week} is {ticket_price}")
day_of_week = input()

ticket_prices = {
    'Monday': 12,
    'Tuesday': 12,
    'Wednesday': 14,
    'Thursday': 14,
    'Friday': 12,
    'Saturday': 16,
    'Sunday': 16
}

if day_of_week in ticket_prices:
    print(f"{ticket_prices[day_of_week]}")
else:
    print("Invalid input")

