import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    #Seleccionar una palabra al azar de palabras validas de la lista
    palabra= random.choice(palabras)
    
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
        
        
    return palabra.upper()#regresa string en mayusculas

def ahorcado():
    
    print("===================================================")
    print(" !BIENVENIDO AL JUEGO DEL AHORCADO!")
    print("====================================================")
    
    palabra = obtener_palabra_valida(palabras)
    
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase) # no contiene la Ñ
    
    vidas = 7
    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        # P A C D
        print(f"te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
        #metodo join une todos los elementos de un conjunto con el caracter que se espesifica
        
        #mostrar el estado actual de la palabra
        #List Comprehension
        palabra_lista =[letra if letra in letras_adivinadas else '-' for letra in palabra]
        #mostrar estadp del ahorcado
        print(vidas_diccionario_visual[vidas])
        #mostrar las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        letra_usuario = input("Escoge una letra: ").upper()
        #Si la letra escogida por el usuario esta en el abecedario
        #y no esta en el junto de letras que ya se han ingresado,
        #se añade la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
           letras_adivinadas.add(letra_usuario)
           
           #si la letra esta en la palabra
           #quitar la letra del conjunto de letras pendoente por adivinar.
           #si no esta en la palabra quitar 1 vida
           if letra_usuario in letras_por_adivinar:
               letras_por_adivinar.remove(letra_usuario)
        #remove metodo para trabajar con conjuntos
               print('')
           else:
               vidas -= 1
               print(f"\nTu letra, {letra_usuario} no esta en la palabra. ")
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
            
        else:
            print("\nEsta letra no es valida")           
    #El juego llega a esta linea cuando se adivinan todas las letras de la palabra o 
    #cuando se agotan las vodas del jugador
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"!Ahorcado! Perdiste. Lo lamento: La palabra era: {palabra}")
    else:
        print(f"!Excelente! !Adivinaste la Palabra {palabra}!")
        
ahorcado()