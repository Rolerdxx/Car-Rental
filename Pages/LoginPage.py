from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("./UI/login_D.ui", self)
        self.passline.setEchoMode(QtWidgets.QLineEdit.Password)

    def getemail(self):
        return self.emailline.text()

    def getpassword(self):
        return self.passline.text()