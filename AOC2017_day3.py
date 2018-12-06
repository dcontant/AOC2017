from itertools import cycle
from math import ceil
import pprint

def out_spiral(n):
    '''
    create a n*n matrix with outward clockwise spiral of integers starting at the center with 1 up to n*n
    '''
    if n%2==0:
        return 'ERROR: n must be odd'
    global x, y, direction, matrix
    matrix = [[0]* n for row in range(n)]
    # center of spiral, n must be odd
    x,y  = n//2, n//2
    matrix[x][y] = 1
    direction = (-1,0)  # north
    headings = cycle([(0,1),(1,0),(0,-1),(-1,0)]) # east,south,west,north
    
    def move(n):
        global x,y,matrix
        x += direction[0]
        y += direction[1]
        matrix[x][y] = n
             
    def turn_clockwise():
        global direction
        direction = next(headings)
        
    i = 2
    for j in range(n):
        for k in range(2):
            for l in range(j+1):
                if i > n*n:
                    break
                move(i)
                i += 1
            turn_clockwise()
    return matrix



def out_spiral_2(n, target):
    '''
    create a n*n matrix, with outward clockwise spiral of integers starting at the center with 1 up to n*n
    each cell is the sum of adjacent cell AT THE TIME OF CREATION
    it returns a cell when it is superior to target
    '''
    if n%2 == 0:
        n += 1
    global x, y, direction, matrix
    matrix = [[0]* n for row in range(n)]
    # center of spiral, n must be odd
    x,y  = n//2, n//2
    matrix[x][y] = 1
    direction = (-1,0)  # north
    headings = cycle([(0,1),(1,0),(0,-1),(-1,0)]) # east,south,west,north
    
    def move(n):
        global x,y,matrix
        x += direction[0]
        y += direction[1]
        surrounding_total = sum(matrix[x-1][y-1:y+2]) + sum(matrix[x][y-1:y+2]) + sum(matrix[x+1][y-1:y+2])
        matrix[x][y] = surrounding_total
        return surrounding_total
        
             
    def turn_clockwise():
        global direction
        direction = next(headings)
        
    i = 2
    for j in range(n):
        for k in range(2):
            for l in range(j+1):
                if i > n*n:
                    break
                current = move(i)
                if current > target:
                    pprint.pprint(matrix)
                    return current
                i += 1
            turn_clockwise()
    return matrix




def find_distance(a,b):
    n = ceil(max(a,b)**0.5)
    if n%2 == 0:
        n += 1
    matrix = out_spiral(n)
    for i, row in  enumerate(matrix):
        try:
            a_coordinates = (i, row.index(a))
        except ValueError:
            pass
        try:
            b_coordinates = (i, row.index(b))
        except ValueError:
            pass
    return abs(a_coordinates[0] - b_coordinates[0]) + abs(a_coordinates[1] - b_coordinates[1])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"
    print('all good')
                

print('part 1:', find_distance(1,289326))
print('part 2:', out_spiral_2(10,289326))
    
