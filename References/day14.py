#Read File
begin = ''
insertionRules = {}

with open('testInput.txt') as f:
    fileLines = f.read().splitlines()

    begin = fileLines[0]
    for fl in fileLines:
        if '->' in fl:
            temp = fl.split(' ')
            insertionRules[temp[0]] = temp[2]

#--------------------------------------------------#

#Part 1
template = begin

def getResult():
    temp = template[0]

    for pair in ([template[i: i + 2] for i in range(len(template) + 1 - 2)]):
        if pair in insertionRules:
            temp += insertionRules[pair] + pair[1]
    
    return temp

def mostMinusLeast():
    freq = {}
    for i in template:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    m = freq[max(freq, key = freq.get)]
    l = freq[min(freq, key = freq.get)]
    diff = m - l
    print(str(m) + " - " + str(l) + " = " + str(diff))

for i in range(0, 10):
    template = getResult()

print("Part 1: ")
mostMinusLeast()

#--------------------------------------------------#

#Part 2
template = begin

pairs = {}
def getPairs(it):
    for i in range(0, len(template)-1):
        p = template[i] + template[i+1]
        if p in pairs:
            pairs[p] += 1
        else:
            pairs[p] = 1
    
    for i in range(0, it):
        nP = []
        for pair in pairs:
            insert = insertionRules[pair]
            nP.append(pair[0] + insert)
            nP.append(insert + pair[1])
        for p in nP:
            if p in pairs:
                pairs[p] += 1
            else:
                pairs[p] = 1

def getLetters():
    letters = {}
    for pair in pairs:
        p = pair[0]
        if p in letters:
            letters[p] += pairs[pair]
        else:
            letters[p] = pairs[pair]

        p = pair[1]
        if p in letters:
            letters[p] += pairs[pair]
        else:
            letters[p] = pairs[pair]

    letters[list(letters.keys())[0]] += pairs[list(pairs.keys())[0]]
    letters[list(letters.keys())[len(letters)-1]] += pairs[list(pairs.keys())[0]]
    return letters


getPairs(10)
print(pairs)
letters = getLetters()
print(letters)
print("Part 2: ")
print(str(letters[max(letters, key = letters.get)])
         + " - " 
         + str(letters[min(letters, key = letters.get)])
         + " = " 
         + str(letters[max(letters, key = letters.get)]
             - letters[min(letters, key = letters.get)]))