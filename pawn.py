from piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = color + '_' + 'P'
        self.count = 0

    def getLegalMoves(self, board):
        position = self.getPosition()
        LegalMovesListNull = []
        LegalMovesListDestroyable = []
        DoubleAdvance = False
        for row in board:
            for tile in row:
                if tile.getPosition() == position:
                    if self.getCount() == 0:
                        DoubleAdvance = True
                    if self.getColor() == 'B':
                        if position[0] + 1 < 8 and board[position[0] + 1][position[1]].getName() == '   ':
                            LegalMovesListNull.append(board[position[0] + 1][position[1]])
                            if DoubleAdvance and position[0] + 2 < 8 and board[position[0] + 2][position[1]].getName() == '   ':
                                LegalMovesListNull.append(board[position[0] + 2][position[1]])
                        if position[0] + 1 < 8 and position[1] + 1 < 8 and board[position[0] + 1][position[1] + 1].getName() != '   ' and board[position[0] + 1][position[1] + 1].getColor() != tile.getColor():
                            LegalMovesListDestroyable.append(board[position[0] + 1][position[1] + 1])
                        if position[0] + 1 < 8 and position[1] - 1 > -1 and board[position[0] + 1][position[1] - 1].getName() != '   ' and board[position[0] + 1][position[1] - 1].getColor() != tile.getColor():
                            LegalMovesListDestroyable.append(board[position[0] + 1][position[1] - 1])
                    else:
                        if position[0] - 1 > -1 and board[position[0] - 1][position[1]].getName() == '   ':
                            LegalMovesListNull.append(board[position[0] - 1][position[1]])
                            if DoubleAdvance and position[0] - 2 < 8 and board[position[0] - 2][position[1]].getName() == '   ':
                                LegalMovesListNull.append(board[position[0] - 2][position[1]])
                        if position[0] - 1 > -1 and position[1] + 1 < 8 and board[position[0] - 1][position[1] + 1].getName() != '   ' and board[position[0] - 1][position[1] + 1].getColor() != tile.getColor():
                            LegalMovesListDestroyable.append(board[position[0] - 1][position[1] + 1])
                        if position[0] - 1 > -1 and position[1] - 1 > -1 and board[position[0] - 1][position[1] - 1].getName() != '   ' and board[position[0] - 1][position[1] - 1].getColor() != tile.getColor():
                            LegalMovesListDestroyable.append(board[position[0] - 1][position[1] - 1])
        self.LegalMovesList = [LegalMovesListNull, LegalMovesListDestroyable]
        return self.LegalMovesList
