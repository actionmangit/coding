i = 1
result = 0

while i <= 9:
  result += 1
  i += 1

print(result)

print("###############################")

i = 1
result = 0

while i <= 9:
  if i % 2 == 1:
    result += i
  i += 1

print(result)

print("###############################")

result = 0

for i in range(1, 10):
  result += i

print(result)

print("###############################")

score = [90, 85, 77, 65, 97]
cheating_list = {2, 4}

for i in range(5):
  if i + 1 in cheating_list:
    continue
  if score[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")

print("###############################")

for i in range(2, 10):
  for j in range(1, 10):
    print(i, "X", j, "=", i * j)
  print()