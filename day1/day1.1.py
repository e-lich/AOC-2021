input = open("day1/input1.txt" , "r")

L = input.readlines()
count = 0

for i in range(1, len(L)):
    if int(L[i]) > int(L[i - 1]):
        count += 1

print("It increased", count, "times.")