# time_of_day = int(input())
# day_of_week = input()
#
# if time_of_day >= 10 and time_of_day <= 18:
#     if day_of_week == 'Monday':
#         print("Open")
#     elif day_of_week == 'Tuesday':
#         print("Open")
#     elif day_of_week == 'Wednesday':
#         print("Open")
#     elif day_of_week == 'Thursday':
#         print("Open")
#     elif day_of_week == 'Friday':
#         print("Open")
#     elif day_of_week == 'Saturday':
#         print("Open")
#     elif day_of_week == 'Sunday':
#         print("closed")
# else:
#     print("closed")

time_of_day = int(input())
day_of_week = input()

if 10 <= time_of_day <= 18 and day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
    print("Open")
else:
    print("Closed")
