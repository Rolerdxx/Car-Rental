def login(db, email):
    mycursor = db.cursor()
    query = "SELECT * FROM userr WHERE email='" + email + "'"
    mycursor.execute(query)
    return mycursor.fetchone()



def changepassword(db, email, newpass):
    cursor = db.cursor()
    query = "UPDATE userr SET passwordEn = '"+newpass[2:-1]+"' WHERE email = '"+email+"'"
    print(query)
    try:
        cursor.execute(query)
    except db.Error as err:
        print("Something went wrong: {}".format(err))
    return cursor.rowcount

def Signup(db, data):
    mycursor = db.cursor()
    query = "INSERT INTO userr (nom,prenom,email,passwordEn) VALUES(%s, %s, %s, %s)"
    mycursor.execute(query, data)

