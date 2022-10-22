def MathOp(a,b):
    division = a/b
    division_entero=a//b
    division_modulo=a%b
    potencia=a**b
    return[division,division_entero,division_modulo,potencia]


n=int(input("ingrese numero uno: "))
n1=int(input("ingrese numero dos: "))

[division,division_entero,division_modulo,potencia]=MathOp(n,n1)


print(division)
print(division_entero)
print(division_modulo)
print(potencia)