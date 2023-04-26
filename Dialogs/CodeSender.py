from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
import random
import string
from Helpers.EmailSender import SendEmail


def get_random_string(length):
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class CodeSenderDialog(QDialog):
    def __init__(self, email, parent=None):
        super().__init__(parent)
        loadUi("./UI/sendcode_D.ui", self)
        self.code = get_random_string(8)
        self.email = email
        SendEmail(self.email, "Verification code to reset password", '<strong>Your Code Is:' + self.code + '</strong>')

    def getcode(self):
        return self.code

    def getcodeentered(self):
        return self.codelab.text()
