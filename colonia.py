from bacteria import Bacteria

class Colonia:
    def __init__(self, ambiente):
        """
        constructor de la colonia.
        - recibe el ambiente en el que vive.
        - tendra una lista de bacterias que viven en ese ambiente.
        """
        self.ambiente = ambiente
        self.bacterias = []  # Esta lista se completa desde Ambiente, es donde se guardan todas las bacterias de esta colonia

    def paso(self):
        """ 
        simula un paso de tiempo en la colonia.
        cada bacteria se alimenta, puede morir por inanicion, y puede dividirse.
        """

        # copia de la lista original para evitar errores al modificarla mientras iteramos
        bacterias_activas = self.bacterias.copy()

        for bacteria in bacterias_activas: 
            if bacteria.estado == "activa": #verificar si esta viva
                # Paso 1: se alimenta
                bacteria.alimentar(self.ambiente) #llamamos el metodo alimentar 

                # Paso 2: si sobrevive, puede dividirse
                if bacteria.estado == "activa":
                    bacteria.dividirse(self.ambiente, self.bacterias) #solo se divide si sigue viva 

#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
    def reporte_estado(self):
    #contar las bacterias
        total = len(self.bacterias)
        activas = 0
        muertas = 0
        resistentes = 0

        for b in self.bacterias:
            if b.estado == "activa":
                activas += 1
                if b.resistente:
                    resistentes += 1
            elif b.estado == "muerta":
                muertas += 1

        print("----- REPORTE DE ESTADO DE LA COLONIA -----")
        print(f"total de bacterias: {total}")
        print(f"bacterias activas: {activas}")
        print(f"bacterias muertas: {muertas}")
        print(f"bacterias resistentes: {resistentes}")
        print("-------------------------------------------")


    def exportar_csv(self, nombre_archivo):
        """
        Exporta un archivo CSV con la información actual de cada bacteria.
        El archivo incluirá: ID, raza, estado, si es resistente, energía y posición.
        """

        import csv

        with open(nombre_archivo, mode='w', newline='') as archivo:
            escritor = csv.writer(archivo)

            # Escribimos la cabecera del archivo
            escritor.writerow(['ID', 'Raza', 'Estado', 'Resistente', 'Energía', 'Fila', 'Columna'])

            # Escribimos una fila por cada bacteria
            for b in self.bacterias:
                escritor.writerow([
                    b.id,
                    b.raza,
                    b.estado,
                    'Sí' if b.resistente else 'No',
                    b.energia,
                    b.fila,
                    b.columna
                ])

        print(f"Se exportó el estado de la colonia a '{nombre_archivo}' correctamente.")

#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------



