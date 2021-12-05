#--------------------------------------------------#

#Read File
calls = []
boards = []
with open('inputDay4.txt') as f:
    lines = f.read().splitlines()

    #Grab the calls
    calls = lines[0].split(',')

    #Clean up the lines
    lines.remove(lines[0])

    #Grab the boards
    tempBoard = []
    tempLine = []
    for l in lines:
        if l == '':
            boards.append(tempBoard)
            tempBoard = []
        else:
            tempLine = l.split()
            tempBoard.append(tempLine)
    if len(tempBoard) > 0:
        boards.append(tempBoard)
    
    boards.remove(boards[0])     

#--------------------------------------------------#

#Check if there is bingo
def checkWon(board):
    if checkRows(board) == 1:
        return 1
    elif checkColumns(board) == 1:
        return 1
    else:
        return 0
def checkRows(board):
    for row in board:
        checks = 0
        for num in row:
            if num == 'X':
                checks=checks+1
        if checks == 5:
            return 1
def checkColumns(board):
    for i in range(5):
        checks = 0
        for row in board:
            if row[i] == 'X':
                checks = checks+1
        if checks == 5:
            return 1

#Check if call is in a board, replace with X
def updateBoard(val):
    countB = 0
    countR = 0
    countN = 0
    for board in boards:
        for row in board:
            for num in row:
                if num==val:
                    markX(countB, countR, countN)
                countN = countN+1
            countN = 0
            countR = countR+1
        countR = 0
        countB = countB+1
    countB = 0
def markX(b,r,n):
    boards[b][r][n] = 'X'

#Add Unmarked Numbers
def sumUnmark(board):
    sum = 0
    for row in board:
        for num in row:
            if num != "X":
                sum = sum + int(num)
    return sum

#--------------------------------------------------#

#Part 1:
b = 0
justCalled = 0
breakOut = False

for call in calls:
    b = 0
    justCalled = call
    updateBoard(call)
    
    for board in boards:
        b = b+1
        if checkWon(board) == 1:
            breakOut = True
            break
    if breakOut == True:
        break

print(sumUnmark(boards[b-1])*int(justCalled))

#--------------------------------------------------#

#Part 2:
#if its in the other list then keep going
b = 0
called = []
winners = []
boardsL = boards
cBoards = 0

for call in calls:
    b = 0
    updateBoard(call)
    
    for board in boardsL:
        b = b+1
        if checkWon(board) == 1:
            if board not in winners:
                winners.append(board)
                called.append(call)
                boardsL.remove(board)

print(sumUnmark(winners[-1])*int(called[-1]))