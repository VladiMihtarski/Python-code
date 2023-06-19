name_movie = input()
all_tickets = 0
general_students = 0
total_standard = 0
total_kids = 0

while name_movie != "Finish":
    free_seats = int(input())
    sold_tickets = 0
    student_tickets = 0
    standard_tickets = 0
    kids_tickets = 0

    ticket_type = input()
    while ticket_type != "End":
        sold_tickets += 1
        all_tickets += 1

        if ticket_type == "student":
            student_tickets += 1
            general_students += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            total_standard += 1
        elif ticket_type == "kid":
            kids_tickets += 1
            total_kids += 1

        if sold_tickets == free_seats:
            break

        ticket_type = input()

    occupancy_percent = sold_tickets / free_seats * 100
    print(f"{name_movie} - {occupancy_percent:.2f}% full.")

    name_movie = input()

students_percent = general_students / all_tickets * 100
standard_percent = total_standard / all_tickets * 100
kids_percent = total_kids / all_tickets * 100

print(f"Total tickets: {all_tickets}")
print(f"{students_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kids_percent:.2f}% kids tickets.")
