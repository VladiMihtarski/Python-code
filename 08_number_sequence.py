n = int(input())

min_number = None
max_number = None

for i in range(n):
    number = int(input())

    if min_number is None or number < min_number:
        min_number = number

    if max_number is None or number > max_number:
        max_number = number

print("Min number:", min_number)
print("Max number:", max_number)
