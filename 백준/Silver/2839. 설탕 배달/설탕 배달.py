weight = int(input())
plasticBag = 0 # 봉지 개수

while weight >= 0:
  if weight % 5 == 0: # kg이 5로 다 담아지는 경우
    plasticBag += weight // 5 # kg을 5로 나누어서 봉지 개수 저장
    print(plasticBag) # 온전히 5로만 분배한 봉지 수 출력
    break 
  # kg이 5로 다 담아지지 않는 경우
  weight = weight - 3
  plasticBag = plasticBag + 1 # kg가 5의 배수가 될 때까지 kg-3, 3kg 봉지 개수+1 

else:
  print(-1)
