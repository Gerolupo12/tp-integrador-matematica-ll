from constantes import DNIS_PREDEFINIDOS
from Parte_2A import generar_conjunto, interseccion_todos


# ** Implementación en código de expresiones lógicas en lenguaje natural **


# 1) Si todos los conjuntos contienen al menos n dígitos en común, entonces el grupo tiene n dígitos comunes.
def verificar_digitos_comunes(documentos):
    """
    Verifica el resultado de la intersección de conjuntos y muestra los dígitos comunes.

    Args:
        interseccion_resultado (set): Conjunto de dígitos comunes resultantes de la intersección.

    Returns:
        out (None): Imprime los dígitos comunes o un mensaje si no hay dígitos comunes.
    """

    # Transformamos los documentos en conjuntos y los asignamos a una lista
    conjuntos = [generar_conjunto(dni) for dni in documentos]

    # Intersecamos los conjuntos
    digitos_comunes = interseccion_todos(conjuntos)

    # Verificamos si hay dígitos comunes y los mostramos ordenados.
    if digitos_comunes:
        print(
            f"Los dígitos comunes en todos los conjuntos son: {sorted(digitos_comunes)}"
        )
    else:
        print("No hay dígitos comunes en todos los conjuntos.")


# 2) Si hay más conjuntos con cantidad impar de elementos que conjuntos con cantidad par, entonces el grupo se
# etiqueta como “grupo impar”.
def determinar_grupo_impar(documentos):
    """
    Determina si el grupo se etiqueta como 'grupo impar' o no,
    según la cantidad de conjuntos con número par e impar de elementos.

    Args:
        conjuntos (list): Lista de conjuntos a evaluar.

    Returns:
        out (None): Se imprime el resultado directamente.
    """

    # Transformamos los documentos en conjuntos y los asignamos a una lista
    conjuntos = [generar_conjunto(dni) for dni in documentos]

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


# ** Programa Principal **


# Esta sección se ejecuta al iniciar el script.
if __name__ == "__main__":
    print("\n=== VERIFICACIÓN DE DÍGITOS COMUNES CON DNIS PREDEFINIDOS ===\n")
    # Verificamos los dígitos comunes en todos los conjuntos.
    verificar_digitos_comunes(DNIS_PREDEFINIDOS)

    print("\n=== DETERMINACIÓN DEL GRUPO IMPAR ===\n")
    # Determinamos si el grupo es impar o no.
    determinar_grupo_impar(DNIS_PREDEFINIDOS)
