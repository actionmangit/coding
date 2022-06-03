# basic
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[4])

# 5

a = list()
print(a)

# []

a = []
print(a)

# []

n = 10
a = [0] * n
print(a)

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("###############################")

# index
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1])

# 9

print(a[-3])

# 7

a[3] = 7
print(a)

# [1, 2, 3, 7, 5, 6, 7, 8, 9]

print("###############################")

# slicing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4])

# [2, 3, 4]

print("###############################")

# compli
array = [i for i in range(20) if i % 2 == 1]
print(array)

# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

array = [i * i for i in range(1, 10)]
print(array)

# [1, 4, 9, 16, 25, 36, 49, 64, 81]

n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

n = 3
m = 4
array = [[0] * m] * n
print(array)

# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

array[1][1] = 5
print(array)

# [[0, 5, 0, 0], [0, 5, 0, 0], [0, 5, 0, 0]]

print("###############################")

# list method
a = [1, 4, 3]
print("기본 리스트: ", a)

a.append(2)
print("삽입: ", a)

# [1, 4, 3, 2], O(1)

a.sort()
print("오름차순 정렬: ", a)

# [1, 2, 3, 4], O(NlogN)

a.sort(reverse = True)
print("내림차순 정렬: ", a)

# [4, 3, 2, 1], O(NlogN)

a.reverse()
print("원소 뒤집기: ", a)

# [1, 2, 3, 4], O(N)

a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)

# [1, 2, 3, 3, 4], O(N)

print("값이 3인 데이터 개수: ", a.count(3))

# 2, O(N)

a.remove(1)
print("값이 1인 데이터 삭제: ", a)

# [2, 3, 3, 4], O(N)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

# [1, 2, 4]