evaluar = """ titulo: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of 
capturing unprecedented details of large-scale complex systems. However, the specialized knowledge required for 
developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing 
an initial implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing 
ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful 
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable 
modeling system that can exploit the largest HPC resources and emerging computing architectures.
"""
#separo el titulo para poder procesarlo
titulo = evaluar.split("resumen: ")[0].split("titulo: ")[1].split("\n")[0].split(" ")

if (len(titulo) <= 10):
  print("Ok")
else:
  print("El titulo debe tener 10 palabras como máximo")

#separo el resumen, para poder procesar cada una de 
#las frases que lo componen
resumen = evaluar.split("resumen: ")[1].split(".")
resumen.remove("\n")
facil = aceptable = dificil = muy_dificil = 0
for elem in resumen:
  #separo las frses en listas de palabras, con las palabras que componen a cada frase
  palabra = elem.split(" ")
  #elimino los caracteres vacios dentro de las listas
  if "" in palabra:
    palabra.remove("")
  cant_words = len(palabra)
  if (cant_words <= 12):
    facil+=1
  if ( 13 <= cant_words <= 17):
    aceptable += 1
  if (18 <= cant_words <= 25):
    dificil += 1
  if (cant_words > 25):
    muy_dificil += 1

print(f"Facil: {facil}")
print(f"Aceptable: {aceptable}")
print(f"Dificil: {dificil}")
print(f"Muy Dificil: {muy_dificil}")