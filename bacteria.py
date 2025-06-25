class Bacteria:
    def __init__(self, id_bacteria, raza, energia, fila, columna, resistente=False):
        """
        Constructor de Bacteria.
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

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

    def alimentar(self, ambiente):
        """
        Permite a la bacteria alimentarse desde el ambiente.
        - Se accede a la celda del ambiente en la que se encuentra usando fila y columna.
        - Se extrae una cantidad de nutrientes aleatoria entre 15 y 25.
        - La energía de la bacteria aumenta, y los nutrientes del ambiente disminuyen.
        - Si la energía sigue siendo muy baja (< 10), la bacteria muere por inanición.
        """   

        # Si está muerta, no puede alimentarse
        if self.estado != "activa":
            print(f"{self.id} no se alimenta porque está {self.estado}.")
            return

        # Obtener nutrientes en su celda actual
        nutrientes_disponibles = ambiente.nutrientes[self.fila][self.columna]

            
        # Nutrientes que desea consumir (entre 15 y 25)
        import random
        cantidad_deseada = random.randint(15, 25)

        # No puede consumir más de lo que hay
        cantidad_real = min(cantidad_deseada, nutrientes_disponibles)

        # Quitar nutrientes del ambiente
        ambiente.nutrientes[self.fila][self.columna] -= cantidad_real

        # Aumentar energía de la bacteria
        self.energia += cantidad_real

        print(f"{self.id} se alimentó con {cantidad_real} unidades. Energía actual: {self.energia}")

        # Revisión por inanición: si aún con lo consumido está muy débil, muere
        if self.energia < 10:
            print(f"{self.id} tiene energía muy baja ({self.energia}). Morirá por inanición.")
            self.morir()    

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

    def mutar(self):
        """
        Representa la posibilidad de que la bacteria mute al dividirse.
        - Se aplica una probabilidad del 5%.
        - Si muta, se vuelve resistente a antibióticos u otros factores ambientales.
        """

        # Solo pueden mutar las bacterias vivas
        if self.estado != "activa":
            print(f"{self.id} no puede mutar porque está {self.estado}.")
            return

        import random
        probabilidad_mutacion = 0.05  # 5%

        numero_azar = random.random()  # número entre 0.0 y 1.0

        if numero_azar <= probabilidad_mutacion:
            self.resistente = True
            print(f"{self.id} ha mutado. Ahora es RESISTENTE.")
        else:
            print(f"{self.id} NO mutó (número generado: {numero_azar:.4f}).")

#----------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

    def dividirse(self, ambiente, lista_bacterias):
        """
        Simula la división celular por mitosis.
        - Solo se divide si la energía ≥ 70.
        - La hija nace en una celda vecina vacía.
        - Se divide la energía entre madre e hija.
        - La hija puede mutar (5%).
        - Se agrega la hija a la lista de bacterias del sistema.
        """

        # Verifica si está viva
        if self.estado != "activa":
            print(f"{self.id} no puede dividirse porque está {self.estado}.")
            return

        # Condición de energía mínima
        if self.energia < 70:
            print(f"{self.id} no tiene suficiente energía para dividirse. Tiene {self.energia}.")
            return

        # Buscar celdas vecinas vacías
        posiciones_vecinas = self.obtener_vecinas_libres(ambiente)

        if not posiciones_vecinas:
            print(f"{self.id} no puede dividirse porque no hay espacio alrededor.")
            return

        # Elegir una posición aleatoria entre las vecinas vacías
        import random
        fila_hija, col_hija = random.choice(posiciones_vecinas)

        # Generar ID para la hija
        # self.id es el ID de la madre
        # len(lista_bacterias) cuenta cuántas bacterias hay actualmente.
        # Le suma 1 para generar un número nuevo y no repetido.
        # f"texto{variable}" es una f-string: una forma moderna y clara de armar cadenas.
        nuevo_id = f"{self.id}-h{len(lista_bacterias) + 1}" #SI LA MADRE FUERA B4 Y HUBIERAN 10 BACTERIAS, 
                                                            #nuevo_id = f"b4-h11"  # hija número 11 creada por b4


        # Dividir energía
        energia_hija = self.energia // 2
        self.energia -= energia_hija

        # Crear bacteria hija (igual raza)
        hija = Bacteria(nuevo_id, self.raza, energia_hija, fila_hija, col_hija)

        # Aplicar mutación a la hija
        hija.mutar()

        # Poner a la hija en la grilla
        ambiente.grilla[fila_hija][col_hija] = hija

        # Agregar a la lista de bacterias del sistema
        lista_bacterias.append(hija)

        print(f"{self.id} se dividió. Nueva hija: {hija.id} en ({fila_hija},{col_hija}) con energía {energia_hija}")

#--------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

    def obtener_vecinas_libres(self, ambiente):

    # Busca celdas vecinas (arriba, abajo, izquierda, derecha) que estén vacías.
    # Retorna una lista con las coordenadas disponibles para ubicar una hija.

        vecinas = []

        # Obtenemos el tamaño de la grilla
        cantidad_filas = len(ambiente.grilla)
        cantidad_columnas = len(ambiente.grilla[0])

        # Revisar celda de arriba
        nueva_fila = self.fila - 1
        nueva_columna = self.columna
        if nueva_fila >= 0:
            if ambiente.grilla[nueva_fila][nueva_columna] is None:
                vecinas.append((nueva_fila, nueva_columna))

        # Revisar celda de abajo
        nueva_fila = self.fila + 1
        nueva_columna = self.columna
        if nueva_fila < cantidad_filas:
            if ambiente.grilla[nueva_fila][nueva_columna] is None:
                vecinas.append((nueva_fila, nueva_columna))

        # Revisar celda a la izquierda
        nueva_fila = self.fila
        nueva_columna = self.columna - 1
        if nueva_columna >= 0:
            if ambiente.grilla[nueva_fila][nueva_columna] is None:
                vecinas.append((nueva_fila, nueva_columna))

        # Revisar celda a la derecha
        nueva_fila = self.fila
        nueva_columna = self.columna + 1
        if nueva_columna < cantidad_columnas:
            if ambiente.grilla[nueva_fila][nueva_columna] is None:
                vecinas.append((nueva_fila, nueva_columna))

        return vecinas

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------





