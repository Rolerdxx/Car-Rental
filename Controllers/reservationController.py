def savereservation(db,ref,carid,userid,priceperday,nbrDays):
    print("khdama tahua")
    cursor = db.cursor()
    prix=calculTotalPrice(nbrDays,priceperday)
    sql = "insert into reservation(id,date,nbrDays,iduser,idvoiture,prix	) values(%s,CURDATE(),%s,%s,%s,%s) "
    values = (ref, int(nbrDays), userid, int(carid),prix)
    print(values)
    cursor.execute(sql, values)
def calculTotalPrice(nbrDays,prixperday):
    return int(nbrDays)*prixperday