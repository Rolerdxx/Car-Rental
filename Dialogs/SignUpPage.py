import re
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
from Helpers.MessageBox import msgbox
from Dialogs.CodeSender import CodeSenderDialog
from Helpers.Encrypt import EncryptPass


class SignupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("./UI/Singup.ui", self)
        self.mdpline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Sibtn.clicked.connect(self.passwordvalidation)
        self.Cnclbtn.clicked.connect(self.reject)

    def datagets(self):
        data = []
        data.append(self.nomline.text())
        data.append(self.prline.text())
        data.append(self.mailine.text())
        hashh = EncryptPass(self.mdpline.text())
        data.append(hashh)
        return data

    def passwordvalidation(self):
        sipassword = self.mdpline.text()
        siname = self.nomline.text()
        siprenom = self.prline.text()
        simail = self.mailine.text()
        if siname == "":
            msgbox("Error", "last name line is empty")
        elif siprenom == "":
            msgbox("Error", "first name line is empty")
        elif not re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', simail):
            msgbox("Error", "email invalid")
        elif len(sipassword) < 8:
            msgbox("Error", "password has to longer than 7 characters")
        elif sipassword.isdigit():
            msgbox("Error", "password should contain letters")
        elif sipassword.isupper():
            msgbox("Error", "password should contain lower characters")
        else:
            emailveri = CodeSenderDialog(email=simail)
            res = emailveri.exec()
            if res:
                if emailveri.getcode() == emailveri.getcodeentered():
                    self.accept()
                else:
                    msgbox("Error", "Wrong code")
            else:
                self.reject()


