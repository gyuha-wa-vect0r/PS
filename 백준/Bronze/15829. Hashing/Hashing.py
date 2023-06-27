alpha_lower = [chr(i) for i in range(97,123)]
alpha_num = []

l = int(input())
word = list(input())
sum = 0
i = 0

for j in word:
  alpha_num.append(alpha_lower.index(j) + 1)
  
for m in alpha_num:
  sum += (m*(31**i))
  i += 1

print(sum % 1234567891)