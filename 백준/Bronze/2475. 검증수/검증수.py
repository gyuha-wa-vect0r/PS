n = list(map(int, input().split()))
jaegop = 0
for i in n:
  jaegop += (i**2)
print(jaegop%10)