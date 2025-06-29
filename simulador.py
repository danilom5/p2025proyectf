class Simulador:
    def __init__(self, ambiente, colonia):
        # guarda referencias al ambiente y a la colonia
        self.ambiente = ambiente
        self.colonia = colonia
        self.paso_actual = 0

    def run(self, pasos=1):
        for _ in range(pasos):
            print(f"--- paso {self.paso_actual + 1} ---")

            # las bacterias comen y se dividen
            for b in self.colonia.bacterias:
                if b.estado == "activa":
                    b.alimentar()
                    if b.estado == "activa":
                        b.dividirse(self.colonia.bacterias)

            # el ambiente actualiza nutrientes, difunde y aplica presiones
            self.ambiente.actualizar_nutrientes()
            self.ambiente.difundir_nutrientes()
            self.ambiente.aplicar_ambiente()

            self.paso_actual += 1
