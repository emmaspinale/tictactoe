from board import Board, X, O, other_team

WIN = 0
DRAW = 1
LOSS = 2

def show_result(result):
    if result == WIN:
        return 'WIN'
    if result == DRAW:
        return 'DRAW'
    if result == LOSS:
        return 'LOSS'

def ai(board0, team):

    for x0, y0 in board0.empty_cells():
        board1 = board0.copy()
        board1.set_cell(x0, y0, team)
        if board1.has_won(team):
            return WIN, x0, y0
        if board1.is_draw():
            continue
        broke = False
        for x1, y1 in board1.empty_cells():
            board2 = board1.copy()
            board2.set_cell(x1, y1, other_team(team))
            if board2.has_won(other_team(team)):
                broke = True
                break
            if board2.is_draw():
                broke = True
                break
            result, _, _ = ai(board2, team)
            if result != WIN:
                broke = True
                break
        if not broke:
            return WIN, x0, y0

    for x0, y0 in board0.empty_cells():
        board1 = board0.copy()
        board1.set_cell(x0, y0, team)
        if board1.is_draw():
            return DRAW, x0, y0
        broke = False
        for x1, y1 in board1.empty_cells():
            board2 = board1.copy()
            board2.set_cell(x1, y1, other_team(team))
            if board2.has_won(other_team(team)):
                broke = True
                break
            # if board2.is_draw():
            #     broke = True
            #     break
            result, _, _ = ai(board2, team)
            if result == LOSS:
                 broke = True
                 break
        if not broke:
            return DRAW, x0, y0


    for x0, y0 in board0.empty_cells():
        return LOSS, x0, y0

def arbitrary_empty_cell(board):
    return board.empty_cells()[0]

def play():
    board = Board()
    while True:

        board.print()

        if board.has_won(O):
            print("O WON")
            return
        if board.is_draw():
            print("DRAW")
            return

        result, x, y = ai(board, X)

        print()
        print('ai returns', show_result(result), x, y)

        board.set_cell(x, y, X)

        print()
        board.print()

        if board.has_won(X):
            print("X WON")
            return
        if board.is_draw():
            print("DRAW")
            return

        print("GO: ", end='')
        x, y = get_move()
        board.set_cell(x, y, O)

    # while True:
    #     print(get_move())


def get_move():
    kbd = input()
    x, y = map(int, kbd.split(','))
    return x, y

play()
