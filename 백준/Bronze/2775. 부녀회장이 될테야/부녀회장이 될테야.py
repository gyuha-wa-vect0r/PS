case = int(input())

for i in range(case):
  k = int(input())
  n = int(input())
  people = [i for i in range(1, n+1)]

  for h in range(k):
    for f in range(1, n):
      people[f] = people[f] + people[f-1]

  print(people[-1])