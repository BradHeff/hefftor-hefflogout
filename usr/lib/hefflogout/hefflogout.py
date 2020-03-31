from pathlib import Path
import cairo
import gi
import os
import GUI

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk, GdkPixbuf
from gi.repository import Gdk

home = os.path.expanduser("~")
base_dir = os.path.dirname(os.path.realpath(__file__))
here = Path(__file__).resolve()
working_dir = ''.join([str(here.parents[2]), "/share/hefflogout/"])


class TransparentWindow(Gtk.Window):
    cmd_shutdown = "systemctl poweroff"
    cmd_restart = "systemctl reboot"
    cmd_suspend = "pmi action suspend"
    cmd_lock = "betterlockscreen -l dimblur"
    cmd_logout = "openbox --exit"

    def __init__(self):
        Gtk.Window.__init__(self)

        self.set_size_request(300, 220)

        self.connect('destroy', Gtk.main_quit)
        self.connect('draw', self.draw)
        self.connect("key-press-event", self.on_keypress)
        self.connect("window-state-event", self.on_window_state_event)
        self.set_decorated(False)
        self.set_position(Gtk.WindowPosition.CENTER)

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)

        self.fullscreen()
        self.set_app_paintable(True)
        GUI.GUI(self, Gtk, GdkPixbuf, working_dir, os)
        self.show_all()

    def on_click(self, widget, event, data):
        self.click_button(widget, data)

    def on_window_state_event(self, widget, ev):
        self.__is_fullscreen = bool(ev.new_window_state & Gdk.WindowState.FULLSCREEN)

    def draw(self, widget, context):
        context.set_source_rgba(0, 0, 0, 0.6)
        context.set_operator(cairo.OPERATOR_SOURCE)
        context.paint()
        context.set_operator(cairo.OPERATOR_OVER)

    def on_keypress(self, widget=None, event=None, data=None):
        self.shortcut_keys = ["Escape", "S", "R", "U", "L", "K", "H"]

        for key in self.shortcut_keys:
            if event.keyval == Gdk.keyval_to_lower(Gdk.keyval_from_name(key)):
                self.click_button(widget, key)

    def click_button(self, widget, data=None):
        if (data == 'L'):
            self.__exec_cmd(self.cmd_logout)

        elif (data == 'R'):
            self.__exec_cmd(self.cmd_restart)

        elif (data == 'S'):
            self.__exec_cmd(self.cmd_shutdown)

        elif (data == 'U'):
            self.__exec_cmd(self.cmd_suspend)

        elif (data == 'H'):
            self.__exec_cmd(self.cmd_hibernate)

        elif (data == 'K'):
            self.__exec_cmd(self.cmd_lock)

        Gtk.main_quit()

    def __exec_cmd(self, cmdline):
        os.system(cmdline)


TransparentWindow()
Gtk.main()
