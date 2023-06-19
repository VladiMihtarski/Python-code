expected_amount = int(input())  # Сумата, която се очаква да бъде събрана
total_cash = 0  # Обща сума в брой
total_card = 0  # Обща сума с карта
cash_counter = 0  # Брояч на плащания в брой
card_counter = 0  # Брояч на плащания с карта
payment_method = "cash"  # Начален метод на плащане е "брой"
iteration_counter = 2  # Брояч на интерациите

while True:
    price = input()  # Цена на продукт
    if price == "End":
        break

    price = int(price)

    if payment_method == "cash":
        if price > 100:
            print("Error in transaction!")
        else:
            total_cash += price
            cash_counter += 1
            print("Product sold!")

    if payment_method == "card":
        if price < 10:
            print("Error in transaction!")
        else:
            total_card += price
            card_counter += 1
            print("Product sold!")

    iteration_counter += 1

    if iteration_counter % 2 == 0:
        payment_method = "cash"
    else:
        payment_method = "card"

    if total_cash + total_card >= expected_amount:
        break

average_cash = total_cash / cash_counter if cash_counter > 0 else 0
average_card = total_card / card_counter if card_counter > 0 else 0

if total_cash + total_card >= expected_amount:
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
else:
    print("Failed to collect required money for charity.")
