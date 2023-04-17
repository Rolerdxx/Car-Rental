import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import pyqtcss
from Pages.MainPage import MainWindow

stylesheet = """
        MainWindow {
            background-image: url("./images/mainimage.jpg"); 
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
