n = int(input("Enter an integer n: "))

num = 1
stop = False
for i in range(1, n+1):
    for j in range(i):
        if num > n:
            stop = True
            break
        print(num, end=" ")
        num += 1
    print()
    if stop:
        break
