# Peter wants to buy N video cards, M processors and P number of RAM. If the number of video cards is
# greater than the number of processors, you get a 15% discount on the final bill. The following prices apply:
# • Video card – BGN 250/pc.
# • Processor – 35% of the price of purchased video cards/pcs.
# • RAM memory – 10% of the price of purchased video cards/pcs.
# To calculate the amount needed to purchase the materials and to calculate whether the budget will be enough.

V_CARD = 250

budget = float(input())
number_v_card = int(input())
number_processors = int(input())
number_ram = int(input())

# calculate total price of video cards
video_cards_price = number_v_card * V_CARD

# calculate price of processors and RAM
processors_price = number_processors * (0.35 * video_cards_price)
ram_price = number_ram * (0.1 * video_cards_price)

# calculate total price and apply discount if necessary
total_price = video_cards_price + processors_price + ram_price
if number_v_card > number_processors:
    total_price *= 0.85
print(total_price)
# check if budget is enough and print result
if budget >= total_price:
    remaining_budget = budget - total_price
    print(f"You have {remaining_budget:.2f} leva left!")
else:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
