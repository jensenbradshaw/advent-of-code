def openFile(filename):
    '''Takes in a string containing a file name,
    returns an array of the lines of the file.'''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines

def solution(line, size):
    '''Takes in a string containing the line of the file representing the
    signal, and the size of the marker, returns an int of the solution.'''
    marker = []

    for i in range(len(line)):
        if len(marker) == size:
            if len(set(marker)) == size:
                return i
                
            marker.pop(0)

        marker.append(line[i])

f = openFile('day6.txt')

print("Solution 1:", solution(f[0], 4))
print("Solution 2:", solution(f[0], 14))