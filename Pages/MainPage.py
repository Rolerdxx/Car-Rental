from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from Database.CarRental_database import CarRentalDB
from Pages.MessageBox import msgbox
from Pages.LoginPage import LoginDialog
from PyQt5.QtGui import QPixmap
import bcrypt


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("./UI/tabw.ui", self)
        self.currentuser = "Guest"
        self.db = CarRentalDB()
        # self.tableWidget.setColumnWidth(0,250)
        self.loaddata()
        self.pushButton.clicked.connect(self.click)
        self.loginbutton.clicked.connect(self.login)

    def loaddata(self):
        cars = self.db.getallcars()
        for row_number, row_data in enumerate(cars):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if column_number == 0:
                    item = self.getImageLabel(column_data)
                    self.tableWidget.setCellWidget(row_number, column_number, item)
                elif column_number == 6:
                    if item == "1":
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem("Available"))
                    else:
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem("Reserved"))
                else:
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
        self.tableWidget.verticalHeader().setDefaultSectionSize(80)

    def click(self):
        print("Search!!!!A")

    def login(self):
        logdialog = LoginDialog(self)
        logdialog.setFixedHeight(400)
        logdialog.setFixedWidth(711)
        response = logdialog.exec()
        if response:
            email = logdialog.getemail()
            password = logdialog.getpassword()
            user = self.db.login(email)
            if user:
                password = password.encode('utf-8')
                hashed = user[4][2:-1]
                hashed = hashed.encode('utf-8')
                if bcrypt.checkpw(password, hashed):
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
