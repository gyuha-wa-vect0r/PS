t = int(input())

d = [0] * 12 # n에 대한 모든 경우의 수(n = 12까지)를 저장할 배열 d 선언
d[0] = 0; d[1] = 1; d[2] = 2; d[3] = 4 # n = 0 ~ 3까지 경우의 수 저장

for _ in range(t):
  n = int(input())
  if n <= 3:
    print(d[n])
  else:
    for i in range(4, n+1):
      d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[i])