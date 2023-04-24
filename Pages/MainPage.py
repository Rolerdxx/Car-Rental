from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from Database.CarRental_database import CarRentalDB
from Pages.MessageBox import msgbox
from Pages.LoginPage import LoginDialog
from PyQt5.QtGui import QPixmap
import bcrypt


# Class dyal main page


class MainWindow(QDialog):
    def __init__(self):  # Hada constructor hadchi hna kayexecuta fach kat7el l page
        super(MainWindow, self).__init__()
        loadUi("./UI/tabw.ui", self)
        self.currentuser = "Guest"
        self.db = CarRentalDB()
        # self.tableWidget.setColumnWidth(0,250)
        self.loaddata()
        self.Filter.clicked.connect(self.filter)  # connect Filter button m3a fonction dyalha
        self.loginbutton.clicked.connect(self.login)  # connect login button m3a fonction dyalha

    def loaddata(self):  # fonction katjib ga3 cars mn database o kat afichihom f tableWidget
        cars = self.db.getallcars()
        self.showdata(cars)
    def loaddata2(self,marque,modele,carburant,place,transmission,prix):
        print("khdama")
        cars2=self.db.getsomecars(marque,modele,carburant,place,transmission,prix)
        print("khdama 2")
        self.showdata(cars2)

    def showdata(self, cars):  # had fonction katched cars li jawha f parametre o kataffechihom f table
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

    def filter(self):
       marque=self.marque.currentText()
       modele = self.modele.text()
       carburant = self.carburant.currentText()
       place = self.place.text()
       transmission=self.transmission.currentText()
       prix=self.prix.text()
       error=self.error
       if(marque=="none" and transmission=="none" and carburant=="none" and prix=="" and place=="" and modele==""):
           error.setText("empty champs!!!")
       else:
           self.loaddata2(marque,modele,carburant,place,transmission,prix)


















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
