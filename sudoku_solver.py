# 1. Pick an empty space (0 means empty)
# 2. try all numbers
# 3. Once a number works, move to the next
# 4. Repeat
# 5. Backtrack

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
# Printing board function
def print_board(boar):
# Everytime on third row we print horizontal line
    for i in range(len(boar)):
        if i % 3==0 and i != 0:
            print("- - - - - - - - - - - -  ")
# For every position on the row we will check 
# if it is the third element and draw an horizontal line
        for j in range(len(boar[0])):
            if j % 3 == 0 and j!= 0:
                print(" | ", end="") # end="" basically means stay on the same line

# Checking if we are at the last position

            if j == 8:
                print(boar[i][j])
            else:
                print(str(boar[i][j]) + " ", end="")

# Pick an empty square
def find_empty(boar):
    for i in range(len(boar)):
        for j in range(len(boar[0])):
            if boar[i][j] == 0:
                return (i, j) # row and column of empty space
    return None

# Checking validity of the board's point
def valid(boar, num, pos):
    # Check row
    for i in range(len(boar[0])):
        if boar[pos[0]][i] == num and pos[1] != i: # Of course after the and is there so that we ignore the number we just put in
            return False
    # Check column
    for i in range(len(boar)):
        if boar[i][pos[1]] == num and pos[0] != i: # Of course after the and is there so that we ignore the number we just put in
            return False
    # Check the 3x3 cubes
    box_x = pos[1] // 3   # top left box will be (0,0), mid-top (1,0) etc
    box_y = pos[0] // 3   # Values can go from 0 to 2

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if boar[i][j] == num and (i, j) != pos:
                return False
    return True

# Backtracking algorithm (is recursive, it calls itself)
def solve(boar):

    find = find_empty(boar)
    if not find:
        return True
    else:
        row, col = find
    # loop through 1 to 10 and add them to the first empty, then check if they are valid
    for i in range(1,10):
        if valid(boar, i, (row, col)):
            boar[row][col] = i
        # Keep calling itself until it is solved that will return true
            if solve(boar):
                return True
        # if the program gets here it resets the value since it was not the right one
            boar[row][col] = 0
    return False

print_board(board)
solve(board)
print("_______________________________")
print_board(board)

