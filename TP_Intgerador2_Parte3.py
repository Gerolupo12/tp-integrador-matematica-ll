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
    "Mubilla Yanela",
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



"""operaciones entre conjuntos"""

# Funciones para operadores entre conjuntos
def union_todos(conjuntos):
    resultado = conjuntos[0] # Empezamos a recorrer (en el for a continuación) partiendo desde el primer elemento de la lista "conjuntos".
    for c in conjuntos[1:]: # Recorremos los elementos de "conjuntos" desde el elemento en posición 1 en adelante.
        resultado = resultado | c # Realizamos la unión con "|" y la almacenamos en resultado (hasta terminar de iterar cada elemento de la lista)
    return resultado

def interseccion_todos(conjuntos):
    resultado = conjuntos[0] 
    for c in conjuntos[1:]: 
        resultado = resultado & c # Realizamos la intersección con "&"
    return resultado

def diferencia_S_todos(conjuntos):
    union_total = union_todos(conjuntos)
    interseccion_total = interseccion_todos(conjuntos)
    return union_total - interseccion_total

def diferencias_por_pares(conjuntos, letras):
     for i in range(len(conjuntos)):
        for j in range(len(conjuntos)):
            if i != j:
                diferencia = conjuntos[i] - conjuntos[j]
                print(f"Diferencia {letras[i]} - {letras[j]}: {sorted(diferencia)}")


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

print("Unión de todos los conjuntos:", sorted(union_todos(conjuntos)))
print("Intersección de todos los conjuntos:", sorted(interseccion_todos(conjuntos)))
print("Diferencia simétrica de todos los conjuntos:", sorted(diferencia_S_todos(conjuntos)))
print("Diferencias por pares entre los conjuntos:")
diferencias_por_pares(conjuntos, letras)
