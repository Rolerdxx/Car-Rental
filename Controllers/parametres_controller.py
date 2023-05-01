def getallmarques(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT distinct marque FROM voiture where marque IS NOT NULL")
    return mycursor.fetchall()


def getalltransmissions(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT distinct transmission  FROM voiture where transmission is not NULL")
    return mycursor.fetchall()


def getallcarburants(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT distinct carburant  FROM voiture where carburant is not NULL")
    return mycursor.fetchall()
