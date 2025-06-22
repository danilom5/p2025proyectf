class Bacteria:
    def __init__(self, id_bacteria, raza, energia, fila, columna, resistente=False):
        """
        Constructor de la clase Bacteria.
        - id_bacteria: Identificador unico para rastrear la bacteria (ej: b1,b2, o cualquier otro, para diferenciarse de una en otra).
        - raza: Representa el tipo, A o B o C etc
        - energia: Energía inicial que tendrá la bacteria.
        - fila, columna: Posición en la grilla donde vive la bacteria
        - resistente: Booleano que indica si tiene resistencia a factores ambientales como los antibioticos
        """
        self.id = id_bacteria
        self.raza = raza
        self.energia = energia
        self.resistente = resistente
        self.estado = "activa" # Estado vital: activa o muerta

        # Ubicación espacial en la grilla del ambiente
        self.fila = fila
        self.columna = columna


    def alimentar(self):
        pass

    def dividirse(self):
        pass

    def mutar(self):
        pass

    def morir(self):
        pass
        #energias random