from pieces.piece import Piece


class King(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = color + '_' + 'K'

    def getLegalMoves(self, board):
        LegalMovesListNull = []
        LegalMovesListDestroyable = []
        for row in board:
            for tile in row:
                if tile.position == self.position:
                    positions = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
                    for pos in positions:
                        row = self.position[0] + pos[0]
                        column = self.position[1] + pos[1]
                        if self.isInBound(row, column):
                            if board[row][column].isNull():
                                LegalMovesListNull.append(board[row][column])
                            elif board[row][column].color != tile.color:
                                LegalMovesListDestroyable.append(board[row][column])
        self.LegalMovesList = [LegalMovesListNull, LegalMovesListDestroyable]
        return self.LegalMovesList
