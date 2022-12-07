import math

text = open("day7/input7.txt", "r")

L = text.readline().split(',')

product = 1.0
fuel = 0

for i in L:
    if i != '0':
        product *= int(i)
        print(product)

result = math.floor(pow(product, 1 / len(L)))

for i in L:
    fuel += abs(int(i) - result)


print("The horizontal position is", result, "\b, the crabs will have to use", fuel, "fuel to get there.")