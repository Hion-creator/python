#concatenar cadenas de caracteres.
#supongamos que queremos crear una cadena que diga
#aprender a programar con __________.

# organizacion = "FreeCodeCamp"

# print("Aprende a programar con " + organizacion)
# print("Aprende a programar con {}".format(organizacion))
# print(f"Aprende a programar con{organizacion}")#f-string


# mad libs (historias locas)

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("verbo: ")
sustantivo_plural = input("Sustantivo plural: ")

madlib = f"!programar es tan {adj} !Siempre me emociona porque me encanta {verbo1} problemas. !Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}"

print(madlib)