from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = color + '_' + 'P'
        self.count = 0

    def getLegalMoves(self, board):
        LegalMovesListNull = []
        LegalMovesListDestroyable = []
        for row in board:
            for tile in row:
                if tile.position == self.position:
                    i = 0
                    if self.color == 'B':
                        i = 1
                    else:
                        i = -1
                    row = self.position[0] + i
                    column = self.position[1]
                    if self.isInBound(row, column) and board[row][column].isNull():
                        LegalMovesListNull.append(board[row][column])
                        row = self.position[0] + 2 * i
                        column = self.position[1]
                        if self.count == 0 and self.isInBound(row, column) and board[row][column].isNull():
                            LegalMovesListNull.append(board[row][column])
                    row = self.position[0] + i
                    column = self.position[1] - 1
                    if self.isInBound(row, column) and not board[row][column].isNull() and board[row][column].color != tile.color:
                        LegalMovesListDestroyable.append(board[row][column])
                    row = self.position[0] + i
                    column = self.position[1] + 1
                    if self.isInBound(row, column) and not board[row][column].isNull() and board[row][column].color != tile.color:
                        LegalMovesListDestroyable.append(board[row][column])
        self.LegalMovesList = [LegalMovesListNull, LegalMovesListDestroyable]
        return self.LegalMovesList
