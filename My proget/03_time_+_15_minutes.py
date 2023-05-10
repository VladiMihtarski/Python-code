enter_hour = int(input())
enter_minutes = int(input())

future_min = (enter_minutes + 15) % 60
future_h = (enter_hour + (enter_minutes + 15) // 60) % 24

print(f"{future_h:01d}:{future_min:02d}")
