name_on_actor = input()
academy_points = float(input())
number_of_assessors = int(input())

total_points = academy_points
for _ in range(number_of_assessors):
    judge_name = input()
    judge_points = float(input())
    points = len(judge_name) * judge_points / 2.0
    total_points += points
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {name_on_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {name_on_actor} you need {needed_points:.1f} more!")