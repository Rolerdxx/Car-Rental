def login(db, email):
    mycursor = db.cursor()
    query = "SELECT * FROM userr WHERE email='" + email + "'"
    mycursor.execute(query)
    return mycursor.fetchone()


def Signup(db, data):
    mycursor = db.cursor()
    query = "INSERT INTO userr (nom,prenom,email,passwordEn) VALUES(%s, %s, %s, %s)"
    mycursor.execute(query, data)