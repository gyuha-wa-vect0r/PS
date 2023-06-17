t = int(input())

for _ in range(t):
  room = [0]
  height, room_floor, guest = map(int, input().split())

  for i in range(1, room_floor + 1):
    for j in range(1, height + 1):
      if i < 10:
        room_num = str(j) + '0' + str(i)
        room.append(int(room_num))
      elif i >= 10:
        room_num = str(j) + str(i)
        room.append(int(room_num))
  
  print(room[guest])