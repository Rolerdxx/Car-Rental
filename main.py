import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap
import pyqtcss
import mysql.connector
import bcrypt


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="carrental"
)

currentuser = "Guest"

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("tabw.ui",self)
        # self.tableWidget.setColumnWidth(0,250)
        # self.tableWidget.setColumnWidth(1,100)
        # self.tableWidget.setColumnWidth(2,350)
        self.loaddata()
        self.pushButton.clicked.connect(self.click)
        self.loginbutton.clicked.connect(self.login)


    def loaddata(self):
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM voiture")
        cars = mycursor.fetchall()
        for row_number, row_data in enumerate(cars):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data);
                if (column_number == 1):
                    item = self.getImageLabel(column_data)
                    self.tableWidget.setCellWidget(row_number, column_number, item)
                else:
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
        self.tableWidget.verticalHeader().setDefaultSectionSize(80)
        # row = 0
        # self.tableWidget.setRowCount(len(cars))
        # for car in cars:
        #     image = self.getImageLabel(car[3])
        #     self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(car[1]))
        #     self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(image))
        #     self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(car[4]))
        #     self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(car[5])))
        #     self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(car[6]))
        #     self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(car[7]))
        #     self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(car[8])))
        #     row = row + 1
    def click(self):
        print("Search!!!!A")

    def login(self):
        logdialog = LoginDialog(self)
        logdialog.setStyleSheet(stylesheet2)
        response = logdialog.exec()
        if response:
            email = logdialog.getEmail()
            password = logdialog.getPassword()
            mycursor = db.cursor()
            query = "SELECT * FROM userr WHERE email='"+email+"'"
            mycursor.execute(query)
            user = mycursor.fetchone()
            if user:
                password = password.encode('utf-8')
                hash = user[4][2:-1]
                hash = hash.encode('utf-8')
                if bcrypt.checkpw(password, hash):
                    currentuser = user
                    self.loginbutton.move(1500, 1500)
                    txt = "Good Morning " + user[2] + " " + user[1] + "!"
                    self.label.setText(txt)
                else:
                    msgbox("Login", "Password Incorrect")
            else:
                msgbox("Login", "Cannot login")

    def getImageLabel(self, image):
        imageLabel = QtWidgets.QLabel(self)
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap = QPixmap()
        pixmap.loadFromData(image, 'jpg')
        imageLabel.setPixmap(pixmap)
        return imageLabel


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("login_D.ui",self)
        self.passline.setEchoMode(QtWidgets.QLineEdit.Password)

    def getEmail(self):
        print(self)
        return self.emailline.text()

    def getPassword(self):
        return self.passline.text()

def msgbox(title,message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

    returnValue = msgBox.exec()
    if returnValue == QtWidgets.QMessageBox.Ok:
        print('OK clicked')


stylesheet2 = """
        QDialog {
            background-image: url("./login.jpg"); 
            background-repeat: no-repeat; 
            background-position: center;
        }
"""


stylesheet = """
        MainWindow {
            background-image: url("./mainimage.jpg"); 
            background-repeat: no-repeat; 
            background-position: center;
        }
"""

style_string = pyqtcss.get_style("dark_blue")
app = QApplication(sys.argv)
app.setStyleSheet(style_string)
mainwindow = MainWindow()
mainwindow.setStyleSheet(stylesheet)
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(1067)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
