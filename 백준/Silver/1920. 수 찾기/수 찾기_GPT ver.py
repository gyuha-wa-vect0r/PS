def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Sort the array
arr.sort()

# Perform binary search for each query
m = int(input())
queries = list(map(int, input().split()))

# Process queries
for query in queries:
    result = binary_search(arr, query)
    print(result)
