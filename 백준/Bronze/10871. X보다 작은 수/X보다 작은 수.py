a, b = input().split()
n = int(a)
x = int(b)

array = list(map(int, input().split()))
output = []

for i in range(n):
  if x > array[i]:
    output.append(array[i])
  
for i in range(len(output)):
  print(output[i], end = " ")