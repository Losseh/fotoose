from gui.file_chooser import choose_directory
from logic.utils import is_image_file, map_to_chronological_names, retain_letters
from system.utils import rename_files, map_files_to_creation_time

from os import listdir
from os.path import join, basename

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Fotoose")

        accel = Gtk.AccelGroup()
        accel.connect(Gdk.keyval_from_name('N'), Gdk.ModifierType.CONTROL_MASK, 0, self.accel_previous_onclick)
        accel.connect(Gdk.keyval_from_name('M'), Gdk.ModifierType.CONTROL_MASK, 0, self.accel_next_onclick)
        accel.connect(Gdk.keyval_from_name('O'), Gdk.ModifierType.CONTROL_MASK, 0, self.accel_choose_directory)
        self.add_accel_group(accel)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.vbox.set_homogeneous(False)
        self.add(self.vbox)

        self.upper_box = Gtk.Box(spacing=6)
        self.middle_box = Gtk.Box(spacing=6)
        self.bottom_box = Gtk.Box(spacing=6)

        self.button_choose_dir = Gtk.Button(label="Choose directory")
        self.button_choose_dir.connect("clicked", self.button_choose_directory_onclick)
        self.upper_box.pack_start(self.button_choose_dir, True, True, 0)

        # initialization of the middle box
        self.button_previous = Gtk.Button(label="<")
        self.button_previous.connect("clicked", self.button_previous_onclick)

        self.button_next = Gtk.Button(label=">")
        self.button_next.connect("clicked", self.button_next_onclick)

        self.image = Gtk.Image()

        self.middle_box.pack_start(self.button_previous, True, True, 0)
        self.middle_box.pack_start(self.image, True, True, 0)
        self.middle_box.pack_start(self.button_next, True, True, 0)
        #

        self.label = Gtk.Label()
        self.bottom_box.pack_start(self.label, True, True, 0)
        self.vbox.pack_start(self.upper_box, True, True, 0)
        self.vbox.pack_start(self.middle_box, True, True, 0)
        self.vbox.pack_start(self.bottom_box, True, True, 0)

        self.rename_photos_button = Gtk.Button(label="Rename chronologically")
        self.rename_photos_button.connect('clicked', self.button_rename_photos)
        self.rename_photos_button.set_sensitive(False)
        self.vbox.pack_start(self.rename_photos_button, True, True, 0)

        self.path = None
        self.images = []
        self.active_image_id = 0
        self.set_empty_image()

    def button_choose_directory_onclick(self, widget):
        self.choose_dir(widget)

    def accel_choose_directory(self, *args):
        self.choose_dir(args[1])

    def choose_dir(self, widget):
        self.path = choose_directory(self, widget)
        self.open_dir()

    def open_dir(self):
        files = listdir(self.path)
        images = [f for f in files if is_image_file(join(self.path, f))]
        images.sort()
        self.open_images(images)
        self.rename_photos_button.set_sensitive(len(images) > 0)

    def button_previous_onclick(self, widget):
        self.previous_image()

    def accel_previous_onclick(self, *args):
        if self.button_previous.get_sensitive():
            self.previous_image()

    def previous_image(self):
        self.active_image_id -= 1
        self.update_image()

    def button_next_onclick(self, widget):
        self.next_image()

    def accel_next_onclick(self, *args):
        if self.button_next.get_sensitive():
            self.next_image()

    def button_rename_photos(self, widget):
        # TODO: this should be a method in some kind of Controller class
        file_to_creation_time = map_files_to_creation_time(self.path, self.images)

        max_number_of_files = 10000
        assert len(file_to_creation_time) < max_number_of_files, "The program does not manage to rename more than 10000 files"

        directory_name = retain_letters(basename(self.path)).lower()
        old_to_new_names = map_to_chronological_names(directory_name, file_to_creation_time)
        rename_files(self.path, old_to_new_names)
        #

        self.open_dir()

    def next_image(self):
        self.active_image_id += 1
        self.update_image()

    def open_images(self, images):
        if len(images) > 0:
            self.images = images
            self.active_image_id = 0
            self.update_image()
        else:
            self.set_empty_image()

    def update_image(self):
        image_id = self.active_image_id
        number_of_images = len(self.images)
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename=join(self.path, self.images[image_id]),
            width=1000,
            height=1000,
            preserve_aspect_ratio=True)
        self.image.set_from_pixbuf(pixbuf)
        self.button_previous.set_sensitive(image_id > 0)
        self.button_next.set_sensitive(image_id < number_of_images - 1)
        self.label.set_text("Photo {} / {}".format(image_id + 1, number_of_images))

    def set_empty_image(self):
        self.image.set_from_pixbuf(None)
        self.button_previous.set_sensitive(False)
        self.button_next.set_sensitive(False)
        self.label.set_text("No photos chosen")
