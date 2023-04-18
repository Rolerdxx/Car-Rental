def getallcars(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture")
    return mycursor.fetchall()
