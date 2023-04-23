from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap


class CarPage(QDialog):
    def __init__(self, main, test):
        super(CarPage, self).__init__()
        loadUi("./UI/carpage.ui", self)
        self.main = main
        self.imagelabel.setText(test)
        print(main.cars)
        self.backButton.clicked.connect(self.goback)

    def goback(self):
        self.main.widget.setCurrentIndex(0)

