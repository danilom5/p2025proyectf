import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
import matplotlib
matplotlib.use("Agg")  # para que no abra ventanas extras y tire error


def generar_imagen_grilla(ruta_salida, grilla):

    grilla = np.array(grilla)



                                   # 5 indica que se quieren 5 colores diferentes (para los valores 0–4)
    cmap = plt.cm.get_cmap("Set1", 5) #Set1 es una paleta de colores con 5 categorías distintas.
    fig, ax = plt.subplots(figsize=(5, 5))
    cax = ax.matshow(grilla, cmap=cmap)

    leyenda = [
        Patch(facecolor=cmap(1/5), label="Bacteria activa"),
        Patch(facecolor=cmap(2/5), label="Muerta"),
        Patch(facecolor=cmap(3/5), label="Resistente"),
        Patch(facecolor=cmap(4/5), label="Biofilm"),
    ]
    ax.legend(handles=leyenda, loc="upper right", bbox_to_anchor=(1.4, 1))

    ax.set_xticks([])
    ax.set_yticks([])

    for i in range(10): #escribirle el numer
        for j in range(10):
            val = grilla[i, j]
            if val > 0:
                ax.text(j, i, str(int(val)), va="center", ha="center", color="white")

    plt.title("Grilla bacteriana estilo paso 1)")
    plt.tight_layout()
    plt.savefig(ruta_salida) 
    plt.close()
