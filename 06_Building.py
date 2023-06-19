floors = int(input())
rooms_per_floor = int(input())

if floors == 1:
    for room in range(rooms_per_floor):
        print("L" + str(floors) + str(room), end=" ")
else:
    for floor in range(floors, 0, -1):
        if floor == floors:
            for room in range(rooms_per_floor):
                print("L" + str(floors) + str(room), end=" ")
        else:
            for room in range(rooms_per_floor):
                if floor % 2 == 0:
                    print("O" + str(floor) + str(room), end=" ")
                else:
                    print("A" + str(floor) + str(room), end=" ")
        print()