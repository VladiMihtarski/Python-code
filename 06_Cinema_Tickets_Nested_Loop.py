total_student_tickets = 0
total_standard_tickets = 0
total_kids_tickets = 0
total_tickets = 0

while True:
    film = input()

    if film == "Finish":
        break

    total_seats = int(input())

    student_tickets = 0
    standard_tickets = 0
    kids_tickets = 0
    current_tickets = 0

    while current_tickets < total_seats:
        ticket_type = input()

        if ticket_type == "End":
            break

        if ticket_type == "student":
            student_tickets += 1
            total_student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            total_standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
            total_kids_tickets += 1

        current_tickets += 1
        total_tickets += 1

    percent_full = (current_tickets / total_seats) * 100
    print(f"{film} - {percent_full:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{(total_student_tickets / total_tickets * 100):.2f}% student tickets.")
print(f"{(total_standard_tickets / total_tickets * 100):.2f}% standard tickets.")
print(f"{(total_kids_tickets / total_tickets * 100):.2f}% kids tickets.")
