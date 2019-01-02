X = True
O = False

def show_piece(piece):
    if piece is None:
        return ' '
    elif piece == X:
        return 'X'
    elif piece == O:
        return 'O'

def other_team(team):
    if team == X:
        return O
    if team == O:
        return X

class Board(object):

    def __init__(self):
        self.board = [[None] * 3, [None] * 3, [None] * 3]

    def get_cell(self, x, y):
        return self.board[x][y]

    def set_cell(self, x, y, piece):
        self.board[x][y] = piece

    def copy(self):
        other = Board()
        for i in range(3):
            for j in range(3):
                other.set_cell(i, j, self.get_cell(i, j))
        return other

    def print(self):
        # print('-------------')
        # for i in range(3):
        #     print('| ', end='')
        #     for j in range(3):
                
        #         print(show_piece(self.get_cell(i, j)), end=' | ')

        #     print('')
        #     print('----+---+----')

        print('┏━━━┳━━━┳━━━┓')
        print('┃', end= ' ')
        print(show_piece(self.get_cell(0, 0)), end =' ┃ ' )
        print(show_piece(self.get_cell(0, 1)), end =' ┃ ')
        print(show_piece(self.get_cell(0, 2)), end =' ┃')
        print('')

        print('┣━━━╋━━━╋━━━┫')

        print('┃', end= ' ')
        print(show_piece(self.get_cell(1, 0)), end =' ┃ ' )
        print(show_piece(self.get_cell(1, 1)), end =' ┃ ')
        print(show_piece(self.get_cell(1, 2)), end =' ┃')
        print('')

        print('┣━━━╋━━━╋━━━┫')

        print('┃', end= ' ')
        print(show_piece(self.get_cell(2, 0)), end =' ┃ ' )
        print(show_piece(self.get_cell(2, 1)), end =' ┃ ')
        print(show_piece(self.get_cell(2, 2)), end =' ┃')
        print('')

        print('┗━━━┻━━━┻━━━┛')

# ┏━━━┳━━━┳━━━┓
# ┃ X ┃ X ┃ X ┃
# ┣━━━╋━━━╋━━━┫
# ┃ X ┃ X ┃ X ┃
# ┣━━━╋━━━╋━━━┫
# ┃ X ┃ X ┃ X ┃
# ┗━━━┻━━━┻━━━┛


    def has_won(self, team):

        for i in range(3):
            won = True
            for j in range(3):
                if self.get_cell(i, j) != team:
                    won = False
                    break
            if won:
                return True

        for j in range(3):
            won = True
            for i in range(3):
                if self.get_cell(i, j) != team:
                    won = False
                    break
            if won:
                return True

        if self.get_cell(0, 0) == team and self.get_cell(1, 1) == team and self.get_cell(2, 2) == team:
            return True
        elif self.get_cell(0, 2) == team and self.get_cell(1, 1) == team and self.get_cell(2, 0) == team:
            return True

        return False

    def is_draw(self):
        if self.has_won(X):
            return False
        elif self.has_won(O):
            return False

        for i in range(3):
            for j in range(3):
                if self.get_cell(i, j) == None:
                    return False

        return True

    def empty_cells(self):
        empties = []

        for i in range(3):
            for j in range(3):
                if self.get_cell(i, j) == None:
                    empties.append((i, j))

        return empties


def test():
    no = Board()
    no.set_cell(0, 0, piece.X)
    no.set_cell(1, 1, piece.X)

    print('no:')
    no.print()
    print(no.has_won(piece.X))

    yes = no.copy()
    yes.set_cell(2, 2, piece.X)

    print('yes:')
    yes.print()
    print(yes.has_won(piece.X))

# test()
