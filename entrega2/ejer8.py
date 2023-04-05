#Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si 
#la misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del inglés por lo cual 
#las palabras que nombra no son heterogramas en español). 
#Un Heterograma es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.

palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()

letras = []

for c in palabra:
  if c in letras:
    print("La palabra NO ES un heterograma")
    break
  else:
    letras.append(c)
    print(f"{letras}")
print(f"La palabra ES un heterograma")