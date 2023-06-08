n, m = map(int, input().split())

nonListen = set()
nonSee = set()
for i in range(n):
  name_nonListen = input()
  nonListen.add(name_nonListen)
for j in range(m):
  name_nonSee = input()
  nonSee.add(name_nonSee)

nonAll = nonListen & nonSee
nonAll_list = list(nonAll)
nonAll_list.sort()

print(len(nonAll_list))
for f in nonAll_list:
  print(f)
