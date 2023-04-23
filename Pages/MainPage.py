from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from Database.CarRental_database import CarRentalDB
from Pages.MessageBox import msgbox
from Pages.LoginPage import LoginDialog
from Pages.CarPage import CarPage
from Helpers.ImageLabel import getImageLabel
import bcrypt


# Class dyal main page


class MainWindow(QDialog):
    def __init__(self, widget):  # Hada constructor hadchi hna kayexecuta fach kat7el l page
        super(MainWindow, self).__init__()
        loadUi("./UI/tabw.ui", self)
        self.widget = widget
        self.currentuser = "Guest"
        self.db = CarRentalDB()
        self.carpagecounter = 0
        self.cars = []
        self.selected = None
        # self.tableWidget.setColumnWidth(0,250)
        self.loaddata()
        self.Filter.clicked.connect(self.filter)  # connect Filter button m3a fonction dyalha
        self.loginbutton.clicked.connect(self.login)  # connect login button m3a fonction dyalha
        self.tableWidget.itemClicked.connect(self.select)
        self.reserveButton.clicked.connect(self.switchpage)

    def loaddata(self):  # fonction katjib ga3 cars mn database o kat afichihom f tableWidget
        self.cars = self.db.getallcars()
        self.showdata(self.cars)

    def showdata(self, cars):  # had fonction katched cars li jawha f parametre o kataffechihom f table
        for row_number, row_data in enumerate(cars):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if column_number == 0:
                    item = getImageLabel(self, column_data)
                    self.tableWidget.setCellWidget(row_number, column_number, item)
                elif column_number == 6:
                    if item == "1":
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem("Available"))
                    else:
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem("Reserved"))
                else:
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
        self.tableWidget.verticalHeader().setDefaultSectionSize(80)

    def filter(self):
        print("Search!!!!A")

    def select(self):
        self.selected = self.tableWidget.currentRow()

    def switchpage(self):
        if self.selected is not None:
            carpage = CarPage(self)
            self.carpagecounter += 1
            self.widget.addWidget(carpage)
            self.widget.setCurrentIndex(self.carpagecounter)

    def login(self):
        logdialog = LoginDialog(self)
        logdialog.setFixedHeight(400)
        logdialog.setFixedWidth(711)
        logdialog.setWindowTitle("Login Page")
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