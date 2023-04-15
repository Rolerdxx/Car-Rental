import bcrypt



v = "b'$2b$10$ZW4RQwNQR6XNvncihOoMdOnkhTwVHVxnxaDTFWhxy2yh6HCfxcmdi'"

vv = v[2:-1]



print(vv)

vv = vv.encode('utf-8')



p = "d"

p = p.encode('utf-8')

print(bcrypt.checkpw(p,vv))