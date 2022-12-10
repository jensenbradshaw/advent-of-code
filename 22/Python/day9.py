class Knot:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.parent = None
        self.child = None
        if name == 'T':
            self.visited_nodes = {(0, 0)}

    def addChild(self, child):
        self.child = child
        child.parent = self

    def updateKnot(self):
        '''Updates a knot's position based on where it's parent has moved to,
        and then if the knot has a child, updates that child's position. If the
        knot does not have a child it is the tail and the new position is added
        to the set of visited nodes.'''
        # Left
        if self.parent.x - self.x == -2 and self.parent.y == self.y:
            self.x -= 1
        # Right
        elif self.parent.x - self.x == 2 and self.parent.y == self.y:
            self.x += 1
        # Up
        elif self.parent.y - self.y == 2 and self.parent.x == self.x:
            self.y += 1
        # Down
        elif self.parent.y - self.y == -2 and self.parent.x == self.x:
            self.y -= 1
        # Up-Left
        elif ((self.parent.x - self.x) == -2 and (self.parent.y - self.y == 1 or self.parent.y - self.y == 2)) or (self.parent.x - self.x == -1 and self.parent.y - self.y == 2):
            self.x -= 1
            self.y += 1 
        # Up-Right
        elif ((self.parent.x - self.x) == 2 and (self.parent.y - self.y == 1 or self.parent.y - self.y == 2)) or (self.parent.x - self.x == 1 and self.parent.y - self.y == 2):
            self.x += 1
            self.y += 1
        # Down-Left
        elif ((self.parent.x - self.x) == -2 and (self.parent.y - self.y == -1 or self.parent.y - self.y == -2)) or (self.parent.x - self.x == -1 and self.parent.y - self.y == -2):
            self.x -= 1
            self.y -= 1
        # Down-Right
        elif ((self.parent.x - self.x) == 2 and (self.parent.y - self.y == -1 or self.parent.y - self.y == -2)) or (self.parent.x - self.x == 1 and self.parent.y - self.y == -2):
            self.x += 1
            self.y -= 1 

        if self.child is not None:
            if abs(self.child.x - self.x) > 1 or abs(self.child.y - self.y) > 1:
                self.child.updateKnot()
        else:
            self.visited_nodes.add((self.x, self.y))
            

class Head(Knot):
    def moveHead(self, direction, amount):
        '''Takes in the direction to move and how many times to move, moves the
        head of the knot that direction and then updates the child knot.'''
        for i in range(int(amount)):
            if direction == 'L':
                self.x -= 1
                if abs(self.child.x - self.x) > 1:
                    self.child.updateKnot()
            elif direction == 'R':
                self.x += 1
                if abs(self.child.x - self.x) > 1:
                    self.child.updateKnot()
            elif direction == 'U':
                self.y += 1
                if abs(self.child.y - self.y) > 1:
                    self.child.updateKnot()
            elif direction == 'D':
                self.y -= 1
                if abs(self.child.y - self.y) > 1:
                    self.child.updateKnot()
        
def openFile(filename):
    '''Takes in a string containing a file name, returns an array of the lines
    of the file.'''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines

def makeRope(part2):
    '''Takes in whether or not it's part 2 and returns the head of a rope which
    is 2 or 10 knots long.'''
    knot_H = Head('H')
    if not part2:
        knot_T = Knot('T')
        knot_H.addChild(knot_T)
    else:
        knot_1 = Knot('1')
        knot_H.addChild(knot_1)
        knot_2 = Knot('2')
        knot_1.addChild(knot_2)
        knot_3 = Knot('3')
        knot_2.addChild(knot_3)
        knot_4 = Knot('4')
        knot_3.addChild(knot_4)
        knot_5 = Knot('5')
        knot_4.addChild(knot_5)
        knot_6 = Knot('6')
        knot_5.addChild(knot_6)
        knot_7 = Knot('7')
        knot_6.addChild(knot_7)
        knot_8 = Knot('8')
        knot_7.addChild(knot_8)
        knot_T = Knot('T')
        knot_8.addChild(knot_T)

    return knot_H

def solution(moves, part2):
    '''Takes in an array of strings representing head movement and whether or
    not it's part 2, returns the number of spaces that have been visited by the
    tail knot of the rope.'''
    head = makeRope(part2)
    
    tail = head
    while tail.child:
        tail = tail.child

    for move in moves:
        direction, amount = move.split()
        
        head.moveHead(direction, amount)

    return len(tail.visited_nodes)

f = openFile('day9.txt')

print("Solution 1:", solution(f, False))
print("Solution 2:", solution(f, True))