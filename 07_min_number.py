smallest = float('inf')
number = input()

while number != 'Stop':
    number = int(number)
    if number < smallest:
        smallest = number

    number = input()

print(smallest)
