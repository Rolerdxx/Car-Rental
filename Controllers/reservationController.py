def savereservation(db,carid,userid,priceperday,nbrDays):
    print("khdama tahua")
    cursor = db.cursor()
    prix=calculTotalPrice(int(nbrDays),float(priceperday))
    sql = f"insert into reservation(date,nbrDays,iduser,idvoiture,prix) values(now(),{nbrDays},{userid},{carid},{prix}) "
    cursor.execute(sql)
    db.commit()
def calculTotalPrice(nbrDays,prixperday):
    return nbrDays*prixperday