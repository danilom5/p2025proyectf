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

        def alimentar(self, ambiente): #Parámetro `ambiente`:** es un objeto externo (de la clase `Ambiente`) que tiene la matriz de nutrientes (`ambiente.nutrientes`)
            """
        Permite a la bacteria alimentarse desde el ambiente.
        - Se accede a la celda del ambiente en la que se encuentra usando fila y columna.
        - Se extrae una cantidad de nutrientes aleatoria entre 15 y 25.
        - La energía de la bacteria aumenta, y los nutrientes del ambiente disminuyen.
            """

        # Si la bacteria no está activa (está muerta), no se alimenta
        if self.estado != "activa": #evita que una que este muerta se pueda alimentar
            print(f"{self.id} no se alimenta porque está {self.estado}.")
            return

        # Obtener los nutrientes de su celda actual en el ambiente
        nutrientes_disponibles = ambiente.nutrientes[self.fila][self.columna]

        # Determinar cuánto intenta consumir (valor aleatorio entre 15 y 25)
        import random
        cantidad_deseada = random.randint(15, 25)

        # Asegurarse de no consumir más de lo disponible
        cantidad_real = min(cantidad_deseada, nutrientes_disponibles)

        # Restar nutrientes del ambiente
        ambiente.nutrientes[self.fila][self.columna] -= cantidad_real

        # Aumentar energía de la bacteria
        self.energia += cantidad_real

        print(f"{self.id} se alimentó con {cantidad_real} unidades. Energía actual: {self.energia}")


    
    
    
    
    
    
    
    
    
    
    
    
    def dividirse(self):
        pass

    def mutar(self):
        pass

    def morir(self):
        pass
        #energias random