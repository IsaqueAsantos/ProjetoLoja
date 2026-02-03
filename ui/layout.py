def center(widget, x=0.5, y=0.5):
    widget.place(relx=x, rely=y, anchor="center")


def fill(widget):
    widget.pack(fill="both", expand=True)
