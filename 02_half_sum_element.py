import sys

max_num = -sys.maxsize
num_sum = 0

num_count = int(input())

for _ in range(num_count):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    num_sum += current_num

rest_sum = num_sum - max_num

if max_num == rest_sum:
    print(f"Yes\nSum = {max_num}")
else:
    diff = abs(max_num - rest_sum)
    print(f"No\nDiff = {diff}")



# n = int(input("Въведете броя на целите числа: "))
#
# numbers = []
# total_sum = 0
#
# print("Въведете числата:")
# for _ in range(n):
#     num = int(input())
#     numbers.append(num)
#     total_sum += num
#
# has_matching_number = False
# matching_number = 0
#
# for num in numbers:
#     if num == total_sum - num:
#         has_matching_number = True
#         matching_number = num
#         break
#
# if has_matching_number:
#     print("Yes")
#     print("Sum =", matching_number)
# else:
#     diff = abs(max(numbers) - (total_sum - max(numbers)))
#     print("No")
#     print("Diff =", diff)
