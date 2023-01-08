# 5 8 3
n, m, k = map(int, input().split())
# 2 4 5 4 6
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 최대값이 들어 갈 수 있는 횟수
count = (m // k + 1) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

# 46
print(result)
