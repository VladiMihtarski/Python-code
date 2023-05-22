# Ivan decides to improve the World Record in long distance swimming. The record in seconds is entered on the console,
# that Ivan needs to improve, the distance in meters he needs to swim and the time in seconds for him to swim a distance of 1m.
# Write a program that calculates whether the task has been completed, given that:
# water resistance slows him down every 15m by 12.5 seconds. When calculating how many times Ivancho will be late,
# due to water resistance, the result must be rounded down to the nearest whole number.
# To calculate the time in seconds for Ivancho to swim the distance and the difference to the World Record.


# record_sec = float(input())  # we read the record as a real number
# distance = float(input())  # we read the distance as a real number
# time_m = float(input())  # we read the time to float 1 meter as a real number
#
# from math import floor # to use the round down function
#
# water_resistance = floor(distance / 15) * 12.5  # we calculate how many times Ivan will slow down and round it down to the nearest whole number
# time = distance * time_m + water_resistance  # we calculate the time to float the distance with water resistance
# difference = abs(record_sec - time)  # we calculate the difference between the record and Ivan's time
#
# if time < record_sec:
#     print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
# else:
#     print(f'No, he failed! He was {difference:.2f} seconds slower.')

record_sec = float(input())  # we read the record as a real number
distance = float(input())  # we read the distance as a real number
time_m = float(input())  # we read the time to float 1 meter as a real number

water_resistance = (distance // 15) * 12.5  # we calculate how many times Ivan will slow down and round it down to the nearest whole number
time = distance * time_m + water_resistance  # we calculate the time to float the distance with water resistance
difference = abs(record_sec - time)  # we calculate the difference between the record and Ivan's time

if time < record_sec:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')
