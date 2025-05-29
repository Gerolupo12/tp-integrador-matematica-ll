## TRABAJO PRÁCTICO INTEGRADOR II ##
# MATEMÁTICA Y PROGRAMACIÓN I#

# Parte 1: Desarrollo Matemático (Conjuntos y Lógica)

# Redactar al menos dos expresiones lógicas en lenguaje natural, que puedan luego implementarse en Python y
# escribir en la documentación que van a presentar cual seria el resultado con los conjuntos que tienen.

# A continuación, se presentan 5 CONJUNTOS creados a partir de los DNIs de cada uno de los integrantes del equipo.
A = {1, 3, 4, 5, 8}  # Estudiante: Ramallo Geronimo DNI: 45413855
B = {0, 1, 3, 4, 5}  # Estudiante: Mubilla Yanella: DNI: 44011335
C = {0, 2, 3, 4, 6, 7, 8}  # Estudiante: Lahoz Cristian   DNI: 32084674
D = {3, 4, 5, 6, 7, 9}  # Estudiante: Lagos Alejandro  DNI: 35569473
E = {1, 2, 3, 4, 6, 8}  # Estudiante: Maldonado Ariana DNI: 36184823

# Lista conformada por los 5 conjuntos existentes.
lista_de_conjuntos = [A, B, C, D, E]


# ** 1) Si todos los conjuntos contienen al menos n dígitos en común, entonces el grupo tiene n dígitos comunes.


def verificar_digitos_comunes(conjuntos: list) -> None:
    """
    Verifica si todos los conjuntos contienen números en común y los muestra.
    :param conjuntos: list - Lista de conjuntos a evaluar.
    :return: None - Se imprime el resultado directamente.
    """
    # Inicialización de un conjunto vacío para almacenar los dígitos comunes.
    digitos_comunes = set()

    # Uso de bucle for para recorrer cada conjunto de la lista "conjuntos".
    for i, conjunto in enumerate(conjuntos):
        # Si es el primer conjunto, lo asignamos directamente a "digitos_comunes".
        if i == 0:
            digitos_comunes = conjunto
        else:
            # Realizamos la intersección con el conjunto actual.
            digitos_comunes &= conjunto  # & es el operador de intersección.

    # Verificamos si hay dígitos comunes y los mostramos ordenados.
    if digitos_comunes:
        print(
            f"Los dígitos comunes en todos los conjuntos son: {sorted(digitos_comunes)}"
        )
    else:
        print("No hay dígitos comunes en todos los conjuntos.")


# ** 2) Si hay más conjuntos con cantidad impar de elementos que conjuntos con cantidad par, entonces el grupo se
# ** etiqueta como “grupo impar”.


def determinar_grupo_impar(conjuntos: list) -> None:
    """
    Determina si el grupo se etiqueta como 'grupo impar' o no,
    según la cantidad de conjuntos con número par e impar de elementos.
    :param conjuntos: list - Lista de conjuntos a evaluar.
    :return: None - Se imprime el resultado directamente.
    """
    # Inicialización de contadores para la cantidad de conjuntos con número par e impar de elementos.
    impares = 0
    pares = 0

    # Uso de bucle for para recorrer cada conjunto de la lista "conjuntos".
    for conjunto in conjuntos:
        # Se verifica si la cantidad de elementos de cada conjunto es par.
        if len(conjunto) % 2 == 0:
            # Si es par, incrementamos el contador de conjuntos pares.
            pares += 1
        else:
            # Si es impar, incrementamos el contador de conjuntos impares.
            impares += 1

    # Condicional para comparar que tipo de conjuntos es mayor en cantidad.
    if impares > pares:
        print("El grupo se etiqueta como 'grupo impar'.")
    else:
        print("No se cumple con la condición para ser 'grupo impar'.")


# Programa principal
if __name__ == "__main__":
    # Verificamos los dígitos comunes en todos los conjuntos.
    verificar_digitos_comunes(lista_de_conjuntos)

    # Determinamos si el grupo es impar o no.
    determinar_grupo_impar(lista_de_conjuntos)
