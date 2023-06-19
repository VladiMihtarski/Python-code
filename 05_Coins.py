resto = float(input("Въведете рестото: "))

coins = 0  # брой монети

resto_in_cents = int(resto * 100)  # превръщаме сумата в центове

while resto_in_cents >= 200:
    coins += 1
    resto_in_cents -= 200

while resto_in_cents >= 100:
    coins += 1
    resto_in_cents -= 100

while resto_in_cents >= 50:
    coins += 1
    resto_in_cents -= 50

while resto_in_cents >= 20:
    coins += 1
    resto_in_cents -= 20

while resto_in_cents >= 10:
    coins += 1
    resto_in_cents -= 10

while resto_in_cents >= 5:
    coins += 1
    resto_in_cents -= 5

while resto_in_cents >= 2:
    coins += 1
    resto_in_cents -= 2

coins += resto_in_cents  # връщаме монети от 1 стотинка

print("Брой монети за връщане:", coins)
#
# resto = float(input("Въведете рестото: "))
#
# coins = 0  # брой монети
#
# coin_values = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]  # номинали на наличните монети
#
# resto_in_cents = int(resto * 100)  # превръщаме сумата в центове
#
# for coin in coin_values:
#     while resto_in_cents >= int(coin * 100):
#         coins += 1
#         resto_in_cents -= int(coin * 100)
#
# if resto_in_cents > 0:
#     coins += 1
#
# print("Брой монети за връщане:", coins)

