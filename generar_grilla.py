import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
import matplotlib
matplotlib.use("Agg")  # ← Esto evita que matplotlib use una GUI como Tkinter


def generar_imagen_grilla(ruta_salida):
    # Creamos una grilla 10x10 con valores aleatorios entre 0 y 4
    grilla = np.random.randint(0, 5, size=(10, 10))

    cmap = plt.cm.get_cmap("Set1", 5)
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

    for i in range(10):
        for j in range(10):
            val = grilla[i, j]
            if val > 0:
                ax.text(j, i, str(int(val)), va="center", ha="center", color="white")

    plt.title("Grilla bacteriana (falsa)")
    plt.tight_layout()
    plt.savefig(ruta_salida)
    plt.close()
