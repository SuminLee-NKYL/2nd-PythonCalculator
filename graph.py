import sys
import numpy as np
from PyQt5.QtWidgets import *
from math import *

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Graph(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.sc = MplCanvas()
        toolbar = NavigationToolbar(self.sc, self)

        self.equation = QLineEdit()
        button = QPushButton("Draw")
        button.clicked.connect(self.draw_graph)
        layout_equation_button = QHBoxLayout()
        layout_equation_button.addWidget(self.equation)
        layout_equation_button.addWidget(button)

        layout = QVBoxLayout()
        layout.addLayout(layout_equation_button)
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)

        self.setLayout(layout)
        self.show()

    def draw_graph(self):
        formula = self.equation.text()
        xs = np.linspace(0, 10, 101)
        
        try:
            ys = [eval(formula) for x in xs]
            self.sc.axes.cla()
            self.sc.axes.plot(xs, ys, color = 'blue', lw = 1)
            self.sc.axes.set_xlabel("x")
            self.sc.axes.set_ylabel("y")
            self.sc.axes.grid()
            self.sc.draw()
        except Exception as e:
            QMessageBox.critical(self, "Error", "Wrong equation : {}".format(e))
