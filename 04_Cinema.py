capacity = int(input())
income = 0

people = input()
while people != "Movie time!":
    people = int(people)
    if people > capacity:
        print("The cinema is full.")
        break
    else:
        income += people * 5
        capacity -= people
        if people % 3 == 0:
            income -= 5
    people = input()

if people == "Movie time!":
    print(f"There are {capacity} seats left in the cinema.")

print(f"Cinema income - {income} lv.")
