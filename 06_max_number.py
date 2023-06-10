largest = float('-inf')
number = input()

while number != 'Stop':
    number = int(number)
    if number > largest:
        largest = number

    number = input()

print(largest)
