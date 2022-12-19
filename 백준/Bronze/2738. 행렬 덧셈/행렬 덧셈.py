a, b = input().split()
x, y = int(a), int(b) #x가 행이고 y가 열이다!!
mat1, mat2 = [], []

for i in range(x):
  input1 = list(map(int, input().split()))
  mat1.append(input1)

for j in range(x):
  input2 = list(map(int, input().split()))
  mat2.append(input2)

for l in range(x):
  for h in range(y):
    print(mat1[l][h] + mat2[l][h], end = " ")

  print()
