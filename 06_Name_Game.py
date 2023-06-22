winner_name = ""
winner_points = 0
last_player_name = ""

player_name = input()

while player_name != "Stop":
    player_points = 0

    for _ in range(len(player_name)):
        number = int(input())
        if number == ord(player_name[_]):
            player_points += 10
        else:
            player_points += 2

    if player_points > winner_points or (player_points == winner_points and last_player_name != ""):
        winner_name = player_name
        winner_points = player_points

    last_player_name = player_name
    player_name = input()

print(f"The winner is {winner_name} with {winner_points} points!")
