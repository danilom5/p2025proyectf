#Ambiente
#grilla: matriz que representa el entorno.
#nutrientes: cantidad de nutrientes por celda.
#factor ambiental: puede representar antibi´oticos u otras presiones.
#M´etodos: actualizar nutrientes(), difundir nutrientes(), aplicar ambiente().

class Ambiente:
    def __init__(self, ancho, alto, nivel_nutriente=100):
        self.grilla = [[None for _ in range(ancho)] for _ in range(alto)]
        self.nutrientes = [[nivel_nutriente for _ in range(ancho)] for _ in range(alto)]
        self.factor_ambiental = None  # ej: antibióticos

    def actualizar_nutrientes(self):
        pass

    def difundir_nutrientes(self):
        pass

    def aplicar_ambiente(self):
        pass
