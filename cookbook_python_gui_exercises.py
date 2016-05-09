import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import Spinbox

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
        print(self.widget.bbox("insert"))
        print(type(self.widget.bbox("insert")))
        x, y, cx, cy = self.widget.bbox("insert").split()
        x = int(x)
        y = int(y)
        cx = int(cx)
        cy = int(cy)
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


def createToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

win = tk.Tk()
win.title("Python GUI")
# Adding tabs
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.pack(expand=1, fill="both")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

# Creating a container frame to hold all other widgets
monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)

# Second label for second tab
monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
monty2.grid(column=0, row=0, padx=8, pady=4)
# win.resizable(0,0)
# Adding a label
aLabel = ttk.Label(monty, text="A label")
aLabel.grid(column=0, row=0)

# Button Click event callback function
def clickMe():
	action.configure(text='Hello ' + name.get()+ ' ' + numberChosen.get())
	# aLabel.configure(foreground='red')

# Adding a button
action = ttk.Button(monty, text="Click Me!", command=clickMe)
# Position button in second row, second column (zero-based)
action.grid(column=2, row=1)

# Changing label
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W')

# Adding a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky=tk.W)
# Place cursor into name Entry
nameEntered.focus()

# Adding combo box widgets
ttk.Label(monty, text="Choose a number: ").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Creating three checkbuttons

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)
chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty2, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Adding Radio buttons
colors = ["Blue", "Gold", "Red"]

# Radiobutton callback
def radCall():
	radSel = radVar.get()
	if radSel == 0: 
		# win.configure(background=colors[0])
		monty2.configure(text='Blue')
	elif radSel == 1:
		# win.configure(background=colors[1])
		monty2.configure(text='Gold')
	elif radSel == 2: 
		# win.configure(background=colors[2])
		monty2.configure(text='Red')

# create three radiobuttons
radVar = tk.IntVar()
# Select non-existing index for radVar
radVar.set(99)

# Create three radiobutton widgets with a loop
for col in range(3):
	curRad = 'rad' + str(col)
	curRad = tk.Radiobutton(monty2, text=colors[col], variable=radVar, value=col, command=radCall)
	curRad.grid(column=col, row=5, sticky=tk.W)

# Spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

# Adding a Spinbox widget
# spin = Spinbox(monty, from_=0, to=10, width=5, bd=8, command=_spin)
# Adding a Spinbox widget using a set of values
spin = Spinbox(monty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=_spin)
spin.grid(column=0, row=2)
# Adding a second Spinbox widget
spin2 = Spinbox(monty, values=(0, 50, 100), width=5, bd=8, relief=tk.RAISED, command=_spin)
spin2.grid(column=1, row=2)

# Add a tooltip
createToolTip(spin, 'This is a Spin control.')

# Using a sccrolled text control
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)

# Create a container to hold labels
labelsFrame = ttk.LabelFrame(monty2, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7, padx=20, pady=40)

# Place labels into the container element
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

# Add space around labels inside labelFrame
for child in labelsFrame.winfo_children():
	child.grid_configure(padx=8, pady=4)

# Place cursor into name Entry
nameEntered.focus()

# Menu bar with functionality
def _quit():
	win.quit()
	win.destroy()
	exit()

menuBar = Menu(win)
win.config(menu=menuBar)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Display a message box
# Callback function
def _msgBox():
	# mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter: \nThe Year is 2016.')
	# Warning box
	# mBox.showwarning('Python Message Warning Box', 'A Python GUI created using tkinter: \nWarning: There might be a bug in this code.')
	# Error box
	# mBox.showerror('Python Message Warning Box', 'A Python GUI created using tkinter:\nError: Houston we DO have a serious PROBLEM!')
    answer = mBox.askyesno("Python Message Dual Choice Box", "Are you sure you really wish to do this?")
    print(answer)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)

# Change the main windows icon
# win.iconbitmap(r'/usr/bin/python3/icon/path')

win.mainloop()
