import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.numbers = []
        self.lb = QLabel(str(self.numbers))

        self.initUI()

    def initUI(self):
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)

        self.btn = QPushButton('quit', self)
        self.btn.clicked.connect(QCoreApplication.instance().quit)

        self.btn2 = QPushButton('draw', self)
        self.btn2.clicked.connect(self.lotto)

        form_lbx.addWidget(self.lb)
        form_lbx.addWidget(self.btn)
        form_lbx.addWidget(self.btn2)

        #tlb.valueChanged.connect()

        self.setWindowTitle('application')
        self.setGeometry(300, 300, 300, 200)
        self.update()
        self.show()

    def lotto(self):
        b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.numbers = random.sample(b, 6)
        self.lb.setText(str(self.numbers))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


