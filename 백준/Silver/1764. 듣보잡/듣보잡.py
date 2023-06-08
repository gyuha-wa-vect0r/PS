n, m = map(int, input().split())

nonListen = []
nonSee = []
for i in range(n):
  name_nonListen = input()
  nonListen.append(name_nonListen)
for j in range(m):
  name_nonSee = input()
  nonSee.append(name_nonSee)

nonAll_Sort = nonListen + nonSee
nonAll_Sort.sort()
nonAll = [0] + nonAll_Sort

duplication = []
for k in range(1, len(nonAll)):
  if nonAll[k-1] == nonAll[k]:
    duplication.append(nonAll[k])

print(len(duplication))
for f in duplication:
  print(f)