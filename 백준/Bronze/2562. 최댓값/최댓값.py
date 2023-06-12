n = [0] * 10

for i in range(1, 10):
  n[i] = int(input())

print(max(n))
print(n.index(max(n)))