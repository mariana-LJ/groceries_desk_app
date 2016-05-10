import tkinter as tk
import Tooltip as tt
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import Spinbox


class OOP():
    def __init__(self):
        # Create instance
        self.win = tk.Tk()
        # Add a title
        self.win.title("Python GUI")
        self.createWidgets()

    # Button Click event callback function
    def clickMe(self):
        self.action.configure(text='Hello ' + self.name.get()+ ' ' + self.numberChosen.get())
        # aLabel.configure(foreground='red')

    # Radiobutton callback
    def radCall(self):
        radSel = self.radVar.get()
        if radSel == 0:
            # win.configure(background=colors[0])
            self.monty2.configure(text='Blue')
        elif radSel == 1:
            # win.configure(background=colors[1])
            self.monty2.configure(text='Gold')
        elif radSel == 2:
            # win.configure(background=colors[2])
            self.monty2.configure(text='Red')

    # Spinbox callback
    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scr.insert(tk.INSERT, value + '\n')

    # Display a message box Callback function
    def _msgBox(self):
        # mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter: \nThe Year is 2016.')
        # Warning box
        # mBox.showwarning('Python Message Warning Box', 'A Python GUI created using tkinter: \nWarning: There might be a bug in this code.')
        # Error box
        # mBox.showerror('Python Message Warning Box', 'A Python GUI created using tkinter:\nError: Houston we DO have a serious PROBLEM!')
        answer = mBox.askyesno("Python Message Dual Choice Box", "Are you sure you really wish to do this?")
        print(answer)

    # Menu bar with functionality
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def createWidgets(self):
        # Adding tabs
        self.tabControl = ttk.Notebook(self.win)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Tab 1')
        self.tabControl.pack(expand=1, fill="both")
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='Tab 2')

        # Creating a container frame to hold all other widgets
        self.monty = ttk.LabelFrame(self.tab1, text=' Monty Python ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)

        # Second label for second tab
        self.monty2 = ttk.LabelFrame(self.tab2, text=' The Snake ')
        self.monty2.grid(column=0, row=0, padx=8, pady=4)
        # win.resizable(0,0)
        # Adding a label
        self.aLabel = ttk.Label(self.monty, text="A label")
        self.aLabel.grid(column=0, row=0)


        # Adding a button
        self.action = ttk.Button(self.monty, text="Click Me!", command=self.clickMe)
        # Position button in second row, second column (zero-based)
        self.action.grid(column=2, row=1)

        # Changing label
        ttk.Label(self.monty, text="Enter a name:").grid(column=0, row=0, sticky='W')

        # Adding a textbox entry widget
        self.name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.monty, width=12, textvariable=self.name)
        self.nameEntered.grid(column=0, row=1, sticky=tk.W)
        # Place cursor into name Entry
        self.nameEntered.focus()

        # Adding combo box widgets
        ttk.Label(self.monty, text="Choose a number: ").grid(column=1, row=0)
        self.number = tk.StringVar()
        self.numberChosen = ttk.Combobox(self.monty, width=12, textvariable=self.number, state='readonly')
        self.numberChosen['values'] = (1, 2, 4, 42, 100)
        self.numberChosen.grid(column=1, row=1)
        self.numberChosen.current(0)

        # Creating three checkbuttons

        self.chVarDis = tk.IntVar()
        self.check1 = tk.Checkbutton(self.monty2, text="Disabled", variable=self.chVarDis, state='disabled')
        self.check1.select()
        self.check1.grid(column=0, row=4, sticky=tk.W)
        self.chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.monty2, text="UnChecked", variable=self.chVarUn)
        self.check2.deselect()
        self.check2.grid(column=1, row=4, sticky=tk.W)
        self.chVarEn = tk.IntVar()
        self.check3 = tk.Checkbutton(self.monty2, text="Enabled", variable=self.chVarEn)
        self.check3.select()
        self.check3.grid(column=2, row=4, sticky=tk.W)

        # Adding Radio buttons
        self.colors = ["Blue", "Gold", "Red"]

        # create three radiobuttons
        self.radVar = tk.IntVar()
        # Select non-existing index for radVar
        self.radVar.set(99)

        # Create three radiobutton widgets with a loop
        for col in range(3):
            curRad = 'rad' + str(col)
            curRad = tk.Radiobutton(self.monty2, text=self.colors[col], variable=self.radVar, value=col, command=self.radCall)
            curRad.grid(column=col, row=5, sticky=tk.W)

        # Adding a Spinbox widget
        # spin = Spinbox(monty, from_=0, to=10, width=5, bd=8, command=_spin)
        # Adding a Spinbox widget using a set of values
        self.spin = Spinbox(self.monty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=self._spin)
        self.spin.grid(column=0, row=2)
        # Adding a second Spinbox widget
        self.spin2 = Spinbox(self.monty, values=(0, 50, 100), width=5, bd=8, relief=tk.RAISED, command=self._spin)
        self.spin2.grid(column=1, row=2)

        # Add a tooltip
        tt.createToolTip(self.spin, 'This is a Spin control.')

        # Using a sccrolled text control
        self.scrolW = 30
        self.scrolH = 3
        self.scr = scrolledtext.ScrolledText(self.monty, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, sticky='WE', columnspan=3)

        # Create a container to hold labels
        self.labelsFrame = ttk.LabelFrame(self.monty2, text=' Labels in a Frame ')
        self.labelsFrame.grid(column=0, row=7, padx=20, pady=40)

        # Place labels into the container element
        ttk.Label(self.labelsFrame, text="Label1").grid(column=0, row=0)
        ttk.Label(self.labelsFrame, text="Label2").grid(column=0, row=1)
        ttk.Label(self.labelsFrame, text="Label3").grid(column=0, row=2)

        # Add space around labels inside labelFrame
        for child in self.labelsFrame.winfo_children():
            child.grid_configure(padx=8, pady=4)

        # Place cursor into name Entry
        self.nameEntered.focus()

        # Create a menu
        self.menuBar = Menu(self.win)
        self.win.config(menu=self.menuBar)
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="New")
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self._quit)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        self.helpMenu = Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="About", command=self._msgBox)
        self.menuBar.add_cascade(label="Help", menu=self.helpMenu)

        # Change the main windows icon
        # win.iconbitmap(r'/usr/bin/python3/icon/path')


# =========================
# Start GUI
# =========================
oop = OOP()
oop.win.mainloop()
