hall_rent = float(input())

statuettes_cost = hall_rent * 0.7
catering_cost = statuettes_cost * 0.85
voicing_cost = catering_cost / 2

total_cost = hall_rent + statuettes_cost + catering_cost + voicing_cost

print(f"{total_cost:.2f}")
