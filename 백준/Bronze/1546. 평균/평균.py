sub = int(input())
table = list(map(int, input().split()))
maxscore = max(table)
sumscore = sum(table)
edittable = []

for i in table:
 edittable.append(int(i)/maxscore*100)

result = sum(edittable) / sub

print(result)
