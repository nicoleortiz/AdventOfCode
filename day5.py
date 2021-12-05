#Read File
lines = []

with open('inputDay5.txt') as f:
    fileLines = f.read().splitlines()

    tempLine = []
    for fl in fileLines:
        temp = fl.split()
        for t in temp:
            if ',' in t:
                tempLine.append(t.split(','))
        lines.append(tempLine)
        tempLine = []

#--------------------------------------------------#
def printField():
    for row in field:
        print(row)

def makeField():
    field = [[0]* 1000 for i in range(1000)]
    return field

field = makeField()

def mark(a, b):
    if field[a][b] > 0:
        field[a][b] = field[a][b] + 1
    else:
       field[a][b] = 1

def drawLine(axis, axisP, begin, end):
    if end < begin:
        t = begin
        begin = end
        end = t
    if axis == 'x':
        while begin <= end:
            mark(begin, axisP)
            begin = begin+1
    if axis == 'y':
        while begin <= end:
            mark(axisP, begin)
            begin = begin+1

def diagonal(x1, y1, x2, y2):
    if x1 < x2 and y1 < y2:
        while x1 <= x2:
            mark(x1, y1)
            x1 = x1+1
            y1 = y1+1
    elif x1 > x2 and y1 < y2:
        while x1 >= x2:
            mark(x1, y1)
            x1 = x1-1
            y1 = y1+1
    elif x1 < x2 and y1 > y2:
        while x1 <= x2:
            mark(x1, y1)
            x1 = x1+1
            y1 = y1-1
    elif x1 > x2 and y1 > y2:
        while x1 >= x2:
            mark(x1, y1)
            x1 = x1-1
            y1 = y1-1

def line(points):
    p1a = int(points[0][0])
    p1b = int(points[0][1])
    p2a = int(points[1][0])
    p2b = int(points[1][1])

    if p1a == p2a:
        drawLine('y', p1a, p1b, p2b)
    elif p1b == p2b:
        drawLine('x', p1b, p1a, p2a)
    else:
        diagonal(p1a, p1b, p2a, p2b)

def overlap():
    c = 0
    for row in field:
        for p in row:
            if p >= 2:
                c = c+1
    return c
#--------------------------------------------------#

for p in lines:
    line(p)

#Part 1 : comment out else: diagonal in line() & replace with idk print(diagonal)

print(overlap())
