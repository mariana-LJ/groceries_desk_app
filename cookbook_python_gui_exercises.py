import time
import tkinter as tk

import Queues as qs
import Tooltip as tt
import URL as url

from queue import Queue
from os import makedirs
from os import path
from socketserver import BaseRequestHandler, TCPServer
from threading import Thread
from tkinter import filedialog as fd
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext
from tkinter import Spinbox
from tkinter import ttk

# Module level GLOBALS
GLOBAL_CONST = 42
fDir = path.dirname(__file__)
netDir = fDir + '\\Backup'
if not path.exists(netDir):
    makedirs(netDir, exist_ok=True)


class RequestHandler(BaseRequestHandler):
    # override base class handle method
    def handle(self):
        print('Server connected to: ', self.client_address)
        while True:
            rsp = self.request.recv(512)
            if not rsp:
                break
            self.request.send(b'Server received: ' + rsp)


def startServer():
    serv = TCPServer(('', 24000), RequestHandler)
    serv.serve_forever()


class OOP():

    def __init__(self):
        # Start TCP/IP server in its own thread
        svrT = Thread(target=startServer, daemon=True)
        svrT.start()
        # Create a Queue
        self.guiQueue = Queue()
        # Create instance
        self.win = tk.Tk()
        # Add a title
        self.win.title("Python GUI")
        self.createWidgets()
        self.defaultFileEntries()

    def methodInAThread(self, numOfLoops=10):
        for idx in range(numOfLoops):
            time.sleep(1)
            self.scr.insert(tk.INSERT, str(idx) + '\n')
            time.sleep(1)

    def defaultFileEntries(self):
        self.fileEntry.delete(0, tk.END)
        self.fileEntry.insert(0, fDir)
        if len(fDir) > self.entryLen:
            self.fileEntry.config(width=len(fDir) + 3)
            self.fileEntry.config(state='readonly')

        self.netwEntry.delete(0, tk.END)
        self.netwEntry.insert(0, netDir)
        if len(netDir) > self.entryLen:
            self.netwEntry.config(width=len(netDir) + 3)

    # Button Click event callback function
    def clickMe(self):
        #self.action.configure(text='Hello ' + self.name.get()+ ' ' + self.numberChosen.get())
        # aLabel.configure(foreground='red')
        # self.createThread(8)
        qs.writeToScrol(self)
        time.sleep(2)
        htmlData = url.getHtml()
        print(htmlData)
        self.scr.insert(tk.INSERT, htmlData)

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
        self.nameEntered = ttk.Entry(self.monty, width=24, textvariable=self.name)
        self.nameEntered.grid(column=0, row=1, sticky=tk.W)
        self.nameEntered.delete(0, tk.END)
        self.nameEntered.insert(0, '< default name>')
        # Place cursor into name Entry
        #self.nameEntered.focus()
        self.tabControl.select(1)

        # Adding combo box widgets
        ttk.Label(self.monty, text="Choose a number: ").grid(column=1, row=0)
        self.number = tk.StringVar()
        self.numberChosen = ttk.Combobox(self.monty, width=14, textvariable=self.number, state='readonly')
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

        # Using a sccrolled text control
        self.scrolW = 40
        self.scrolH = 10
        self.scr = scrolledtext.ScrolledText(self.monty, width=self.scrolW, height=self.scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, sticky='W', columnspan=3)

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

        # Add a tooltip
        tt.createToolTip(self.spin, 'This is a Spin control.')

        # Add tooltips for more widgets
        tt.createToolTip(self.nameEntered, 'This is an entry control.')
        tt.createToolTip(self.action, 'This is a button control.')
        tt.createToolTip(self.scr, 'This is a scrolled text control.')

        ###################################################################
        # Create Manage Files Frame
        mngFilesFrame = ttk.LabelFrame(self.tab2, text='Manage Files: ')
        mngFilesFrame.grid(column=0, row=1, sticky='WE', padx=10, pady=5)

        # Button Callback
        def getFilename():
            print('hello from getFileName')
            fDir = path.dirname(__file__)
            fName = fd.askopenfilename(parent=self.win, initialdir=fDir)

        # Add widgets to manage files frame
        lb = ttk.Button(mngFilesFrame, text="Browse to File...", command=getFilename)
        lb.grid(column=0, row=0, sticky=tk.W)

        file = tk.StringVar()
        self.entryLen = self.scrolW
        self.fileEntry = ttk.Entry(mngFilesFrame, width=self.entryLen, textvariable=file)
        self.fileEntry.grid(column=1, row=0, sticky=tk.W)

        logDir = tk.StringVar()
        self.netwEntry =ttk.Entry(mngFilesFrame, width=self.entryLen, textvariable=logDir)
        self.netwEntry.grid(column=1, row=1, sticky=tk.W)

        def copyFile():
            import shutil
            src = self.fileEntry.get()
            file = src.split('/')[-1]
            dest = self.netwEntry.get() + '\\' + file
            try:
                shutil.copy(src, dest)
                mBox.showinfo('Copy File to Network', 'Success: File copied.')
            except FileNotFoundError as err:
                mBox.showerror('Copy File to Network', '*** Failed to copy file! **\n\n' + str(err))
            except Exception as ex:
                mBox.showerror('Copy File to Network', '*** Failed to copy file! **\n\n' + str(ex))

        cb = ttk.Button(mngFilesFrame, text="Copy File to: ", command=copyFile)
        cb.grid(column=0, row=1, sticky=tk.E)

        # Add some space around each label
        for child in mngFilesFrame.winfo_children():
            child.grid_configure(padx=6, pady=6)

    # Running methods in Threads
    def createThread(self, num):
        self.runT = Thread(target=self.methodInAThread, args=[num])
        self.runT.setDaemon(True)
        self.runT.start()

        # textBoxes are the Consumers of Queue data
        writeT = Thread(target=self.useQueues, daemon=True)
        writeT.start()

    # Create queue instances
    def useQueues(self):
        # guiQueue = Queue()  # create queue instance
        # print(guiQueue)
        #for idx in range(10):
            #guiQueue.put('Message from a queue: ' + str(idx))

        #while True:
            #print(guiQueue.get())

        # Now using a class memeber Queue
        while True:
            print(self.guiQueue.get())



# =========================
# Start GUI
# =========================
oop = OOP()
oop.win.mainloop()
