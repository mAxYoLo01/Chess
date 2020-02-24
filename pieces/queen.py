from pieces.piece import Piece
from pieces.rook import Rook
from pieces.bishop import Bishop


class Queen(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = color + '_' + 'Q'

    def getLegalMoves(self, board):
        rookQ = Rook(self.color)
        rookQ.position = self.position
        legalRook = rookQ.getLegalMoves(board)
        bishopQ = Bishop(self.color)
        bishopQ.position = self.position
        legalBishop = bishopQ.getLegalMoves(board)
        self.LegalMovesList = [legalRook[0] + legalBishop[0], legalRook[1] + legalBishop[1]]
        return self.LegalMovesList
