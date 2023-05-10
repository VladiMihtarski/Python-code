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
