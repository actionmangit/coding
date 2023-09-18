point = input()

rows = ["a", "b", "c", "d", "e", "f", "g", "h"]

garoChar = point[0]
inputX = rows.index(garoChar) + 1
inputY = int(point[1])

changeX = [1, -1, 2, 2, 1, -1, -2, -2]
changeY = [2, 2, -1, 1, -2, -2, -1, 1]

print(inputX)
print(inputY)
print("================")

count = 0
result = 0
for i in changeX:
    x, y = inputX, inputY
    x += i
    y += changeY[count]

    print(x, y)

    if x >= 1 and y >= 1:
        result += 1

    count += 1

print(result)
