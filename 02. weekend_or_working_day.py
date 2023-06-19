day = input("Enter a day: ")

if day == "Monday" \
        or day == "Tuesday" \
        or day == "Wednesday" \
        or day == "Thursday" \
        or day == "Friday":
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Error")

# Second version


# day = input("Enter a day: ")
#
# if day.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
#     print("Working day")
# elif day.lower() in ["saturday", "sunday"]:
#     print("Weekend")
# else:
#     print("Error")
