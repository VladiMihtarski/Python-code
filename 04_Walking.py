goal_steps = 10000
total_steps = 0

while total_steps < goal_steps:
    command = input()

    if command == "Going home":
        steps = int(input())
        total_steps += steps
        break

    steps = int(command)
    total_steps += steps

if total_steps >= goal_steps:
    difference = total_steps - goal_steps
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    difference = goal_steps - total_steps
    print(f"{difference} more steps to reach goal.")
