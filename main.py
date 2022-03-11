board = [[x for x in range(3)] for _ in range(3)]
for i in range(9):
    board[i // 3][i % 3] = i + 1

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
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]: return True
    
    for i in range(3):
        if columns[i][0] == columns[i][1] and columns[i][1] == columns[i][2]: return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True

def check_for_draw():
    for i in range(9):
        y = i // 3
        x = i % 3
        if board[y][x] == i + 1:
            return False

    return True

def handle_turn(player):
    print(f"{player}, input your move from 1-9")
    print()
    print_board()
    print()
    inp = int(input())
    y, x = (inp - 1)// 3, (inp - 1) % 3
    board[y][x] = player

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
