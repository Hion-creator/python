"""
busqueda ingenua
"""
import random
import time

def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):#len toda la lista
        if lista[i] == objetivo:
            return i
    return -1

mi_lista = [1,3,5,10,12]
print(busqueda_ingenua(mi_lista, 15))     
#range(len(lista)) -> 0, 1, 2, 3, 4, ....., len(lista)-1

#busqueda binaria
def busqueda_binaria(lista, objetivo,limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 # inicio de la lista
    if limite_superior is None:
        limite_superior = len(lista)-1  #final de la lista len= total lista.
    
    if limite_superior < limite_inferior:
        return -1
    
    punto_medio = (limite_inferior+limite_superior)//2
    
    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista,objetivo,limite_inferior,(punto_medio-1))
    else:
        return busqueda_binaria(lista, objetivo, (punto_medio+1), limite_superior)

if __name__=='__main__':
    #crear lista ordenada con 10000 numeros aleatorios.
    tamaño=10000
    conjunto_inicial = set()
    
    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño,3*tamaño))
    
    lista_ordenada=sorted(list(conjunto_inicial))
    #list=convierte en lista
    #sorted= ordena los elementos
    
    #medir el tiempo de busqueda ingenua
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada,objetivo)
    fin=time.time()
    print(f"tiempo de busqueda ingenua: {fin - inicio} segundos")
    
    #medir el tiempo de busqueda binaria
    
    inicio= time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin=time.time()
    print(f"tiempo de busqueda binaria: {fin-inicio} segundo")        