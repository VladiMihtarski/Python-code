jobs = input().split(", ")
target_index = int(input())

tasks = []
for i, job in enumerate(jobs):
    tasks.append((i, int(job)))

tasks.sort(key=lambda x: (x[1], x[0]))

clock_cycles = 0
for i, task in enumerate(tasks):
    clock_cycles += task[1]
    if task[0] == target_index:
        break

print(clock_cycles)