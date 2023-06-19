weather = float(input())

if weather >= 26 and weather <= 35:
    message = "Hot"
elif weather >= 20.1 and weather <= 25.9:
    message = "Warm"
elif weather >= 15.0 and weather <= 20.0:
    message = "Mild"
elif weather >= 12.00 and weather <= 14.9:
   message = "Cool"
elif weather >= 5.00 and weather <= 11.9:
    message = "Cold"
else:
    message = "unknown"

print(message)
