unsatisfactory_grades = int(input())
average_score = 0
problem_count = 0
unsatisfactory_count = 0
last_problem = ""

while unsatisfactory_count < unsatisfactory_grades:
    problem_name = input()
    if problem_name == "Enough":
        break
    grade = int(input())

    if grade <= 4:
        unsatisfactory_count += 1

    average_score += grade
    problem_count += 1
    last_problem = problem_name

if unsatisfactory_count == unsatisfactory_grades:
    print(f"You need a break, {unsatisfactory_count} poor grades.")
else:
    average_score /= problem_count
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problem_count}")
    print(f"Last problem: {last_problem}")
