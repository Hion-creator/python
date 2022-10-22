import random 


def adivina_el_numero_computadora(x):
    
    print("===============================")
    print(" !Bienvenido(a) al juego! ")
    print("================================")
    print(f"Seleccioana un numero entre 1 y {x} para que la computadora intente adivinarlo")
    
    limite_inferior = 1 #[1,x]
    limite_superior = x
    
    respuesta = ""
    while respuesta != "c":
        # Generar una prediccion
        if limite_inferior != limite_superior: # [1,10]
            prediccion = random.randint(limite_inferior, limite_superior)
        else: 
            prediccion = limite_inferior # tambien podria ser limite superior.
            
        # Obtener respuesta del usuario
        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()
        
        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
            
    print(f" !Felicitaciones! La computadora adivino tu numero correctamente: {prediccion}")

    
adivina_el_numero_computadora (10)
            
        # intervalo inicial: [1,10]
        # prediccion: 6
        # Respuesta: "a"
        # Intervalo: [1,5]