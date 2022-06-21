data = "Hello World"
print(data)

data = "Don't you know \"Python\"?"
print(data)

a = "Hello"
b = "World"

print(a + " " + b)

a = "String"

print(a * 3)

a = "ABCDEF"
print(a[2 : 4])

print("###############################")

a = (1, 2, 3, 4)
print(a)

#a[2] = 7

print("###############################")

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재합니다.")

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
  print(data[key])

print("###############################")

data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)

print("###############################")

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b)
print(a & b)
print(a - b)

data = set([1, 2, 3])
print(data)

data.add(4)
print(data)

data.update([5, 6])
print(data)

data.remove(3)
print(data)