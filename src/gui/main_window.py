from gui.file_chooser import choose_directory, choose_file
from logic.utils import is_image_file

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Fotoose")

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.vbox.set_homogeneous(False)
        self.add(self.vbox)

        self.upper_box = Gtk.Box(spacing=6)
        self.middle_box = Gtk.Box(spacing=6)
        self.bottom_box = Gtk.Box(spacing=6)

        self.button1 = Gtk.Button(label="Choose file")
        self.button1.connect("clicked", self.button1_clicked)
        self.upper_box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Choose directory")
        self.button2.connect("clicked", self.button2_clicked)
        self.upper_box.pack_start(self.button2, True, True, 0)

        self.image = Gtk.Image()
        self.middle_box.pack_start(self.image, True, True, 0)

        self.label = Gtk.Label()
        self.label.set_text("No directory chosen")
        self.bottom_box.pack_start(self.label, True, True, 0)

        self.vbox.pack_start(self.upper_box, True, True, 0)
        self.vbox.pack_start(self.middle_box, True, True, 0)
        self.vbox.pack_start(self.bottom_box, True, True, 0)

    def button1_clicked(self, widget):
        image = choose_file(self, widget)
        if is_image_file(image):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                filename=image,
                width=200,
                height=200,
                preserve_aspect_ratio=True)

            self.image.set_from_pixbuf(pixbuf)

        print ("chose file: {}".format(image))

    def button2_clicked(self, widget):
        directory = choose_directory(self, widget)
        self.label.set_text(directory)
        print ("chose directory: {}".format(directory))
