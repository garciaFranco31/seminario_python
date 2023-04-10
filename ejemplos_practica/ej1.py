#Crear una lista de números pares del 0 al 10

#definida por comprensión
# numeros_pares = [num for num in range(11) if num % 2 == 0]
# #print(numeros_pares)

# #Definida por extensión
# numeros_pares2 = []
# for num in range(11):
#     if num % 2 == 0:
#         numeros_pares2.append(num)
# #print(numeros_pares2)

#Crear una lista de los cuadrados del 1 al 15
# #cuadrados por comprensión
# cuadrados = [num**2 for num in range(1,6)]
# #print(cuadrados)

# #cuadrados por extensión
# cuadrados2 = []
# for num in range(1,6):
#     cuadrados2.append(num**2)
# #print(cuadrados2)

#3.Crear una lista de las vocales en una cadena de texto:

# cadena = "hola ¿como estas?"
# lista_vocales = []
# for char in cadena.lower():
#     if char in "aeiou":
#         lista_vocales.append(char)
# print(lista_vocales)

# lista_vocales2 = [char for char in cadena.lower() if char in "aeiou"]
# print(lista_vocales2)

# vocales = list(filter(lambda char: char in "aeiou", cadena.lower()))
# print(vocales)

#4.Crear una lista de las palabras en una cadena de texto:
cadena = "hola, ¿cómo estás?"

palabras = [palabra for palabra in cadena.split(" ")]
print(palabras)

palabras_extension = []
for palabra in cadena.split():
    palabras_extension.append(palabra)
print(palabras_extension)