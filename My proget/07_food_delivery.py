chicken = 10.35
menu_with_fish = 12.40
vegetarian_menu = 8.15

psc_chicken_menu = int(input())
psc_menu_with_fish = int(input())
psc_vegetarian_menu = int(input())

total_price = psc_chicken_menu * chicken\
              + psc_menu_with_fish * menu_with_fish\
              + psc_vegetarian_menu * vegetarian_menu

dessert = 0.2
delivery = 2.5

total_price += total_price * dessert
total_price += delivery

print("{:.2f}".format(total_price))
