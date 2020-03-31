

def GUI(self, Gtk, GdkPixbuf, working_dir, os):
    mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    mainbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    self.add(mainbox)

    vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)

    Esh = Gtk.EventBox()
    Esh.connect("button_press_event", self.on_click, "S")
    Er = Gtk.EventBox()
    Er.connect("button_press_event", self.on_click, "R")
    Es = Gtk.EventBox()
    Es.connect("button_press_event", self.on_click, "U")
    Elk = Gtk.EventBox()
    Elk.connect("button_press_event", self.on_click, "K")
    El = Gtk.EventBox()
    El.connect("button_press_event", self.on_click, "L")

    psh = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'shutdown.svg'), 64, 64)
    imagesh = Gtk.Image().new_from_pixbuf(psh)

    pr = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'restart.svg'), 64, 64)
    imager = Gtk.Image().new_from_pixbuf(pr)

    ps = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'suspend.svg'), 64, 64)
    images = Gtk.Image().new_from_pixbuf(ps)

    plk = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'lock.svg'), 64, 64)
    imagelk = Gtk.Image().new_from_pixbuf(plk)

    plo = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'logout.svg'), 64, 64)
    imagelo = Gtk.Image().new_from_pixbuf(plo)

    Esh.add(imagesh)
    Er.add(imager)
    Es.add(images)
    Elk.add(imagelk)
    El.add(imagelo)

    lbl1 = Gtk.Label(label="Shutdown")
    lbl2 = Gtk.Label(label="Reboot")
    lbl3 = Gtk.Label(label="Suspend")
    lbl4 = Gtk.Label(label="Lock")
    lbl5 = Gtk.Label(label="Logout")

    vbox1.pack_start(Esh, False, False, 0)
    vbox1.pack_start(lbl1, False, False, 0)
    vbox2.pack_start(Er, False, False, 0)
    vbox2.pack_start(lbl2, False, False, 0)
    vbox3.pack_start(Es, False, False, 0)
    vbox3.pack_start(lbl3, False, False, 0)
    vbox4.pack_start(Elk, False, False, 0)
    vbox4.pack_start(lbl4, False, False, 0)
    vbox5.pack_start(El, False, False, 0)
    vbox5.pack_start(lbl5, False, False, 0)

    hbox1.pack_start(vbox1, False, False, 30)
    hbox1.pack_start(vbox2, False, False, 30)
    hbox1.pack_start(vbox3, False, False, 30)
    hbox1.pack_start(vbox4, False, False, 30)
    hbox1.pack_start(vbox5, False, False, 30)

    mainbox2.pack_start(hbox1, True, False, 0)

    mainbox.pack_start(mainbox2, True, False, 0)
