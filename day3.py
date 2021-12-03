#Check Most Common
from io import StringIO


def mostCommon(list):
    countZ = 0
    countO = 0
    for l in list:
        l = int(l)
        if l == 0:
            countZ = countZ + 1
        if l == 1:
            countO = countO + 1
    if countZ > countO:
        return 0
    if countO > countZ:
        return 1
    return 2

#Check Least Common
def leastCommon(list):
    countZ = 0
    countO = 0
    for l in list:
        l = int(l)
        if l == 0:
            countZ = countZ + 1
        if l == 1:
            countO = countO + 1
    if countZ > countO:
        return 1
    if countO > countZ:
        return 0
    return 2

#Add Up The Binary
def addUp(list):
    sum = 0
    if list[0] == 1:
        sum = sum + 2048
    if list[1] == 1:
        sum = sum + 1024
    if list[2] == 1:
        sum = sum + 512
    if list[3] == 1:
        sum = sum + 256
    if list[4] == 1:
        sum = sum + 128
    if list[5] == 1:
        sum = sum + 64
    if list[6] == 1:
        sum = sum + 32
    if list[7] == 1:
        sum = sum + 16
    if list[8] == 1:
        sum = sum + 8
    if list[9] == 1:
        sum = sum + 4
    if list[10] == 1:
        sum = sum + 2
    if list[11] == 1:
        sum = sum + 1
    return sum

#Update List
def updateList(list, position, accept):
    updated = []
    for l in list:
        if int(l[position]) == accept:
            updated.append(l)
    return updated

#Find the Rating
def getRating(data, c):
    list = []
    common = 2

    for i in range(12):
        for o in data:
            list.append(o[i])
            if c == 0:
                common = leastCommon(list)
            if c == 1:
                common = mostCommon(list)
            if common == 2:
                common = c
        data = updateList(data, i, common)
        list.clear()
        if len(data) <= 1:
            break
    
    return data[0]

#Make string into list
def listify(s):
    sList = []
    nList = []
    sList[:0] = s
    for l in sList:
        nList.append(int(l))
    return nList

#--------------------------------------------------#

#Read File
lines = []
with open('inputDay3.txt') as f:
    lines = f.read().splitlines()

#--------------------------------------------------#

#Part 1:
gamma = []
epsilon = []

list = []
for i in range(12):
    for line in lines:
        list.append(line[i])
    gamma.append(mostCommon(list))
    epsilon.append(leastCommon(list))
    list.clear()

print("Part 1: ")
print(addUp(gamma)*addUp(epsilon))

#--------------------------------------------------#

#Part 2:
oxygenGenerator = addUp(listify(getRating(lines, 1)))
co2Scrubber = addUp(listify(getRating(lines, 0)))

print("Part 2: ")
print(oxygenGenerator*co2Scrubber)
