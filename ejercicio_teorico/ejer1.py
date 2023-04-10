import csv
import os

def evaluar_condicion (usuario):
    #Esta función es la encargada de evaluar si el usuario cumple con la condición pedida, y devuelve
    #un valor de tipo boolean, es decir, si el usuario visualizó el estado de la entrega, se devolverá true
    #y en caso contrario, devolverá false.

    if "Tarea: Entrega 1" in usuario["Contexto del evento"]:
        if "Se ha visualizado el estado de la entrega" in usuario["Nombre evento"]:
            return false #no cumple la condición, es decir, que vio el estado de la entrega
    return true #cumple condición, no vió el estado de la entrega

def generar_usuarios(diccionario_usuarios, formato=None):
    #Esta función se encarga de recibir el diccionario con los usuarios generado por el archivo csv, y aplicarles
    #el filtro deseado utilizando la funcion "evaluar_condicion", para así generar una nueva lista,
    #en la cual solamente se encuentren los usuarios que no hayan visualizado la tarea

    filtro_usuarios = list(filter(evaluar_condicion,diccionario_usuarios))
    nombres_usuarios = list({usuario:"Nombre " for usuario in filtro_usuarios})
    if formato == "A":
        return [u.upper() for u in nombres_usuarios]
    elif formato == "a":
        return [u.lower() for u in nombres_usuarios]
   

path = os.path.realpath("")
file_path = os.path.join(path, "log_catedras.csv")
with open (file_path) as archivo:
    lector = csv.DictReader (archivo, delimiter=",")
    header = next(lector)
    Format = input("A: imprimir nombre en mayuscula \n a: imprimir nombres en minuscula")
    usuarios = generar_usuarios(lector, Format)

    print("---------------------")
    print("Usuario en el sistema ")
    print("---------------------")
    for usuario in sorted(usuarios):
        print("{:-^20}".format(usuario))