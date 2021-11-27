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

    @property
    def bin_value(self):
        return self.bin_value
    @bin_value.setter
    def bin_value(self,bin_value):
        self.bin_value = bin_value

    def set_binary_matrix(self,matrix_x_size,matrix_y_size):
        '''
        square size1
        :param matix_size:
        :return:
        '''
        self.binary_matrix_x_size = matrix_x_size
        self.binary_matrix_y_size = matrix_y_size
        self.binary_matrix=list(range(0,self.binary_matrix_x_size*self.binary_matrix_y_size))
        self.bin_value = "".join(['0'*((self.binary_matrix_x_size)*(self.binary_matrix_y_size))])
        self.dec_value = int(self.bin_value,2)
        pass

    def load_bin_value(self,bin_value):
        try:
            if bin_value.index('0b'):
                self.bin_value = bin_value[2:]
        except:
            self.bin_value = bin_value

    def load_dec_value(self,dec_value):
        pass

    def paint_binary_matrix(self,painter,x,y,width,height):
        # get the bin_value
        self.bin_value = int(self.bin_value,2)

        i = len(self.bin_value)-1
        for ry in range(y,y+height,int(height/self.binary_matrix_y_size)+1):
            for rx in range(x,x+width,int(width/self.binary_matrix_x_size)+1):
                bit=self.bin_value[i]
                #print (bit)
                if i<0 : break # if bin value is lesser than bin matrix size
                #painter.setPen(QPen(Qt.green, 1, Qt.SolidLine))
                if bit == '1':
                    painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
                    painter.drawRect(rx, ry, int(width/self.binary_matrix_x_size), int(height/self.binary_matrix_y_size))
                else:
                    painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
                    painter.drawRect(rx, ry, int(width / self.binary_matrix_x_size),int(height / self.binary_matrix_y_size))
                #print(rx,ry, int(width/self.binary_matrix_x_size), int(height/self.binary_matrix_y_size))
                i-=1




class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.imagecreator=ImageCreator()
        self.imagecreator.set_binary_matrix(8,8)
        self.imagecreator.load_bin_value("1111111110000001100000011000000110000001100000011000000111111111")
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
        self.imagecreator.dec_value+=1
        self.imagecreator.paint_binary_matrix(painter,100,15,800,600)
        #painter.drawRect(100, 15, 400, 200)



App = QApplication(sys.argv)

window = Window()
sys.exit(App.exec())