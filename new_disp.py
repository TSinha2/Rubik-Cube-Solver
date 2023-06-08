import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtWidgets import QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt

class CubeSide(QWidget):
    def __init__(self, color):
        super(CubeSide, self).__init__()

        layout = QGridLayout()

        for row in range(3):
            for col in range(3):
                color_widget = QWidget()
                color_widget.setAutoFillBackground(True)
                palette = color_widget.palette()
                palette.setColor(QPalette.Window, QColor(color))
                color_widget.setPalette(palette)
                layout.addWidget(color_widget, row, col)

        self.setLayout(layout)


class CubeNet(QWidget):
    def __init__(self):
        super(CubeNet, self).__init__()

        self.setWindowTitle("Cube Net")

        layout = QGridLayout()

        # Yellow side
        layout.addWidget(CubeSide('yellow'), 0, 1)

        # White side
        layout.addWidget(CubeSide('white'), 2, 1)

        # Red side
        layout.addWidget(CubeSide('red'), 1, 1)

        # Blue side
        layout.addWidget(CubeSide('blue'), 1, 0)

        # Orange side
        layout.addWidget(CubeSide('orange'), 1, 2)

        # Green side
        layout.addWidget(CubeSide('green'), 1, 3)

        self.setLayout(layout)


app = QApplication(sys.argv)

window = CubeNet()
window.show()

app.exec_()
