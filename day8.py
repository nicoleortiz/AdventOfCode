#Read File
lines = []
with open('inputDay8.txt') as f:
    for line in f:
        lines.append(line.strip().split(' | '))

signalPatterns = []
outputValues = []
for l in lines:
    signalPatterns.append(l[0].split(' '))
    outputValues.append(l[1].split(' '))

#--------------------------------------------------#

segments = [[], [], [], [], [], [], [], []]
order = ['z', 'z', 'z', 'z', 'z', 'z', 'z']
frequency = {}

def solveBasicPatterns(patterns):
    # Get Signals of 1, 4, 7, 8 (uniques)
    for p in patterns:
        p = list(p)
        p.sort()
        if len(p) == 2:
            segments[0].extend(p)
        if len(p) == 3:
            segments[6].extend(p)
        if len(p) == 4:
            segments[3].extend(p)
        if len(p) == 7:
            segments[7].extend(p)
    

def solvePatterns(patterns):
    solveBasicPatterns(patterns)
    getFrequency(patterns)

    # A --------------------------
    for i in segments[6]:
        if i not in segments[0]:
            order[0] = i
    # B --------------------------
    order[1] = frequency[6][0]
    # C --------------------------
    c = frequency[8]
    c.remove(order[0])
    order[2] = c[0]
    # E --------------------------
    order[4] = frequency[4][0]
    # F --------------------------
    order[5] = frequency[9][0]

    #DG --------------------------
    dg = frequency[7]
    if dg[0] in segments[3]:
        order[3] = dg[0]
        order[6] = dg[1]
    else:
        order[3] = dg[1]
        order[6] = dg[0]

def getFrequency(patterns):
    for i in segments[7]:
        c = 0
        for p in patterns:
            if i in p:
                c=c+1
        if c not in frequency.keys():
            frequency[c] = []
        frequency[c].append(i)
        c = 0

def matchOutput(outputs):
    values = []
    for o in outputs:
        o = list(o)
        o.sort()
        values.append(getNum(o))
    
    value = int(''.join(str(e) for e in values))
    return value

def getNum(signal):
    if signal == segments[0]:
        return 1
    if signal == segments[3]:
        return 4
    if signal == segments[6]:
        return 7
    if signal == segments[7]:
        return 8

    if order[1] in signal:
        if order[2] in signal:
            if order[3] in signal:
                return 9
            return 0
        if order[4] in signal:
            return 6
        else:
            return 5
    if order[4] in signal:
        return 2
    return 3

def getSum(values):
    sum = 0
    for v in values:
        sum = sum + v
    return sum

def getUniques(values):
    total = 0
    for value in values:
        value = list(str(value))
        for v in value:
            if '1' == v:
                total = total + 1
            if '4' == v:
                total = total + 1
            if '7' == v:
                total = total + 1
            if '8' == v:
                total = total + 1
    return total
#--------------------------------------------------#
values = []
part1Counter = 0
#conf = signalPatterns[0]

for conf in signalPatterns:
    solvePatterns(conf)
    values.append(matchOutput(outputValues[signalPatterns.index(conf)]))
    segments = [[], [], [], [], [], [], [], []]
    order = ['z', 'z', 'z', 'z', 'z', 'z', 'z']
    frequency = {}

print("Part 1: " + str(getUniques(values)))
print("Part 2: " + str(getSum(values)))



