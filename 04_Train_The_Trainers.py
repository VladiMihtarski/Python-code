n = int(input())

total_presentations = 0
total_grade = 0

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    presentation_grade = 0
    for _ in range(n):
        grade = float(input())
        presentation_grade += grade

    average_grade = presentation_grade / n

    print(f"{presentation_name} - {average_grade:.2f}.")

    total_presentations += 1
    total_grade += average_grade

final_average = total_grade / total_presentations

print(f"Student's final assessment is {final_average:.2f}.")
