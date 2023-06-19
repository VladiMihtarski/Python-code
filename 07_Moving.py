width = int(input())
length = int(input())
height = int(input())

total_volume = width * length * height
free_space = total_volume

command = input()
while command != "Done":
    boxes = int(command)
    free_space -= boxes

    if free_space <= 0:
        break

    command = input()

if free_space >= 0:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")