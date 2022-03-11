def print_board():
    for i in board:
        for j in i:
            print(j, end=' ')
        print()

def check_for_win(target):
    columns = list(zip(*board))

    row_win = False
    for i in range(3):
        if all([True if x == target else False for x in board[i]]):
            row_win = True

    
    col_win = False
    for i in range(3):
        if all([True if x == target else False for x in columns[i]]):
            col_win = True

    left_diag = []
    for i in range(0, 9, 4):
        y, x = i // 3, i % 3
        left_diag.append(True if board[y][x] == target else False)

    right_diag = []
    for i in range(2, 8, 2):
        y, x = i // 3, i % 3
        right_diag.append(True if board[y][x] == target else False)

    left_diag = all(left_diag)
    right_diag = all(right_diag)

    return any([left_diag, right_diag, row_win, col_win])

def check_for_draw():
    all_spots = []
    for i in range(9):
        y = i // 3
        x = i % 3
        all_spots.append(board[y][x])

    all_spots = [True if x in ['X', 'O'] else False  for x in all_spots]
    return all(all_spots)

def handle_turn(player):
    print(f"{player}, input your move from 0-8")
    print()
    print_board()
    print()
    inp = int(input())
    y, x = inp // 3, inp % 3
    board[y][x] = player

    if check_for_win(player) == True:
        print(f"{player} wins.")
        return True

    if check_for_win('O' if player == 'X' else 'X') == True:
        print(f"{'O' if player == 'X' else 'X'} wins.")
        return True
        
    if check_for_draw():
        print("DRAW")
        return True
        
    return False

board = [[x for x in range(3)] for _ in range(3)]
for i in range(1, 9):
    board[i // 3][i % 3] = i

while True:
    if handle_turn('X'):
        break
    if handle_turn('O'):
        break
