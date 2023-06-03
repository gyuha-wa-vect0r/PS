case = int(input())

for i in range(case):
  k = int(input())
  n = int(input())
  people = [i for i in range(1, n+1)] 
  # people이라는 변수에 0층에서 1부터 n호까지의 각각 사람수를 리스트에 담아두었다.

  for h in range(k):
    for f in range(1, n):
      people[f] = people[f] + people[f-1] 
      # 0층 i호에 사는 거주민 수를 리스트에 담고
      # 이를 반복문을 통해서 층이 바뀌면 i호에 사는 사람들도 늘어나는 것을 차근차근 바꿔주는것이다.
      # 마지막으로 반복문이 끝나면 k층 n호까지 사는 거주민들이 리스트에 담겨져있으니
      # 마지막 인덱스를 출력하면 k층 n호에 사는데 필요한 거주민 수를 출력할 수 있다.

  print(people[-1])
