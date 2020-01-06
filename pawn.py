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
        for row in board:
            for tile in row:
                if tile.getPosition() == position:
                    i = 0
                    if self.getColor() == 'B':
                        i = 1
                    else:
                        i = -1
                    row = position[0] + i
                    column = position[1]
                    if self.isInBound(row, column) and board[row][column].isNull():
                        LegalMovesListNull.append(board[row][column])
                        row = position[0] + 2 * i
                        column = position[1]
                        if self.getCount() == 0 and self.isInBound(row, column) and board[row][column].isNull():
                            LegalMovesListNull.append(board[row][column])
                    row = position[0] + i
                    column = position[1] - 1
                    if self.isInBound(row, column) and not board[row][column].isNull() and board[row][column].getColor() != tile.getColor():
                        LegalMovesListDestroyable.append(board[row][column])
                    row = position[0] + i
                    column = position[1] + 1
                    if self.isInBound(row, column) and not board[row][column].isNull() and board[row][column].getColor() != tile.getColor():
                        LegalMovesListDestroyable.append(board[row][column])
        self.LegalMovesList = [LegalMovesListNull, LegalMovesListDestroyable]
        return self.LegalMovesList
