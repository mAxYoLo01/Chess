class Piece:
    def __init__(self, color):
        self.color = color
        self.count = 0

    def getName(self):
        return self.name

    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def getColor(self):
        return self.color

    def getCount(self):
        return self.count

    def incrementCount(self):
        self.count += 1

    def isInBound(self, row, column):
        return row > -1 and row < 8 and column > -1 and column < 8

    def isNull(self):
        return False
