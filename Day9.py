#Read File
#lines = [['2','1','9','9','9','4','3','2','1','0'], ['3','9','8','7','8','9','4','9','2','1'],['9','8','5','6','7','8','9','8','9','2'],['8','7','6','7','8','9','6','7','8','9'],['9','8','9','9','9','6','5','6','7','8']]

data = []
with open('inputDay9.txt') as f:
    data = f.read().splitlines()

lines = []
for d in data:
    lines.append(list(d))

#--------------------------------------------------#

def surroundings(map, row, col, count):
    curr = int(map[row][col])
    around = []
    
    if row == 0:
        around.append([map[row+1][col], row+1, col])
        if col == 0:
            around.append([map[row][col+1], row, col+1])
        elif col == len(map[row])-1:
            around.append([map[row][col-1], row, col-1])
        else:
            around.append([map[row][col+1], row, col+1])
            around.append([map[row][col-1], row, col-1])
    elif row == len(map)-1:
        around.append([map[row-1][col], row-1, col])
        if col == 0:
            around.append([map[row][col+1], row, col+1])
        elif col == len(map[row])-1:
            around.append([map[row][col-1], row, col-1])
        else:
            around.append([map[row][col+1], row, col+1])
            around.append([map[row][col-1], row, col-1])
    elif col == 0:
        around.append([map[row][col+1], row, col+1])
        if row == 0:
            around.append([map[row+1][col], row+1, col])
        elif row == len(map)-1:
            around.append([map[row-1][col], row-1, col])
        else:
            around.append([map[row+1][col], row+1, col])
            around.append([map[row-1][col], row-1, col])
    elif col == len(map[row])-1:
        around.append([map[row][col-1], row, col-1])
        if row == 0:
            around.append([map[row+1][col], row+1, col])
        elif row == len(map)-1:
            around.append([map[row-1][col], row-1, col])
        else:
            around.append([map[row+1][col], row+1, col])
            around.append([map[row-1][col], row-1, col])
    else:
        around.append([map[row][col+1], row, col+1])
        around.append([map[row][col-1], row, col-1])
        around.append([map[row+1][col], row+1, col])
        around.append([map[row-1][col], row-1, col])

    check = getLeast(curr, row, col, around)

    if check[0] < curr:
        return surroundings(map, check[1], check[2], count)
    elif check[0] == 9:
        return surroundings(map, check[1], check[2]+1, count)
    elif check[0] == curr:
        return check

def getLeast(curr, currX, currY, around):
    r = [curr, currX, currY]
    
    for a in around:
        i = int(a[0])
        if i < r[0]:
            r = [i, a[1], a[2]]

    return r

#basins = {}
#basin = []
#visited = []
#def getBasinE(point):
#    visited.append(point)
#    getBasinN(point)
#    getBasinS(point)
#    getBasinW(point)
#    if point[2] < len(lines[0])-1:
#        p = lines[point[1]][point[2]+1]
#        if p != '9':
#            basin.append(p)
#            visited.append(point)
#            getBasinE([p, point[1], point[2]+1])
            
#def getBasinW(point):
#    if point[2] > 0:
#        p = lines[point[1]][point[2]-1]
#        if p != '9':
#            basin.append(p)
#            getBasinW([p, point[1], point[2]-1])
#def getBasinN(point):
#    if point[1] < len(lines)-1:
#        p = lines[point[1]-1][point[2]]
#        if p != '9':
#            basin.append(p)
#            getBasinN([p, point[1]-1, point[2]])
#def getBasinS(point):
#    if point[1] > 0:
#        p = lines[point[1]+1][point[2]]
#        if p != '9':
#            basin.append(p)
#            getBasinS([p, point[1]+1, point[2]])

#def getBasins(point):
#    strPoint = str(point[0]) + str(point[1]) + str(point[2])
#    getBasinE(point)
#    basins[strPoint] = basin
    

#--------------------------------------------------#

#Gather The Low Points
lowPoints = []
for y in range(0, len(lines)-1):
    for x in range(0, len(lines[0])-1):
        trackMe = str(lines[y][x]) + str(y) + str(x)
        point = surroundings(lines, y, x, trackMe)
        if point not in lowPoints:
            lowPoints.append(point)

#Sum Of The Lowest Points
sum = 0
for point in lowPoints:
    sum = sum + (point[0]+1)

#Get the basins of low points
#for point in lowPoints:
    #basin = []
    #getBasins(point)
#getBasins(lowPoints[1])

print("Part 1: " + str(sum))
#print("Part 2: " + str(product))

#print(str(l1) + " " + str(l2) + " " + str(l3))

#Printing The Test
#for y in range(0, len(lines)):
#    for x in range(0, len(lines[0])):
#        point = [int(lines[y][x]), y, x]
#        if point in lowPoints:
#            print("\033[91m" + str(point[0]) + "\033[0m", end=" ")
#        else: 
#            print(lines[y][x], end=" ")
#    print()
#    print()