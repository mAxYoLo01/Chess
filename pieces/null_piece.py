class NullPiece:
    def __init__(self, position):
        self.position = position

    def getLegalMoves(self, board):
        self.LegalMovesList = [[], []]
        return self.LegalMovesList

    def isNull(self):
        return True
