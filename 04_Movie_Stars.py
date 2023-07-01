budget = float(input())
remaining_budget = budget

command = input()

while command != "ACTION":
    actor_name = command
    if len(actor_name) > 15:
        actor_honorarium = 0.2 * remaining_budget
    else:
        actor_honorarium = float(input())

    if actor_honorarium > remaining_budget:
        needed_budget = actor_honorarium - remaining_budget
        print(f"We need {needed_budget:.2f} leva for our actors.")
        exit()

    remaining_budget -= actor_honorarium
    command = input()

print(f"We are left with {remaining_budget:.2f} leva.")
