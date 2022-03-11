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
    print('checking')

    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2]) and board[i][0] != ' ':
            print('row win')
            return board[i][0]

    for i in range(3):
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i]) and board[0][i] != ' ':
            print('col win')
            return board[0][i]

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != ' ':
        print('primary diag win')
        return board[0][0]

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) and board[0][2] != ' ':
        print('secondary diag win')
        return board[0][2]


def check_for_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def handle_turn(player):
    print_board()
    print(f"{player}, input the row and column of your move in this format: `row col`")
    print()
    inp = input().split()
    row, col = int(inp[0]), int(inp[1])
    board[row][col] = player
    print_board()
    print(row, col)
    print(board[row][col])

    winner = check_for_win()
    if winner == 'X':
        print("X wins.")
        return True
    elif winner == 'O':
        print("O wins.")
        return True

    if check_for_draw():
        print("DRAW")
        return True

    return False

while True:
    if handle_turn('X'):
        print_board()
        break
    if handle_turn('O'):
        print_board()
        break
