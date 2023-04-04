#5) Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras, y sobre ella, 
#informe la cantidad de palabras en las que se encuentra el string. 
#No distingir entre mayúsculas y minúsculas.

frase = input("Ingrese una frase: ")
cadena = input("Ingrese una palabra: ")

cant = 0

cadena = cadena.lower()
frase = frase.lower().split()
for palabra in frase:
    if cadena in palabra:
      cant += 1

print(f"La cantidad de veces que se repite {cadena} en la frase es: {cant}")