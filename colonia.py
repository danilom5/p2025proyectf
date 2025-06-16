#Colonia
#bacterias: lista de objetos Bacteria.
#ambiente: instancia de la clase Ambiente.
#M´etodos: paso(), reporte estado(), exportar csv().

from ambiente import Ambiente
from bacteria import Bacteria

class Colonia:
    def __init__(self, ambiente):
        self.bacterias = []  # lista de Bacteria
        self.ambiente = ambiente

    def paso(self):
        pass

    def reporte_estado(self):
        pass

    def exportar_csv(self, nombre_archivo):
        pass
