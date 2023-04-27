

from PyQt5 import QtCore, QtGui, QtWidgets


class resevationPage(object):
    id = 0
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(514, 301)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 348, 159))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.datedebut = QtWidgets.QDateEdit(self.layoutWidget)
        self.datedebut.setMinimumDate(QtCore.QDate(2023, 4, 26))
        self.datedebut.setObjectName("datedebut")
        self.horizontalLayout.addWidget(self.datedebut)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.datefin = QtWidgets.QDateEdit(self.layoutWidget)
        self.datefin.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2023, 4, 26), QtCore.QTime(0, 0, 0)))
        self.datefin.setObjectName("datefin")
        self.horizontalLayout_2.addWidget(self.datefin)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.price = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.price.setFont(font)
        self.price.setObjectName("price")
        self.horizontalLayout_3.addWidget(self.price)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.reserve) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Reservation Page"))
        self.label.setText(_translate("Dialog", "Date de debut:"))
        self.label_2.setText(_translate("Dialog", "Date de fin:"))
        self.label_3.setText(_translate("Dialog", "Price :"))
        self.price.setText(_translate("Dialog", "0"))

    def reserve(self):
        resevationPage.id+=1
        dateDB=self.datedebut.date()
        dateFN=self.datefin.date()
        #i need the current user id
        #i need the car id
        #i need the price by day of car selected
        return 0

