#Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada la 
#siguiente tabla de valores del juego Scrabble:

tabla_puntos = {"A": 1, "E":1, "I":1, "O":1, "U":1, "L":1, "N":1, "R":1, "S":1, "T":1,
           "D":2 , "G":2,
           "B":3, "C":3, "M":3,"P":3,
           "F":4, "H":4, "W":4, "Y":4,
           "K":5,
           "J":8, "X":8,
           "Q":10, "Z":10
          }

palabra = input("Ingrese una palabra: ")

puntaje = 0

for letra in palabra:
    puntaje += tabla_puntos.get(letra.upper())
print(f"El puntaje obtenido con la palabra {palabra}, fue: {puntaje}")