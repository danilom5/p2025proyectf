import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio
from acerca import mostrar_acerca_de
from generar_grilla import generar_imagen_grilla

class Ventana(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Colonia Bacteriana")
        self.set_default_size(800, 600)

        header = Gtk.HeaderBar()
        self.set_titlebar(header)

        # Label cantidad inicial
        self.lbl_cantidad = Gtk.Label(label="Cantidad inicial: 0")
        header.pack_start(self.lbl_cantidad)

        # Botón siguiente paso
        btn_siguiente = Gtk.Button(label="Siguiente paso")
        btn_siguiente.connect("clicked", self.on_siguiente_paso)
        header.pack_start(btn_siguiente)

        # Menú hamburguesa
        menu = Gio.Menu()
        menu.append("Acerca de", "app.acerca")

        menu_btn = Gtk.MenuButton()
        menu_btn.set_icon_name("open-menu-symbolic")
        menu_btn.set_menu_model(menu)
        header.pack_end(menu_btn)

        # Imagen de la grilla
        self.imagen = Gtk.Image()
        self.imagen.set_hexpand(True)
        self.imagen.set_vexpand(True)

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        caja.append(self.imagen)
        self.set_child(caja)

        # Conectar acción del menú
        app = self.get_application()
        app.add_action(self._crear_accion("acerca", lambda *a: mostrar_acerca_de(self)))

    def _crear_accion(self, nombre, funcion):
        accion = Gio.SimpleAction.new(nombre, None)
        accion.connect("activate", funcion)
        return accion

    def on_siguiente_paso(self, boton):
        print("Generando nueva imagen...")
        ruta = "grilla1.png"
        generar_imagen_grilla(ruta)
        self.imagen.set_from_file(ruta)

