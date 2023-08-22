# n으로 나누는 것이 유리
n, k = map(int, input().split())

result = 0

while n != 1:
    if n % k == 0:
        n = n / k
    else:
        n -= 1
    result += 1

print(result)
