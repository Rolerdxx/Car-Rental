from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from Helpers.ImageLabel import getImageLabel
from PyQt5.QtGui import QPixmap
from Pages.reservation import reservationPage
class CarPage(QDialog):
    def __init__(self, main):
        super(CarPage, self).__init__()
        loadUi("./UI/carpage.ui", self)
        self.main = main
        self.car = main.cars[main.selected]
        self.backButton.clicked.connect(self.goback)
        self.reserveButton.clicked.connect(self.reserveit)
        self.filldata()

    def goback(self):
        self.main.widget.setCurrentIndex(0)

    def filldata(self):
        pixmap = QPixmap()
        pixmap.loadFromData(self.car[1], 'jpg')
        self.imagelabel.setPixmap(pixmap)
        self.marquelabel.setText(self.car[2])
        self.modelelabel.setText(self.car[3])
        self.carburantlabel.setText(self.car[4])
        self.placeslabel.setText(str(self.car[5]))
        self.transmissionlabel.setText(self.car[6])
        self.statelabel.setText(str(self.car[7]))
        self.pricelabel.setText(str(self.car[8])+" DH")

    def reserveit(self,userid):
        state=self.statelabel.text()
        price=self.pricelabel.text()
        carid=self.car[0]
        reservationPage.reserveIt(carid,userid,price)
        if state=="1":
            self.Dialog = QtWidgets.QDialog()
            self.ui = reservationPage()
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()
