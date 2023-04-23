from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from Helpers.ImageLabel import getImageLabel
from PyQt5.QtGui import QPixmap


class CarPage(QDialog):
    def __init__(self, main):
        super(CarPage, self).__init__()
        loadUi("./UI/carpage.ui", self)
        self.main = main
        self.car = main.cars[main.selected]
        self.backButton.clicked.connect(self.goback)
        self.filldata()

    def goback(self):
        self.main.widget.setCurrentIndex(0)

    def filldata(self):
        pixmap = QPixmap()
        pixmap.loadFromData(self.car[0], 'jpg')
        self.imagelabel.setPixmap(pixmap)
        self.marquelabel.setText(self.car[1])
        self.modelelabel.setText(self.car[2])
        self.carburantlabel.setText(self.car[3])
        self.placeslabel.setText(str(self.car[4]))
        self.transmissionlabel.setText(self.car[5])
        self.statelabel.setText(str(self.car[6]))
        self.pricelabel.setText(str(self.car[7])+" DH")

