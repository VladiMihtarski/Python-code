destination = input()
while destination != "End":
    budget = float(input())
    savings = 0
    while savings < budget:
        amount = float(input())
        savings += amount
    print("Going to", destination + "!")
    destination = input()


# while True:
#     destination = input()
#     if destination == "End":
#         break
#     budget = float(input())
#     savings = 0
#     enough_savings = False
#     while not enough_savings:
#         amount = float(input())
#         savings += amount
#         if savings >= budget:
#             enough_savings = True
#     print("Going to", destination + "!")
