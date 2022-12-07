input = open("day3/input3.txt", "r")

L_oxy = input.readlines()
L_co2 = list(L_oxy)

oxy = 0
co2 = 0

idx = 0

look = ''
 
while(len(L_oxy) > 1):
    zeros = 0
    ones = 0
    for i in L_oxy:
        if i[idx] == '0':
            zeros += 1
        else:
            ones += 1
    L_oxy2 = []
    if zeros > ones:
        look = '0'
    else:
        look = '1'
    for i in L_oxy:
        if i[idx] == look:
            L_oxy2.append(i)
    idx += 1
    L_oxy = L_oxy2

idx = 0

while(len(L_co2) > 1):
    zeros = 0
    ones = 0
    for i in L_co2:
        if i[idx] == '0':
            zeros += 1
        else:
            ones += 1
    L_co22 = []
    if zeros > ones:
        look = '1'
    else:
        look = '0'
    for i in L_co2:
        if i[idx] == look:
            L_co22.append(i)
    idx += 1
    L_co2 = L_co22

for i in range(0, len(L_oxy[0]) - 1):
    oxy += int(L_oxy[0][i]) * pow(2, len(L_oxy[0]) - 2 - i)
    co2 += int(L_co2[0][i]) * pow(2, len(L_oxy[0]) - 2 - i)

print("The life support rating of the submarine is", oxy * co2, "\b.")
