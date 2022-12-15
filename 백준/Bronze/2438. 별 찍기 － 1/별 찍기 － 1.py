case = input()
x = int(case)

for i in range(0, x):
    for j in range (0, i+1):
        print("*", end = '')
    print()