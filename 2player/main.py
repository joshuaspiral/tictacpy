board = [[' ' for _ in range(3)] for x in range(3)]

def print_board():
    for i in board:
        print('-'*13)
        for j in i:
            print('|', end=' ')
            print(j, end=' ')
        print('|', end='')
        print()
    print('-'*13)

def check_for_win():
    columns = list(zip(*board))

    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ' ': return True
    
    for i in range(3):
        if columns[i][0] == columns[i][1] and columns[i][1] == columns[i][2] and board[i][0] != ' ': return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
        return True

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

def check_for_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def handle_turn(player):
    print_board()
    print(f"{player}, input the row of your move")
    print()
    row = int(input())
    print(f"{player}, input the column of your move")
    print()
    col = int(input())
    board[row][col] = player
    print_board()
    print(row, col)
    print(board[row][col])

    if check_for_win() == True:
        print(f"{player} wins.")
        return True

    if check_for_win() == True:
        print(f"{'O' if player == 'X' else 'X'} wins.")
        return True
        
    if check_for_draw():
        print("DRAW")
        return True
        
    return False

while True:
    if handle_turn('X'):
        break
    if handle_turn('O'):
        break
