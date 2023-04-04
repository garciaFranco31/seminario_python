#Dado el siguiente texto guardado en la varible jupyter_info, solicite por teclado una letra e imprima las 
#palabras que comienzan con dicha letra. En caso que no se haya inrgesado un letra, indique el error. 
#Ver: módulo string

import string

jupyter_info = """ JupyterLab is a web-based interactive development environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing ones.
"""

text = jupyter_info.lower().split(' ')

letter = input("Ingrese una letra: ")
if len(letter) == 0:
    print("no se ha ingresado ninguna letra, intente nuevamente")
for word in text:
    if word.startswith(letter):
        print(word)