testlines = ['[({(<(())[]>[[{[]{<()<>>',
            '[(()[<>])]({[<{<<[]>>(',
            '{([(<{}[<>[]}>{[]{[(<()>',
            '(((({<>}<{<{<>}{[]{[]{}',
            '[[<[([]))<([[{}[[()]]]',
            '[{[{({}]{}}([{[{{{}}([]',
            '{<[[]]>}<{[{[{[]{()[[[]',
            '[<(<(<(<{}))><([]([]()',
            '<{([([[(<>()){}]>(<<{{',
            '<{([{{}}[<[[[<>{}]]]>[]]']

lines = []
with open('inputDay10.txt') as f:
    lines = f.read().splitlines()

#--------------------------------------------------#

scores={"(": 3, "[": 57, "{": 1197, "<": 25137, ")": 3, "]": 57, "}": 1197, ">": 25137}

#--------------------------------------------------#

#Part 1:

sum=0

for line in testlines:
    #print(line)
    points = [0]
    for char in line:
        if char in ("}", ")", ">", "]"):
            if points[-1] == scores[char]:
                points.pop(-1)
            else:
                sum += scores[char]
                break
        else:
            points.append(scores[char])
        #print(points)

print(sum)

#--------------------------------------------------#

#Part 2:

l = []
sc = [0, 3, 57, 1197, 25137]

for line in lines:
    points = []
    for char in line:
        if char in ("}", ")", ">", "]"):
            if points[-1] == scores[char]:
                points.pop(-1)
            else:
                break
        else:
            points.append(scores[char])

    else:
        o = 0
        for char in points[::-1]:
            o *= 5
            o += sc.index(char)
        l.append(o)

l = sorted(l)
print(l[len(l)//2])