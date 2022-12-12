import numpy as np

def openFile(filename):
    '''Takes in a string containing a file name, returns an array of the lines
    of the file.'''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines

def parseGridForVisibility(tree_grid, visibility_grid):
    '''Takes in a 2d array representing tree heights and a 2d array representing
    their visibility scores, returns them after parsing from left and right.'''
    number_of_rows = len(tree_grid)
    number_of_columns = len(tree_grid[0])

    for i in range(number_of_rows):
        highest_left = 0
        highest_right = 0

        for j in range(number_of_columns):
            if (tree_grid[i][j] > highest_left) or (j == 0):
                visibility_grid[i][j] = 1
                highest_left = tree_grid[i][j]

            if (tree_grid[i][-(j+1)] > highest_right) or (j == 0):
                visibility_grid[i][-(j+1)] = 1
                highest_right = tree_grid[i][-(j+1)]
    
    return visibility_grid

def parseGridForScenic(tree_grid, scenic_grid):
    '''Takes in a 2d array representing tree heights and a 2d array representing
    their scenic scores, returns them after parsing from the left and right.'''
    number_of_rows = len(tree_grid)
    number_of_columns = len(tree_grid[0])

    for i in range(number_of_rows):
        for j in range(number_of_columns):
            scenic_sum = 0

            for k in range(j-1, -1, -1):
                scenic_sum += 1
                if tree_grid[i][j] <= tree_grid[i][k]:
                    break

            scenic_grid[i][j] *= scenic_sum

            scenic_sum = 0

            for k in range(j+1, number_of_columns):
                scenic_sum += 1
                if tree_grid[i][j] <= tree_grid[i][k]:
                    break

            scenic_grid[i][j] *= scenic_sum

    return scenic_grid

def solution(lines, part2):
    '''Takes in an array containing the lines of the files and whether or not
    it's part 2, returns either the total visibility score of the forest or the
    highest scenic score possible of a tree.'''
    tree_grid = np.array([[int(value) for value in line[:-1]] for line in lines])

    if not part2:
        visibility_grid = np.array([[0 for value in line[:-1]] for line in lines])

        visibility_grid = parseGridForVisibility(tree_grid, visibility_grid)
        # Transpose to parse up and down
        visibility_grid = parseGridForVisibility(tree_grid.T, visibility_grid.T)

        visibility_sum = 0
        for row in visibility_grid:
            for value in row:
                visibility_sum += value

        return visibility_sum
    
    else:
        scenic_grid = np.array([[1 for value in line[:-1]] for line in lines])

        scenic_grid = parseGridForScenic(tree_grid, scenic_grid)
        # Transpose to parse up and down
        scenic_grid = parseGridForScenic(tree_grid.T, scenic_grid.T)

        highest_scenic = 0
        for row in scenic_grid:
            for value in row:
                if value > highest_scenic:
                    highest_scenic = value

        return highest_scenic

f = openFile('day8.txt')

print("Solution 1:", solution(f, False))
print("Solution 2:", solution(f, True))