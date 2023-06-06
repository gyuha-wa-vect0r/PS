weight = int(input())
plasticBag = 0

while weight >= 0:
  if weight % 5 == 0:
    plasticBag += weight // 5 
    print(plasticBag)
    break 
    
  weight = weight - 3
  plasticBag = plasticBag + 1 
    
else:
  print(-1)