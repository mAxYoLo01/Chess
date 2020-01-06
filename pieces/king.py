from pieces.piece import Piece


class King(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = color + '_' + 'K'

    def getLegalMoves(self, board):
        position = self.getPosition()
        LegalMovesListNull = []
        LegalMovesListDestroyable = []
        for row in board:
            for tile in row:
                if tile.getPosition() == position:
                    positions = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
                    for pos in positions:
                        row = position[0] + pos[0]
                        column = position[1] + pos[1]
                        if self.isInBound(row, column):
                            if board[row][column].isNull():
                                LegalMovesListNull.append(board[row][column])
                            elif board[row][column].getColor() != tile.getColor():
                                LegalMovesListDestroyable.append(board[row][column])
        self.LegalMovesList = [LegalMovesListNull, LegalMovesListDestroyable]
        return self.LegalMovesList
