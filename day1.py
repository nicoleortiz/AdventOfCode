#Function To Compare Data
def checkBig(list, p):
    count = 0
    prev = p
    for l in list:
        il = int(l)
        if il > prev:
            count = count+1
        prev = il
    return count

#Read File
lines = []
with open('inputDay1.txt') as f:
    lines = f.read().splitlines()

#--------------------------------------------------#

#Part 1:
print("Part 1: ")
print(checkBig(lines, 189))

#--------------------------------------------------#

#Part 2:
window = 3
groups = []
sums = []

for i in range(len(lines) - window + 1):
    groups.append(lines[i: i + window])

for group in groups:
    sum = 0
    for num in group:
        sum = sum + int(num)
    sums.append(sum)

print("Part 2: ")
print(checkBig(sums, 1000))