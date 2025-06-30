import matplotlib.pyplot as plt

class Simulador:
    def __init__(self, ambiente, colonia):
        self.ambiente = ambiente
        self.colonia = colonia
        self.paso_actual = 0

        # listas para registrar la evolución
        self.historial_activas = []
        self.historial_resistentes = []

    def run(self, pasos=1):
        for _ in range(pasos):
            print(f"--- paso {self.paso_actual + 1} ---")

            for b in self.colonia.bacterias:
                if b.estado == "activa":
                    b.alimentar()
                    if b.estado == "activa":
                        b.dividirse(self.colonia.bacterias)

            self.ambiente.actualizar_nutrientes()
            self.ambiente.difundir_nutrientes()
            self.ambiente.aplicar_ambiente()

            # contar activas y resistentes
            activas = 0
            resistentes = 0
            for b in self.colonia.bacterias:
                if b.estado == "activa":
                    activas += 1
                    if b.resistente:
                        resistentes += 1

            # guardar valores
            self.historial_activas.append(activas)
            self.historial_resistentes.append(resistentes)

            self.paso_actual += 1



    def graficar_evolucion(self):
      
        pasos = list(range(1, self.paso_actual + 1))
        activas = self.historial_activas
        resistentes = self.historial_resistentes

        plt.figure(figsize=(8, 4))
        plt.plot(pasos, activas, label="bacterias activas", marker="o")
        plt.plot(pasos, resistentes, label="bacterias resistentes", marker="s")
        
        plt.xlabel("paso de simulación")
        plt.ylabel("cantidad de bacterias")
        plt.title("evolución de la colonia")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        plt.savefig("evolucion_colonia.png")
        plt.close()

        print("se generó la gráfica 'evolucion_colonia.png'")
