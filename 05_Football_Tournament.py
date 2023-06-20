team_name = input()
games_played = int(input())

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    total_points = 0
    wins = 0
    draws = 0
    losses = 0

    for _ in range(games_played):
        result = input()

        if result == 'W':
            total_points += 3
            wins += 1
        elif result == 'D':
            total_points += 1
            draws += 1
        elif result == 'L':
            losses += 1

    win_rate = (wins / games_played) * 100

    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {losses}")
    print(f"Win rate: {win_rate:.2f}%")
