# Инициализиране на променливите за най-силната дума и силата й
most_powerful_word = ""
max_power = 0

# Четене на първата дума
word = input()

# Цикъл за обработка на думите
while word != "End of words":
    power = 0

    # Изчисляване на силата на думата
    for char in word:
        power += ord(char)

    # Проверка дали думата започва с гласна буква
    if word[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
        power *= len(word)
    else:
        power = int(power / len(word))

    # Проверка дали текущата дума е най-силна до момента
    if power > max_power:
        most_powerful_word = word
        max_power = power

    # Четене на следващата дума
    word = input()

# Извеждане на резултата
print(f"The most powerful word is {most_powerful_word} - {max_power}")
