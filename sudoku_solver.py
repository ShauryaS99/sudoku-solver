from sudoku_scraper import scrape

example_board = [
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

def solve(board):
    next_candidate = is_empty(board)
    if not next_candidate:
        return board
    else:
        row = next_candidate[0]
        col = next_candidate[1]
        for x in range(1,10):
            valid = validate(board, x, row, col)
            if valid:
                board[row][col] = x
                result = solve(board)
                if result:
                    return result
                else:
                    board[row][col] = 0
        return None
def validate(board, num, row, col):
    #Validate Row
    if num in board[row]:
        return False
    #Validate Col
    column_lst = get_column(board, col)
    if num in column_lst:
        return False
    #Validate Square
    square_lst = get_square(board, row, col)
    if num in square_lst:
        return False
    #Else it is Valid
    return True

def get_column(board, col):
    return [row[col] for row in board]
def get_square(board, row, col):
    #Gets Limits of Square
    row_section = int(row / 3)
    col_section = int(col / 3)
    row_lb = row_section * 3
    row_ub = row_lb + 3
    col_lb = col_section * 3
    col_ub = col_lb + 3
    #Adds Elements of Square to List
    square_lst = []
    for row in range(row_lb,row_ub):
        for col in range(col_lb, col_ub):
            square_lst.append(board[row][col])
    return square_lst

def is_empty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return (row, col)
    return None
def print_board(board):
    for row in range(len(board)):
        if row != 0 and row % 3 == 0:
            print("- - - - - - - - - - - - - ")

        for col in range(len(board[row])):
            if col != 0 and col % 3 == 0:
                print(" | ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")

#Execute Code w/ Input Board
def execute(input_board):
    dupl_board = [row[:] for row in input_board]
    print("Original Board:")
    print_board(dupl_board)
    solved_board = solve(dupl_board)
    print("\n Solved Board:")
    print_board(solved_board)

input_board = scrape()
execute(input_board)