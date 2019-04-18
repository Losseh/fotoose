from gui.main_window import MainWindow

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import logging

logging.basicConfig(level=logging.DEBUG)

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
