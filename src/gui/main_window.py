from gui.file_chooser import choose_directory, choose_file

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Fotoose")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Choose file")
        self.button1.connect("clicked", self.button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Choose directory")
        self.button2.connect("clicked", self.button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

    def button1_clicked(self, widget):
        print ("chose file: {}".format(choose_file(self, widget)))

    def button2_clicked(self, widget):
        print ("chose directory: {}".format(choose_directory(self, widget)))
