import mysql.connector
from Controllers.User_Controller import login
from Controllers.Car_Controller import getallcars, getsomecars
from Controllers.parametres_controller import getallmarques, getallcarburants, getalltransmissions


class CarRentalDB:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="carrental"
    )

    def login(self, email):
        return login(self.db, email)

    def getallcars(self):
        return getallcars(self.db)

    def getsomecars(self, marque, modele, carburant, place, transmission, prix):
        return getsomecars(self.db, marque, modele, carburant, place, transmission, prix)

    def getmarques(self):
        return getallmarques(self.db)

    def getcarburants(self):
        return getallcarburants(self.db)

    def gettransmissions(self):
        return getalltransmissions(self.db)
