secret_command = 'con'
current_word = ''
found_c = False
found_o = False
found_n = False



while True:
    char = input()

    if char == 'End':
        if found_c and found_o and found_n:
            break

    if char.isalpha():
        if len(char) == 1:  # Проверка за вход с една буква
            if found_c and found_o and found_n:
                current_word += char
        if char == 'c' and not found_c:
            found_c = True
        elif char == 'o' and not found_o:
            found_o = True
        elif char == 'n' and not found_n:
            found_n = True
        else:
            current_word += char

        if found_c and found_o and found_n:
            print(current_word, end=' ')
            current_word = ''
            found_c = False
            found_o = False
            found_n = False

    elif not char.strip():  # Проверка за празен низ
        continue
