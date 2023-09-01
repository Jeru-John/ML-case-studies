
def find_princess_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'p':
                return i, j

def find_bot_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'm':
                return i, j

def rescue_princess(grid):
    bot_position = find_bot_position(grid)
    princess_position = find_princess_position(grid)
    
    moves = []
    
    while bot_position != princess_position:
        bot_row, bot_col = bot_position
        princess_row, princess_col = princess_position
        
        if bot_row < princess_row:
            moves.append('DOWN')
            bot_row += 1
        elif bot_row > princess_row:
            moves.append('UP')
            bot_row -= 1
        
        if bot_col < princess_col:
            moves.append('RIGHT')
            bot_col += 1
        elif bot_col > princess_col:
            moves.append('LEFT')
            bot_col -= 1
        
        bot_position = (bot_row, bot_col)
    
    return moves

# Read input
N = int(input())
grid = [list(input()) for _ in range(N)] #gives a 2 dimensional list ( like a matrix )
#for _ in range(N) iterates through this sequence. The underscore _ is used as a placeholder variable when you don't need the value of the current iteration variable. It's often used when you're only interested in the iteration count.

# Solve the problem and print the moves
moves = rescue_princess(grid)
for move in moves:
    print(move)