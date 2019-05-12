#gi.repository#  GObject, Gtk, AppIndicator
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Pango', '1.0')
from gi.repository import Gtk as gtk
from gi.repository import Pango as pango

from modules import stats as stats
from modules import io as io

def run():
    window = ConfigWindow()
    window.show_all()
    gtk.main()

def label(self, text, size):
    hbox = gtk.VBox(True, 1)

    label = gtk.Label()

    font = pango.FontDescription("/Montserrat.ttf " + str(size))
    label.modify_font(font)
    label.set_markup(text)

    hbox.set_homogeneous(True)
    hbox.pack_start(label, True, True, 0)

    return hbox

def saveBottomButtons():
    hbox = gtk.HBox(True, 5)

    saveButton = gtk.Button("Save")
    saveButton.connect("clicked", io.save)
    cancelButton = gtk.Button("Cancel")
    cancelButton.connect("clicked", gtk.main_quit)

    hbox.pack_start(saveButton, False, False, 0)
    hbox.pack_start(cancelButton, False, False, 0)

    return hbox

def checkBox(self, text, active):
    hbox = gtk.HBox(True, 5)

    label = gtk.Label(text)

    cbtn = gtk.Switch()
    cbtn.set_active(active)

    #hbox.set_homogeneous(True)
    hbox.pack_start(label, False, False, 0)
    hbox.pack_start(cbtn, True, False, 0)

    #fix = gtk.Fixed()
    #fix.put(hbox, 0, 0)

    return hbox

class ConfigWindow(gtk.Window):
    def create(self):
        self.connect("destroy", gtk.main_quit)
        self.set_icon_from_file("resources/imgs/favicon.png")
        self.set_title("User Preferences")
        self.set_default_size(256, 384)
        self.set_border_width(10)
        #self.set_interactive_debugging(True)

    def switchAction(self, switch, bool):
            if switch.get_active():
                bool = True
            else:
                bool = False

    def __init__(self):
        super(ConfigWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.create()

        #mainBox
        mainBox = gtk.Box()

        #VBox
        vbox = gtk.VBox(spacing = 7)

        title = label(self,"<b>User Preferences</b>", 20)
        subtitle = label(self,"<b>Show in top bar:</b>", 13)
        cpuSwitch = checkBox(self, "CPU", True)
        #cpuSwitch.connect("notify::active", self.switchAction(cpuSwitch, stats.cpuBool))
        ramSwitch = checkBox(self, "RAM", False)
        #ramSwitch.connect("notify::active", self.switchAction(ramSwitch, stats.ramBool))
        diskSwitch = checkBox(self, "DISK", False)
        #diskSwitch.connect("notify::active", self.switchAction(diskSwitch, stats.diskBool))

        bottomButtons = saveBottomButtons()

        vbox.add(title)
        vbox.add(subtitle)
        vbox.add(cpuSwitch)
        vbox.add(ramSwitch)
        vbox.add(diskSwitch)

        align = gtk.Alignment(xalign = 1.0, yalign = 1.0, xscale = 0, yscale = 0.3)
        align.add(bottomButtons)

        vbox.add(align)

        #packagerObject
        box = gtk.Box(spacing=1)
        #fix = gtk.Fixed()

        #fix.put(box, 0, 0)
        self.add(box)
        box.pack_start(vbox, True, False, 0)
