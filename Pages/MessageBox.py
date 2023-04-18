from PyQt5 import QtWidgets


def msgbox(title, message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

    returnValue = msgBox.exec()
    if returnValue == QtWidgets.QMessageBox.Ok:
        print('OK clicked')
