num = int(input())
words = []
for _ in range(num):
  words.append(input())
after_rd = list(set(words))  # rd : remove_duplication
after_rd.sort()
after_rd.sort(key=len)

for i in after_rd:
  print(i)