n = int(input("Enter the value of n: "))

even_sum = 0
odd_sum = 0

print("Enter the numbers:")
for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:  # четна позиция
        even_sum += num
    else:  # нечетна позиция
        odd_sum += num

diff = abs(even_sum - odd_sum)
if diff == 0:
    print("Yes")
    print("Sum =", even_sum)
else:
    print("No")
    print("Diff =", diff)
