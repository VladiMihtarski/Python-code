# Напишете програма за конвертиране на щатски долари (USD) в български лева (BGN). Използвайте фиксиран курс между долар и лев: 1 USD = 1.79549 BGN.

EXCHANGE_RATE = 1.79549

usd = float(input())
bgn = usd * EXCHANGE_RATE
print(bgn)
