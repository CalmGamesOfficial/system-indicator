import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

#Menu Options#
def quit_option(source):
    gtk.main_quit()

class optionsMenu():
    def menu(self):
        menu = gtk.Menu()
        item_quit = gtk.MenuItem('Quit')
        item_quit.connect('activate', quit_option)
        menu.append(item_quit)
        menu.show_all()
        return menu
