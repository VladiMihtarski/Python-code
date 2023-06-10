text = input()

total_value = 0

for char in text:
    if char == 'a':
        total_value += 1
    elif char == 'e':
        total_value += 2
    elif char == 'i':
        total_value += 3
    elif char == 'o':
        total_value += 4
    elif char == 'u':
        total_value += 5

print(total_value)


# text = input("Въведете текст: ")
#
# vowels_values = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
#
# total_value = 0
#
# for char in text:
#     if char.lower() in vowels_values:
#         total_value += vowels_values[char.lower()]
#
# print("Сумата на стойностите на гласните букви е:", total_value)