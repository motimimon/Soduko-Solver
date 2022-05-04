puzzle = [
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
def solve(puzzle):
    find = find_empty_square(puzzle)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(puzzle, i, (row, col)):
            puzzle[row][col] = i

            if solve(puzzle):
                return True

            puzzle[row][col] = 0

    return False


def valid(puzzle, num, position):
    # Check row
    for i in range(len(puzzle[0])):
        if puzzle[position[0]][i] == num and position[1] != i:
            return False

    # Check column
    for i in range(len(puzzle)):
        if puzzle[i][position[1]] == num and position[0] != i:
            return False

    # Check puzzlex
    puzzlex_x = position[1] // 3
    puzzlex_y = position[0] // 3

    for i in range(puzzlex_y*3, puzzlex_y*3 + 3):
        for j in range(puzzlex_x * 3, puzzlex_x*3 + 3):
            if puzzle[i][j] == num and (i,j) != position:
                return False

    return True

#Create a visual representation of your puzzleard

def show_puzzle(puzzle):
    for i in range(len(puzzle)):
        if i%3 == 0 and i != 0:
            print("__________________________")
        for x in range(len(puzzle[0])):
            if x % 3 == 0 and x !=0 :
                print("|", end="")
            if x == 8:
                print(puzzle[i][x])
            else:
                print(str(puzzle[i][x]) + " ", end="")

#Create a function to find the empty sqares (represented by "0")
def find_empty_square(puzzle):
    for i in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            if puzzle[i][x] == 0:
                return (i,x)
    

show_puzzle(puzzle)
solve(puzzle)
print("___________________")
show_puzzle(puzzle)
