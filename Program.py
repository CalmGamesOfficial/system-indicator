#gi.repository#  GObject, Gtk, AppIndicator
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import GObject
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appIndicator

#other libs#  time, signal, psutil, threading
import time
import signal
import psutil
from threading import Thread

#app modules# io, stats, userPreferences, optionsMenu
#import modules.io as io
#import modules.stats as stats
import modules.userPreferences as config
from modules.menu import optionsMenu as menu
#Gobal Vars#
APPINDICATOR_ID = "SystemViewer"
timeToUpdate = 1
menu = menu()

class Indicator():
    #Main#
    def __init__(self):
        #Indicator
        config.create()
        self.indicator = appIndicator.Indicator.new(APPINDICATOR_ID, 'whatever', appIndicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(appIndicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(menu.menu())
        self.indicator.set_label("CPU: " + str(psutil.cpu_percent()) + "%", APPINDICATOR_ID)

        #Update
        self.update = Thread(target=self.show_seconds)
        self.update.setDaemon(True)
        self.update.start()

        #Return
        gtk.main()

    #Other defs#
    def show_seconds(self):
        while True:
            time.sleep(timeToUpdate)
            cpu = "CPU: " + str(psutil.cpu_percent()) + "%"
            GObject.idle_add(self.indicator.set_label, cpu, APPINDICATOR_ID, priority=GObject.PRIORITY_DEFAULT)

#__Init__
signal.signal(signal.SIGINT, signal.SIG_DFL)
GObject.threads_init()
Indicator()
