import re

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets



class SignupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("./UI/Singup.ui", self)
        self.mdpline.setEchoMode(QtWidgets.QLineEdit.Password)
    def datagets(self):
        data=[]
        data.append(self.nomline.text())
        data.append(self.prline.text())
        data.append(self.mailine.text())
        data.append(self.mdpline.text())
        return data

    def passwordvalidation(self, mdpline):
        mdp = mdpline.text()
        if(len(mdp)<8):
            return False
        if not re.search("[a-z]", mdp):
            return False
        if not re.search("[A-Z]", mdp):
            return False
        if not re.search("[0-9]", mdp):
            return False
        return True



