#2605

stunum = int(input())
picknum = list(map(int, input().split()))

queue = []

for i in range(stunum):
  queue.insert(i-picknum[i], i+1)

for j in queue:
  print(j, end = ' ')