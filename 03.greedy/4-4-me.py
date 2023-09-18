row, column = int(input().split())
x, y, direction = int(input().split())

maps = []
for i in range(row):
    maps.append(list(input().split()))

while True:
    move_x, move_y = x, y


