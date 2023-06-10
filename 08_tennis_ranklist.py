number_of_tournaments = int(input())
starting_points = int(input())
total_points = starting_points
tournament_wins = 0

for _ in range(number_of_tournaments):
    tournament_stage = input()
    if tournament_stage == "W":
        total_points += 2000
        tournament_wins += 1
    elif tournament_stage == "F":
        total_points += 1200
    elif tournament_stage == "SF":
        total_points += 720

average_points = (total_points - starting_points) // number_of_tournaments
percentage_wins = (tournament_wins / number_of_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}\n{percentage_wins:.2f}%")
