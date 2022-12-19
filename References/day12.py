from collections import defaultdict

edges0 = ['start-A',
        'start-b',
        'A-c',
        'A-b',
        'b-d',
        'A-end',
        'b-end']

edges1 = ['dc-end',
        'HN-start',
        'start-kj',
        'dc-start',
        'dc-HN',
        'LN-dc',
        'HN-end',
        'kj-sa',
        'kj-HN',
        'kj-dc']

edges2 = ['fs-end',
        'he-DX',
        'fs-he',
        'start-DX',
        'pj-DX',
        'end-zg',
        'zg-sl',
        'zg-pj',
        'pj-he',
        'RW-he',
        'fs-DX',
        'pj-RW',
        'zg-RW',
        'start-pj',
        'he-WI',
        'zg-he',
        'pj-fs',
        'start-RW']

edges = ['ey-dv',
        'AL-ms',
        'ey-lx',
        'zw-YT',
        'hm-zw',
        'start-YT',
        'start-ms',
        'dv-YT',
        'hm-ms',
        'end-ey',
        'AL-ey',
        'end-hm',
        'rh-hm',
        'dv-ms',
        'AL-dv',
        'ey-SP',
        'hm-lx',
        'dv-start',
        'end-lx',
        'zw-AL',
        'hm-AL',
        'lx-zw',
        'ey-zw',
        'zw-dv',
        'YT-ms']

#--------------------------------------------------#

connections = defaultdict(list)
def getConns():
    for c in edges:
        line = c.split('-')
        connections[line[0]].append(line[1])
        connections[line[1]].append(line[0])
getConns()

verts = connections.keys()

global counter
counter = 0
def getAllPaths(start, end, visited, path):
    global counter

    visited[start] = True

    if start.isupper(): #UpperCase can always be visiter
        visited[start] = False

    path.append(start)

    if start == end:
        #print(path) 
        counter += 1
    else:
        for i in connections[start]:
            if visited[i] == False:
                getAllPaths(i, end, visited, path)
    path.pop()
    visited[start]= False

def printAllPaths(start, end):
    visited = {}
    for v in verts:
        visited[v] = False
    path = []
    getAllPaths(start, end, visited, path)

printAllPaths('start','end')
print(counter)

#--------------------------------------------------#

#Part 2 Solution: https://dev.to/qviper/advent-of-code-2021-python-solution-day-12-3b40

class Solver:
    def __init__(self, paths):
        self.paths = paths
        self.visited = set()

        print(self.solve(part="1"))
        print(self.solve(part="2"))

    def solve(self, curr_cave="start", part="1"):
        if (curr_cave=="end"):
            return 1
        if curr_cave.islower():
            self.visited.add(curr_cave)

        ways_count = sum([self.solve(cave, part) for cave in self.paths[curr_cave] if cave not in self.visited])
        ways_count += 0 if part!="2" else sum([self.solve(cave, cave) for cave in self.paths[curr_cave] if cave in self.visited and cave != "start"])

        if (curr_cave != part): self.visited.discard(curr_cave)
        return ways_count

s = Solver(connections)