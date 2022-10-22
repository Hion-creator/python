import random

#funcion
def jugar():
    #convierte la cadena en minusculas
    usuario = input("Escoge una opcion: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
    #permite escoger aletoriamente una de las opciones que pongas 
    computadora = random.choice(['pi','pa','ti'])
    
    if usuario == computadora:
        return '!Empate!'
    #funcion
    if gano_el_jugador (usuario, computadora):
        return '!Ganaste!'
    
    return '!Perdiste!'

#funcion
def gano_el_jugador (jugador, oponente):
    #Retornar true (verdadero) si gana o gano el jugador
    #piedra gana a tijera(pi>ti).
    #tijera gana papel(ti>pa).
    #papel gana a piedra (pa>pi).
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())