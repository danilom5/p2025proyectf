def obtener_grilla_visual(colonia):
    """
    Convierte la grilla del ambiente en una matriz de números enteros
    para poder graficar el estado actual de cada celda.
    números:
    - 0: celda vacía
    - 1: bacteria activa
    - 2: bacteria muerta
    - 3: bacteria resistente
    """

    # Obtenemos el tamaño del ambiente
    filas = colonia.ambiente.alto
    columnas = colonia.ambiente.ancho

    # Creamos la matriz que vamos a llenar con los valores
    matriz_visual = []

    # Recorremos cada fila de la grilla
    for i in range(filas):
        fila_numerica = []  # lista que representará una fila de números

        # Recorremos cada columna de la fila actual
        for j in range(columnas):
            # Obtenemos el contenido de la celda actual
            celda = colonia.ambiente.grilla[i][j]

            # Evaluamos qué hay en la celda
            if celda is None:
                # Si no hay nada, la celda está vacía
                fila_numerica.append(0)

            elif celda.estado == "muerta":
                # Si hay bacteria pero está muerta
                fila_numerica.append(2)

            elif celda.resistente:
                # Si está viva y es resistente (mutó)
                fila_numerica.append(3)

            else:
                # Si no está muerta ni es resistente, es activa normal
                fila_numerica.append(1)

        # Agregamos la fila ya convertida a la matriz final
        matriz_visual.append(fila_numerica)

    # Retornamos la matriz completa lista para graficar
    return matriz_visual
