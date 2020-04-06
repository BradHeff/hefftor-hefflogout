# =====================================================
#                  Author Brad Heffernan
# =====================================================

import cairo
import gi
import shutil
import GUI
import Functions as fn
import threading

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk, GdkPixbuf, Gdk, GLib, Gio  # noqa


class TransparentWindow(Gtk.Window):
    cmd_shutdown = "systemctl poweroff"
    cmd_restart = "systemctl reboot"
    cmd_suspend = "systemctl suspend"
    cmd_hibernate = "systemctl hibernate"
    cmd_lock = "betterlockscreen -l dimblur"
    frame_size = 100
    buttons = ["logout",
               "restart",
               "shutdown",
               "suspend",
               "hibernate",
               "lock"]
    binds = {'shutdown': 'S',
             'suspend': 'U',
             'logout': 'L',
             'restart': 'R',
             'lock': 'K',
             'hibernate': 'H',
             'cancel': 'Escape',
             'settings': 'P'}
    theme = "standard"
    active = False
    breaks = False

    def __init__(self):
        super(TransparentWindow, self).__init__(title="Arcolinux Logout")
        self.set_size_request(800, 600)
        self.monitor = 0
        self.connect('delete-event', self.on_close)
        self.connect('draw', self.draw)
        self.connect("key-press-event", self.on_keypress)
        self.connect("window-state-event", self.on_window_state_event)
        self.set_decorated(False)
        self.set_position(Gtk.WindowPosition.CENTER)

        if not fn.os.path.isdir(fn.home + "/.config/hefflogout"):
            fn.os.mkdir(fn.home + "/.config/hefflogout")

        if not fn.os.path.isfile(fn.home + "/.config/hefflogout/hefflogout.conf"):
            shutil.copy("/etc/hefflogout.conf", fn.home + "/.config/hefflogout/hefflogout.conf")

        screen = self.get_screen()

        screens = Gdk.Display.get_default()
        monitor = screens.get_monitor(0)
        rect = monitor.get_geometry()

        width = rect.width
        height = rect.height

        self.resize(width, height)

        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)

        fn.get_config(self, Gdk, fn.config, Gtk)
        # print(self.binds)

        self.fullscreen()
        self.set_app_paintable(True)
        GUI.GUI(self, Gtk, GdkPixbuf, fn.working_dir, fn.os, Gdk, fn)

        if not fn.file_check("/tmp/hefflogout.lock"):
            with open("/tmp/hefflogout.lock", "w") as f:
                f.write("")

    def on_save_clicked(self, widget):
        with open(fn.home + "/.config/hefflogout/hefflogout.conf", "r") as f:
            lines = f.readlines()
            f.close()
        try:
            pos_opacity = fn._get_position(lines, "opacity")
            pos_size = fn._get_position(lines, "icon_size")
            pos_frame_size = fn._get_position(lines, "frame_size")
            pos_theme = fn._get_position(lines, "theme=")

            lines[pos_opacity] = "opacity=" + str(int(self.hscale.get_text())) + "\n"
            lines[pos_size] = "icon_size=" + str(int(self.icons.get_text())) + "\n"
            lines[pos_frame_size] = "frame_size=" + str(int(self.frames.get_text())) + "\n"
            lines[pos_theme] = "theme=" + self.themes.get_active_text() + "\n"

            with open(fn.home + "/.config/hefflogout/hefflogout.conf", "w") as f:
                f.writelines(lines)
                f.close()
        except:
            print("Your missing settings. Please delete the local config for the new config to be copied over.\n\
or use meld to compare the global and local config to add new options.")
        self.popover.popdown()

    def on_cancel_clicked(self, widget):
        fn.os.unlink("/tmp/hefflogout.lock")
        Gtk.main_quit()

    def on_ok_clicked(self, widget):
        self.lbl_stats.set_markup("<span foreground=\"white\">Running ....</span>")  # noqa
        self.breaks = True

    def on_mouse_in(self, widget, event, data):
        if data == self.binds.get('shutdown'):
            psh = GdkPixbuf.Pixbuf().new_from_file_at_size(
                fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/shutdown_blur.svg'), int(self.icon), int(self.icon))
            self.imagesh.set_from_pixbuf(psh)
            self.lbl1.set_markup("<span foreground=\"white\">Shutdown</span>")
        elif data == self.binds.get('restart'):
            pr = GdkPixbuf.Pixbuf().new_from_file_at_size(
                fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/restart_blur.svg'), int(self.icon), int(self.icon))
            self.imager.set_from_pixbuf(pr)
            self.lbl2.set_markup("<span foreground=\"white\">Reboot</span>")
        elif data == self.binds.get('suspend'):
            ps = GdkPixbuf.Pixbuf().new_from_file_at_size(
                fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/suspend_blur.svg'), int(self.icon), int(self.icon))
            self.images.set_from_pixbuf(ps)
            self.lbl3.set_markup("<span foreground=\"white\">Suspend</span>")
        elif data == self.binds.get('lock'):
            plk = GdkPixbuf.Pixbuf().new_from_file_at_size(
                fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/lock_blur.svg'), int(self.icon), int(self.icon))
            self.imagelk.set_from_pixbuf(plk)
            self.lbl4.set_markup("<span foreground=\"white\">Lock</span>")
        elif data == self.binds.get('logout'):
            plo = GdkPixbuf.Pixbuf().new_from_file_at_size(
                fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/logout_blur.svg'), int(self.icon), int(self.icon))
            self.imagelo.set_from_pixbuf(plo)
            self.lbl5.set_markup("<span foreground=\"white\">Logout</span>")
        elif data == self.binds.get('cancel'):
            plo = GdkPixbuf.Pixbuf().new_from_file_at_size(
                fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/cancel_blur.svg'), int(self.icon), int(self.icon))
            self.imagec.set_from_pixbuf(plo)
            self.lbl6.set_markup("<span foreground=\"white\">Cancel</span>")
        elif data == self.binds.get('hibernate'):
            plo = GdkPixbuf.Pixbuf().new_from_file_at_size(
                fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/hibernate_blur.svg'), int(self.icon), int(self.icon))
            self.imageh.set_from_pixbuf(plo)
            self.lbl7.set_markup("<span foreground=\"white\">Hibernate</span>")
        elif data == self.binds.get('settings'):
            pset = GdkPixbuf.Pixbuf().new_from_file_at_size(
                fn.os.path.join(fn.working_dir, 'configure_blur.svg'), 48, 48)
            self.imageset.set_from_pixbuf(pset)
        event.window.set_cursor(Gdk.Cursor(Gdk.CursorType.HAND2))

    def on_mouse_out(self, widget, event, data):
        if not self.active:
            if data == self.binds.get('shutdown'):
                psh = GdkPixbuf.Pixbuf().new_from_file_at_size(
                    fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/shutdown.svg'), int(self.icon), int(self.icon))
                self.imagesh.set_from_pixbuf(psh)
                self.lbl1.set_markup("<span>Shutdown</span>")
            elif data == self.binds.get('restart'):
                pr = GdkPixbuf.Pixbuf().new_from_file_at_size(
                    fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/restart.svg'), int(self.icon), int(self.icon))
                self.imager.set_from_pixbuf(pr)
                self.lbl2.set_markup("<span>Reboot</span>")
            elif data == self.binds.get('suspend'):
                ps = GdkPixbuf.Pixbuf().new_from_file_at_size(
                    fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/suspend.svg'), int(self.icon), int(self.icon))
                self.images.set_from_pixbuf(ps)
                self.lbl3.set_markup("<span>Suspend</span>")
            elif data == self.binds.get('lock'):
                plk = GdkPixbuf.Pixbuf().new_from_file_at_size(
                    fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/lock.svg'), int(self.icon), int(self.icon))
                self.imagelk.set_from_pixbuf(plk)
                self.lbl4.set_markup("<span>Lock</span>")
            elif data == self.binds.get('logout'):
                plo = GdkPixbuf.Pixbuf().new_from_file_at_size(
                    fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/logout.svg'), int(self.icon), int(self.icon))
                self.imagelo.set_from_pixbuf(plo)
                self.lbl5.set_markup("<span>Logout</span>")
            elif data == self.binds.get('cancel'):
                plo = GdkPixbuf.Pixbuf().new_from_file_at_size(
                    fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/cancel.svg'), int(self.icon), int(self.icon))
                self.imagec.set_from_pixbuf(plo)
                self.lbl6.set_markup("<span>Cancel</span>")
            elif data == self.binds.get('hibernate'):
                plo = GdkPixbuf.Pixbuf().new_from_file_at_size(
                    fn.os.path.join(fn.working_dir, 'themes/' + self.theme + '/hibernate.svg'), int(self.icon), int(self.icon))
                self.imageh.set_from_pixbuf(plo)
                self.lbl7.set_markup("<span>Hibernate</span>")
            elif data == self.binds.get('settings'):
                pset = GdkPixbuf.Pixbuf().new_from_file_at_size(
                    fn.os.path.join(fn.working_dir, 'configure.svg'), 48, 48)
                self.imageset.set_from_pixbuf(pset)

    def on_click(self, widget, event, data):
        if not self.active or data == "settings":
            self.click_button(widget, data)

    def on_window_state_event(self, widget, ev):
        self.__is_fullscreen = bool(ev.new_window_state & Gdk.WindowState.FULLSCREEN)  # noqa

    def draw(self, widget, context):
        context.set_source_rgba(0, 0, 0, self.opacity)
        context.set_operator(cairo.OPERATOR_SOURCE)
        context.paint()
        context.set_operator(cairo.OPERATOR_OVER)

    def on_keypress(self, widget=None, event=None, data=None):
        self.shortcut_keys = [self.binds.get('cancel'), self.binds.get('shutdown'), self.binds.get('restart'), self.binds.get('suspend'), self.binds.get('logout'), self.binds.get('lock'), self.binds.get('hibernate'), self.binds.get('settings')]
        self.btnOK.set_sensitive(True)
        for key in self.shortcut_keys:
            if event.keyval == Gdk.keyval_to_lower(Gdk.keyval_from_name(key)):
                self.click_button(widget, key)

    def click_button(self, widget, data=None):
        if not (data == self.binds.get('cancel')) and not (data == self.binds.get('settings')):
            self.btnOK.set_sensitive(True)
            t = threading.Thread(target=fn.run_button,
                                 args=(self, data, Gtk, GLib,))
            t.daemon = True
            t.start()
        elif data == self.binds.get('cancel'):
            fn.os.unlink("/tmp/hefflogout.lock")
            Gtk.main_quit()
        else:
            self.themes.grab_focus()
            self.popover.set_relative_to(self.Eset)
            self.popover.show_all()
            self.popover.popup()

    def on_close(self, widget, data):
        fn.os.unlink("/tmp/hefflogout.lock")
        Gtk.main_quit()


if __name__ == "__main__":
    if not fn.file_check("/tmp/hefflogout.lock"):
        with open("/tmp/hefflogout.pid", "w") as f:
            f.write(str(fn.os.getpid()))
            f.close()

        if not fn.file_check("/tmp/logo.png"):
            file = fn.home + "/.face"
            if not fn.file_check(file):
                file = fn.working_dir + "logo.png"
            fn.subprocess.run(["cp", file, "/tmp/logo.png"])

        style_provider = Gtk.CssProvider()
        style_provider.load_from_path(fn.base_dir + "/hefflogout.css")

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        w = TransparentWindow()
        w.show_all()
        Gtk.main()
    else:
        print("something")
