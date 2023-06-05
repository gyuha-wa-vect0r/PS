# 1157
# 이거 단어를 리스트로 입력받고 인덱스 조회하면서 알파벳 수 카운팅하여 딕셔너리 저장! 카운팅 수 가장 큰 알파벳 대문자 출력하면 끝일듯...
# ? 출력은 stack_alpha의 value에서 stack_alpha의 max()값과 2개 이상 같다고 인지되면 출력하는 것인가...

word = list(input().upper()) # 입력받은 단어의 알파벳을 대문자로 변환
stack_alpha = {} # 입력받은 단어의 알파벳 개수를 저장 할 딕셔너리

# 입력받은 단어의 알파벳 개수 딕셔너리에 저장
for i in word:
  if i not in stack_alpha:
    stack_alpha[i] = 0
  if i in stack_alpha:
    stack_alpha[i] += 1

# print(stack_alpha) -> 딕셔너리 확인용 체크포인트

max_alpha = max(stack_alpha, key = stack_alpha.get) # 딕셔너리의 value 중 가장 큰 수의 key
max_count = max(stack_alpha.values()) # 딕셔너리의 모든 value 중 최댓값

# 딕셔너리 내부에 value 최댓값 개수 측정하기
counter_check = 0
for j in stack_alpha.values(): # 딕셔너리의 모든 value 중에서 하나하나씩 확인할 것
  if j != max_count: 
    counter_check += 0 # 최대값이 발견되지 않는다면 counter_check의 증감 pass
  elif j == max_count:
    counter_check += 1 # 최대값이 발견된다면 counter_check의 증감 go

if counter_check >= 2: # 같은 알파벳이 2개 이상이면 ? 출력
  print('?')
elif counter_check < 2: # 1개 이하이면 최대값에 해당하는 알파벳 대문자 출력
  print(max_alpha)