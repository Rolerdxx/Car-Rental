def login(db, email):
    mycursor = db.cursor()
    query = "SELECT * FROM userr WHERE email='" + email + "'"
    mycursor.execute(query)
    return mycursor.fetchone()
