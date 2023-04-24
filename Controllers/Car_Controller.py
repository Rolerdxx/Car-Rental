def getallcars(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture")
    return mycursor.fetchall()


def getsomecars(marque, modele, carburant, place, transmission, prix, db):
    print("khdama3")
    mycursor1 = db.cursor()
    sql = "SELECT image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture WHERE "
    values = []
    if marque != "none":
        sql += " marque=%s AND"
        values.append(marque)
    elif modele != "":
        sql += " modele = %s AND"
        values.append(modele)
    elif carburant != "none":
        sql += " carburant = %s AND"
        values.append(carburant)
    elif place != "":
        sql += " places = %s AND"
        values.append(place)
    elif transmission != "none":
        sql += " transmission = %s AND"
        values.append(transmission)
    elif prix != "":
        sql += " prixParJour = %s AND"
        values.append(prix)
    elif sql.endswith("AND"):
        sql = sql[:-4]
    mycursor1.execute(sql, values)
    return mycursor1.fetchall()
