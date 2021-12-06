#Read File
lines = []
with open('inputDay6.txt') as f:
    lines = f.read().split(',')

#fish = [3,4,3,1,2]
fish = []
for l in lines:
    fish.append(int(l))

#--------------------------------------------------#

#Part 1:

def newDay(f):
    if f==0:
        newFish()
        return 6
    else:
        return f-1

babyFish = []
def newFish():
    babyFish.append(8)

def part1():
    days = 18
    counter = 0
    while days > 0:
        for f in fish:
            fish[counter] = newDay(f)
            counter = counter+1
        for b in babyFish:
            fish.append(b)
        babyFish = []
        counter = 0
        days = days-1

    print(len(fish))

#--------------------------------------------------#

#Part 2:
c = [0,0,0,0,0,0,0,0,0]

for f in fish:
    if f==1:
        c[1] = c[1]+1
    if f==2:
        c[2] = c[2]+1
    if f==3:
        c[3] = c[3]+1
    if f==4:
        c[4] = c[4]+1
    if f==5:
        c[5] = c[5]+1
    if f==6:
        c[6] = c[6]+1
    if f==7:
        c[7] = c[7]+1
    if f==8:
        c[8] = c[8]+1

days = 256
while days > 0:
    hold = c[0]
    for i in range(0,8):
        c[i] = c[i+1]
    c[8] = hold
    c[6] = c[6]+hold
    days = days-1
    
sum = 0
for f in c:
    sum = sum + f

print(sum)