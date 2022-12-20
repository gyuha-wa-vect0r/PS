a = input()

#대소문자 ASCII Code 차이 : 32

for i in range(len(a)):
  if ord(a[i]) >= 65 and ord(a[i]) <= 90: # 대문자 -> 소문자
    down = ord(a[i]) + 32
    print(chr(down), end = "")

  elif ord(a[i]) >= 97 and ord(a[i]) <= 122:
    up = ord(a[i]) - 32
    print(chr(up), end = "")
