from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog


class EmailGetterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("./UI/emailgetter_D.ui", self)

    def getemail(self):
        return self.emailline.text()
