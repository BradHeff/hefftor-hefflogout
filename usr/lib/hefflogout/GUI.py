
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
    vbox6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox8 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox9 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox10 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    buttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    Esh = Gtk.EventBox()
    Esh.connect("button_press_event", self.on_click, "S")
    Esh.connect("button-press-event", self.on_click)
    Esh.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    Esh.connect("enter-notify-event", self.on_mouse_in, "S")  # 2
    Esh.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    Esh.connect("leave-notify-event", self.on_mouse_out, "S")  # 2

    Er = Gtk.EventBox()
    Er.connect("button_press_event", self.on_click, "R")
    Er.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    Er.connect("enter-notify-event", self.on_mouse_in, "R")  # 2
    Er.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    Er.connect("leave-notify-event", self.on_mouse_out, "R")  # 2

    Es = Gtk.EventBox()
    Es.connect("button_press_event", self.on_click, "U")
    Es.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    Es.connect("enter-notify-event", self.on_mouse_in, "U")  # 2
    Es.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    Es.connect("leave-notify-event", self.on_mouse_out, "U")  # 2

    # Elk = Gtk.EventBox()
    # Elk.connect("button_press_event", self.on_click, "K")
    # Elk.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    # Elk.connect("enter-notify-event", self.on_mouse_in, "K")  # 2
    # Elk.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    # Elk.connect("leave-notify-event", self.on_mouse_out, "K")  # 2

    El = Gtk.EventBox()
    El.connect("button_press_event", self.on_click, "L")
    El.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    El.connect("enter-notify-event", self.on_mouse_in, "L")  # 2
    El.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    El.connect("leave-notify-event", self.on_mouse_out, "L")  # 2

    # Ec = Gtk.EventBox()
    # Ec.connect("button_press_event", self.on_click, "Escape")
    # Ec.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    # Ec.connect("enter-notify-event", self.on_mouse_in, "Escape")  # 2
    # Ec.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    # Ec.connect("leave-notify-event", self.on_mouse_out, "Escape")  # 2

    Eh = Gtk.EventBox()
    Eh.connect("button_press_event", self.on_click, "H")
    Eh.add_events(Gdk.EventMask.ENTER_NOTIFY_MASK)  # 1
    Eh.connect("enter-notify-event", self.on_mouse_in, "H")  # 2
    Eh.add_events(Gdk.EventMask.LEAVE_NOTIFY_MASK)  # 1
    Eh.connect("leave-notify-event", self.on_mouse_out, "H")  # 2

    psh = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'shutdown.svg'), 64, 64)
    self.imagesh = Gtk.Image().new_from_pixbuf(psh)

    # pc = GdkPixbuf.Pixbuf().new_from_file_at_size(
    #     os.path.join(working_dir, 'cancel.svg'), 64, 64)
    # self.imagec = Gtk.Image().new_from_pixbuf(pc)

    pr = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'restart.svg'), 64, 64)
    self.imager = Gtk.Image().new_from_pixbuf(pr)

    ps = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'suspend.svg'), 64, 64)
    self.images = Gtk.Image().new_from_pixbuf(ps)

    # plk = GdkPixbuf.Pixbuf().new_from_file_at_size(
    #     os.path.join(working_dir, 'lock.svg'), 64, 64)
    # self.imagelk = Gtk.Image().new_from_pixbuf(plk)

    plo = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'logout.svg'), 64, 64)
    self.imagelo = Gtk.Image().new_from_pixbuf(plo)

    ph = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(working_dir, 'hibernate.svg'), 64, 64)
    self.imageh = Gtk.Image().new_from_pixbuf(ph)

    Esh.add(self.imagesh)
    Er.add(self.imager)
    Es.add(self.images)
    # Elk.add(self.imagelk)
    El.add(self.imagelo)
    # Ec.add(self.imagec)
    Eh.add(self.imageh)

    lbl1 = Gtk.Label(label="Shutdown")
    lbl2 = Gtk.Label(label="Reboot")
    lbl3 = Gtk.Label(label="Suspend")
    # lbl4 = Gtk.Label(label="Lock")
    lbl5 = Gtk.Label(label="Logout")
    # lbl6 = Gtk.Label(label="Cancel")
    lbl7 = Gtk.Label(label="Hibernate")
    self.lbl_stats = Gtk.Label()
    lblUser = Gtk.Label(label=fn.username)

    pu = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(fn.home, '.face'), 64, 64)
    imageu = Gtk.Image().new_from_pixbuf(pu)

    frame = Gtk.Frame()
    frame.set_css_name("frame")
    frame.set_name("frame")
    frame.add(imageu)

    btnOK = Gtk.Button("OK")
    btnOK.set_size_request(140, 30)
    btnOK.set_css_name("button")
    btnCancel = Gtk.Button("Cancel")
    btnCancel.set_size_request(140, 30)
    btnCancel.set_css_name("button")

    vbox1.pack_start(Esh, False, False, 0)
    vbox1.pack_start(lbl1, False, False, 0)
    vbox2.pack_start(Er, False, False, 0)
    vbox2.pack_start(lbl2, False, False, 0)
    vbox3.pack_start(Es, False, False, 0)
    vbox3.pack_start(lbl3, False, False, 0)
    # vbox4.pack_start(Elk, False, False, 0)
    # vbox4.pack_start(lbl4, False, False, 0)
    vbox5.pack_start(El, False, False, 0)
    vbox5.pack_start(lbl5, False, False, 0)
    # vbox6.pack_start(Ec, False, False, 0)
    # vbox6.pack_start(lbl6, False, False, 0)
    vbox7.pack_start(Eh, False, False, 0)
    vbox7.pack_start(lbl7, False, False, 0)

    # hbox1.pack_start(vbox6, False, False, 10)
    hbox1.pack_start(vbox1, False, False, 10)
    hbox1.pack_start(vbox2, False, False, 10)
    hbox1.pack_start(vbox3, False, False, 10)
    hbox1.pack_start(vbox7, False, False, 10)
    # hbox1.pack_start(vbox4, False, False, 10)
    hbox1.pack_start(vbox5, False, False, 10)

    vbox9.pack_start(btnOK, False, False, 0)
    vbox10.pack_start(btnCancel, False, False, 0)

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
