import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def choose_directory(parent, widget):
    dialog = Gtk.FileChooserDialog("Please choose a folder", parent,
                                   Gtk.FileChooserAction.SELECT_FOLDER,
                                   (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                    "Select", Gtk.ResponseType.OK))
    dialog.set_default_size(800, 400)

    chosen_directory = None
    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        chosen_directory = dialog.get_filename()
        print("Select clicked")
        print("Folder selected: " + chosen_directory)
    elif response == Gtk.ResponseType.CANCEL:
        print("Cancel clicked")

    dialog.destroy()

    return chosen_directory


def choose_file(parent, widget):
    dialog = Gtk.FileChooserDialog("Please choose a file", parent,
        Gtk.FileChooserAction.OPEN,
        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

    add_filters(dialog)

    chosen_file = None
    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        chosen_file = dialog.get_filename()
        print("Open clicked")
        print("File selected: " + chosen_file)
    elif response == Gtk.ResponseType.CANCEL:
        print("Cancel clicked")

    dialog.destroy()
    return chosen_file


def add_filters(dialog):
    filter_text = Gtk.FileFilter()
    filter_text.set_name("Text files")
    filter_text.add_mime_type("text/plain")
    dialog.add_filter(filter_text)

    filter_py = Gtk.FileFilter()
    filter_py.set_name("Python files")
    filter_py.add_mime_type("text/x-python")
    dialog.add_filter(filter_py)

    filter_any = Gtk.FileFilter()
    filter_any.set_name("Any files")
    filter_any.add_pattern("*")
    dialog.add_filter(filter_any)
