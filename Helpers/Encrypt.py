import bcrypt


def CheckPass(passe, hashh):
    passe = passe.encode('utf-8')
    hashh = hashh.encode('utf-8')
    return bcrypt.checkpw(passe, hashh)


def EncryptPass(passe):
    passe = passe.encode('utf-8')
    salt = bcrypt.gensalt()
    hashh = bcrypt.hashpw(passe, salt)
    return str(hashh)[2:-1]
