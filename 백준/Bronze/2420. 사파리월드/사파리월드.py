a, b = input().split()
x = int(a)
y = int(b)

if x - y > 0:
    print(x - y)
elif x - y < 0:
    print((x - y)*(-1))