input = open("day5/input5.txt", "r")

L = input.readlines()

all = []
line = ['.'] * 1000
field = []
for i in range(0, 1000):
    field.append(list(line))

count = 0
x = 0
y = 0

def overlaps(a0, a1, b0, b1):
    if a0 < b0 and b0 < a1:
        return True
    elif b0 < a0 and a0 < b1:
        return True
    elif a1 == b0 or b1 == a0:
        return True
    else:
        return False

for i in L:
    line = i.split()
    intervals = []
    interval = line[0].split(',')
    intervals.append(int(interval[0]))
    intervals.append(int(interval[1]))
    interval = line[2].split(',')
    intervals.append(int(interval[0]))
    intervals.append(int(interval[1]))
    all.append(intervals)

for interval in all:
    if interval[0] == interval[2]:
        if interval[1] > interval[3]:
            x = interval[3]
            y = interval[1]
        else:
            x = interval[1]
            y = interval[3]
        for i in range(x, y + 1):
            if field[i][interval[0]] == '.':
                field[i][interval[0]] = 1
            else:
                field[i][interval[0]] += 1
    elif interval[1] == interval[3]:
        if interval[0] > interval[2]:
            x = interval[2]
            y = interval[0]
        else:
            x = interval[0]
            y = interval[2]
        for i in range(x, y + 1):
            if field[interval[1]][i] == '.':
                field[interval[1]][i] = 1
            else:
                field[interval[1]][i] += 1
    elif interval[0] < interval[2] and interval[1] < interval[3]:
        diff = interval[2] - interval[0] + 1
        for i in range(0, diff):
            if field[interval[1] + i][interval[0] + i] == '.':
                field[interval[1] + i][interval[0] + i] = 1
            else:
                field[interval[1] + i][interval[0] + i] += 1
    elif interval[0] > interval[2] and interval[1] > interval[3]:
        diff = interval[0] - interval[2] + 1
        for i in range(0, diff):
            if field[interval[3] + i][interval[2] + i] == '.':
                field[interval[3] + i][interval[2] + i] = 1
            else:
                field[interval[3] + i][interval[2] + i] += 1        
    elif interval[0] < interval[2] and interval[1] > interval[3]:
        diff = interval[2] - interval[0] + 1
        for i in range(0, diff):
            if field[interval[1] - i][interval[0] + i] == '.':
                field[interval[1] - i][interval[0] + i] = 1
            else:
                field[interval[1] - i][interval[0] + i] += 1
    elif interval[0] > interval[2] and interval[1] < interval[3]:
        diff = interval[0] - interval[2] + 1
        for i in range(0, diff):
            if field[interval[1] + i][interval[0] - i] == '.':
                field[interval[1] + i][interval[0] - i] = 1
            else:
                field[interval[1] + i][interval[0] - i] += 1 

for i in field:
    for j in i:
        if j != '.' and j >= 2:
            count += 1

print("At least two lines overlap at", count, "points.")
    