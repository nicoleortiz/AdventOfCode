lines = ['6318185732',
        '1122687135',
        '5173237676',
        '8754362612',
        '5718474666',
        '8443654137',
        '1247634346',
        '1446514585',
        '6717288267',
        '1727871228']

lines = [[int(char) for char in line] for line in lines]

#--------------------------------------------------#

class octopus:
    def __init__(self, value):
        self.value  = value
        self.flashed = 0
    def increase(self):
        self.value += 1
        if self.value > 9 and not self.flashed:
            self.to_flash()
    def to_flash(self):
        if not self.flashed:
            self.flashed = 1
    def flash(self):
        if self.flashed == 1:
            self.flashed = 2
            return True
        else:
            return False
    def reset(self):
        if self.flashed == 2:
            self.value = 0
            self.flashed = 0
            return True
        else:
            return False

#--------------------------------------------------#

map = []
for line in lines:
    map.append([octopus(int(x)) for x in line])

width = len(map[0])
height = len(map)

flashes = 0

for step in range(1, 1001):
    for x in map:
        for y in x:
            y.increase()
    flash = True
    while flash:
        flash = False
        for xx, x in enumerate(map):
            for yy, y in enumerate(x):
                if y.flashed == 1:
                    y.flash()
                    flashes += 1
                    flash = True
                    for w in [-1, 0, 1]:
                        for h in [-1, 0, 1]:
                            if w == h == 0:
                                continue
                            if 0 <= yy + w < width and 0 <= xx + h < height:
                                map[xx+h][yy+w].increase()

    count = 0
    for a in map:
        for b in a:
            if b.reset():
                count += 1
    if count == 100:
        print("Step: " + str(step))
        break

print("Flashes: " + str(flashes))