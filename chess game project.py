import sys 
from PyQt5.Qtwidgets import QApplication, QMainwindow, Qwidget, QgridLayout, Qlabel
from PyQt5.QtGui import Qpixmap

class ChessGame(QMainwindow):
    def __init__(self):
        super().__int__()
        
        #set up main window 
        self.setWindowTitle("Chess Game")
        self.setGeometry(100, 100, 500, 500)
        #creating a central widget to hold the chess board
        central_widget = QWidget(self)
        self.setCentralWidget(cental_widget)
        #creating a grid layout for the chess board
        grid_layout = QGridLayout(Central_widget)

        #adding labels for the chess board
        self.squares =[]
        for row in range(8):
            self.square.append([])
            
