# Bacteria
#id: identificador ´unico.
#raza: identificador gen´etico o especie.
#energia: nivel de energ´ıa actual.
#resistente: booleano que indica si es resistente.
#estado: activa o muerta.
#M´etodos: alimentar(), dividirse(), mutar(), morir().

class Bacteria:
    def __init__(self, id_bacteria, raza, energia, resistente=False):
        self.id = id_bacteria
        self.raza = raza
        self.energia = energia
        self.resistente = resistente
        self.estado = "activa"  # o "muerta"

    def alimentar(self):
        pass

    def dividirse(self):
        pass

    def mutar(self):
        pass

    def morir(self):
        pass
