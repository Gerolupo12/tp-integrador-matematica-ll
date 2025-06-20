## TRABAJO PRÁCTICO INTEGRADOR II ##
# MATEMÁTICA Y PROGRAMACIÓN #

# Parte 2: Desarrollo del Programa en Python
# ACTIVIDAD Nº1
# A. Operaciones con DNIs

# A.1 - Ingreso de los DNIs (reales o ficticios).
# A.2 - Generación automática de los conjuntos de dígitos únicos.
# A.3 - Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
# A.4 - Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
# A.5 - Suma total de los dígitos de cada DNI.
# A.6 - Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.


# ** Importaciones de constantes **

from constantes import ESTUDIANTES, DNIS_PREDEFINIDOS, LETRAS


# ** Definición de funciones necesarias para el análisis de grupos **


def analizar_grupo(
    estudiantes=ESTUDIANTES, letras=LETRAS, documentos_predefinidos=None
):
    """
    Función principal que coordina el ingreso o uso de DNIs, la generación de conjuntos,
    y la realización de operaciones y análisis entre ellos.

    Permite al usuario ingresar manualmente los DNIs o utilizar una lista predefinida,
    lo cual es útil para automatizar pruebas o presentaciones

    Args:
        estudiantes (list): Lista de nombres de los estudiantes.
        letras (str): String de letras que identifican a cada conjunto.
        documentos_predefinidos (list or None): Lista opcional de DNIs (como strings).
            Si se proporciona, se omite el ingreso manual y se usan estos valores directamente.

    Returns:
        out (None): Muestra los resultados en la consola.
    """

    # Si hay documentos predefinidos, los usamos directamente
    if documentos_predefinidos:
        # Asignamos la lista de DNIs a una nueva lista
        documentos = documentos_predefinidos

        # Transformamos los documentos en conjuntos y los asignamos a una lista
        conjuntos = [generar_conjunto(dni) for dni in documentos]

        # Mostrar conjuntos generados
        print("\n=== USANDO DNIs PREDEFINIDOS ===\n")

        # Se crea el bucle for para recorrer los conjuntos y sus respectivos nombres.
        for i, dni in enumerate(documentos):
            # Se formatea el conjunto utilizando la función "formatear_conjunto".
            conjunto_formateado = formatear_conjunto(conjuntos[i])

            # Se imprime el conjunto formateado junto con la letra y el nombre del estudiante.
            print(f"{letras[i]} = {conjunto_formateado:<25}({estudiantes[i]})")
    else:
        # Modo manual: se ingresan los DNIs uno por uno
        # Listas vacías para guardar los DNIs y los conjuntos generados
        documentos = []
        conjuntos = []

        # Ingreso y validación de datos
        print("\n=== INGRESE LOS DNIs (sin puntos ni separadores) ===\n")

        # Recorremos cada estudiante del grupo
        for nombre in estudiantes:
            # Se llama a la función con el nombre del estudiante
            dni = ingreso_documento(nombre)

            # Validación del DNI ingresado: debe contener solo dígitos y tener una longitud de 8 caracteres.
            while not (dni.isdigit() and len(dni) == 8):
                # Si no cumple con las condiciones, se solicita nuevamente el ingreso del DNI.
                print(
                    "El DNI ingresado no es válido. Debe contener solo dígitos y tener una longitud de 8 caracteres.\n"
                )
                dni = ingreso_documento(nombre)

            # Agregamos el DNI a la lista de documentos.
            documentos.append(dni)

            # Generamos el conjunto de dígitos únicos a partir del DNI ingresado.
            conjuntos.append(generar_conjunto(dni))

        # Mostrar conjuntos
        print("\n=== CONJUNTOS GENERADOS ===\n")

        # Se crea el bucle for para recorrer los conjuntos y sus respectivos nombres.
        for i in range(len(conjuntos)):
            # Se formatea el conjunto utilizando la función "formatear_conjunto".
            conjunto_formateado = formatear_conjunto(conjuntos[i])

            # Se imprime el conjunto formateado junto con la letra y el nombre del estudiante.
            print(f"{letras[i]} = {conjunto_formateado:<25}({estudiantes[i]})")

    print("\n* OPERACIONES BÁSICAS ENTRE CONJUNTOS *")

    print("\n=== UNIÓN ===\n")
    # Se llama a la función para calcular la unión de todos los conjuntos.
    mostrar_operacion(conjuntos, letras, "U", union_todos)

    print("\n=== INTERSECCIÓN ===\n")
    # Se llama a la función para calcular la intersección de todos los conjuntos.
    mostrar_operacion(conjuntos, letras, "∩", interseccion_todos)

    print("\n=== DIFERENCIA SIMÉTRICA ===\n")
    # Se llama a la función para calcular la diferencia simétrica de todos los conjuntos.
    mostrar_operacion(conjuntos, letras, "Δ", diferencia_S_todos)

    print("\n=== DIFERENCIAS POR PARES ===\n")
    # Se llama a la función para calcular las diferencias entre cada par de conjuntos.
    diferencias_por_pares(conjuntos, letras)

    print("\n* OPERACIONES ADICIONALES *")

    print("\n=== FRECUENCIA DE DÍGITOS POR DNI ===\n")
    # Se llama a la función para analizar la frecuencia de los dígitos en los DNIs ingresados.
    analizar_frecuencia_dnis(documentos, letras, estudiantes)

    print("\n=== FRECUENCIA DE LOS DÍGITOS EN LOS CONJUNTOS ===\n")
    # Se llama a la función para analizar la frecuencia de los dígitos en los conjuntos.
    analizar_frecuencia_conjuntos(conjuntos)

    print("\n=== SUMA TOTAL DE LOS DÍGITOS DE CADA DNI ===\n")
    # Se llama a la función para calcular la suma total de los dígitos de cada DNI.
    suma_total_digitos(documentos, letras)


def ingreso_documento(nombre):
    """
    Función que solicita el ingreso del documento de un estudiante.

    Args:
        nombre (str): Nombre del estudiante para mostrar en la solicitud de ingreso.

    Returns:
        out (str): Documento ingresado sin puntos ni separadores.
    """

    return input(f"{nombre:<20} -> ")


def generar_conjunto(dni):
    """
    Función que genera un conjunto de dígitos únicos a partir del DNI ingresado.

    Args:
        dni (str): Documento ingresado sin puntos ni separadores.

    Returns:
        out (set): Conjunto de dígitos únicos del DNI.
    """

    return set(dni)


def formatear_conjunto(conjunto):
    """
    Función que formatea un conjunto para su visualización.

    Args:
        conjunto (set): Conjunto de dígitos únicos a formatear.

    Returns:
        out (str): Conjunto formateado como cadena de texto.
    """

    # "sorted" se utiliza para ordenar los elementos del conjunto antes de retornarlo.
    # "replace" se utiliza para reemplazar los corchetes por llaves y las comillas simples por nada.
    return str(sorted(conjunto)).replace("[", "{").replace("]", "}").replace("'", "")


def representar_operacion(cantidad_conjuntos, letras, operador):
    """
    Genera una representación en string de una operación entre múltiples conjuntos

    Args:
        contidad_conjuntos (int): Cantidad de conjuntos a operar
        letras (str): String con las letras identificadoras de cada conjunto
        operador (str): Operador a representar ('U', '∩', o 'Δ')

    Returns:
        out (str): Representación de la operación (ej: "A U B U C")
    """

    # Lista para almacenar las partes de la representación
    partes = []

    # Recorremos los conjuntos
    for i in range(cantidad_conjuntos):
        # Agregamos la letra correspondiente al conjunto actual
        partes.append(letras[i])

        # Comprobamos si no es el último conjunto
        if i < cantidad_conjuntos - 1:
            # Agregamos el operador
            partes.append(operador)

    return " ".join(partes)


def union_todos(conjuntos):
    """
    Función que realiza la unión de todos los conjuntos.

    Args:
        conjuntos (list): Lista de conjuntos a unir.

    Returns:
        out (set): Conjunto ordenado con la unión de todos los conjuntos.
    """

    # Inicializamos el resultado con una COPIA del primer conjunto de la lista.
    # Los conjuntos en Python son objetos mutables que se pasan por referencia. Si asignáramos directamente (sin copy()),
    # estaríamos trabajando con la MISMA instancia en memoria. Esto garantiza que las operaciones posteriores no afecten
    # accidentalmente a conjuntos[0]
    resultado = conjuntos[0].copy()  # Nueva instancia del primer conjunto

    # Recorremos los elementos de "conjuntos" desde el elemento en posición 1 en adelante.
    for c in conjuntos[1:]:
        # Realizamos la unión con "|" y la almacenamos en resultado (hasta terminar de iterar cada elemento de la lista)
        resultado |= c

    return resultado


def interseccion_todos(conjuntos):
    """
    Función que realiza la intersección de todos los conjuntos.

    Args:
        conjuntos (list): Lista de conjuntos a intersectar.

    Returns:
        out (set): Conjunto ordenado con la intersección de todos los conjuntos.
    """

    # Inicializamos el resultado con una COPIA del primer conjunto de la lista.
    # Los conjuntos en Python son objetos mutables que se pasan por referencia. Si asignáramos directamente (sin copy()),
    # estaríamos trabajando con la MISMA instancia en memoria. Esto garantiza que las operaciones posteriores no afecten
    # accidentalmente a conjuntos[0]
    resultado = conjuntos[0].copy()  # Nueva instancia del primer conjunto

    # Recorremos los elementos de "conjuntos" desde el elemento en posición 1 en adelante.
    for c in conjuntos[1:]:
        # Realizamos la intersección con "&" y la almacenamos en resultado (hasta terminar de iterar cada elemento de la lista)
        resultado &= c

    return resultado


def diferencia_S_todos(conjuntos):
    """
    Función que calcula la diferencia simétrica de todos los conjuntos.

    Args:
        conjuntos (list): Lista de conjuntos a calcular la diferencia simétrica.

    Returns:
        out (set): Conjunto ordenado con la diferencia simétrica de todos los conjuntos.
    """

    # Realizamos la unión de todos los conjuntos.
    union_total = union_todos(conjuntos)

    # Realizamos la intersección de todos los conjuntos.
    interseccion_total = interseccion_todos(conjuntos)

    return union_total - interseccion_total


def diferencias_por_pares(conjuntos, letras):
    """
    Función que calcula y muestra la diferencia entre cada par de conjuntos.

    Args:
        conjuntos (list): Lista de conjuntos a comparar.
        letras (str): String de letras que identifican a cada conjunto.

    Returns:
        out (None): Muestra las diferencias en la consola.
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
                    # Si la diferencia no es un conjunto vacío ∅, mostramos el resultado formateado
                    print(
                        f"{letras[i]} - {letras[j]} = {formatear_conjunto(diferencia)}"
                    )
                else:
                    # Si la diferencia es un conjunto vacío, mostramos un mensaje especial
                    print(f"{letras[i]} - {letras[j]} = ∅ (conjunto vacío)")


def mostrar_operacion(conjuntos, letras, operador, funcion_operacion):
    """
    Función que muestra el resultado de una operación entre conjuntos.

    Args:
        conjuntos (list): Lista de conjuntos a operar.
        letras (str): String de letras que identifican a cada conjunto.
        operador (str): Operador a utilizar ('U', '∩', 'Δ').
        funcion_operacion (callable): Función que realiza la operación entre conjuntos.

    Returns:
        out (None): Muestra el resultado de la operación en la consola.
    """

    # Asiganción de la cantidad de conjuntos que se van a operar.
    cantidad_conjuntos = len(conjuntos)

    # Se utiliza la función "representar_operacion" para crear una representación
    # en string de la operación entre los conjuntos.
    operacion_str = representar_operacion(cantidad_conjuntos, letras, operador)

    # Llamamos a la función de operación para obtener el resultado.
    resultado = funcion_operacion(conjuntos)

    # Formateamos el resultado utilizando la función "formatear_conjunto".
    resultado_str = formatear_conjunto(resultado) if resultado else "∅ (conjunto vacío)"

    # Mostramos el resultado de la operación en la consola.
    print(f"{operacion_str} = {resultado_str}")


def analizar_frecuencia_dnis(documentos, letras, estudiantes):
    """
    Función que analiza la frecuencia de los dígitos en los DNIs ingresados.

    Args:
        documentos (list): Lista de DNIs ingresados.
        letras (str): String de letras que identifican a cada DNI.

    Returns:
        out (None): Muestra la frecuencia de los dígitos en la consola.
    """

    # Lista para almacenar las frecuencias individuales de cada DNI
    frecuencias_individuales = []

    # Recorremos cada DNI ingresado
    for i, dni in enumerate(documentos):
        # Dicccionario para almacenar la frecuencia de cada dígito en el DNI actual
        frecuencia = {}

        # Recorremos cada dígito en el DNI actual.
        for digito in dni:
            # Convertimos el dígito a entero para usarlo como clave y actualizamos su frecuencia en el diccionario.
            frecuencia[digito] = frecuencia.get(digito, 0) + 1

        # Agregamos la frecuencia del DNI actual a la lista de frecuencias individuales.
        # Esto nos permite almacenar la frecuencia de cada DNI por separado.
        frecuencias_individuales.append(frecuencia)

        # Ordenamos los dígitos del diccionario de frecuencia.
        digitos_ordenados = sorted(frecuencia.items())

        # Formateamos la salida para mostrar los dígitos y sus frecuencias.
        # Usamos una comprensión de lista para crear una cadena con el formato "f(digito)=frecuencia".
        detalle = ", ".join([f"f({d})={c}" for d, c in digitos_ordenados])

        # Mostramos el resultado en la consola, incluyendo la letra del conjunto y el DNI.
        print(f"{letras[i]}: [{estudiantes[i]}] -> {detalle}")


def analizar_frecuencia_conjuntos(conjuntos):
    """
    Función que analiza la frecuencia de los dígitos en los conjuntos.

    Args:
        conjuntos (list): Lista de conjuntos a analizar.

    Returns:
        out (None): Muestra la frecuencia de cada dígito en la consola.
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

    # Obtenemos el valor máximo de frecuencia para normalizar la visualización.
    # Si el diccionario de frecuencia está vacío, usamos 1 para evitar división por cero.
    max_freq = max(frecuencia.values()) if frecuencia else 1

    # Iteramos sobre los dígitos ordenados en el diccionario de frecuencia.
    for digito in sorted(frecuencia):
        # Obtenemos la frecuencia del dígito actual.
        freq = frecuencia[digito]

        # Creamos una barra de frecuencia proporcional al valor máximo.
        barra = "■" * int(freq * 20 / max_freq)

        # Mostramos el dígito, la barra de frecuencia y la cantidad de conjuntos que lo contienen.
        print(f"{digito}: {barra} {freq} conjuntos")


def suma_total_digitos(documentos, letras):
    """
    Función que calcula la suma total de los dígitos de todos los DNIs.

    Args:
        documentos (list): Lista de DNIs ingresados.
        letras (str): String de letras que identifican a cada DNI.

    Returns:
        out (None): Muestra la suma total de los dígitos de cada DNI en la consola.
    """

    # Recorremos cada conjunto en la lista de documentos
    for i in range(len(documentos)):
        # Convertimos cada dígito a entero y sumamos
        suma = sum(int(digito) for digito in documentos[i])

        # Mostramos la suma total de los dígitos del conjunto
        print(f"Σ dig({letras[i]}) = {suma}")


# ** Programa Principal **


# Esta sección se ejecuta al iniciar el script.
if __name__ == "__main__":
    print(
        "=== BIENVENIDA/O AL PROGRAMA DE INTEGRACIÓN DE MATEMÁTICA CON PROGRAMACION 1 ===\n"
    )
    print(
        "Vamos a realizar operaciones de conjuntos y lógicas entre los dígitos de los DNIs de 5 estudiantes\n"
    )
    print("¿Desea ingresar los DNIs manualmente o utilizar los valores predefinidos?")
    print("1 - Ingresar manualmente")
    print("2 - Usar DNIs predefinidos del equipo")

    opcion = input("\nSeleccione una opción (1 o 2) -> ")

    if opcion == "2":
        analizar_grupo(documentos_predefinidos=DNIS_PREDEFINIDOS)
    else:
        analizar_grupo()
