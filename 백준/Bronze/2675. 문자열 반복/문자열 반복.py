t = int(input())

for _ in range(t):
  num, word = map(str, input().split())
  alpha = list(word)

  for j in alpha:
    for i in range(1, int(num)+1):
      print(j, end = "")

  print("")