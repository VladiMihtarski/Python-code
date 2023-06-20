first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

for first in range(2, first_limit + 1, 2):
    for second in range(2, second_limit + 1):
        if second == 2 or second == 3 or second == 5 or second == 7:
            for third in range(2, third_limit + 1, 2):
                print(str(first) + str(second) + str(third))




# def generate_pins():
#     first_limit = int(input())
#     second_limit = int(input())
#     third_limit = int(input())
# 
#     valid_pins = []
# 
#     for first in range(2, first_limit + 1, 2):
#         for second in range(2, second_limit + 1):
#             if is_prime(second):
#                 for third in range(2, third_limit + 1, 2):
#                     valid_pins.append(str(first) + str(second) + str(third))
# 
#     return valid_pins
# 
# 
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# 
# 
# pins = generate_pins()
# 
# for pin in pins:
#     print(pin)
