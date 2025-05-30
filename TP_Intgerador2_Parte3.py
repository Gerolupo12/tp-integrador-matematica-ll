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


# ** Definición de variables y listas necesarias **

# Lista con los nombres de cada uno de los estudiantes.
estudiantes = [
    "Ramallo Gerónimo",
    "Mubilla Yanela",
    "Lahoz Cristian",
    "Lagos Alejandro",
    "Maldonado Ariana",
]
# Letras para identificar a cada uno de los conjuntos.
letras = ["A", "B", "C", "D", "E"]


# ** Definición de funciones necesarias para el análisis de grupos **


def analizar_grupo(estudiantes: list = estudiantes, letras: list = letras) -> None:
    """
    Función principal que coordina el ingreso de DNIs, generación de conjuntos,
    y operaciones entre conjuntos.
    :param estudiantes: list - Lista de nombres de los estudiantes.
    :param letras: list - Lista de letras que identifican a cada conjunto.
    :return: None - Muestra los resultados en la consola.
    """

    # Listas vacías para guardar los DNIs y los conjuntos generados
    conjuntos = []

    # Ingreso y validación de datos
    print("=== INGRESO DE DNIs ===")

    # Bucle para ingresar los documentos y generar los conjuntos correspondientes.
    for nombre in estudiantes:
        # Se llama a la función con el nombre del estudiante
        dni = ingreso_documento(nombre)
        # Generamos y guardamos el conjunto.
        conjuntos.append(generar_conjunto(dni))

    # Mostrar conjuntos
    print("\n=== CONJUNTOS GENERADOS ===\n")

    # Se crea el bucle for para mostrar los conjuntos con la letra y el nombre de los estudiantes.
    for i in range(len(conjuntos)):
        # Se muestran los conjuntos de forma ordenada
        observar_conjunto(letras[i], estudiantes[i], conjuntos[i])

    # Mostrar operaciones básicas entre conjuntos
    print("\n=== OPERACIONES BÁSICAS ENTRE CONJUNTOS ===")
    # Se llama a las funciones y se muestra su resultado. Se utiliza "sorted" para ordenar los
    # elementos del conjunto antes de mostrarlos. Se reemplazan los corchetes por llaves para una
    # mejor presentación.
    print("\nUNIÓN")
    print(
        "A U B U C U D U E = ",
        (
            str(sorted(union_todos(conjuntos))).replace("[", "{").replace("]", "}")
            if union_todos(conjuntos)
            else "∅ (conjunto vacío)"
        ),
    )
    print("\nINTERSECCIÓN")
    print(
        "A ∩ B ∩ C ∩ D ∩ E = ",
        (
            str(sorted(interseccion_todos(conjuntos)))
            .replace("[", "{")
            .replace("]", "}")
            if interseccion_todos(conjuntos)
            else "∅ (conjunto vacío)"
        ),
    )
    print("\nDIFERENCIA SIMÉTRICA")
    print(
        "A Δ B Δ C Δ D Δ E = ",
        (
            str(sorted(diferencia_S_todos(conjuntos)))
            .replace("[", "{")
            .replace("]", "}")
            if diferencia_S_todos(conjuntos)
            else "∅ (conjunto vacío)"
        ),
    )
    print("\nDIFERENCIAS POR PARES")
    diferencias_por_pares(conjuntos, letras)

    # Análisis adicionales
    print("\n=== FRECUENCIA DE LOS DÍGITOS EN LOS CONJUNTOS ===\n")
    # Se llama a la función para analizar la frecuencia de los dígitos en los conjuntos.
    analizar_frecuencia(conjuntos)

    print("\n=== SUMA TOTAL DE LOS DÍGITOS DE CADA CONJUNTO ===\n")
    # Se llama a la función para calcular la suma total de los dígitos de cada conjunto.
    suma_total_digitos(conjuntos, letras)


def ingreso_documento(nombre: str) -> str:
    """
    Función que solicita el ingreso del documento de un estudiante.
    :param nombre: str - Nombre del estudiante.
    :return: str - Documento ingresado sin puntos ni separadores.
    """
    return input(f"Ingrese el documento de {nombre} (sin puntos ni separadores) -> ")


def generar_conjunto(dni: str) -> set:
    """
    Función que genera un conjunto de dígitos únicos a partir del DNI ingresado.
    :param dni: str - Documento ingresado sin puntos ni separadores.
    :return: set - Conjunto de dígitos únicos del DNI.
    """
    return set(dni)


def observar_conjunto(letra: str, nombre: str, conjunto: set) -> None:
    """
    Función que muestra el conjunto con su letra y nombre correspondiente.
    :param letra: str - Letra que identifica al conjunto.
    :param nombre: str - Nombre del estudiante.
    :param conjunto: set - Conjunto de dígitos únicos del DNI.
    :return: None - Muestra el conjunto en la consola.
    """
    # "Sorted" se utiliza para ordenar los elementos del conjunto antes de mostrarlos.
    print(
        f"{letra} = {str(sorted(conjunto)).replace('[', '{').replace(']', '}')}   ->   ({nombre})"
    )


def union_todos(conjuntos: list) -> set:
    """
    Función que realiza la unión de todos los conjuntos.
    :param conjuntos: list - Lista de conjuntos a unir.
    :return: set - Conjunto ordenado con la unión de todos los conjuntos.
    """
    # Inicializamos el resultado con el primer conjunto de la lista.
    resultado = conjuntos[0].copy()

    # Recorremos los elementos de "conjuntos" desde el elemento en posición 1 en adelante.
    for c in conjuntos[1:]:
        # Realizamos la unión con "|" y la almacenamos en resultado (hasta terminar de iterar cada elemento de la lista)
        resultado |= c

    return resultado


def interseccion_todos(conjuntos: list) -> set:
    """
    Función que realiza la intersección de todos los conjuntos.
    :param conjuntos: list - Lista de conjuntos a intersectar.
    :return: set - Conjunto ordenado con la intersección de todos los conjuntos.
    """
    # Inicializamos el resultado con el primer conjunto de la lista.
    resultado = conjuntos[0].copy()

    # Recorremos los elementos de "conjuntos" desde el elemento en posición 1 en adelante.
    for c in conjuntos[1:]:
        # Realizamos la intersección con "&" y la almacenamos en resultado (hasta terminar de iterar cada elemento de la lista)
        resultado &= c

    return resultado


def diferencia_S_todos(conjuntos: list) -> set:
    """
    Función que calcula la diferencia simétrica de todos los conjuntos.
    :param conjuntos: list - Lista de conjuntos a calcular la diferencia simétrica.
    :return: set - Conjunto ordenado con la diferencia simétrica de todos los conjuntos.
    """
    # Realizamos la unión de todos los conjuntos.
    union_total = union_todos(conjuntos)

    # Realizamos la intersección de todos los conjuntos.
    interseccion_total = interseccion_todos(conjuntos)

    return union_total - interseccion_total


def diferencias_por_pares(conjuntos: list, letras: list) -> None:
    """
    Función que calcula y muestra la diferencia entre cada par de conjuntos.
    :param conjuntos: list - Lista de conjuntos a comparar.
    :param letras: list - Lista de letras que identifican a cada conjunto.
    :return: None - Muestra las diferencias en la consola.
    """
    # Bucle anidado para calcular la diferencia entre cada par de conjuntos
    for i in range(len(conjuntos)):
        # Evitamos comparar el conjunto consigo mismo
        for j in range(len(conjuntos)):
            # Si los índices son diferentes, calculamos la diferencia
            # y mostramos el resultado.
            if i != j:
                # Calculamos la diferencia entre los conjuntos i y j
                diferencia = conjuntos[i] - conjuntos[j]

                # Mostramos la diferencia ordenada
                if diferencia:
                    # Convertimos el conjunto a una cadena ordenada y reemplazamos los corchetes
                    print(
                        f"{letras[i]} - {letras[j]} = {str(sorted(diferencia)).replace('[', '{').replace(']', '}')}"
                    )
                else:
                    # Si la diferencia es un conjunto vacío, mostramos un mensaje especial
                    print(f"{letras[i]} - {letras[j]} = ∅ (conjunto vacío)")


def analizar_frecuencia(conjuntos: list) -> None:
    """
    Función que analiza la frecuencia de los dígitos en los conjuntos.
    :param conjuntos: list - Lista de conjuntos a analizar.
    :return: None - Muestra la frecuencia de cada dígito en la consola.
    """
    # Diccionario para almacenar la frecuencia de cada dígito
    frecuencia = {}
    # Recorremos cada conjunto y contamos la frecuencia de cada dígito
    # en todos los conjuntos.
    for conjunto in conjuntos:
        # Recorremos cada dígito en el conjunto actual
        # y actualizamos su frecuencia en el diccionario.
        for digito in conjunto:
            # Convertimos el dígito a entero para usarlo como clave
            digito = int(digito)
            # Actualizamos la frecuencia del dígito
            # Si el dígito no está en el diccionario, lo inicializamos en 0.
            frecuencia[digito] = frecuencia.get(digito, 0) + 1

    # Mostramos la frecuencia de cada dígito ordenada por dígito
    for digito, count in sorted(frecuencia.items()):
        print(f"Dígito {digito}: aparece en {count} conjuntos")


def suma_total_digitos(conjuntos: list, letras: list) -> int:
    """
    Función que calcula la suma total de los dígitos de todos los conjuntos.
    :param conjuntos: list - Lista de conjuntos a sumar.
    :param letras: list - Lista de letras que identifican a cada conjunto.
    :return: None - Muestra la suma total de los dígitos de cada conjunto en la consola.
    """
    # Recorremos cada conjunto en la lista de conjuntos
    print(conjuntos)
    for i in range(len(conjuntos)):
        # Calculamos la suma de los dígitos en el conjunto actual
        # Convertimos cada dígito a entero y sumamos
        suma = sum(int(digito) for digito in conjuntos[i])
        # Mostramos la suma total de los dígitos del conjunto
        print(f"Σ dig({letras[i]}) = {suma}")


# ** Código principal para ejecutar el programa **

if __name__ == "__main__":
    # Llamamos a la función principal para iniciar el análisis de grupos
    analizar_grupo()
