excursion_price = float(input())
puzzle_pcs = int(input())
dolls_pcs = int(input())
teddy_bears_pcs = int(input())
minions_pcs = int(input())
trucks_pcs = int(input())

PUZZLE = 2.60
DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2

toys_count = puzzle_pcs + dolls_pcs \
             + teddy_bears_pcs + minions_pcs + trucks_pcs

toys_price = puzzle_pcs * PUZZLE + \
             dolls_pcs * DOLL + teddy_bears_pcs * TEDDY_BEAR \
             + minions_pcs * MINION + trucks_pcs * TRUCK

if toys_count >= 50:
    toys_price *= 0.75

rent_price = toys_price * 0.1
profit = toys_price - rent_price

if profit >= excursion_price:
    left_money = profit - excursion_price
    print(f"Yes! {left_money:.2f} lv left.")
else:
    needed_money = excursion_price - profit
    print(f"Not enough money! {needed_money:.2f} lv needed.")
