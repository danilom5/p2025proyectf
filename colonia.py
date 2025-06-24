#Colonia
#bacterias: lista de objetos Bacteria.
#ambiente: instancia de la clase Ambiente.
#M´etodos: paso(), reporte estado(), exportar csv().

from ambiente import Ambiente
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




