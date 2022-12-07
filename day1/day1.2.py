input = open("day1/input1.txt" , "r")

L = input.readlines()
L1 = []
count = 0

for i in range(0, len(L) - 2):
    L1.append(int(L[i]) + int(L[i + 1]) + int(L[i + 2]))
    print(L1[i])

for i in range(1, len(L1)):
    if int(L1[i]) > int(L1[i - 1]):
        count += 1

print("It increased", count, "times.")