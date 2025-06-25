import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from ventana import Ventana

class MiApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="z.z.z")

    def do_activate(self, *args):
        win = Ventana(self)
        win.present()

app = MiApp()
app.run()
