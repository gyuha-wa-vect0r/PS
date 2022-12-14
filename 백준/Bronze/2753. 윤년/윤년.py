a = input()
x = int(a)

if x % 4 == 0:
    if x % 400 == 0 or x % 100 != 0:
        print("1")
    else:
        print("0")
else:
    print("0")