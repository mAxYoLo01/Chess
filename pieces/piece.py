class Piece:
    def __init__(self, color):
        self.color = color
        self.count = 0

    def isInBound(self, row, column):
        return row > -1 and row < 8 and column > -1 and column < 8

    def isNull(self):
        return False
