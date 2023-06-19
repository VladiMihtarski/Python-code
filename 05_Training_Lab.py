w = float(input())
h = float(input())

corridor_width = 100
desk_width = 70
desk_length = 120

total_width_cm = w * 100
total_length_cm = h * 100

available_width = total_length_cm - corridor_width
desks_per_row = int(available_width / desk_width)
rows = int(total_width_cm / desk_length)

total_desks = rows * desks_per_row - 3

print(total_desks)
