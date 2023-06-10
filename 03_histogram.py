import sys

max_num = -sys.maxsize
num_sum = 0

n = int(input())

count_p1 = count_p2 = count_p3 = count_p4 = count_p5 = 0

for _ in range(n):
    num = int(input())
    num_sum += num
    if num < 200:
        count_p1 += 1
    elif num <= 399:
        count_p2 += 1
    elif num <= 599:
        count_p3 += 1
    elif num <= 799:
        count_p4 += 1
    else:
        count_p5 += 1

p1 = count_p1 / n * 100
p2 = count_p2 / n * 100
p3 = count_p3 / n * 100
p4 = count_p4 / n * 100
p5 = count_p5 / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")