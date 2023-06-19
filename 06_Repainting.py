nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00
bags_price = 0.40
paint_extra = 0.10
nylon_extra = 2
craftsmen_price = 0.30

nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_cost = (nylon + nylon_extra) * nylon_price
paint_cost = (paint + paint * paint_extra) * paint_price
thinner_cost = thinner * thinner_price
bags_cost = bags_price
craftsmen_cost = (nylon_cost + paint_cost + thinner_cost + bags_cost) * craftsmen_price * hours

total_cost = nylon_cost + paint_cost + thinner_cost + bags_cost + craftsmen_cost

print("{:.2f}".format(total_cost))
