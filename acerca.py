from gi.repository import Gtk

def mostrar_acerca_de(ventana):
    dialogo = Gtk.AboutDialog(
        transient_for=ventana,
        modal=True,
        program_name="Simulador Colonia Bacteriana",
        version="1.0",
        comments="Proyecto para modelar colonias bacterianas.\nDesarrollado por Danilo Martínez.",
        authors=["Danilo Martínez"],
        license_type=Gtk.License.GPL_3_0
    )
    dialogo.present()
