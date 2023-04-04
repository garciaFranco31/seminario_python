#Dada una frase identificar mayúsculas, minúsculas y caracteres no letras y contar la cantidad de palabras sin distinguir 
#entre mayúsculas y minúsculas, en la frase.

texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que el de una mujer es de $45.000. 
 Además, las mujeres tienen menos posibilidades de acceder a puestos de liderazgo en las empresas.
"""

mayusculas = 0
minusculas = 0
caracteres = 0
cantidad_palabras = 0

for caracter in texto:
    if caracter.isupper():
        mayusculas += 1
    elif caracter.islower():
        minusculas += 1
    elif not caracter.isalpha() and caracter != " ":  
        caracteres += 1

palabras = texto.lower().split()
print(f"Cantidad de palabras: {len(palabras)}")

print(f"Cantidad Mayusculas: {mayusculas}")
print(f"Cantidad Minusculas: {minusculas}")
print(f"Caracteres No Letras: {caracteres}")