import math

board = [[" " for _ in range(3)] for x in range(3)]
ai = "O"
human = "X"


def best_move(board, maximising_player):
    best_score = -math.inf
    best_move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def minimax(board, depth, is_maximising):
    result = check_for_win(board)
    if result == ai:
        return 1
    elif result == human:
        return -1
    elif result == "DRAW":
        return 0

    if is_maximising:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    if score > best_score:
                        best_score = score
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = human
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    if score < best_score:
                        best_score = score
        return best_score


def print_board():
    for i in range(len(board)):
        print("-" * 13)
        for j in range(len(board[i])):
            print("|", end=" ")
            print(board[i][j], end=" ")
        print("|", end=" ")
        print(i)
    print("-" * 13)
    print(" ", end="")
    print("    ".join([str(x) for x in range(3)]))


def check_for_win(board):

    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2]) and board[i][
            0
        ] != " ":
            return board[i][0]

    for i in range(3):
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i]) and board[0][
            i
        ] != " ":
            return board[0][i]

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][
        0
    ] != " ":
        return board[0][0]

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) and board[0][
        2
    ] != " ":
        return board[0][2]

    draw = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                draw = False

    if draw:
        return "DRAW"

    return None


def handle_turn(player):
    print_board()
    while True:
        print(
            f"{player}, input the row and column of your move in this format: `row col`"
        )
        print()
        inp = input().split()
        row, col = int(inp[0]), int(inp[1])
        if board[row][col] == " ":
            break

    board[row][col] = player
    print_board()
    print(row, col)

    result = check_for_win(board)
    if result == "X":
        print("X wins.")
        return True
    elif result == "O":
        print("O wins.")
        return True

    elif result == "DRAW":
        print("DRAW")
        return True

    return False


while True:
    if handle_turn("X"):
        print_board()
        break

    y, x = best_move(board, True)
    board[y][x] = ai
    result = check_for_win(board)
    if result == "X":
        print("X wins.")
        print_board()
        break
    elif result == "O":
        print("O wins.")
        print_board()
        break

    elif result == "DRAW":
        print("DRAW")
        break
