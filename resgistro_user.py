#Sub modulo 1 entrada de datos y validacion de usuario
print("Welcomo to Sing Up")
newUser=input("Pleace write a new user name: ")
dataBase="Fulanito"
if newUser != dataBase:
    print(F"El nombre de usuario {newUser} Esta disponible")
    #Modulo 2 validacion de contraseña
    user_pass=input("Crea una nueva 8 caracteres maximo\ncontrasena: ")
    if len [user_pass] < 8:
        #Submodulo 2.1 segunda validacion de la contrsena
        sameUserPass=int(input("Por favor vuelva esvrivir la contrasna:"))
        
        if user_pass != sameUserPass:
            print("lo siento las contrasnias con coinciden, vuelva a intentarlo")
        else:
            print("El registro de usuario ha sido exitoso")
        
        
    else:
        print("lo siento la contrasena supera los 8 caracteres")
    
else:
    print(f"Lo siento el nombre {newUser} No esta disponible")