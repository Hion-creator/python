from sqlite3 import DateFromTicks


contador = 0
resultado = 0

while contador <= 4:
    resultado += 1
    if contador %2 == 0:
        contador+= 1
        continue
    #resultado += 1
    contador += 1
print(resultado)
    
    

    
numero = 2 % 2

print(f"el modulo es {numero}")

