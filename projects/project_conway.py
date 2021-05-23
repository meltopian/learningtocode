# Typically two arrays are used, one to hold the current generation
# and one in which to calculate its successor.
# For outside the array, the easiest way to program it is 
# to assume that every cell outside the array is dead
# You could also have the sides and top/bottom connect pacman style


# x = 3
# y = 3
# grid = [" "] * (x * y)
# print(grid)

# Current issues:
# can't cope with more than single digit x/y
# can't cope with more than one comment at the top

'''
---What to do--
If line 1 starts with '#', ignore (add more rules later)
Use line 2 to create x and y variables
Use x and y variables to create an array (x * y)
Fill array using line 3
Print array as ascii text
'''

def makegrid(query):
    x = int(query[4])
    y = int(query[11])
    count = 0
    grid = []
    while count < y:
        grid += [["."] * x]
        count += 1
    return grid, x, y

def conformdata(data):
    count = 0
    newdata = ''
    while count < len(data):
        if data[count].isdigit():
            newdata += data[count + 1] * int(data[count])
            count += 2
        else: 
            newdata += data[count]
            count += 1
    return newdata

def fill_grid(grid, data, x, y):
    # https://codereview.stackexchange.com/questions/2303/python-implementation-of-a-wrapped-conways-game-of-life-board
    '''
    <run_count><tag>
    <run_count> - number of occurances
    <tag> - type of cell
    Run count can be omitted if equal to one
    Last item is followed by a !
    Characters after ! are ignored
    b - dead cell
    o - alive cell
    $ - end of line
    Example - bo$2bo$3o!
    Conformed example - bo$bbo$ooo!
    dead alive dead
    dead dead alive
    alive alive alive
    # '''
    data = conformdata(data)
    currentrow = 0
    currentcol = 0
    for i in data:
        if i == '!':
            break
        if i == '$':
            currentrow += 1
            currentcol = 0
        if i == 'b':
            # grid[currentrow][currentcol] = '.'
            currentcol += 1
        if i == 'o':
            grid[currentrow][currentcol] = '#'
            currentcol += 1
        if currentcol > y:
            break
        if currentrow > x:
            break
    return grid
    
def parse_conway(array):
    firstline = 0
    secondline = 1
    # print (array[0][0])
    if array[0][0] == '#':
        firstline = 1
        secondline = 2
    blankgrid, x, y = makegrid(array[firstline])
    grid = fill_grid(blankgrid, array[secondline], x, y)
    return grid

def read_in_file():
    newlist = []
    with open("c:/codelessons/learningtocode/projects/project_conway_example_2.txt", 'r') as file:
        for line in file:
            newlist.append(line.strip())
    return newlist

def render(grid):
   for i in grid:
        print (''.join(i))

conwaytoconvert = read_in_file()
convertedgrid = parse_conway(conwaytoconvert)
render(convertedgrid)

# rle_example = '''
# #C This is a glider.
# x = 3, y = 3
# bo$2bo$3o!
# '''

#rle_list = plaintext_to_list(rle_example)
#print(parse_conway(rle_list))
#print(rle_example)
#print(rle_list)