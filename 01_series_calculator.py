# Write a program that calculates how long it will take you to watch all the episodes of a series in minutes.
# You will have the number of seasons, number of episodes per season and the duration of an episode.
# There are commercials in each episode that last 20% of the time of an episode.
# You also know that each season ends with a special episode that is 10m longer than usual.
# Login
# 4 lines are read from the console:
# • Series name - text
# • Number of seasons - an integer in the range [1… 10]
# • Number of episodes - an integer in the range [10… 80]
# • Duration of a regular episode without ads - real number in the range [40.0… 65.0]
# Exit
# To print to the console the time it took for all episodes to appear, rounded down to the nearest integer, in the following format:
# "Total time needed to watch the {series name} series is {time} minutes."

series_name = input()
number_seasons = int(input())
number_episodes = int(input())
episode_without_ads = float(input())

total_duration = number_seasons * ((number_episodes * episode_without_ads) \
                                   + (number_episodes * episode_without_ads * 0.2) + 10)

print(f"Total time needed to watch the {series_name} series is {int(total_duration)} minutes.")
