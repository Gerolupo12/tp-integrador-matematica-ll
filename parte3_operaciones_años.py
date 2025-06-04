## TRABAJO PRÁCTICO INTEGRADOR II ##
# MATEMÁTICA Y PROGRAMACIÓN #

# PARTE 2: Desarrollo del Programa en Python

# B. OPERACIONES CON AÑOS DE NACIMIENTO. 

# B.1 - Ingreso de los años de nacimiento. 
# B.2 - Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas. 
# B.3 - Si todos nacieron después del 2000, mostrar "Grupo Z".
# B.4 - Si alguno nació en año bisiesto, mostrar "Tenemos un año especial"
# B.5 - Implementar una función para determinar si un año es bisiesto. 
# B.6 - Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.


## Fecha de nacimiento de los integrantes del equipo:
# A) Ramallo Geronimo: año 2002
# B) Mubilla Yanella: año 2001
# C) Lahoz Cristian: año 1986
# D) Lagos Alejandro: año 1991
# E) Maldonado Ariana: año 1993

""" B.1 - Ingreso de los años de nacimiento. """
# Lista creada con los años de nacimiento de cada uno de los integrantes del equipo. 
años_nacimiento = [1986, 1991, 1993, 2001, 2002]


""" B.2 - Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas. """
# Inicializar contadores para años pares e impares.
par = 0
impar = 0

# Recorrer la lista de años de nacimientos. 
for año in años_nacimiento:
    if año % 2 == 0:
        par += 1                    # Si el año es par, incrementar contador de años pares.  
    else:
        impar += 1                  # Si el año es impar, incrementar contador de años impares. 

# Mostrar los resultados obtenidos en pantalla. 
print(f"Hubo {par} nacimientos en años pares.")
print(f"Hubo {impar} nacimientos en años impares.")


""" B.3 - Si todos nacieron después del 2000, mostrar "Grupo Z". """
# Verificar si todos los estudiantes nacieron después del año 2000. 
todos_son_grupo_z = all(año>2000 for año in años_nacimiento)

# Si todos cumplen con la condición, mostrar en pantalla que son del "Grupo Z". 
if todos_son_grupo_z:
    print("Grupo Z")             
else:                               # De lo contrario, si alguno/s nacieron antes del año 2000, imprimir "No todos pertenecen al Grupo Z".
    print("No todos pertenecen a Grupo Z")    


""" B.4 - Si alguno nació en año bisiesto, mostrar "Tenemos un año especial". """
# Definimos una función para saber si un año es bisiesto. 
def año_bisiesto(año):
    return año % 4 == 0 and (año % 100 !=0 or año % 400 == 0) # Un año es bisiesto si: es divisible por 4 y (no divisible por 100 ó si divisible por 400)

# Verificamos si al menos uno de los elementos de la lista (años), es bisiesto. 
if any(año_bisiesto(año) for año in años_nacimiento):         # La función "any" devolverá True si al menos uno de lo de los años cumple la condición. 
# Mostrar el resultado obtenido en pantalla. 
    print("Tenemos un año especial.")
else: 
    print("No tenemos un año especial.")

""" B.5 - Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales. """
# Lista creada con la edad actual de cada uno de los integrantes del equipo. 
edad_estudiantes = [22, 23, 31, 33, 39]

# Lista creada con la fecha de nacimiento de cada uno de los integrantes del equipo. Se encuentra al inicio de el archivo. 
# años_nacimiento = [1986, 1991, 1993, 2001, 2002]

# Lista vacía en la que se guardará el producto cartesiano. 
prod_cartesiano = []

# Calculo del producto cartesiano de manera manual usando dos ciclos anidados. 
# El primer ciclo recorre cada año en la lista años_nacimiento. 
for año in años_nacimiento:
# El segundo ciclo recorre cada edad en la lista de edad_estudiantes. 
    for edad in edad_estudiantes:
        prod_cartesiano.append((año, edad))  # Por cada combinación de año y edad, se crear un a tupla (año, edad) y se agrega a la lista prod_cartesiano. 

# Mostrar los resultados en pantalla.
# Recorrer la lista prod_cartesiano, imprimiendo cada par (tupla)
for año, edad in prod_cartesiano:
    print(f"Año: {año} - Edad: {edad}")

          
