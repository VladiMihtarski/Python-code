deposited_amount = float(input())
term_of_deposit = float(input())
annual_interest_rate = float(input())

monthly_interest_rate = annual_interest_rate / 12 / 100
amount = deposited_amount + term_of_deposit * ((deposited_amount * monthly_interest_rate))

print(f"{amount:.2f}")
