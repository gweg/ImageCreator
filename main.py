from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QLineEdit
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt,QTimer
import numpy as np

# https://www.programiz.com/python-programming/methods/built-in/property

# screensot
# https://stackoverflow.com/questions/51361674/is-there-a-way-to-take-screenshot-of-a-window-in-pyqt5-or-qt5
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
                    value = ""
                    raise ValueError("value must be composed of 0 or 1")
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
        return self._dec_value
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
            self._dec_value = value
        # string input type
        elif type(value) == str:
            try:
                value.index('0b')

            except:
                pass
            else:
                value = value[2:]
            value=value.rjust(self.matrix_size,"0")
            self._bin_value = value
            self._dec_value = self.string_bin_to_int(value)
            pass
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
        self.matrix_size = (self.binary_matrix_x_size) * (self.binary_matrix_y_size)
        self.binary_matrix=list(range(0,self.matrix_size))
        self._bin_value = "".join(['0'*self.matrix_size])
        self._dec_value = int(self._bin_value,2)



    def load_dec_value(self,dec_value):
        pass

    def paint_binary_matrix(self,painter,x,y,width,height):
        # get the bin_value

        # i = len(self._bin_value)-1
        i=0
        for ry in range(y,y+height,int(height/self.binary_matrix_y_size)+1):
            for rx in range(x,x+width,int(width/self.binary_matrix_x_size)+1):
                bit=self._bin_value[i]
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
                i+=1




class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.counter=0
        self.imagecreator=ImageCreator()
        self.imagecreator.set_binary_matrix(8,8)
        self.imagecreator.bin_value = "1111111110000001100000011000000110000001100000011000000111111111"

        self.title = "PyQt5 Drawing Rectangle"
        self.top = 100
        self.left = 100
        self.width = 1280
        self.height = 768
        self.resize(1024,768)
        self.textbox_bin_value =QLineEdit(self)
        self.textbox_bin_value.setText(str(self.imagecreator.bin_value))
        self.textbox_bin_value.move(64,self.height-100)
        self.textbox_bin_value.setFixedWidth(1000)
        self.textbox_bin_value.setStyleSheet("font-size: 20pt")

        self.textbox_dec_value = QLineEdit(self)
        self.textbox_dec_value.setText(str(self.imagecreator._dec_value))
        self.textbox_dec_value.move(64, self.height - 50)
        self.textbox_dec_value.setFixedWidth(1000)
        font = QtGui.QFont("Courier New", 15)
        self.textbox_dec_value.setFont(font)
        self.textbox_bin_value.setFont(font)
        #self.textbox_dec_value.setStyleSheet("font-name: corrier-new;font-size: 20pt")

        self.InitWindow()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(0)
    def update(self):
        self.repaint()

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
        self.imagecreator.bin_value = bin(self.counter)

        self.textbox_bin_value.setText(str(bin(self.counter))[2:].rjust(self.imagecreator.matrix_size,"0").replace('1','█').replace('0',' '))
        self.textbox_dec_value.setText(str(self.counter))
        #self.label.textbox(str(bin(self.counter)).rjust(self.imagecreator.matrix_size,"0"))
        self.counter+=1
        self.imagecreator.paint_binary_matrix(painter,100,15,800,600)
        #print(self.counter)
        #painter.drawRect(100, 15, 400, 200)



App = QApplication(sys.argv)

window = Window()
sys.exit(App.exec())