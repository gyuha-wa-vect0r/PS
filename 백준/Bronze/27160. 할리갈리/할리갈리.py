# 27160
# 이거 그냥 과일의 수의 총 합이 5인거만 YES 띄우면 되지 않을까.?
# N 받고, 그거만큼 과일이랑 개수 이차원 배열로 묶어서 각 과일별 합 파악하고 5이면 YES, 아니면 NO 출력하기

n = int(input())

card = [['STRAWBERRY',0], ['BANANA',0], ['LIME',0], ['PLUM',0]]

for i in range(n):
  name, quantity = map(str, input().split())
  
  if name == 'STRAWBERRY':
    card[0][1] += int(quantity)
  elif name == 'BANANA':
    card[1][1] += int(quantity)
  elif name == 'LIME':
    card[2][1] += int(quantity)
  elif name == 'PLUM':
    card[3][1] += int(quantity)

if card[0][1] == 5 or card[1][1] == 5 or card[2][1] == 5 or card[3][1] == 5:
  print('YES')
else:
  print('NO')
  
# print(card) -> 카드 누적 확인용