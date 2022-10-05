pesos = int(input("¿Cuántos pesos colombianos tienes?: "))
valor_dolar = 4500
dolares = pesos/ valor_dolar
dolares = round((dolares), 2)
dolares = str(dolares)
print(f"Tienes $ {dolares} dólares")