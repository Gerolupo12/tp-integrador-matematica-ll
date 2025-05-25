## TRABAJO PRÁCTICO INTEGRADOR II ##
# MATEMÁTICA Y PROGRAMACIÓN #

# Parte 1: Desarrollo Matemático (Conjuntos y Lógica)
# ACTIVIDAD Nº5 
# Redactar al menos dos expresiones lógicas en lenguaje natural, que puedan luego implementarse en Python y 
# escribir en la documentación que van a presentar cual seria el resultado con los conjuntos que tienen.

# A continuación, se presentan 5 CONJUNTOS creados a partir de los DNIs de cada uno de los integrantes del equipo. 
A = {1, 3, 4, 5, 8}         # Estudiante: Ramallo Geronimo DNI: 45413855 
B = {0, 1, 3, 4, 5}         # Estudiante: Mubilla Yanella: DNI: 44011335
C = {0, 2, 3, 4, 6, 7, 8}   # Estudiante: Lahoz Cristian   DNI: 32084674
D = {3, 4, 5, 6, 7, 9}      # Estudiante: Lagos Alejandro  DNI: 35569473
E = {1, 2, 3, 4, 6, 8}      # Estudiante: Maldonado Ariana DNI: 36184823

# Lista conformada por los 5 conjuntos existentes. 
conjuntos = [A, B, C, D, E]

# Inicialización de contadores para la cantidad de conjuntos con número par e impar de elementos.
impares = 0
pares = 0

# Uso de bucle for para recorrer cada conjunto de la lista "Conjuntos".
for conjunto in conjuntos:
    if len(conjunto) % 2 == 0: # se verifica si la cantidad de elementos de cada conjunto es par. 
        pares += 1 # si es par, incrementamos el contador de conjuntos pares. 
    else:            
        impares += 1 # si es impar, incrementamos el contador de conjuntos impares. 

# Condicional para comparar que tipo de conjuntos es mayor en cantidad. 
if impares > pares:
    print("El grupo se etiqueta como 'grupo impar'.")
else:
    print("El grupo no cumple con la condición para ser 'grupo impar'.")
