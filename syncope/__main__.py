import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel
)

from syncope.constants import CLEFS
from syncope.exercises.clef import make_tmpfile
from random import randint

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "Syncope"
        self.setWindowTitle(self.title)

        tmpclef = CLEFS[randint(0, 3)]
        make_tmpfile(clef=tmpclef)

        label = QLabel(self)
        pixmap = QPixmap('tmp.cropped.png')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
