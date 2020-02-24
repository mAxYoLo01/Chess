from PyQt5 import QtCore, QtGui, QtTest, QtWidgets
from ui_chessboard import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from board import Board
import sys
import os

board = Board()

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

selected_stylesheet = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(9, 130, 19, 255), stop:1 rgba(35, 179, 9, 255));"
selectable_stylesheet = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(189, 189, 0, 255), stop:1 rgba(204, 204, 0, 255));"
destroyable_stylesheet = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(203, 0, 0, 255), stop:1 rgba(220, 85, 85, 255));"
black_stylesheet = "border: 2px solid;\n background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(123, 119, 120, 255), stop:1 rgba(125, 121, 122, 255));"
white_stylesheet = "border: 2px solid;\n background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(231, 231, 231, 255), stop:1 rgba(246, 251, 247, 255));"
hover1 = "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffff00;\">"
hover2 = "</span></p></body></html>"
hover3 = "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">"


def ButtonToPosition(button):
    row = int(button.objectName()[1]) - 1
    column = None
    if button.objectName()[0] == 'A':
        column = 0
    elif button.objectName()[0] == 'B':
        column = 1
    elif button.objectName()[0] == 'C':
        column = 2
    elif button.objectName()[0] == 'D':
        column = 3
    elif button.objectName()[0] == 'E':
        column = 4
    elif button.objectName()[0] == 'F':
        column = 5
    elif button.objectName()[0] == 'G':
        column = 6
    elif button.objectName()[0] == 'H':
        column = 7
    return (row, column)


def PositionToButton(position):
    row = position[0] + 1
    column = ''
    if position[1] == 0:
        column = 'A'
    elif position[1] == 1:
        column = 'B'
    elif position[1] == 2:
        column = 'C'
    elif position[1] == 3:
        column = 'D'
    elif position[1] == 4:
        column = 'E'
    elif position[1] == 5:
        column = 'F'
    elif position[1] == 6:
        column = 'G'
    elif position[1] == 7:
        column = 'H'
    return column + str(row)


class CustomButton(QtWidgets.QPushButton):
    def __init__(self, parent):
        QtWidgets.QPushButton.__init__(self, parent)

    def enterEvent(self, event):
        if self.objectName()[0] == 'A':
            self.parent().parent().A.setText(hover1 + self.objectName()[0] + hover2)
        elif self.objectName()[0] == 'B':
            self.parent().parent().B.setText(hover1 + self.objectName()[0] + hover2)
        elif self.objectName()[0] == 'C':
            self.parent().parent().C.setText(hover1 + self.objectName()[0] + hover2)
        elif self.objectName()[0] == 'D':
            self.parent().parent().D.setText(hover1 + self.objectName()[0] + hover2)
        elif self.objectName()[0] == 'E':
            self.parent().parent().E.setText(hover1 + self.objectName()[0] + hover2)
        elif self.objectName()[0] == 'F':
            self.parent().parent().F.setText(hover1 + self.objectName()[0] + hover2)
        elif self.objectName()[0] == 'G':
            self.parent().parent().G.setText(hover1 + self.objectName()[0] + hover2)
        elif self.objectName()[0] == 'H':
            self.parent().parent().H.setText(hover1 + self.objectName()[0] + hover2)
        if self.objectName()[1] == '1':
            self.parent().parent().v1.setText(hover1 + self.objectName()[1] + hover2)
        elif self.objectName()[1] == '2':
            self.parent().parent().v2.setText(hover1 + self.objectName()[1] + hover2)
        elif self.objectName()[1] == '3':
            self.parent().parent().v3.setText(hover1 + self.objectName()[1] + hover2)
        elif self.objectName()[1] == '4':
            self.parent().parent().v4.setText(hover1 + self.objectName()[1] + hover2)
        elif self.objectName()[1] == '5':
            self.parent().parent().v5.setText(hover1 + self.objectName()[1] + hover2)
        elif self.objectName()[1] == '6':
            self.parent().parent().v6.setText(hover1 + self.objectName()[1] + hover2)
        elif self.objectName()[1] == '7':
            self.parent().parent().v7.setText(hover1 + self.objectName()[1] + hover2)
        elif self.objectName()[1] == '8':
            self.parent().parent().v8.setText(hover1 + self.objectName()[1] + hover2)

    def leaveEvent(self, event):
        self.parent().parent().A.setText(hover3 + 'A' + hover2)
        self.parent().parent().B.setText(hover3 + 'B' + hover2)
        self.parent().parent().C.setText(hover3 + 'C' + hover2)
        self.parent().parent().D.setText(hover3 + 'D' + hover2)
        self.parent().parent().E.setText(hover3 + 'E' + hover2)
        self.parent().parent().F.setText(hover3 + 'F' + hover2)
        self.parent().parent().G.setText(hover3 + 'G' + hover2)
        self.parent().parent().H.setText(hover3 + 'H' + hover2)
        self.parent().parent().v1.setText(hover3 + '1' + hover2)
        self.parent().parent().v2.setText(hover3 + '2' + hover2)
        self.parent().parent().v3.setText(hover3 + '3' + hover2)
        self.parent().parent().v4.setText(hover3 + '4' + hover2)
        self.parent().parent().v5.setText(hover3 + '5' + hover2)
        self.parent().parent().v6.setText(hover3 + '6' + hover2)
        self.parent().parent().v7.setText(hover3 + '7' + hover2)
        self.parent().parent().v8.setText(hover3 + '8' + hover2)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Chess")
        self.initializeButtons()
        self.selected = None
        self.currentColor = 'B'
        self.selectable = []
        self.destroyable = []
        self.createGridColor()
        self.createIcons()

    def action(self, button):
        position = ButtonToPosition(button)
        board.isCheck('B')
        board.isCheckmate('B')
        if self.selected is None:
            if board.hasPiece(position):
                if board.getPiece(position).getColor() == self.currentColor:
                    self.selected = button
                    LegalMovesList = board.getPiece(position).getLegalMoves(board.getBoard())
                    for LegalNull in LegalMovesList[0]:
                        self.selectable.append(PositionToButton(LegalNull.getPosition()))
                    for LegalDestroyable in LegalMovesList[1]:
                        self.destroyable.append(PositionToButton(LegalDestroyable.getPosition()))
                else:
                    print("Not your turn!")
        else:
            if button != self.selected:
                if button.objectName() in self.selectable or button.objectName() in self.destroyable:
                    self.movingAnimation(self.selected, button)
                    board.move(ButtonToPosition(self.selected), position)
                    self.switchColor()
                else:
                    print("Can't move at this position!")
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
        self.moving.setGeometry(QtCore.QRect(button1.x(), button1.y(), 90, 90))
        icon = QtGui.QIcon()
        button1.setIcon(icon)
        piece = board.getPiece(ButtonToPosition(button1))
        self.moving.setIcon(self.convertToImage(piece))
        incX = (button2.x() - button1.x()) / fluidity
        incY = (button2.y() - button1.y()) / fluidity
        newX = button1.x()
        newY = button1.y()
        if "_N" not in piece.getName():
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
                for row in board.getBoard():
                    for tile in row:
                        if ButtonToPosition(button) == tile.getPosition():
                            button.setIcon(self.convertToImage(tile))

    def convertToImage(self, tile):
        icon = QtGui.QIcon()
        if "B_Q" == tile.getName():
            icon.addPixmap(QtGui.QPixmap(":/Images/black_queen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_K" == tile.getName():
            icon.addPixmap(QtGui.QPixmap(":/Images/black_king.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_B" == tile.getName():
            icon.addPixmap(QtGui.QPixmap(":/Images/black_bishop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_N" == tile.getName():
            icon.addPixmap(QtGui.QPixmap(":/Images/black_knight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_R" == tile.getName():
            icon.addPixmap(QtGui.QPixmap(":/Images/black_rook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_P" == tile.getName():
            icon.addPixmap(QtGui.QPixmap(":/Images/black_pawn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_Q" == tile.getName():
            icon.addPixmap(QtGui.QPixmap(":/Images/white_queen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_K" == tile.getName():
            icon.addPixmap(QtGui.QPixmap(":/Images/white_king.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_B" == tile.getName():
            icon.addPixmap(QtGui.QPixmap(":/Images/white_bishop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_N" == tile.getName():
            icon.addPixmap(QtGui.QPixmap(":/Images/white_knight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_R" == tile.getName():
            icon.addPixmap(QtGui.QPixmap(":/Images/white_rook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_P" == tile.getName():
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

    def initializeButtons(self):
        self.A1 = CustomButton(self.centralwidget)
        self.A2 = CustomButton(self.centralwidget)
        self.A3 = CustomButton(self.centralwidget)
        self.A4 = CustomButton(self.centralwidget)
        self.A5 = CustomButton(self.centralwidget)
        self.A6 = CustomButton(self.centralwidget)
        self.A7 = CustomButton(self.centralwidget)
        self.A8 = CustomButton(self.centralwidget)
        self.B1 = CustomButton(self.centralwidget)
        self.B2 = CustomButton(self.centralwidget)
        self.B3 = CustomButton(self.centralwidget)
        self.B4 = CustomButton(self.centralwidget)
        self.B5 = CustomButton(self.centralwidget)
        self.B6 = CustomButton(self.centralwidget)
        self.B7 = CustomButton(self.centralwidget)
        self.B8 = CustomButton(self.centralwidget)
        self.C1 = CustomButton(self.centralwidget)
        self.C2 = CustomButton(self.centralwidget)
        self.C3 = CustomButton(self.centralwidget)
        self.C4 = CustomButton(self.centralwidget)
        self.C5 = CustomButton(self.centralwidget)
        self.C6 = CustomButton(self.centralwidget)
        self.C7 = CustomButton(self.centralwidget)
        self.C8 = CustomButton(self.centralwidget)
        self.D1 = CustomButton(self.centralwidget)
        self.D2 = CustomButton(self.centralwidget)
        self.D3 = CustomButton(self.centralwidget)
        self.D4 = CustomButton(self.centralwidget)
        self.D5 = CustomButton(self.centralwidget)
        self.D6 = CustomButton(self.centralwidget)
        self.D7 = CustomButton(self.centralwidget)
        self.D8 = CustomButton(self.centralwidget)
        self.E1 = CustomButton(self.centralwidget)
        self.E2 = CustomButton(self.centralwidget)
        self.E3 = CustomButton(self.centralwidget)
        self.E4 = CustomButton(self.centralwidget)
        self.E5 = CustomButton(self.centralwidget)
        self.E6 = CustomButton(self.centralwidget)
        self.E7 = CustomButton(self.centralwidget)
        self.E8 = CustomButton(self.centralwidget)
        self.F1 = CustomButton(self.centralwidget)
        self.F2 = CustomButton(self.centralwidget)
        self.F3 = CustomButton(self.centralwidget)
        self.F4 = CustomButton(self.centralwidget)
        self.F5 = CustomButton(self.centralwidget)
        self.F6 = CustomButton(self.centralwidget)
        self.F7 = CustomButton(self.centralwidget)
        self.F8 = CustomButton(self.centralwidget)
        self.G1 = CustomButton(self.centralwidget)
        self.G2 = CustomButton(self.centralwidget)
        self.G3 = CustomButton(self.centralwidget)
        self.G4 = CustomButton(self.centralwidget)
        self.G5 = CustomButton(self.centralwidget)
        self.G6 = CustomButton(self.centralwidget)
        self.G7 = CustomButton(self.centralwidget)
        self.G8 = CustomButton(self.centralwidget)
        self.H1 = CustomButton(self.centralwidget)
        self.H2 = CustomButton(self.centralwidget)
        self.H3 = CustomButton(self.centralwidget)
        self.H4 = CustomButton(self.centralwidget)
        self.H5 = CustomButton(self.centralwidget)
        self.H6 = CustomButton(self.centralwidget)
        self.H7 = CustomButton(self.centralwidget)
        self.H8 = CustomButton(self.centralwidget)
        self.buttons = [
            [self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8],
            [self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8],
            [self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8],
            [self.D1, self.D2, self.D3, self.D4, self.D5, self.D6, self.D7, self.D8],
            [self.E1, self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8],
            [self.F1, self.F2, self.F3, self.F4, self.F5, self.F6, self.F7, self.F8],
            [self.G1, self.G2, self.G3, self.G4, self.G5, self.G6, self.G7, self.G8],
            [self.H1, self.H2, self.H3, self.H4, self.H5, self.H6, self.H7, self.H8]]
        new_x = 300
        i = 0
        for rowB in self.buttons:
            new_y = 60
            j = 0
            for button in rowB:
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
        self.A1.clicked.connect(lambda: self.action(self.A1))
        self.A2.clicked.connect(lambda: self.action(self.A2))
        self.A3.clicked.connect(lambda: self.action(self.A3))
        self.A4.clicked.connect(lambda: self.action(self.A4))
        self.A5.clicked.connect(lambda: self.action(self.A5))
        self.A6.clicked.connect(lambda: self.action(self.A6))
        self.A7.clicked.connect(lambda: self.action(self.A7))
        self.A8.clicked.connect(lambda: self.action(self.A8))
        self.B1.clicked.connect(lambda: self.action(self.B1))
        self.B2.clicked.connect(lambda: self.action(self.B2))
        self.B3.clicked.connect(lambda: self.action(self.B3))
        self.B4.clicked.connect(lambda: self.action(self.B4))
        self.B5.clicked.connect(lambda: self.action(self.B5))
        self.B6.clicked.connect(lambda: self.action(self.B6))
        self.B7.clicked.connect(lambda: self.action(self.B7))
        self.B8.clicked.connect(lambda: self.action(self.B8))
        self.C1.clicked.connect(lambda: self.action(self.C1))
        self.C2.clicked.connect(lambda: self.action(self.C2))
        self.C3.clicked.connect(lambda: self.action(self.C3))
        self.C4.clicked.connect(lambda: self.action(self.C4))
        self.C5.clicked.connect(lambda: self.action(self.C5))
        self.C6.clicked.connect(lambda: self.action(self.C6))
        self.C7.clicked.connect(lambda: self.action(self.C7))
        self.C8.clicked.connect(lambda: self.action(self.C8))
        self.D1.clicked.connect(lambda: self.action(self.D1))
        self.D2.clicked.connect(lambda: self.action(self.D2))
        self.D3.clicked.connect(lambda: self.action(self.D3))
        self.D4.clicked.connect(lambda: self.action(self.D4))
        self.D5.clicked.connect(lambda: self.action(self.D5))
        self.D6.clicked.connect(lambda: self.action(self.D6))
        self.D7.clicked.connect(lambda: self.action(self.D7))
        self.D8.clicked.connect(lambda: self.action(self.D8))
        self.E1.clicked.connect(lambda: self.action(self.E1))
        self.E2.clicked.connect(lambda: self.action(self.E2))
        self.E3.clicked.connect(lambda: self.action(self.E3))
        self.E4.clicked.connect(lambda: self.action(self.E4))
        self.E5.clicked.connect(lambda: self.action(self.E5))
        self.E6.clicked.connect(lambda: self.action(self.E6))
        self.E7.clicked.connect(lambda: self.action(self.E7))
        self.E8.clicked.connect(lambda: self.action(self.E8))
        self.F1.clicked.connect(lambda: self.action(self.F1))
        self.F2.clicked.connect(lambda: self.action(self.F2))
        self.F3.clicked.connect(lambda: self.action(self.F3))
        self.F4.clicked.connect(lambda: self.action(self.F4))
        self.F5.clicked.connect(lambda: self.action(self.F5))
        self.F6.clicked.connect(lambda: self.action(self.F6))
        self.F7.clicked.connect(lambda: self.action(self.F7))
        self.F8.clicked.connect(lambda: self.action(self.F8))
        self.G1.clicked.connect(lambda: self.action(self.G1))
        self.G2.clicked.connect(lambda: self.action(self.G2))
        self.G3.clicked.connect(lambda: self.action(self.G3))
        self.G4.clicked.connect(lambda: self.action(self.G4))
        self.G5.clicked.connect(lambda: self.action(self.G5))
        self.G6.clicked.connect(lambda: self.action(self.G6))
        self.G7.clicked.connect(lambda: self.action(self.G7))
        self.G8.clicked.connect(lambda: self.action(self.G8))
        self.H1.clicked.connect(lambda: self.action(self.H1))
        self.H2.clicked.connect(lambda: self.action(self.H2))
        self.H3.clicked.connect(lambda: self.action(self.H3))
        self.H4.clicked.connect(lambda: self.action(self.H4))
        self.H5.clicked.connect(lambda: self.action(self.H5))
        self.H6.clicked.connect(lambda: self.action(self.H6))
        self.H7.clicked.connect(lambda: self.action(self.H7))
        self.H8.clicked.connect(lambda: self.action(self.H8))
        self.moving.raise_()


if __name__ == "__main__":
    os.system('cls')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
