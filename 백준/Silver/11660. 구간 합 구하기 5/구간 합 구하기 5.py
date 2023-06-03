import sys

input = sys.stdin.readline

vol, turn = map(int, input().split())
orignal = []
sum_array = [[0] * (vol+1) for _ in range(vol+1)]
print_result = []

for i in range(vol):
    input_row = list(map(int, input().split()))
    orignal.append(input_row)
    
for i in range(1, vol+1):
    for j in range(1, vol+1):
        sum_array[i][j] = sum_array[i][j-1] + sum_array[i-1][j] - sum_array[i-1][j-1] + orignal[i-1][j-1]
        
for k in range(turn):
    x1, y1, x2, y2 = map(int, input().split())
    result = sum_array[x2][y2] - sum_array[x1-1][y2] - sum_array[x2][y1-1] + sum_array[x1-1][y1-1]
    print(result)