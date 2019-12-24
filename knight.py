from piece import Piece


class Knight(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = color + '_' + 'N'

    def getLegalMoves(self, board):
        position = self.getPosition()
        LegalMovesListNull = []
        LegalMovesListDestroyable = []
        for row in board:
            for tile in row:
                if tile.getPosition() == position:
                    positions = [[2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2]]
                    for pos in positions:
                        row = position[0] + pos[0]
                        column = position[1] + pos[1]
                        if self.isInBound(row, column):
                            if board[row][column].getName() == "   ":
                                LegalMovesListNull.append(board[row][column])
                            elif board[row][column].getColor() != tile.getColor():
                                LegalMovesListDestroyable.append(board[row][column])
        self.LegalMovesList = [LegalMovesListNull, LegalMovesListDestroyable]
        return self.LegalMovesList
