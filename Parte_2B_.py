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


"""B.1 - Ingreso de los años de nacimiento."""

# Importar lista de años y edades

from constantes import YEARS, EDAD_ESTUDIANTES


""" B.2 - Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas. """
# Inicializar contadores para años pares e impares.
par = 0
impar = 0

# Recorrer la lista de años de nacimientos.
for año in YEARS:
    if año % 2 == 0:
        par += 1  # Si el año es par, incrementar contador de años pares.
    else:
        impar += 1  # Si el año es impar, incrementar contador de años impares.

# Mostrar los resultados obtenidos en pantalla.
print(f"Hubo {par} nacimientos en años pares.")
print(f"Hubo {impar} nacimientos en años impares.")


""" B.3 - Si todos nacieron después del 2000, mostrar "Grupo Z". """
# Verificar si todos los estudiantes nacieron después del año 2000.
todos_son_grupo_z = all(año > 2000 for año in YEARS)

# Si todos cumplen con la condición, mostrar en pantalla que son del "Grupo Z".
if todos_son_grupo_z:
    print("Grupo Z")
else:  # De lo contrario, si alguno/s nacieron antes del año 2000, imprimir "No todos pertenecen al Grupo Z".
    print("No todos pertenecen a Grupo Z.")


""" B.4 - Si alguno nació en año bisiesto, mostrar "Tenemos un año especial". """


# Definimos una función para saber si un año es bisiesto.
def año_bisiesto(año):
    return año % 4 == 0 and (
        año % 100 != 0 or año % 400 == 0
    )  # Un año es bisiesto si: es divisible por 4 y (no divisible por 100 ó si divisible por 400)


# Verificamos si al menos uno de los elementos de la lista (años), es bisiesto.
if any(
    año_bisiesto(año) for año in YEARS
):  # La función "any" devolverá True si al menos uno de lo de los años cumple la condición.
    # Mostrar el resultado obtenido en pantalla.
    print("Tenemos un año especial.")
else:
    print("No tenemos un año especial.")

""" B.5 - Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales. """

# Lista vacía en la que se guardará el producto cartesiano.
prod_cartesiano = []

# Calculo del producto cartesiano de manera manual usando dos ciclos anidados.
# El primer ciclo recorre cada año en la lista años_nacimiento.
for año in YEARS:
    # El segundo ciclo recorre cada edad en la lista de edad_estudiantes.
    for edad in EDAD_ESTUDIANTES:
        prod_cartesiano.append(
            (año, edad)
        )  # Por cada combinación de año y edad, se crear un a tupla (año, edad) y se agrega a la lista prod_cartesiano.

# Mostrar los resultados en pantalla.
# Recorrer la lista prod_cartesiano, imprimiendo cada par (tupla)
for año, edad in prod_cartesiano:
    print(f"{año}:{edad}")
