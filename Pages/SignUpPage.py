from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog

class SignupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignupWindow,self).__init__()
        loadUi('Signup.ui',self)

        self.signupbtn.clicked.connect(self.handle_signup)
    def handle_signup(self):
        nom1 = self.nomline.text()
        prenom1 = self.prline.text()
        email1 = self.mailine.text()
        password1 = self.mdpline.text()

        signupfunction(nom1, prenom1, email1, password1)

app = QtWidgets.QApplication([])
window = SignupWindow()
window.show()
app.exec_()


