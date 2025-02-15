import random
caract = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input('Digite la longitud de la contraseña'))
password = ''
for i in range(longitud):
    password += random.choice(caract)
print (password)# Password
