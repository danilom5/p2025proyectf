from bacteria import Bacteria
from colonia import Colonia
import random

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
    def inicializar_bacterias(self, cantidad):
        """
        Crea una cantidad de bacterias activas y las distribuye aleatoriamente
        en la grilla. Luego, crea una colonia con esas bacterias.
        """

        # Lista donde guardaremos todas las bacterias creadas
        lista_bacterias = []

        # Bucle hasta colocar la cantidad solicitada
        colocadas = 0
        while colocadas < cantidad:
            # Elegimos una posición aleatoria dentro de los límites
            fila = random.randint(0, self.alto - 1)
            columna = random.randint(0, self.ancho - 1)

            # Verificamos que la celda esté vacía
            if self.grilla[fila][columna] is None:
                # Generamos un ID para esta bacteria
                id_bacteria = f"b{colocadas + 1}"

                # Creamos la bacteria con energía = 50 y raza "A"
                nueva = Bacteria(id_bacteria, "A", 50, fila, columna)

                # La ponemos en la grilla
                self.grilla[fila][columna] = nueva

                # La agregamos a la lista de bacterias
                lista_bacterias.append(nueva)

                # Aumentamos el contador
                colocadas += 1

        # Creamos la colonia con este ambiente
        self.colonia = Colonia(self)

        # Le asignamos la lista de bacterias
        self.colonia.bacterias = lista_bacterias

        print(f"Se inicializaron {cantidad} bacterias activas en el ambiente.")

#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------