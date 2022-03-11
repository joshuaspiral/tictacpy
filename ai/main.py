import math
board = [[' ' for _ in range(3)] for x in range(3)]
ai = 'O'
human = 'X'

def best_move(board, maximising_player):
    best_score = -math.inf
    best_move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = ai
                score = minimax(board, maximising_player)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move
                    

def minimax(board, maximising_player):
    print(board)
    if check_for_win(board) == ai:
        return 1

    if maximising_player:
        best_value = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = ai
                    value = minimax(board, False)
                    best_value = min(value, best_value)
        return best_value
    else:
        best_value = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = ai
                    value = minimax(board, True)
                    best_value = max(value, best_value)
        return best_value

    return 1 
def print_board():
    for i in board:
        print('-'*13)
        for j in i:
            print('|', end=' ')
            print(j, end=' ')
        print('|', end='')
        print()
    print('-'*13)

def check_for_win(board):
    print('checking')

    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2]) and board[i][0] != ' ':
            return board[i][0]

    for i in range(3):
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i]) and board[0][i] != ' ':
            return board[0][i]

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != ' ':
        return board[0][0]

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) and board[0][2] != ' ':
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

    winner = check_for_win(board)
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

    y, x = best_move(board, True)
    board[y][x] = ai
