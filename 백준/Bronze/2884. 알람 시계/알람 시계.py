hr, min = map(int, input().split())

if min >= 45:
  new_min = min - 45
  print(hr, new_min)
else:
  new_hr = hr - 1
  new_min = 60 - (45 - min)
  if new_hr == -1:
    new_hr = 23
  print(new_hr, new_min)