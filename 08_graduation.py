name = input("Име на ученика: ")
total_grades = 0
excluded = False
excluded_grade = 0
grade = 1
failed_attempts = 0

while grade <= 12:
    current_grade = float(input(f"Оценка за {grade} клас: "))

    if current_grade < 4.00:
        failed_attempts += 1
        if failed_attempts > 1:
            excluded = True
            excluded_grade = grade
            break
    else:
        total_grades += current_grade
        grade += 1

if excluded:
    print(f"{name} has been excluded at {excluded_grade} grade")
else:
    average_grade = total_grades / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
