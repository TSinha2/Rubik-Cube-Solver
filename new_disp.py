import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtWidgets import QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt

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


class CubeNet(QWidget):
    def __init__(self):
        super(CubeNet, self).__init__()

        self.setWindowTitle("Cube Net")

        layout = QGridLayout()

        # Yellow side with a grid of green squares
        colors_green = [['green', 'green', 'green'],
                        ['green', 'green', 'green'],
                        ['green', 'green', 'green']]
        layout.addWidget(CubeSide(colors_green), 0, 1)

        # White side with a grid of red squares
        colors_red = [['red', 'red', 'red'],
                      ['red', 'red', 'red'],
                      ['red', 'red', 'red']]
        layout.addWidget(CubeSide(colors_red), 2, 1)

        # Red side with a grid of blue squares
        colors_blue = [['blue', 'blue', 'blue'],
                       ['blue', 'blue', 'blue'],
                       ['blue', 'blue', 'blue']]
        layout.addWidget(CubeSide(colors_blue), 1, 1)

        # Blue side with a grid of yellow squares
        colors_yellow = [['yellow', 'yellow', 'yellow'],
                         ['yellow', 'yellow', 'yellow'],
                         ['yellow', 'yellow', 'yellow']]
        layout.addWidget(CubeSide(colors_yellow), 1, 0)

        # Orange side with a grid of purple squares
        colors_purple = [['purple', 'purple', 'purple'],
                         ['purple', 'purple', 'purple'],
                         ['purple', 'purple', 'purple']]
        layout.addWidget(CubeSide(colors_purple), 1, 2)

        # Green side with a grid of orange squares
        colors_orange = [['orange', 'orange', 'orange'],
                         ['orange', 'orange', 'orange'],
                         ['orange', 'orange', 'orange']]
        layout.addWidget(CubeSide(colors_orange), 1, 3)

        self.setLayout(layout)


app = QApplication(sys.argv)

window = CubeNet()
window.show()

app.exec()
