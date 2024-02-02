#Sub modulo 1 entrada de datos y validacion de usuario
print("Welcomo to Sing Up")
newUser=input("Pleace write a new user name: ")
dataBase="Fulanito"
if newUser != dataBase:
    print(F"El nombre de usuario {newUser} Esta disponible");
else:
    print(f"Lo siento el nombre {newUser} No esta disponible")