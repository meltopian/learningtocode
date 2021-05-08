# 2D Arrays & Algorithm Design

#     Your program should
#         Display a possible state for a game of "Connect 4" (ASCII text grid)
#         A message indicating if a player has won.
#     The game does not have to playable. 
#     It just needs to report if a player has won given a known board state.
#     For A grade, make it playable.

#     ........
#     ........
#     ..R.....
#     ..R...Y.
#     RRY.RYYR

# Connect 4 is 7x6 grid
# Each player gets a color. If 4 pieces of the same color line up 
# horizontally, vertically or diagonally, that player wins

# connect4array = [
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
# ]

def createc4array():
    newc4array = [
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0],
    ]
    return newc4array


def hasplayerwon(player, array):
    # x = 0
    # y = 0
    counter = 0
    horizontal_len = len(array[0])
    vertical_len = len(array)
    # while counter < 4:
    for i in range(vertical_len):
        for j in range(horizontal_len):
            current = array[i][j]
            # print (array[i][j])
            if array[i][j] == player:
                counter += 1
            if array[i][j] != player:
                counter = 0
    if counter >= 4:
        return True

        #     if array[x][i] == player:
        #         print(player)
        #         print('playeryo')
        #         counter += 1
            # x += 1
            # if i == player:
            #     counter += 1

def checkforwin(array):
    for i in range(1, 2):
        if hasplayerwon(i, array) == True:
            return (f'Player {i} has won')
        else:
            return ('No player has won')
        # if i == 3:
        #     return ('No player has won')


def printarray(arraytoprint):
    for i in arraytoprint:
        printthis = ''
        for j in i:
            if j == 0:
                printthis += '.'
            elif j == 1:
                printthis += 'R'
            elif j == 2:
                printthis += 'Y'
            else: 
                printthis += '.'
        print (printthis)

if __name__ == '__main__':
    connect4array = createc4array()
    printarray(connect4array)
    print (checkforwin(connect4array))