import sys
input = sys.stdin.readline

def round2(num):
  return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(input())

if n == 0:
  print(0)

else:
  difficulty = []
  for _ in range(n):
    num = int(input())
    difficulty.append(num)
  difficulty.sort()

  trimmed_average = round2((len(difficulty) * 0.3) / 2)
  del difficulty[0:trimmed_average]
  del difficulty[len(difficulty) - trimmed_average:]

  mean = sum(difficulty) / len(difficulty)
  print(round2(mean))