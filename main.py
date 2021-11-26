from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import numpy as np

# https://www.programiz.com/python-programming/methods/built-in/property
import sys

class ImageCreator:
    def __init__(self):
        self.binary_matrix=[]
    def set_binary_matrix(self,matrix_x_size,matrix_y_size):
        '''
        square size
        :param matix_size:
        :return:
        '''
        self.binary_matrix_x_size = matrix_x_size
        self.binary_matrix_y_size = matrix_y_size
        self.binary_matrix=list(range(0,self.binary_matrix_x_size*self.binary_matrix_y_size))
        #self.binary_number=


    def paint_binary_matrix(self,painter,x,y,width,height):

        for ry in range(y,y+height,int(height/self.binary_matrix_y_size)+1):
            for rx in range(x,x+width,int(width/self.binary_matrix_x_size)+1):
                #painter.setPen(QPen(Qt.green, 1, Qt.SolidLine))
                painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
                painter.drawRect(rx, ry, int(width/self.binary_matrix_x_size), int(height/self.binary_matrix_y_size))
                #print(rx,ry, int(width/self.binary_matrix_x_size), int(height/self.binary_matrix_y_size))





class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.imagecreator=ImageCreator()
        self.imagecreator.set_binary_matrix(64,64)

        self.title = "PyQt5 Drawing Rectangle"
        self.top = 100
        self.left = 100
        self.width = 1280
        self.height = 768
        self.resize(1024,768)
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        #painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        # painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        #painter.setBrush(QBrush(Qt.green, Qt.DiagCrossPattern))
        self.imagecreator.paint_binary_matrix(painter,100,15,800,600)
        #painter.drawRect(100, 15, 400, 200)



App = QApplication(sys.argv)

window = Window()
sys.exit(App.exec())