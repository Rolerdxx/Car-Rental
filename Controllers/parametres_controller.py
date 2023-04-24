def getallmarques(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT distinct modele  FROM voiture")
    return mycursor.fetchall()
def getalltransmissions(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT distinct transmission  FROM voiture")
    return mycursor.fetchall()
def getallcarburants(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT distinct carburant  FROM voiture")
    return mycursor.fetchall()
