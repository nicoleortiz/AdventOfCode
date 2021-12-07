#Read File
lines = []
with open('inputDay7.txt') as f:
    lines = f.read().split(',')

#initial = [16,1,2,0,4,2,7,1,2,14]
initial = []
for l in lines:
    initial.append(int(l))
initial.sort()

#--------------------------------------------------#

fuelUsed = []

def checkFuel_Const():
    sum=0
    for position in range(0,len(initial)):
        for sub in initial:
            sum = sum + abs(sub-position)
        fuelUsed.append(sum)
        sum = 0

def checkFuel_Incr():
    sum=0
    for position in range(0,len(initial)):
        for sub in initial:
            if sub < position:
                sum = sum + incr(sub, position)
            if sub > position:
                sum = sum + incr(position, sub)
        fuelUsed.append(sum)
        sum = 0

def incr(a, b):
    sum = 0
    c = 1
    while a < b:
        sum = sum + c
        c = c + 1
        a = a + 1
    return sum

def getLowest():
    fuelUsed.sort()
    print(fuelUsed[0])

#--------------------------------------------------#

#Part 1:
def part1():
    checkFuel_Const()
    getLowest()

#Part 2:
def part2():
    checkFuel_Incr()
    getLowest()

part2()