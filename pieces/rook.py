from pieces.piece import Piece


class Rook(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = color + '_' + 'R'

    def getLegalMoves(self, board):
        position = self.getPosition()
        LegalMovesListNull = []
        LegalMovesListDestroyable = []
        for row in board:
            for tile in row:
                if tile.getPosition() == position:
                    positions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for pos in positions:
                        i = 1
                        while True:
                            row = position[0] + i * pos[0]
                            column = position[1] + i * pos[1]
                            if self.isInBound(row, column) and board[row][column].isNull():
                                LegalMovesListNull.append(board[row][column])
                                i += 1
                            else:
                                if self.isInBound(row, column) and board[row][column].getColor() != tile.getColor():
                                    LegalMovesListDestroyable.append(board[row][column])
                                break
        self.LegalMovesList = [LegalMovesListNull, LegalMovesListDestroyable]
        return self.LegalMovesList
