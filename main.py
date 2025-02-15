import random #importa la variable random, para generar o escojer de forma aleatoria
caract = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" #todas los digitos disponibles para la contraseña
longitud = int(input('Digite la longitud de la contraseña')) #longitud de la contraseña 
password = '' #variable vacia, se llenara con la longitud de caracteres y los caracteres escogidos aleatoriamente
for i in range(longitud): #repetira determinadamente la accion
    password += random.choice(caract) #escoje de forma aleatoria digitos de la variable caract para completar la contraseña
print (password) # Password
