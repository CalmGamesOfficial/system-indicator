#gi.repository#  GObject, Gtk, AppIndicator
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Pango', '1.0')
from gi.repository import Gtk as gtk
from gi.repository import Pango as pango

#My modules
from modules import stats as stats
from modules import io as io

cpuswitch = gtk.Switch()
ramswitch = gtk.Switch()
ttuSpinButton = gtk.SpinButton()

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

def checkBox(self, text):
    hbox = gtk.HBox(True, 5)

    label = gtk.Label(text)

    cbtn = gtk.Switch()


    if(label == "CPU"):
        cbtn.set_active(stats.cpuBool)
        #cbtn.set_state(stats.cpuBool)

    elif(label == "RAM"):
        cbtn.set_active(stats.ramBool)
        #cbtn.set_state(stats.ramBool)
    elif(label == "DISK"):
        cbtn.set_active(stats.diskBool)
        #cbtn.set_state(stats.diskBool)

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
        self.set_resizable(False)
        self.set_default_size(256, 128)
        self.set_border_width(10)

        print("\033[34mloading...\033[0m")
        print(io.load(stats.cpu))
        print(io.load(stats.ram))
        print(io.load(stats.ttu))

        cpuswitch.set_active(io.load(stats.cpu))
        ramswitch.set_active(io.load(stats.ram))
        ttuSpinButton.set_value(float(io.load(stats.ttu)))

    def saveBottomButtons(self):
        hbox = gtk.HBox(True, 5)

        saveButton = gtk.Button("Save")
        saveButton.connect("clicked", self.onSaveChanges)
        cancelButton = gtk.Button("Exit")
        cancelButton.connect("clicked", gtk.main_quit)

        hbox.pack_start(saveButton, False, False, 0)
        hbox.pack_start(cancelButton, False, False, 0)

        return hbox

    def onSaveChanges(self, button):
        stats.cpuBool  = cpuswitch.get_active()
        stats.ramBool  = ramswitch.get_active()
        stats.ttuValue = ttuSpinButton.get_value()
        print("Saving..")
        io.save(self)
        print("\033[32m Saved \033[0m")
        print("CPU : " + str(stats.cpuBool))
        print("RAM : " + str(stats.ramBool))
        print("TTU : " + str(stats.ttuValue))

    def onSwitchCpu(self, switch, bool):
        if(switch.get_active() == True):
            stats.cpuBool = False
        else:
            stats.cpuBool = True
        cpuswitch.set_active(switch.get_active())

    def onSwitchRam(self, switch, bool):
        if(switch.get_active() == True):
            stats.ramBool = False
        else:
            stats.ramBool = True
        ramswitch.set_active(switch.get_active())

    def onSwitchTtu (self, SpinButton):
        stats.ttuValue = SpinButton.get_value()
        print(stats.ttuValue)

    def __init__(self):
        super(ConfigWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.create()
        #mainBox
        mainBox = gtk.Box()

        #VBox
        vbox = gtk.VBox(spacing = 7)


        """TITLES"""
        title = label(self,"<b>User Preferences</b>", 20)
        subtitle = label(self,"Show in top bar:", 13)

        """CPU SWITCH"""
        cpuBox = gtk.HBox(spacing = 3)
        cpuLabel = label(self, "CPU", 15)
        cpuSwitch = gtk.Switch()
        cpuSwitch.set_active(io.load(stats.cpu))
        cpuSwitch.connect("notify::active", self.onSwitchCpu)
        cpuBox.pack_start(cpuLabel, True, False, 0)
        cpuBox.pack_start(cpuSwitch, True, False, 0)

        """RAM SWITCH"""
        ramBox = gtk.HBox(spacing = 3)
        ramLabel = label(self, "RAM", 15)
        ramSwitch = gtk.Switch()
        ramSwitch.set_active(io.load(stats.ram))
        ramSwitch.connect("notify::active", self.onSwitchRam)
        ramBox.pack_start(ramLabel, True, False, 0)
        ramBox.pack_start(ramSwitch, True, False, 0)

        """TTU SPIN BUTTON"""
        ttuBox = gtk.HBox(spacing = 3)
        ttuLabel = label(self, "Time to Update", 10)
        ttuSpinButton = gtk.SpinButton()

        ttuSpinButton.set_digits(2)
        ttuSpinButton.set_range(0, 5)
        ttuSpinButton.set_increments(0.25, 0.25)
        ttuSpinButton.set_value(float(io.load(stats.ttu)))

        ttuSpinButton.connect("value-changed", self.onSwitchTtu)
        ttuBox.pack_start(ttuLabel, True, False, 0)
        ttuBox.pack_start(ttuSpinButton, True, False, 0)


        bottomButtons = self.saveBottomButtons()

        #vbox.add(title)
        #vbox.add(subtitle)
        vbox.add(cpuBox)
        vbox.add(ramBox)
        vbox.add(ttuBox)

        align = gtk.Alignment(xalign = 1.0, yalign = 1.0, xscale = 0, yscale = 0.3)
        align.add(bottomButtons)

        vbox.add(align)

        #packagerObject
        box = gtk.Box(spacing=1)
        #fix = gtk.Fixed()

        #fix.put(box, 0, 0)
        self.add(box)
        box.pack_start(vbox, True, False, 0)
