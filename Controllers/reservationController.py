def savereservation(db,ref,carid,userid,priceperday,dateDB,dateFN):

    cursor = db.cursor()
    numberofyears=getNumberOfYears(dateDB,dateFN)
    prix=calculTotalPrice(numberofyears,priceperday)
    sql = "insert into reservation(id,date,date_debut,date_return,iduser,idvoiture,prix	) values(%s,CURDATE(),%s,%s,%s,%s,%s) "
    values = (ref, dateDB, dateFN, userid, carid,prix)
    cursor.execute(sql, values)
def getNumberOfYears(date1,date2):
    year1 = date1.year()
    month1 = date1.month()
    day1 = date1.day()

    year2 = date2.year()
    month2 = date2.month()
    day2 = date2.day()
    years_diff = year2 - year1
    if month2 < month1 or (month2 == month1 and day2 < day1):
        years_diff -= 1
    print(years_diff)
    return years_diff
def calculTotalPrice(numberofyears,prixperday):
    return numberofyears*prixperday