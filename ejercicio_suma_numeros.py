valor1 = 15
valor2 = 10
valor3 = 20
resultado = 0

if(valor1 >= 10):
    resultado += 1
    if(valor2 < 10):
        resultado += 1
    else:
        resultado +=1
elif(valor2 <= 15):
    resultado += 1
    if(valor3 <= 10):
       resultado += 1
if (valor3 >= 20):
    resultado += 1
    if(valor1 <= 10):
       resultado += 1
        
print(resultado)

