class Ambiente:
    def __init__(self, ancho, alto, nivel_nutriente=100):
        """
        Constructor del ambiente donde vivirán las bacterias.
        Se crean dos matrices: una para la grilla (con None al inicio)
        y otra para los nutrientes en cada celda.
        """

        # Guardamos las dimensiones del ambiente
        self.ancho = ancho
        self.alto = alto

        # Creamos la grilla (una matriz vacía de bacterias)    es una matriz llena de none
        self.grilla = []  # esto será una lista de listas
        for fila in range(alto):
            fila_actual = []  # esta lista representará una fila
            for columna in range(ancho):
                fila_actual.append(None)  # ninguna bacteria al inicio
            self.grilla.append(fila_actual)

        # Creamos la matriz de nutrientes      en vez de none como la de arriba, esta sera con los nutrientes, va con numeros
        self.nutrientes = []  # otra lista de listas
        for fila in range(alto):
            fila_nutrientes = []
            for columna in range(ancho):
                fila_nutrientes.append(nivel_nutriente)  # cada celda parte con 100 por defecto
            self.nutrientes.append(fila_nutrientes)

        # por ahora queda en none
        self.factor_ambiental = None

        # lo mismo, pero la dejaré creada
        self.colonia = None

#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------