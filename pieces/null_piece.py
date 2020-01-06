class NullPiece:
    def __init__(self, position):
        self.position = position
        self.name = '   '

    def getPosition(self):
        return self.position

    def getName(self):
        return self.name

    def getLegalMoves(self, board):
        self.LegalMovesList = [[], []]
        return self.LegalMovesList

    def isNull(self):
        return True
