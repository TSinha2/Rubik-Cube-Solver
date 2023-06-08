from lib2to3.pytree import convert
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QGridLayout

class CubeSide(QWidget):
    def __init__(self, colors):
        super(CubeSide, self).__init__()

        layout = QGridLayout()

        for row in range(3):
            for col in range(3):
                color_widget = QWidget()
                # color_widget.setFixedSize(85, 85)               
                color_widget.setAutoFillBackground(True)
                palette = color_widget.palette()
                palette.setColor(QPalette.Window, QColor(colors[row][col]))
                color_widget.setPalette(palette)
                layout.addWidget(color_widget, row, col)

        self.setLayout(layout)


def cubeFace2CubeNet(side):
    conversion = {'o': 'orange', 'b': 'blue', 'g': 'green', 'r': 'red', 'w': 'white', 'y': 'yellow'}
    CubeNetFace = []
    for row in side:
        CubeNetFace.append(list(map(lambda i: conversion[i], row)))
    
    return CubeNetFace

class CubeNet(QWidget):
    def __init__(self):
        super(CubeNet, self).__init__()

        self.setWindowTitle("Cube Net")

        layout = QGridLayout()

        # Yellow side 

        colors_yellow = [['yellow', 'yellow', 'yellow'],
                         ['yellow', 'yellow', 'yellow'],
                         ['yellow', 'yellow', 'yellow']]

        layout.addWidget(CubeSide(colors_yellow), 0, 1)

        # White side 
        colors_white = [['white', 'white', 'white'],
                         ['white', 'white', 'white'],
                         ['white', 'white', 'white']]                      
        layout.addWidget(CubeSide(colors_white), 2, 1)

        # Blue side
        colors_blue = [['blue', 'blue', 'blue'],
                       ['blue', 'blue', 'blue'],
                       ['blue', 'blue', 'blue']]
        layout.addWidget(CubeSide(colors_blue), 1, 1)

        # Blue side with a grid of yellow squares
        colors_orange = [['orange', 'orange', 'orange'],
                         ['orange', 'orange', 'orange'],
                         ['orange', 'orange', 'orange']]

        layout.addWidget(CubeSide(colors_orange), 1, 0)

        # Red side
        colors_red = [['red', 'red', 'red'],
                      ['red', 'red', 'red'],
                      ['red', 'red', 'red']]
        layout.addWidget(CubeSide(colors_red), 1, 2)

        # Green side 
        colors_green = [['green', 'green', 'green'],
                        ['green', 'green', 'green'],
                        ['green', 'green', 'green']]

        layout.addWidget(CubeSide(colors_green), 1, 3)

        self.setLayout(layout)


app = QApplication(sys.argv)

window = CubeNet()
window.show()

app.exec()
