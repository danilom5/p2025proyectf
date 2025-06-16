import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from ventana_colonia import Ventana

class MiApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.utalca.colonia")

    def do_activate(self, *args):
        win = Ventana(self)
        win.present()

if __name__ == "__main__":
    app = MiApp()
    app.run()
