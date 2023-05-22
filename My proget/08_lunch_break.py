# During your lunch break, you want to watch an episode of your favorite series.
# Your task is to write a program that will tell if you have enough time to watch the episode.
# During the break, you have time for lunch and time for relaxation.
# Lunch time will be 1/8 of break time and recess time will be 1/4 of break time.
# Login
# 3 lines are read from the console:
# 1. Name of series - text
# 2. Episode duration - an integer in the range [10… 90]
# 3. Rest duration - an integer in the range [10… 120]
# Exit
# Write one line to the console:
# • If there is enough time to watch the episode:
# "You have enough time to watch {series name} and left with {remaining time} minutes free time."
# • If you don't have enough time:
# "You don't have enough time to watch {series name}, you need {necessary time} more minutes."
# Time to be rounded up to the nearest whole number.

import math

series_name = input()
episode_duration = int(input())
b_duration = int(input())

validate_input(episode_duration, 10, 90)
validate_input(rest_duration, 10, 120)

lunch_duration = b_duration / 8
rest_duration = b_duration / 4

total_time = b_duration - lunch_duration - rest_duration
needed_time = episode_duration

if total_time >= needed_time:
    left_time = math.ceil(total_time - needed_time)
    print(f"You have enough time to watch {series_name} and left with {left_time} minutes free time.")
else:
    extra_time = math.ceil(needed_time - total_time)
    print(f"You don't have enough time to watch {series_name}, you need {extra_time} more minutes.")
