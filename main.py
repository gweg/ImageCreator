from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import numpy as np

# https://www.programiz.com/python-programming/methods/built-in/property
import sys

class ImageCreator:
    def __init__(self):
        self.binary_matrix = []
        self._bin_value = ""
        self._dec_value = 0
    def int_to_string_bin(self,value):
        if type(value) == int:
            #convert to string
            value = "".join(bin(value))
            try:
                if value.index('0b')>-1:
                    value = value[2:]
            except:
                pass
            for x in value:
                if int(x) > 1 or int(x) < 0:
                    raise ValueError("value must be composed of 0 or 1")
                    value = ""
            return value
        else:
            raise ValueError("input value must be decimal")
            return ""
    def string_bin_to_int(self,value):
        if type(value) == str:
            try:
                if value.index('0b')>-1:
                    value = value[2:]
            except:
                pass
            value = int(value, 2)
        else:
            raise ValueError("value must be string type")
            value = -1
        return value

    @property
    def bin_value(self):
        return self._bin_value
    @bin_value.setter
    def bin_value(self,value):
        '''
        convert value to bin decimal and bin str
        :param bin_value:
        :return:
        '''
        # int input type
        if type(value) == int:
            self._bin_value = self.int_to_string_bin(value)
            try:
                self._dec_value = value
            except:
                raise ValueError("invalid int value")
        # string input type
        elif type(value) == str:
            try:
                if value.index('0b'):
                    value = value[2:]
            except:
                pass
            self._bin_value = value
            self._dec_value = self.string_bin_to_int(value)
        else:
            raise ValueError("invalid value")


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



    def load_dec_value(self,dec_value):
        pass

    def paint_binary_matrix(self,painter,x,y,width,height):
        # get the bin_value

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
        self.imagecreator.bin_value = "1111111110000001100000011000000110000001100000011000000111111111"
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
        self.imagecreator.bin_value = 255
        self.imagecreator.paint_binary_matrix(painter,100,15,800,600)

        #painter.drawRect(100, 15, 400, 200)



App = QApplication(sys.argv)

window = Window()
sys.exit(App.exec())