def getallcars(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM voiture")
    return mycursor.fetchall()
