text = open("day6/input6.txt", "r")

L = text.readline().split(",")
fish = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0}

for i in L:
    fish[int(i)] += 1

n = int(input("Unesite broj dana: "))

for i in range(n):
    tmp = fish[0]
    for j in range(8):
        fish[j] = fish[j + 1]
    fish[6] += tmp
    fish[8] = tmp

print("After", n, "days, there will be", sum(fish.values()), "lanternfish.")