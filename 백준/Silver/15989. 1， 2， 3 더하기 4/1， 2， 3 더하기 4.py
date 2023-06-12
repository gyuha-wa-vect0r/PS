# dp 배열은 범위 내 모든 n에 대한 경우의 수 저장을 위해 선언되었다.
dp = [1] * 10001  # 모든 양수는 1만 써서 합을 나타내는 방법 1가지씩은 모두 가지고 있으므로 dp 테이블을 1로 초기화 해줬다.

for i in range(2, 10001): # 1로만 구성된 모든 n을 2로 묶을 수 있는 경우
  dp[i] += dp[i - 2]

for i in range(3, 10001): # 1, 2로만 구성된 모든 n을 3로 묶을 수 있는 경우
  dp[i] += dp[i - 3]

# 모든 경우가 저장되었고, 특정 수를 입력받아 dp 배열에서 찾아 저장된 경우의 수 출력

t = int(input())

for _ in range(t):
  n = int(input())
  print(dp[n])
