from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog


class ReservationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("./UI/reservation.ui", self)
