groups = int(input())
total_people = 0

musala_count = 0
monblan_count = 0
kilimandjaro_count = 0
k2_count = 0
everest_count = 0

for _ in range(groups):
    climbers = int(input())
    total_people += climbers

    if climbers <= 5:
        musala_count += climbers
    elif climbers <= 12:
        monblan_count += climbers
    elif climbers <= 25:
        kilimandjaro_count += climbers
    elif climbers <= 40:
        k2_count += climbers
    else:
        everest_count += climbers

musala_percent = musala_count / total_people * 100
monblan_percent = monblan_count / total_people * 100
kilimandjaro_percent = kilimandjaro_count / total_people * 100
k2_percent = k2_count / total_people * 100
everest_percent = everest_count / total_people * 100

print(f'{musala_percent:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimandjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')
