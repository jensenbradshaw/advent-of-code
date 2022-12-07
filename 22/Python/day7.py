class FSItem():

    def __init__(self, name, size=0):
        '''Takes in a string containing the object's name and an int containing
        the object size and assigns them to the object as well as setting the
        object's parent to None.'''
        self.name = name
        self.size = size
        self.parent = None

class Dir(FSItem):

    def __init__(self, name):
        '''Takes in a string containing the object's name, initiliases it as an
        FSItem and assigns the object an empty list of Children.'''
        FSItem.__init__(self, name)
        self.children = []
        self.lessThan100001 = True

    def increaseSize(self, size):
        '''Takes in an int containing a child's size and increases the object's
        size by it. Also modifies global sumSolution.'''
        global sumSolution
        self.size += size

        if self.lessThan100001:
            if self.size < 100000:
                sumSolution += size
            else:
                self.lessThan100001 = False
                sumSolution -= (self.size - size)

        if self.parent is not None:
            self.parent.increaseSize(size)

    def addChild(self, child):
        '''Takes in an object and appends it to a list of the object's children.
        '''
        self.children.append(child)
        child.parent = self
        self.increaseSize(child.size)

    def findChild(self, name):
        '''Takes in a string containing the name of a child, returns the child.
        '''
        for child in self.children:
            if child.name == name:
                return child

    def freeSpace(self, neededSpace, bigDir=70000000):
        '''Takes in an int representing needed space on the root, returns
        smallest dir that is at least neededSpace big.'''
        self.bigDir = bigDir

        if self.bigDir > self.size > neededSpace:
            self.bigDir = self.size

            for child in self.children:
                if type(child) == Dir:
                    self.bigDir = child.freeSpace(neededSpace, self.bigDir)

        return self.bigDir

    def showChildren(self, tab=0, showSelf=True):
        '''Takes in an int containing how deep we are and a bool representing
        if we want to show the current object and prints out the tree from this
        item down.'''
        if showSelf:
            print('-', self.name, "(dir, size=" + str(self.size) + ')')
        for child in self.children:
            if type(child) == Dir:
                print("  "*tab + '-', child.name, "(dir, size=" + str(child.size) + ')')
                child.showChildren((tab+1), False)
            else:
                print("  "*tab + '-', child.name, "(file, size=" + str(child.size) + ')')

def openFile(filename):
    '''Takes in a string containing a file name, returns an array of the lines
    of the file.'''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines
    
def test():
    '''Creates a file system to test the FSItem and Dir classes.'''
    root = Dir('/')
    a = Dir('a')
    root.addChild(a)
    e = Dir('e')
    a.addChild(e)
    e.addChild(FSItem('i', 584))
    a.addChild(FSItem('f', 29116))
    a.addChild(FSItem('g', 2557))
    a.addChild(FSItem("h.list", 62596))
    root.addChild(FSItem("b.txt", 14848514))
    root.addChild(FSItem("c.dat", 8504156))
    d = Dir('d')
    root.addChild(d)
    d.addChild(FSItem('j', 4060174))
    d.addChild(FSItem("d.log", 8033020))
    d.addChild(FSItem("d.ext", 5626152))
    d.addChild(FSItem('k', 7214296))

    root.showChildren()

def buildTree(lines, showTerminal=False, showFileStructure=False):
    '''Takes in an array containing the lines of the file, whether or not you
    want to show the terminal and whether or not you want to show the file
    structure, returns the root object of the file system.'''
    global sumSolution
    sumSolution = 0
    path = ['/']
    root = Dir('/')
    item = root

    for line in lines:
        line = line[:-1].split(" ")

        if line[0] == '$':
            if line[1] == "cd":
                if line[2] == '/':
                    path = ['/']
                    item = root

                elif line[2] == "..":
                    path.pop(-1)
                    item = item.parent

                else:
                    path.append(line[2])
                    item = item.findChild(line[2])

                # Output the cd command
                if showTerminal:
                    print(path, line[0], line[1], line[2])

            # Output the ls command
            elif showTerminal:
                print(path, line[0], line[1])

        elif line[0] == "dir":
            item.addChild(Dir(line[1]))

            # Output the dir
            if showTerminal:
                print(line[0], line[1])
                
        else:
            item.addChild(FSItem(line[1], int(line[0])))

            # Output the file
            if showTerminal:
                print(line[0], line[1])

    # Output the file structure
    if showFileStructure:
        print()
        root.showChildren()

    return root

f = openFile('day7.txt')

root = buildTree(f)
print("Solution 1:", sumSolution)
print("Solution 2:", root.freeSpace(root.size - 40000000))