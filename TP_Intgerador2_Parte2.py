## TRABAJO PRÁCTICO INTEGRADOR II ##
# MATEMÁTICA Y PROGRAMACIÓN #

# Parte 2: Desarrollo del Programa en Python
# ACTIVIDAD Nº1 
# A. Operaciones con DNIs

# A.1 - Ingreso de los DNIs (reales o ficticios).
# A.2 - Generación automática de los conjuntos de dígitos únicos.

## Documentos de los integrantes del equipo:
# A) Ramallo Geronimo: 45413855
# B) Mubilla Yanella: 44011335
# C) Lahoz Cristian: 32084674
# D) Lagos Alejandro: 35569473
# E) Maldonado Ariana: 36184823

# Lista con los nombres de cada uno de los estudiantes. 
estudiantes = [  
    "Ramallo Gerónimo",
    "Mubilla Yanella",
    "Lahoz Cristian",
    "Lagos Alejandro",
    "Maldonado Ariana"
]

letras = ["A", "B", "C", "D", "E"]  # Letras para identificar a cada uno de los conjuntos.  

# Función creada para ingresar el documento de un estudiante.
def ingreso_documento(nombre):  
    return input(f"Ingrese el documento de {nombre} (sin puntos ni separadores): ")  # nombre es el argumento correcto

# Función creada para generar automáticamente el conjunto de dígitos únicos.
def generar_conjunto(dni):  
    return set(dni)  # Convierte el DNI en un conjunto de caracteres únicos

# Función creada para mostrar el conjunto con su letra y nombre correspondiente.
def observar_conjunto(letra, nombre, conjunto):  
    print(f"Conjunto {letra} : {nombre} - {sorted(conjunto)}")  # "Sorted" muestra el conjunto ordenado

# Listas vacías para guardar los DNIs y los conjuntos generados
documentos = []  
conjuntos = []  

# Bucle para ingresar los documentos y generar los conjuntos correspondientes. 
for nombre in estudiantes:
    dni = ingreso_documento(nombre)  # Se llama a la función con el nombre del estudiante
    documentos.append(dni)  # Con "append" guardamos el documento en la lista.
    conjuntos.append(generar_conjunto(dni))  # Generamos y guardamos el conjunto. 

# Se crea el bucle for para mostrar los conjuntos con la letra y el nombre de los estudiantes. 
for i in range(len(conjuntos)):
    observar_conjunto(letras[i], estudiantes[i], conjuntos[i])  # Se muestran los conjuntos de forma ordenada