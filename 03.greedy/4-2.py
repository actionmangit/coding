inHour = int(input())

result = 0

hour = 0
mini = 0
sec = 0

while True:

    if sec == 60:
        sec = 0
        mini += 1

    if mini == 60:
        mini = 0
        hour += 1

    sec += 1

    if hour > inHour:
        break

    if '3' in str(sec) or '3' in str(mini) or '3' in str(hour):
        result += 1
        
print(result)
