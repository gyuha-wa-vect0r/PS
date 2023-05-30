import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
temp = 0
sumlist = [0] # -> 따라서 연산에 아무 지장 없는 0을 미리 넣어주고, index가 1부터 시작되도록 조정

# index     0 1 2  3  4  5  -> 0부터라고 생각하면 안된다! i, j는 자연수.
# num[]       5 4  3  2  1
# sumlist[] 0 5 9 12 14 15

for i in num:
  temp = temp + i
  sumlist.append(temp)

for j in range(m):
  a, b = map(int, input().split())
  print(sumlist[b] - sumlist[a-1]) 
  # b까지 다 더한 값에서 a 전까지 더한 값 날리면 구간의 합이 나온다!
