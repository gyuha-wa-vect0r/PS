student = []

for i in range(0, 30):
  student.append(i+1)

for j in range(0, 28):
  submit = int(input())
  student.remove(submit)

print(min(student))
print(max(student))