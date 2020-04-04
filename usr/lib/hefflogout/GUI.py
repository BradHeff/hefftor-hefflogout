
# =====================================================
#                  Author Brad Heffernan
# =====================================================


def GUI(self, Gtk, GdkPixbuf, working_dir, os, Gdk, fn):
    mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    mainbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    lblbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    lbl = Gtk.Label(label="")

    self.lbl_stat = Gtk.Label()

    lblbox.pack_start(lbl, True, False, 0)
    lblbox.pack_start(self.lbl_stat, True, False, 0)

    overlayFrame = Gtk.Overlay()
    overlayFrame.add(lblbox)
    overlayFrame.add_overlay(mainbox)

    self.add(overlayFrame)

    vboxHead = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    hboxHead = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # vbox6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox8 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox9 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox10 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    buttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.Esh = Gtk.EventBox()
    self.Esh.connect("button_press_event", self.on_click, "S")
    self.Esh.connect("button-press-event", self.on_click)
    self.Esh.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    self.Esh.connect("enter-notify-event", self.on_mouse_in, "S")  # 2
    self.Esh.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    self.Esh.connect("leave-notify-event", self.on_mouse_out, "S")  # 2

    self.Er = Gtk.EventBox()
    self.Er.connect("button_press_event", self.on_click, "R")
    self.Er.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    self.Er.connect("enter-notify-event", self.on_mouse_in, "R")  # 2
    self.Er.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    self.Er.connect("leave-notify-event", self.on_mouse_out, "R")  # 2

    self.Es = Gtk.EventBox()
    self.Es.connect("button_press_event", self.on_click, "U")
    self.Es.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    self.Es.connect("enter-notify-event", self.on_mouse_in, "U")  # 2
    self.Es.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    self.Es.connect("leave-notify-event", self.on_mouse_out, "U")  # 2

    self.Elk = Gtk.EventBox()
    self.Elk.connect("button_press_event", self.on_click, "K")
    self.Elk.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    self.Elk.connect("enter-notify-event", self.on_mouse_in, "K")  # 2
    self.Elk.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    self.Elk.connect("leave-notify-event", self.on_mouse_out, "K")  # 2

    self.El = Gtk.EventBox()
    self.El.connect("button_press_event", self.on_click, "L")
    self.El.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    self.El.connect("enter-notify-event", self.on_mouse_in, "L")  # 2
    self.El.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    self.El.connect("leave-notify-event", self.on_mouse_out, "L")  # 2

    # Ec = Gtk.EventBox()
    # Ec.connect("button_press_event", self.on_click, "Escape")
    # Ec.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    # Ec.connect("enter-notify-event", self.on_mouse_in, "Escape")  # 2
    # Ec.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    # Ec.connect("leave-notify-event", self.on_mouse_out, "Escape")  # 2

    self.Eh = Gtk.EventBox()
    self.Eh.connect("button_press_event", self.on_click, "H")
    self.Eh.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    self.Eh.connect("enter-notify-event", self.on_mouse_in, "H")  # 2
    self.Eh.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    self.Eh.connect("leave-notify-event", self.on_mouse_out, "H")  # 2

    psh = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'themes/' + self.theme + '/shutdown.svg'), 64, 64)
    self.imagesh = Gtk.Image().new_from_pixbuf(psh)

    # pc = GdkPixbuf.Pixbuf().new_from_file_at_size(
    #     os.path.join(working_dir, 'themes/' + self.theme + '/cancel.svg'), 64, 64)
    # self.imagec = Gtk.Image().new_from_pixbuf(pc)

    pr = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'themes/' + self.theme + '/restart.svg'), 64, 64)
    self.imager = Gtk.Image().new_from_pixbuf(pr)

    ps = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'themes/' + self.theme + '/suspend.svg'), 64, 64)
    self.images = Gtk.Image().new_from_pixbuf(ps)

    plk = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'themes/' + self.theme + '/lock.svg'), 64, 64)
    self.imagelk = Gtk.Image().new_from_pixbuf(plk)

    plo = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'themes/' + self.theme + '/logout.svg'), 64, 64)
    self.imagelo = Gtk.Image().new_from_pixbuf(plo)

    ph = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'themes/' + self.theme + '/hibernate.svg'), 64, 64)
    self.imageh = Gtk.Image().new_from_pixbuf(ph)

    self.Esh.add(self.imagesh)
    self.Er.add(self.imager)
    self.Es.add(self.images)
    self.Elk.add(self.imagelk)
    self.El.add(self.imagelo)
    # Ec.add(self.imagec)
    self.Eh.add(self.imageh)

    self.lbl1 = Gtk.Label(label="Shutdown")
    self.lbl2 = Gtk.Label(label="Reboot")
    self.lbl3 = Gtk.Label(label="Suspend")
    self.lbl4 = Gtk.Label(label="Lock")
    self.lbl5 = Gtk.Label(label="Logout")
    # lbl6 = Gtk.Label(label="Cancel")
    self.lbl7 = Gtk.Label(label="Hibernate")
    self.lbl_stats = Gtk.Label()
    self.lbl_stats.set_markup("<span size=\"large\"><b></b></span>")
    lblUser = Gtk.Label(label=fn.username)

    self.imageu = Gtk.Image()
    frame = Gtk.Frame()
    frame.set_size_request(100, 100)
    frame.add(self.imageu)

    self.btnOK = Gtk.Button("OK")
    self.btnOK.set_size_request(140, 30)
    self.btnOK.set_css_name("button")
    self.btnOK.connect("clicked", self.on_ok_clicked)
    self.btnOK.set_sensitive(False)
    self.btnCancel = Gtk.Button("Cancel")
    self.btnCancel.connect("clicked", self.on_cancel_clicked)
    self.btnCancel.set_size_request(140, 30)
    self.btnCancel.set_css_name("button")

    vbox1.pack_start(self.Esh, False, False, 0)
    vbox1.pack_start(self.lbl1, False, False, 0)
    vbox2.pack_start(self.Er, False, False, 0)
    vbox2.pack_start(self.lbl2, False, False, 0)
    vbox3.pack_start(self.Es, False, False, 0)
    vbox3.pack_start(self.lbl3, False, False, 0)
    vbox4.pack_start(self.Elk, False, False, 0)
    vbox4.pack_start(self.lbl4, False, False, 0)
    vbox5.pack_start(self.El, False, False, 0)
    vbox5.pack_start(self.lbl5, False, False, 0)
    # vbox6.pack_start(Ec, False, False, 0)
    # vbox6.pack_start(lbl6, False, False, 0)
    vbox7.pack_start(self.Eh, False, False, 0)
    vbox7.pack_start(self.lbl7, False, False, 0)

    # hbox1.pack_start(vbox6, False, False, 10)
    hbox1.pack_start(vbox1, False, False, 10)
    hbox1.pack_start(vbox2, False, False, 10)
    hbox1.pack_start(vbox3, False, False, 10)
    hbox1.pack_start(vbox7, False, False, 10)
    hbox1.pack_start(vbox4, False, False, 10)
    hbox1.pack_start(vbox5, False, False, 10)

    vbox9.pack_start(self.btnOK, False, False, 0)
    vbox10.pack_start(self.btnCancel, False, False, 0)

    hbox2.pack_start(vbox9, False, False, 0)
    hbox2.pack_start(vbox10, False, False, 0)

    buttonbox.pack_start(hbox2, True, False, 0)

    vboxHead.pack_start(frame, False, False, 0)
    vboxHead.pack_start(lblUser, False, False, 0)

    hboxHead.pack_start(vboxHead, True, False, 0)

    vbox8.pack_start(hboxHead, False, False, 20)
    vbox8.pack_start(hbox1, False, False, 0)
    vbox8.pack_start(self.lbl_stats, False, False, 10)
    vbox8.pack_start(buttonbox, False, False, 20)

    mainbox2.pack_start(vbox8, True, False, 0)

    mainbox.pack_start(mainbox2, True, False, 0)
    # mainbox.pack_start(overlayFrame, False, False, 50)
