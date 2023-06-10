n = int(input("Enter the value of n: "))

left_sum = 0
right_sum = 0

# Въвеждане на левите числа
# print("Enter the left numbers:")
for _ in range(n):
    num = int(input())
    left_sum += num

# Въвеждане на десните числа
# print("Enter the right numbers:")
for _ in range(n):
    num = int(input())
    right_sum += num

# Проверка и отпечатване на резултата
diff = abs(left_sum - right_sum)
if diff == 0:
    print("Yes, sum =", left_sum)
else:
    print("No, diff =", diff)
