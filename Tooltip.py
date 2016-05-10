import tkinter as tk


class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        # print(self.widget.bbox("insert"))
        # print(type(self.widget.bbox("insert")))
        x, y, cx, cy = self.widget.bbox("insert")
        # These steps seem to be necessary for older versions of Python (tkinter??)
        # .split()
        # x = int(x)
        # y = int(y)
        # cx = int(cx)
        # cy = int(cy)
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw =self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


# Create a tooltip tool
def createToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Leave>', leave)
    widget.bind('<Enter>', enter)
