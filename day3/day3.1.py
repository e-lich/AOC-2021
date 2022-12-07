input = open("day3/input3.txt", "r")

L = input.readlines()

zeros = [0] * (len(L[0]) - 1)
ones = [0] * (len(L[0]) - 1)

gamma = 0
epsilon = 0

for i in L:
    for j in range(0, len(zeros)):
        if i[j] == '0':
            zeros[j] += 1
        else:
            ones[j] += 1
 

for i in range(0, len(zeros)):
    if zeros[i] > ones[i]:
        epsilon += pow(2, len(zeros) - 1 - i)
    else:
        gamma += pow(2, len(zeros) - 1 - i)

print("The power consumption is", gamma * epsilon, "\b.")
