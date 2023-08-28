n = int(input())

plan = input().split()

resultX = 1
resultY = 1
for i in plan:

    x, y = resultX, resultY

    if i == 'R':
        x += 1
    elif i == 'U':
        y -= 1
    elif i == 'D':
        y += 1
    elif i == 'L':
        x -= 1

    if x > n or y > n or x < 1 or y < 1:
        continue

    resultX, resultY = x, y

print(resultX, resultY)
