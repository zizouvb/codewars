def check(unsorted_list):
    unsorted_list.sort()
    for i in range(1,10):
        if i!=unsorted_list[i-1]:
            return False
    return True
def check_row(board,row_index):
    row = board[row_index]
    return check(row)
def check_col(board,col_index):
    col = [i[col_index] for i in board]
    return check(col)
    
def check_square(board,y,x):
    square=[board[y][x:x+3],board[y+1][x:x+3],board[y+2][x:x+3]]
    square = [num for subsquare in square for num in subsquare]
    return check(square)

def valid_solution(board):
    for col_index in range(9):
        if (not check_col(board,col_index)): return False
        if (col_index%3==0):
            for square_nb in range(3):
                if (not check_square(board,square_nb*3,col_index)): return False
    for row_index in range(9):
        if (not check_row(board,row_index)): return False
    return True
