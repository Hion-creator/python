#escribe un programa que permita generar la tabla 
# de multiplicar de un numero entero positivo N, comenzando desde 1

#si el usuario escribe un numero incorrecto, el programa no se ejecuta. En cambio, pregunta de nuevo la informacion hasta que el dato ingresado sea correcto.

comprobar = True

while comprobar == True:
    n_entero=int(input("Ingrese un numero entero positivo: "))

    if (n_entero > 0):
        
        comprobar= False
        
        #range crea listas segun la cantidad de un numero (x,a) teniendo en cuenta que el a no lo incluye
        for  i in range(1,11):
        
            print(f" {n_entero} por {i} es igual a {n_entero*(i)} ")
              
    else:            
        print("El numero ingresado no es correcto. Intentalo nuevamente.")


