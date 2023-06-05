import sys

quantity = int(sys.stdin.readline())
num = []

for i in range(quantity):
  num.append(int(sys.stdin.readline()))

num.sort()
for j in num:
  print(j)
