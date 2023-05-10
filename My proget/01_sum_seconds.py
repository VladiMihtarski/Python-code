# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50). Да се напише програма, която чете времената на състезателите в секунди,
# въведени от потребителя и пресмята сумарното им време във формат "минути:секунди". Секундите да се изведат с водеща нула (2  "02", 7  "07", 35  "35"). 

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60
seconds = total_time % 60

formatted_minutes = str(minutes).zfill(1)
formatted_seconds = str(seconds).zfill(2)
convert_time = f"{formatted_minutes}:{formatted_seconds}"

print(f"{convert_time}")
