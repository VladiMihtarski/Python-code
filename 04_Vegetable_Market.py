price_vegetables = float(input())
fruit_price = float(input())
Total_kilograms_of_vegetables = int(input())
Total_kilograms_of_fruit = int(input())

income = ((price_vegetables * Total_kilograms_of_vegetables) \
          + (fruit_price * Total_kilograms_of_fruit)) / 1.94
print(f"{income:.2f}")


# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     print()
#     i += 1
#
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()