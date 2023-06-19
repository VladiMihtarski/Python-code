# while True:
#     voucher_cost = input()
#     if voucher_cost.isdigit() and 1 <= int(voucher_cost) <= 100000:
#         voucher_cost = int(voucher_cost)
#         break
#
# ticket_number = 0
# another_count = 0
#
# while True:
#     purchase_name = input().strip()
#     if not purchase_name:
#         break
#     if purchase_name == "End" or voucher_cost == 0:
#         break
#     if len(purchase_name) > 8:
#         ticket_price = ord(purchase_name[0]) + ord(purchase_name[1])
#         if ticket_price <= voucher_cost:
#             voucher_cost -= ticket_price
#             ticket_number += 1
#     else:
#         other_price = ord(purchase_name[0])
#         if other_price <= voucher_cost:
#             voucher_cost -= other_price
#             another_count += 1
#
# print(ticket_number)
# print(another_count)

voucher_cost = int(input())
move_tickets = 0
another_purchases = 0

while True:
    purchase = input()
    if purchase == "End":
        break

    if len(purchase) > 8:
        cost = ord(purchase[0]) + ord(purchase[1])
    else:
        cost = ord(purchase[0])

    if cost > voucher_cost:
        break

    if len(purchase) > 8:
        move_tickets += 1
    else:
        another_purchases += 1

    voucher_cost -= cost

print(f"{move_tickets}\n{another_purchases}")