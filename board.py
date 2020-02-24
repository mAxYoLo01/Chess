from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.pawn import Pawn
from pieces.null_piece import NullPiece


class Board:
    def __init__(self):
        self.createNewBoard()

    def createNewBoard(self):
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(NullPiece((i, j)))
            self.board.append(row)
        rookB1 = Rook('B')
        rookB2 = Rook('B')
        knightB1 = Knight('B')
        knightB2 = Knight('B')
        bishopB1 = Bishop('B')
        bishopB2 = Bishop('B')
        queenB = Queen('B')
        kingB = King('B')
        pawnB1 = Pawn('B')
        pawnB2 = Pawn('B')
        pawnB3 = Pawn('B')
        pawnB4 = Pawn('B')
        pawnB5 = Pawn('B')
        pawnB6 = Pawn('B')
        pawnB7 = Pawn('B')
        pawnB8 = Pawn('B')
        rookW1 = Rook('W')
        rookW2 = Rook('W')
        knightW1 = Knight('W')
        knightW2 = Knight('W')
        bishopW1 = Bishop('W')
        bishopW2 = Bishop('W')
        queenW = Queen('W')
        kingW = King('W')
        pawnW1 = Pawn('W')
        pawnW2 = Pawn('W')
        pawnW3 = Pawn('W')
        pawnW4 = Pawn('W')
        pawnW5 = Pawn('W')
        pawnW6 = Pawn('W')
        pawnW7 = Pawn('W')
        pawnW8 = Pawn('W')
        self.addPiece(rookB1, (0, 0))
        self.addPiece(knightB1, (0, 1))
        self.addPiece(bishopB1, (0, 2))
        self.addPiece(queenB, (0, 3))
        self.addPiece(kingB, (0, 4))
        self.addPiece(bishopB2, (0, 5))
        self.addPiece(knightB2, (0, 6))
        self.addPiece(rookB2, (0, 7))
        self.addPiece(pawnB1, (1, 0))
        self.addPiece(pawnB2, (1, 1))
        self.addPiece(pawnB3, (1, 2))
        self.addPiece(pawnB4, (1, 3))
        self.addPiece(pawnB5, (1, 4))
        self.addPiece(pawnB6, (1, 5))
        self.addPiece(pawnB7, (1, 6))
        self.addPiece(pawnB8, (1, 7))
        self.addPiece(pawnW1, (6, 0))
        self.addPiece(pawnW2, (6, 1))
        self.addPiece(pawnW3, (6, 2))
        self.addPiece(pawnW4, (6, 3))
        self.addPiece(pawnW5, (6, 4))
        self.addPiece(pawnW6, (6, 5))
        self.addPiece(pawnW7, (6, 6))
        self.addPiece(pawnW8, (6, 7))
        self.addPiece(rookW1, (7, 0))
        self.addPiece(knightW1, (7, 1))
        self.addPiece(bishopW1, (7, 2))
        self.addPiece(queenW, (7, 3))
        self.addPiece(kingW, (7, 4))
        self.addPiece(bishopW2, (7, 5))
        self.addPiece(knightW2, (7, 6))
        self.addPiece(rookW2, (7, 7))

    def printBoard(self):
        boardToPrint = "#############################################################\n\n "
        boardToPrint += " |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |\n"
        i = 0
        for row in self.board:
            boardToPrint += str(i)
            for tile in row:
                boardToPrint += " | " + tile.name
            boardToPrint += " |\n"
            i += 1
        print(boardToPrint)

    def printLegalMovesBoard(self, position):
        piece = self.board[position[0]][position[1]]
        try:
            ListToPrint = piece.getLegalMoves(self.board)
            BoardToPrint = []
            for i in range(8):
                row = []
                for j in range(8):
                    row.append("   ")
                BoardToPrint.append(row)
            for row in self.board:
                for tile in row:
                    if piece.position == tile.position:
                        BoardToPrint[self.board.index(row)][row.index(tile)] = " O "
                    for null in ListToPrint[0]:
                        if null.position == tile.position:
                            BoardToPrint[self.board.index(row)][row.index(tile)] = " - "
                    for destroyable in ListToPrint[1]:
                        if destroyable.position == tile.position:
                            BoardToPrint[self.board.index(row)][row.index(tile)] = " X "
            ToPrint = "#############################################################\n\n "
            ToPrint += " |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |\n"
            i = 0
            for row in BoardToPrint:
                ToPrint += str(i)
                for tile in row:
                    ToPrint += " | " + tile
                ToPrint += " |\n"
                i += 1
            print(ToPrint)
        except AttributeError:
            print("A NullPiece() does not have any legal moves!")

    def move(self, position1, position2):
        piece = self.board[position1[0]][position1[1]]
        LegalMovesList = piece.getLegalMoves(self.board)[0] + piece.getLegalMoves(self.board)[1]
        CanMove = False
        for legalMoves in LegalMovesList:
            if legalMoves.position == position2:
                self.addPiece(piece, position2)
                self.removePiece(position1)
                piece.count += 1
                CanMove = True
                break
        if not CanMove:
            print("Can't move at this position!")

    def addPiece(self, piece, position):
        piece.position = position
        self.board[position[0]][position[1]] = piece

    def removePiece(self, position):
        self.board[position[0]][position[1]] = NullPiece(position)

    def hasPiece(self, position):
        return not self.board[position[0]][position[1]].isNull()

    def isCheck(self, color):
        king = None
        otherColorLegalMoves = []
        for row in self.board:
            for tile in row:
                if not tile.isNull():
                    if tile.name == color + '_K':
                        king = tile
                    if color not in tile.name and self.hasPiece(tile.position):
                        tileDestroyable = tile.getLegalMoves(self.board)[1]
                        for legalMove in tileDestroyable:
                            if legalMove not in otherColorLegalMoves:
                                otherColorLegalMoves.append(legalMove)
        if king in otherColorLegalMoves:
            return True
        else:
            return False
