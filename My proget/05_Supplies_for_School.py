pen_package_price = 5.80
mark_package_price = 7.20
cleaner_price = 1.20

num_pen = int(input())
num_mark = int(input())
num_cleaner = int(input())
discount = int(input())

total_cost = (num_pen * pen_package_price) + (num_mark * mark_package_price) + (num_cleaner * cleaner_price)
discount_amount = (discount / 100) * total_cost
total_cost -= discount_amount
print(f"{total_cost:.1f} ")
