
# =====================================================
#                  Author Brad Heffernan
# =====================================================

import subprocess
import os
from pathlib import Path
import configparser
import getpass
from time import sleep
import threading

username = getpass.getuser()
home = os.path.expanduser("~")
base_dir = os.path.dirname(os.path.realpath(__file__))
# here = Path(__file__).resolve()
working_dir = ''.join([str(Path(__file__).parents[2]), "/share/hefflogout/"])
config = "/etc/hefflogout.conf"
# config = ''.join([str(Path(__file__).parents[3]), "/etc/hefflogout.conf"])


def cache_bl(self, GLib, Gtk):
    if os.path.isfile("/usr/bin/betterlockscreen"):
        with subprocess.Popen(["betterlockscreen", "-u",
                               self.wallpaper],
                              shell=False,
                              stdout=subprocess.PIPE) as f:
            for line in f.stdout:
                GLib.idle_add(self.lbl_stat.set_markup,
                              "<span  foreground=\"white\" size=\"large\"><b>" + line.decode().strip() +"</b></span>")  # noqa

        GLib.idle_add(self.lbl_stat.set_text, "")
        os.unlink("/tmp/hefflogout.lock")
        os.system(self.cmd_lock)
        Gtk.main_quit()
    else:
        print("not installed betterlockscreen.")


def get_config(self, Gdk, config):
    self.parser = configparser.SafeConfigParser()
    self.parser.read(config)

    # Set some safe defaults
    self.opacity = 0.6

    # Check if we're using HAL, and init it as required.
    if self.parser.has_section("settings"):
        if self.parser.has_option("settings", "opacity"):
            self.opacity = int(self.parser.get("settings", "opacity"))/100
        if self.parser.has_option("settings", "lock_wallpaper"):
            self.wallpaper = self.parser.get("settings", "lock_wallpaper")

    if self.parser.has_section("commands"):
        if self.parser.has_option("commands", "lock"):
            self.cmd_lock = self.parser.get("commands", "lock")

def _get_logout():
    out = subprocess.run(["sh", "-c", "env | grep DESKTOP_SESSION"],
                         shell=False, stdout=subprocess.PIPE)
    desktop = out.stdout.decode().split("=")[1].strip()

    if desktop in ("herbstluftwm", "/usr/share/xsessions/herbstluftwm"):
        return "herbstclient quit"
    elif desktop in ("bspwm", "/usr/share/xsessions/bspwm"):
        return "pkill bspwm"
    elif desktop in ("jwm", "/usr/share/xsessions/jwm"):
        return "pkill jwm"
    elif desktop in ("openbox", "/usr/share/xsessions/openbox"):
        return "pkill openbox"
    elif desktop in ("awesome", "/usr/share/xsessions/awesome"):
        return "pkill awesome"
    elif desktop in ("qtile", "/usr/share/xsessions/qtile"):
        return "pkill qtile"
    elif desktop in ("xmonad", "/usr/share/xsessions/xmonad"):
        return "pkill xmonad"
    elif desktop in ("dwm", "/usr/share/xsessions/dwm"):
        return "pkill dwm"
    elif desktop in ("i3", "/usr/share/xsessions/i3"):
        return "pkill i3"
    elif desktop in ("spectrwm", "/usr/share/xsessions/spectrwm"):
        return "pkill spectrwm"
    # elif desktop in ("xfce", "/usr/share/xsessions/xfce"):
    #     return "xfce4-session-logout --logout"

    return None


def run_button(self, data, Gtk, GLib):

    if not (data == 'K'):
        for i in range(10, 0, -1):
            if self.breaks:
                break

            GLib.idle_add(self.lbl_stats.set_markup,
                          "<span foreground=\"white\">Are you sure? " +
                          str(i) + " seconds</span>")
            sleep(1)
    GLib.idle_add(self.lbl_stats.set_markup,
                  "<span size=\"large\"><b></b></span>")
    if (data == 'L'):
        command = _get_logout()
        os.unlink("/tmp/hefflogout.lock")
        os.system(command)
        Gtk.main_quit()

    elif (data == 'R'):
        os.unlink("/tmp/hefflogout.lock")
        os.system(self.cmd_restart)
        Gtk.main_quit()

    elif (data == 'S'):
        os.unlink("/tmp/hefflogout.lock")
        os.system(self.cmd_shutdown)
        Gtk.main_quit()

    elif (data == 'U'):
        os.unlink("/tmp/hefflogout.lock")
        os.system(self.cmd_suspend)
        Gtk.main_quit()

    elif (data == 'H'):
        os.unlink("/tmp/hefflogout.lock")
        os.system(self.cmd_hibernate)
        Gtk.main_quit()

    elif (data == 'K'):
        if not os.path.isdir(home + "/.cache/i3lock"):
            if os.path.isfile(self.wallpaper):
                GLib.idle_add(toggle_buttons, self, False)
                GLib.idle_add(self.lbl_stat.set_markup,
                              "<span  foreground=\"white\" size=\"large\"><b>Caching lockscreen images for a faster locking next time</b></span>")  # noqa
                GLib.idle_add(self.lbl_stats.set_markup,
                              "<span foreground=\"white\">This will take a few seconds, please wait....</span>")
                t = threading.Thread(target=cache_bl,
                                     args=(self, GLib, Gtk,))
                t.daemon = True
                t.start()
            else:
                GLib.idle_add(self.lbl_stat.set_markup,
                              "<span foreground=\"white\" size=\"large\"><b>You need to set a wallpaper in the config file first</b></span>")  # noqa
        else:
            os.unlink("/tmp/hefflogout.lock")
            os.system(self.cmd_lock)
            Gtk.main_quit()
    else:
        os.unlink("/tmp/hefflogout.lock")
        Gtk.main_quit()


def toggle_buttons(self, state):
    self.btnOK.set_sensitive(state)
    self.btnCancel.set_sensitive(state)
    self.Esh.set_sensitive(state)
    self.Er.set_sensitive(state)
    self.Es.set_sensitive(state)
    self.El.set_sensitive(state)
    self.Eh.set_sensitive(state)


def file_check(file):
    if os.path.isfile(file):
        return True
