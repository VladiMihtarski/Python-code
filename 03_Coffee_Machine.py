city = input()  # Име на града
package = input()  # Вид на пакета
vip_discount = input()  # Притежание на VIP отстъпка
stay_days = int(input())  # Дни за престой

price_per_day = 0  # Цена за ден
total_price = 0  # Обща цена

# Проверка на входните данни и изчисляване на цената
if city == "Bansko" or city == "Borovets":
    if package == "withEquipment":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day -= price_per_day * 0.1
    elif package == "noEquipment":
        price_per_day = 80
        if vip_discount == "yes":
            price_per_day -= price_per_day * 0.05
    else:
        print("Invalid input!")
        exit(0)
elif city == "Varna" or city == "Burgas":
    if package == "withBreakfast":
        price_per_day = 130
        if vip_discount == "yes":
            price_per_day -= price_per_day * 0.12
    elif package == "noBreakfast":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day -= price_per_day * 0.07
    else:
        print("Invalid input!")
        exit(0)
else:
    print("Invalid input!")
    exit(0)

if stay_days < 1:
    print("Days must be a positive number!")
else:
    if stay_days > 7:
        stay_days -= 1
    total_price = price_per_day * stay_days
    print(f"The price is {total_price:.2f} lv! Have a nice time!")
