import bcrypt
#
# # example password
# password = 'passwordabc'
#
# # converting password to array of bytes
# bytes = password.encode('utf-8')
#
# # generating the salt
# salt = bcrypt.gensalt()
#
# # Hashing the password
# hash = bcrypt.hashpw(bytes, salt)
#
# print(hash)
#
# # Taking user entered password
# userPassword = 'password000'
#
# # encoding user password
# userBytes = userPassword.encode('utf-8')
#
# # checking password
# result = bcrypt.checkpw(userBytes, hash)
#
# print(result)


v = "b'$2b$10$ZW4RQwNQR6XNvncihOoMdOnkhTwVHVxnxaDTFWhxy2yh6HCfxcmdi'"

vv = v[2:-1]



print(vv)

vv = vv.encode('utf-8')



p = "d"

p = p.encode('utf-8')

print(bcrypt.checkpw(p,vv))