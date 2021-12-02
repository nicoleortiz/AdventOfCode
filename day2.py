#Read File
lines = []
with open('inputDay2.txt') as f:
    for line in f:
        lines.append(line.strip().split(' '))

#--------------------------------------------------#

#Part 1
x = 0
y = 0

for line in lines:
    if line[0] == "forward":
        x = x + int(line[1])
    elif line[0] == "down":
        y = y + int(line[1])
    elif line[0] == "up":
        y = y - int(line[1])

horizontal = x * y

print("Part 1: ")
print(horizontal)

#--------------------------------------------------#

#Part 2
x = 0
y = 0
aim = 0

for line in lines:
    if line[0] == "forward":
        x = x + int(line[1])
        y = y + (aim * int(line[1]))
    elif line[0] == "down":
        aim = aim + int(line[1])
    elif line[0] == "up":
        aim = aim - int(line[1])

horizontal = x * y

print("Part 2: ")
print(horizontal)