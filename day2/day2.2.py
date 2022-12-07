input = open("day2/input2.txt", "r")

L = input.readlines()
L1 = []

horizontal = 0
depth = 0
aim = 0

for i in L:
    L1 = i.split()
    if L1[0] == "forward":
        horizontal += int(L1[1])
        depth += aim * int(L1[1])
    elif L1[0] == "down":
        aim += int(L1[1])
    else:
        aim -= int(L1[1])


print("The result is", horizontal * depth, "\b.")