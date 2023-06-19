training_fee = int(input())

percentages_without_discount_shoes = 0.4
percentages_without_discount_team = 0.2

shoes_price = training_fee - (percentages_without_discount_shoes * training_fee)
team_price = shoes_price - (percentages_without_discount_team * shoes_price)
ball_price = team_price  / 4
accessories_price = ball_price / 5

total_price = shoes_price + team_price + ball_price + accessories_price + training_fee

print(f"{total_price:.2f}")
