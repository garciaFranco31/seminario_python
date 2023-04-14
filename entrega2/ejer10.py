#  10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
#  programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
#  A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
#  notas. Utilizar esta estructura para la resolución de los siguientes items.
#  B. Calcular el promedio de notas de cada estudiante.
#  C. Calcular el promedio general del curso.
#  D. Identificar al estudiante con la nota promedio más alta.
#  E. Identificar al estudiante con la nota más baja.

#  Nota:
# • Las 3 estructuras están ordenadas de forma que los elementos en la misma posición corresponden
# a un mismo alumno.
# • Realizar funciones con cada items



def agrupar_estudiantes_y_notas(lista_nombres, notas1, notas2):

    #utilizando las tres tuplas, las agrupo utilizando zip() para así obtener una nueva estructura, que en este caso será
    #un diccionario, que recibe el nombre de estudiantes, con el nombre del alumno como clave y una tupla con dos elementos, 
    #uno que represanta la 1er nota y el otro la 2da.

    agrupo_estudiantes_con_notas = zip(lista_nombres, notas1, notas2)
    estudiantes_y_notas = {nombre: (nota1, nota2) for nombre, nota1, nota2 in agrupo_estudiantes_con_notas}
    return estudiantes_y_notas

def calcular_promedio_por_estudiante(estudiantes):
    #genero un nuevo diccionario, en el cual ahora, se va a almacenar la nota promedio
    #de cada uno de los estudiantes
    promedios_estudiantes = {}
    for nombre in estudiantes:
        promedios_estudiantes[nombre] = sum(estudiantes[nombre])/len(estudiantes[nombre])
    #print(promedio)
    return promedios_estudiantes

def promedio_de_la_clase(promedios):
    #suma el total de los promedios de toda la clase y devuelve.
    return sum(promedios.values())/len(promedios)

def buscar_mayor_promedio(promedios):
    #devuelve el nombre del estudiante con mayor promedio
    return max(promedios.items(), key= lambda estudiante: estudiante[1])[0].capitalize()

def buscar_menor_promedio(promedios):
    #devuelve el nombre del estudiante con menor promedio
    return min(promedios.items(), key=lambda estudiante: estudiante[1])[0].capitalize()


#main

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [
  81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12,
  77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95,
  18, 7, 74, 60, 9, 65, 93, 63, 74
]
notas_2 = [
  30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64,
  13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19,
  47, 15, 31, 39, 15, 74, 33, 57, 10
]


#armo una lista con los nomrbes de todos los alumnos
lista_nombres = nombres.replace("\n", "").replace("'", "").replace(" ","").split(",")
#print(lista_nombres)
estudiantes = agrupar_estudiantes_y_notas(lista_nombres, notas_1, notas_2)
print(estudiantes)
promedio_por_estudiante = calcular_promedio_por_estudiante(estudiantes)
print(promedio_por_estudiante)
promedio_clase = promedio_de_la_clase(promedio_por_estudiante)
print(promedio_clase)
maximo_promedio = buscar_mayor_promedio(promedio_por_estudiante)
print(maximo_promedio)
minimo_promedio = buscar_menor_promedio(promedio_por_estudiante)
print(minimo_promedio)
