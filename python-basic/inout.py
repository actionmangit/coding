# 1
n = int(input())

# 2 3 4 5 6
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

print("###############################")

# 3 4 6
n, m, k = map(int, input().split())

print(n, m, k)

print("###############################")

import sys

# Hello World
data = sys.stdin.readline().rstrip()
print(data)

a = 1
b = 2

print(a, b)

print("###############################")

a = 1
b = 2

print(a)
print(b)

print("###############################")

answer = 7

print("정답은 " + str(answer) + "입니다.")

print("###############################")

answer = 7

print("정답은", str(answer), "입니다.")

print("###############################")

answer = 7 
print(f"정답은 {answer}입니다")