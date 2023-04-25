from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog


class SignupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("./UI/Singup.ui", self)
    def datagets(self):
        data=[]
        data.append(self.nomline.text())
        data.append(self.prline.text())
        data.append(self.mailine.text())
        data.append(self.mdpline.text())
        return data




