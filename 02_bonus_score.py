starting_number = int(input())

extra_points = 0

if starting_number <= 100:
    extra_points += 5
elif starting_number <= 1000:
    extra_points += starting_number * 0.2
else:
    extra_points += starting_number * 0.1

if starting_number % 2 == 0:
    extra_points += 1

if starting_number % 10 == 5:
    extra_points += 2

total_score = starting_number + extra_points

print(f"{extra_points}\n{total_score}")
