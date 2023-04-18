import mysql.connector
from Controllers.User_Controller import login
from Controllers.Car_Controller import getallcars


class CarRentalDB:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="carrental"
    )

    def login(self, email):
        return login(self.db, email)

    def getallcars(self):
        return getallcars(self.db)
