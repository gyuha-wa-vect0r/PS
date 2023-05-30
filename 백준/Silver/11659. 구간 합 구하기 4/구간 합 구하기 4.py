import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
temp = 0
sumlist = [0]
for i in num:
  temp = temp + i
  sumlist.append(temp)

for j in range(m):
  a, b = map(int, input().split())
  print(sumlist[b] - sumlist[a-1]) 