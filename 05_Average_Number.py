n = int(input("Enter the number of numbers: "))

total = 0
count = 0

while count < n:
    num = int(input("Enter a number: "))
    total += num
    count += 1

average = total / n
formatted_average = "{:.2f}".format(average)

print(formatted_average)
