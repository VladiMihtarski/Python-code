number = int(input())
all_output = 0
for x1 in range(0, number + 1):
    for x2 in range(0, number + 1):
        for x3 in range(0, number + 1):
            if x1 + x2 + x3 == number:
                all_output +=1
print(all_output)
