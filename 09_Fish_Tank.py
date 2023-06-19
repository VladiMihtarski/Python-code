length = int(input())
width = int(input())
height = int(input())
percent_used_capacity = float(input())

size_aquarium = length * width * height
full_space = size_aquarium * (percent_used_capacity / 100)
water_volume = size_aquarium - full_space
liters = water_volume / 1000

print("{:.5f}".format(liters))


# water_volume = length * width * height * (1 - (percent_used_capacity / 100))
# liters = water_volume / 1000
#
# print("{:.5f}".format(liters))