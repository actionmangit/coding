# 3 3
n, m = map(int, input().split())

result = 0
# 3 1 2
# 4 1 4
# 2 2 2
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

# 2
print(result)


