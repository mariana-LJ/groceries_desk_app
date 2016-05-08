import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

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
	mBox.showerror('Python Message Warning Box', 'A Python GUI created using tkinter:\nError: Houston we DO have a serious PROBLEM!')


helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)

win.mainloop()
