import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio
from acerca import mostrar_acerca_de
from hacerlagrilla import generar_imagen_grilla
from simulador import Simulador
from ambiente import Ambiente
from grilla_visual import obtener_grilla_visual 
from colonia import Colonia
from grilla_visual import obtener_grilla_visual
from gi.repository import GdkPixbuf
import os

class Ventana(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)

        # crear el ambiente
        ambiente = Ambiente(ancho=10, alto=10)

        # inicializar bacterias (por ejemplo, 20)
        lista_bacterias = ambiente.inicializar_bacterias(20)

        # crear la colonia
        colonia = Colonia(lista_bacterias)

        # crear el simulador con ese ambiente y colonia
        self.simulador = Simulador(ambiente, colonia)

        # guardar referencias útiles
        self.colonia = colonia
        self.ambiente = ambiente

#________________________________________________________________________________________________________

        self.set_title("Colonia Bacteriana")
        self.set_default_size(800, 600)

        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)

        # Label cantidad inicial
        self.lbl_cantidad = Gtk.Label(label="Cantidad inicial: 0")
        self.header.pack_start(self.lbl_cantidad)

        # Botón siguiente paso
        btn_siguiente = Gtk.Button(label="Siguiente paso")
        btn_siguiente.connect("clicked", self.on_siguiente_paso)
        self.header.pack_start(btn_siguiente)

        # Botón ver gráfico
        btn_grafico = Gtk.Button(label="Ver gráfico evolución")
        btn_grafico.connect("clicked", self.on_ver_grafico)
        self.header.pack_start(btn_grafico)

        # Menú hamburguesa
        menu = Gio.Menu()
        menu.append("Acerca de", "app.acerca")

        menu_btn = Gtk.MenuButton()
        menu_btn.set_icon_name("open-menu-symbolic")
        menu_btn.set_menu_model(menu)
        self.header.pack_end(menu_btn)

        # imagen para mostrar la grilla
        self.img = Gtk.Image()
        self.img.set_hexpand(True)
        self.img.set_vexpand(True)


        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        caja.append(self.img)
        self.set_child(caja)

        # Conectar acción del menú
        app = self.get_application()
        app.add_action(self._crear_accion("acerca", lambda *a: mostrar_acerca_de(self)))

    def _crear_accion(self, nombre, funcion):
        accion = Gio.SimpleAction.new(nombre, None)
        accion.connect("activate", funcion)
        return accion

    def on_siguiente_paso(self, boton):
        # ejecutar un paso de simulacion
        self.simulador.run(1)


        # convertir la grilla del ambiente en matriz visual
        grilla_numerica = obtener_grilla_visual(self.ambiente.grilla)
        ruta = generar_imagen_grilla(grilla_numerica)

        # cargar la imagen en el Image widget
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(ruta)
        self.img.set_from_pixbuf(pixbuf)
        ruta = generar_imagen_grilla(grilla_numerica)

        # cargar la imagen en el Image widget
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(ruta)
        self.img.set_from_pixbuf(pixbuf)

        # contar cantidad de bacterias activas
        cantidad_activas = 0
        for b in self.colonia.bacterias:
            if b.estado == "activa":
                cantidad_activas += 1

        # mostrar en el label
        self.lbl_cantidad.set_text(f"Cantidad activa: {cantidad_activas}")


        

    def on_ver_grafico(self):
        self.simulador.graficar_evolucion()

        import subprocess
        subprocess.run(["xdg-open", "evolucion_colonia.png"])




