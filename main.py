import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import pyqtcss
from Pages.MainPage import MainWindow

style_string = pyqtcss.get_style("dark_orange")
app = QApplication(sys.argv)
app.setStyleSheet(style_string)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow(widget)
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(1067)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
