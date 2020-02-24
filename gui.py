from PyQt5 import QtCore, QtGui, QtTest, QtWidgets
from ui_chessboard import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from board import Board
import sys
import os

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

selected_stylesheet = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(9, 130, 19, 255), stop:1 rgba(35, 179, 9, 255));"
selectable_stylesheet = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(189, 189, 0, 255), stop:1 rgba(204, 204, 0, 255));"
destroyable_stylesheet = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(203, 0, 0, 255), stop:1 rgba(220, 85, 85, 255));"
black_stylesheet = "border: 2px solid;\n background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(123, 119, 120, 255), stop:1 rgba(125, 121, 122, 255));"
white_stylesheet = "border: 2px solid;\n background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(231, 231, 231, 255), stop:1 rgba(246, 251, 247, 255));"
hoverEnter = "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffff00;\">"
hoverLeave = "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">"
hoverEnd = "</span></p></body></html>"


def ButtonToPosition(button):
    alphabet = 'ABCDEFGH'
    for letter in alphabet:
        if letter == button.objectName()[0]:
            return (int(button.objectName()[1]) - 1, alphabet.index(letter))


def PositionToButton(position):
    return 'ABCDEFGH'[position[1]] + str(position[0] + 1)


class CustomButton(QtWidgets.QPushButton):
    def __init__(self, parent):
        QtWidgets.QPushButton.__init__(self, parent)

    def mousePressEvent(self, event):
        window.action(self)

    def enterEvent(self, event):
        column = self.parent().parent().columns
        row = self.parent().parent().rows
        for i in range(column.count()):
            if column.itemAt(i).widget().objectName() == self.objectName()[0]:
                column.itemAt(i).widget().setText(hoverEnter + column.itemAt(i).widget().objectName() + hoverEnd)
        for i in range(row.count()):
            if row.itemAt(i).widget().objectName()[1] == self.objectName()[1]:
                row.itemAt(i).widget().setText(hoverEnter + row.itemAt(i).widget().objectName()[1] + hoverEnd)

    def leaveEvent(self, event):
        column = self.parent().parent().columns
        row = self.parent().parent().rows
        for i in range(column.count()):
            column.itemAt(i).widget().setText(hoverLeave + column.itemAt(i).widget().objectName() + hoverEnd)
            row.itemAt(i).widget().setText(hoverLeave + row.itemAt(i).widget().objectName()[1] + hoverEnd)


board = Board()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, board):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.board = Board()
        self.setupUi(self)
        self.setWindowTitle("Chess")
        self.initializeButtons()
        self.selected = None
        self.currentColor = 'W'
        self.selectable = []
        self.destroyable = []
        self.createGridColor()
        self.createIcons()

    def action(self, button):
        self.printText("")
        position = ButtonToPosition(button)
        if self.selected is None:
            if self.board.hasPiece(position):
                if self.board.board[position[0]][position[1]].color == self.currentColor:
                    if self.board.isCheck(self.currentColor):
                        if self.currentColor == 'W':
                            self.printText("White king is in check!")
                        else:
                            self.printText("Black king is in check!")
                    self.selected = button
                    LegalMovesList = self.board.board[position[0]][position[1]].getLegalMoves(self.board.board)
                    for LegalNull in LegalMovesList[0]:
                        self.selectable.append(PositionToButton(LegalNull.position))
                    for LegalDestroyable in LegalMovesList[1]:
                        self.destroyable.append(PositionToButton(LegalDestroyable.position))
                else:
                    self.printText("Not your turn!")
        else:
            if button != self.selected:
                if button.objectName() in self.selectable or button.objectName() in self.destroyable:
                    self.movingAnimation(self.selected, button)
                    self.board.move(ButtonToPosition(self.selected), position)
                    if self.board.isCheck(self.currentColor):
                        self.printText("Checkmate! New game?")
                        self.yes.setGeometry(QtCore.QRect(self.yes.x(), 920, 100, 60))
                        self.no.setGeometry(QtCore.QRect(self.no.x(), 920, 100, 60))
                    self.switchColor()
                else:
                    self.printText("Can't move at this position!")
            self.selected = None
            self.selectable = []
            self.destroyable = []
        self.createGridColor()
        self.createIcons()

    def switchColor(self):
        if self.currentColor == 'B':
            self.currentColor = 'W'
        else:
            self.currentColor = 'B'

    def movingAnimation(self, button1, button2):
        fluidity = 20
        position = ButtonToPosition(button1)
        self.moving.setGeometry(QtCore.QRect(button1.x(), button1.y(), 90, 90))
        icon = QtGui.QIcon()
        button1.setIcon(icon)
        piece = self.board.board[position[0]][position[1]]
        self.moving.setIcon(self.convertToImage(piece))
        incX = (button2.x() - button1.x()) / fluidity
        incY = (button2.y() - button1.y()) / fluidity
        newX = button1.x()
        newY = button1.y()
        if "_N" not in piece.name:
            for _ in range(fluidity):
                newX += incX
                newY += incY
                self.moving.setGeometry(QtCore.QRect(newX, newY, 90, 90))
                QtTest.QTest.qWait(25)
        else:
            """Moving 2 tiles abroad first, then 1 tile only for the Knight."""
            if abs(button2.x() - button1.x()) == 180:
                for _ in range(fluidity):
                    newX += incX
                    self.moving.setGeometry(QtCore.QRect(newX, newY, 90, 90))
                    QtTest.QTest.qWait(25)
                for _ in range(fluidity):
                    newY += incY
                    self.moving.setGeometry(QtCore.QRect(newX, newY, 90, 90))
                    QtTest.QTest.qWait(25)
            else:
                for _ in range(fluidity):
                    newY += incY
                    self.moving.setGeometry(QtCore.QRect(newX, newY, 90, 90))
                    QtTest.QTest.qWait(25)
                for _ in range(fluidity):
                    newX += incX
                    self.moving.setGeometry(QtCore.QRect(newX, newY, 90, 90))
                    QtTest.QTest.qWait(25)
        self.moving.setGeometry(QtCore.QRect(-100, -100, 90, 90))
        self.moving.setIcon(icon)

    def createIcons(self):
        for rowButton in self.buttons:
            for button in rowButton:
                for row in self.board.board:
                    for tile in row:
                        if ButtonToPosition(button) == tile.position:
                            button.setIcon(self.convertToImage(tile))

    def convertToImage(self, tile):
        icon = QtGui.QIcon()
        if tile.isNull():
            pass
        elif "B_Q" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_queen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_K" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_king.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_B" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_bishop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_N" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_knight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_R" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_rook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_P" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_pawn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_Q" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_queen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_K" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_king.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_B" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_bishop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_N" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_knight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_R" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_rook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_P" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_pawn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def createGridColor(self):
        i = 1
        j = 1
        for row in self.buttons:
            for button in row:
                if j % 2 == 1:
                    if i % 2 == 1:
                        button.setStyleSheet(white_stylesheet)
                    else:
                        button.setStyleSheet(black_stylesheet)
                else:
                    if i % 2 == 1:
                        button.setStyleSheet(black_stylesheet)
                    else:
                        button.setStyleSheet(white_stylesheet)
                if i % 8 == 0:
                    j += 1
                i += 1
                for tile in self.selectable:
                    if button.objectName() == tile:
                        button.setStyleSheet(button.styleSheet() + selectable_stylesheet)
                for tile in self.destroyable:
                    if button.objectName() == tile:
                        button.setStyleSheet(button.styleSheet() + destroyable_stylesheet)
                if self.selected is not None and button.objectName() == self.selected.objectName():
                    button.setStyleSheet(button.styleSheet() + selected_stylesheet)

    def printText(self, text):
        self.text.setText("<html><head/><body><p align=\"center\"><span style=\"font-size:28pt;font-weight:600;color:#ffffff;\">" + text + "</span></p></body></html>")

    def startNewGame(self):
        self.board.__init__()
        self.currentColor = 'W'
        self.printText("")
        self.yes.setGeometry(QtCore.QRect(self.yes.x(), -100, 100, 60))
        self.no.setGeometry(QtCore.QRect(self.no.x(), -100, 100, 60))
        self.createGridColor()
        self.createIcons()

    def initializeButtons(self):
        self.buttons = []
        for _ in range(8):
            row = [CustomButton(self.centralwidget) for _ in range(8)]
            self.buttons.append(row)
        new_x = 60
        i = 0
        for row in self.buttons:
            new_y = 60
            j = 0
            for button in row:
                button.setGeometry(QtCore.QRect(new_x, new_y, 90, 90))
                button.setObjectName(PositionToButton((j, i)))
                button.setIconSize(QtCore.QSize(60, 60))
                button.setCheckable(False)
                button.setDefault(False)
                button.setFlat(False)
                button.raise_()
                new_y += 90
                j += 1
            new_x += 90
            i += 1
        self.moving.raise_()
        self.yes.clicked.connect(lambda: self.startNewGame())
        self.no.clicked.connect(lambda: sys.exit())


if __name__ == "__main__":
    os.system('cls')
    app = QApplication(sys.argv)
    window = MainWindow(board)
    window.show()
    sys.exit(app.exec_())
