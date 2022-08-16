def add(a, b):
  return a + b

print(add(3, 7))

print("###############################")

def add(a, b):
  print('함수의 결과:', a + b)

add(3, 7)

print("###############################")

def add(a, b):
  print('함수의 결과:', a + b)

add(b = 3, a = 7)

print("###############################")

a = 0

def func():
  global a
  a += 1

for i in range(10):
  func()

print(a)

print("###############################")

def add(a, b):
  return a + b

print(add(3, 7))

print((lambda a, b: a + b)(3, 7))