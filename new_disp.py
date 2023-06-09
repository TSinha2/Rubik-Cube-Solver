import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from cube import Cube
from numpy import fliplr

class CubeSide(QWidget):
    def __init__(self, colors):
        super(CubeSide, self).__init__()

        layout = QGridLayout()

        for row in range(3):
            for col in range(3):
                color_widget = QWidget()
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

        # Algorithm input
        algorithm_input = QLineEdit()
        algorithm_input.setPlaceholderText("Enter algorithm")
        layout.addWidget(algorithm_input, 0, 0, 1, 4)

        # Cube
        test_cube = Cube()
        test_cube.algorithm_parser("D' L2 F' R2 B2 L U2 D' L' R' U2 D L' F' B' R F2 D B D' R U2 R2 U L2")

        # Yellow side
        colors_yellow = cubeFace2CubeNet(test_cube.get_cube()[1])
        self.yellow_side = CubeSide(colors_yellow)
        layout.addWidget(self.yellow_side, 1, 1)

        # White side
        colors_white = cubeFace2CubeNet(test_cube.get_cube()[0])
        self.white_side = CubeSide(colors_white)
        layout.addWidget(self.white_side, 3, 1)

        # Blue side
        colors_blue = cubeFace2CubeNet(test_cube.get_cube()[2])
        self.blue_side = CubeSide(colors_blue)
        layout.addWidget(self.blue_side, 2, 1)

        # Orange side
        colors_orange = cubeFace2CubeNet(test_cube.get_cube()[5])
        self.orange_side = CubeSide(colors_orange)
        layout.addWidget(self.orange_side, 2, 0)

        # Red side
        colors_red = cubeFace2CubeNet(fliplr(test_cube.get_cube()[4]))
        self.red_side = CubeSide(colors_red)
        layout.addWidget(self.red_side, 2, 2)

        # Green side
        colors_green = cubeFace2CubeNet(fliplr(test_cube.get_cube()[3]))
        self.green_side = CubeSide(colors_green)
        layout.addWidget(self.green_side, 2, 3)

        self.setLayout(layout)

        # Connect Enter key press to algorithm parsing
        algorithm_input.returnPressed.connect(self.parse_algorithm)

        self.test_cube = test_cube

    def parse_algorithm(self):
        algorithm = self.sender().text()
        self.sender().clear()          
        self.test_cube.algorithm_parser(algorithm)
        self.update_cube_net()

    def update_cube_net(self):
        colors_yellow = cubeFace2CubeNet(self.test_cube.get_cube()[1])
        self.update_side_colors(self.yellow_side, colors_yellow)

        colors_white = cubeFace2CubeNet(self.test_cube.get_cube()[0])
        self.update_side_colors(self.white_side, colors_white)

        colors_blue = cubeFace2CubeNet(self.test_cube.get_cube()[2])
        self.update_side_colors(self.blue_side, colors_blue)

        colors_orange = cubeFace2CubeNet(self.test_cube.get_cube()[5])
        self.update_side_colors(self.orange_side, colors_orange)

        colors_red = cubeFace2CubeNet(self.test_cube.get_cube()[4])
        self.update_side_colors(self.red_side, colors_red)

        colors_green = cubeFace2CubeNet(self.test_cube.get_cube()[3])
        self.update_side_colors(self.green_side, colors_green)

    def update_side_colors(self, side_widget, colors):
        layout = side_widget.layout()
        for row in range(3):
            for col in range(3):
                color_widget = layout.itemAtPosition(row, col).widget()
                palette = color_widget.palette()
                palette.setColor(QPalette.Window, QColor(colors[row][col]))
                color_widget.setPalette(palette)

app = QApplication(sys.argv)

window = CubeNet()
window.show()

app.exec()
