# Дефиниране на цените на различните видове цветя
rose_price = 5
dahlia_price = 3.80
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

# Четене на вида цветя, броя цветя и бюджета от конзолата
flower_type = input()
flower_count = int(input())
budget = int(input())

# Инициализиране на променливи за отстъпките и увеличенията в цената
discount = 0
price_increase = 0

# Проверка за отстъпка при закупуване на повече от 80 рози
if flower_type == "Roses" and flower_count > 80:
    discount = 0.1

# Проверка за отстъпка при закупуване на повече от 90 далии
if flower_type == "Dahlias" and flower_count > 90:
    discount = 0.15

# Проверка за отстъпка при закупуване на повече от 80 лалета
if flower_type == "Tulips" and flower_count > 80:
    discount = 0.15

# Проверка за увеличение на цената при закупуване на по-малко от 120 нарциса
if flower_type == "Narcissus" and flower_count < 120:
    price_increase = 0.15

# Проверка за увеличение на цената при закупуване на по-малко от 80 гладиоли
if flower_type == "Gladiolus" and flower_count < 80:
    price_increase = 0.2

# Изчисляване на крайната цена на цветята
total_price = 0

if flower_type == "Roses":
    total_price = (rose_price * flower_count) * (1 - discount) * (1 + price_increase)
elif flower_type == "Dahlias":
    total_price = (dahlia_price * flower_count) * (1 - discount) * (1 + price_increase)
elif flower_type == "Tulips":
    total_price = (tulip_price * flower_count) * (1 - discount) * (1 + price_increase)
elif flower_type == "Narcissus":
    total_price = (narcissus_price * flower_count) * (1 - discount) * (1 + price_increase)
elif flower_type == "Gladiolus":
    total_price = (gladiolus_price * flower_count) * (1 - discount) * (1 + price_increase)

# Проверка дали бюджетът е достатъчен
if budget >= total_price:
    remaining_amount = budget - total_price
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {remaining_amount:.2f} leva left.")
else:
    needed_amount = total_price - budget
    print(f"Not enough money, you need {needed_amount:.2f} leva more.")
