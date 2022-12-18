a = input()
n = int(a)

array = list(map(int, input().split()))

b = input()
v = int(b)

output = []

for i in range(n):
  if array[i] == v:
    output.append(array[i])
  
print(len(output))
