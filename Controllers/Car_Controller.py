def getallcars(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT id,image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture")
    return mycursor.fetchall()


def getsomecars(db, marque, modele, carburant, place, transmission, prix):
    mycursor = db.cursor()
    sql = "SELECT image,marque,modele,carburant,places,transmission,state,prixParJour FROM voiture WHERE"
    values = []
    if marque != "none":
        sql += " marque=%s AND"
        print(marque)
        values.append(marque)
    if modele != "":
        sql += " lower(modele) like %s AND"
        values.append(modele.lower())
    if carburant != "none":
        sql += " carburant = %s AND"
        values.append(carburant)
    if place != "":
        sql += " places = %s AND"
        values.append(int(place))
    if transmission != "none":
        sql += " transmission = %s AND"
        values.append(transmission)
    if prix != "":
        sql += " prixParJour < %s AND"
        values.append(float(prix))
    if sql.endswith("AND"):
        sql = sql[:-4]
    mycursor.execute(sql, values)
    return mycursor.fetchall()
def changestate(db,carid):
    mycursor = db.cursor()
    sql=f"UPDATE voiture SET state = '0' WHERE id ={carid}"
    print(sql,carid,carid)
    mycursor.execute(sql)
    db.commit()