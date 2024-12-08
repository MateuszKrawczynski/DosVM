from tkinter import *
from tkinter import filedialog
import os , shutil
root = Tk()
root.title("DosVM")
Label(root,text="DosVM",foreground="blue",font=("arial",30,"normal")).grid(row=0,column=0,padx=300)
def flash():
    flash = Tk()
    flash.title("DosVM - Insert flash devices")
    Label(flash,text="Select the flash drive port",foreground="blue",font=("arial",30,"normal")).grid(row=0,column=0)
    Label(flash,text="After selecting the port, you will select a folder which will be copied on this virtual flash drive").grid(row=1,column=0)
    class selection:
        def b(self=None):
            shutil.rmtree(f"{os.getcwd()}\\EXTERNAL_DRIVES\\B")
            os.mkdir(f"{os.getcwd()}\\EXTERNAL_DRIVES\\B")
            dir = filedialog.askdirectory()
            os.system(f'robocopy "{dir}" "{os.getcwd()}\\EXTERNAL_DRIVES\\B" /E')
            flash.destroy()
        def d(self=None):
            shutil.rmtree(f"{os.getcwd()}\\EXTERNAL_DRIVES\\D")
            os.mkdir(f"{os.getcwd()}\\EXTERNAL_DRIVES\\D")
            dir = filedialog.askdirectory()
            os.system(f'robocopy "{dir}" "{os.getcwd()}\\EXTERNAL_DRIVES\\D" /E')
            flash.destroy()
        def e(self=None):
            shutil.rmtree(f"{os.getcwd()}\\EXTERNAL_DRIVES\\E")
            os.mkdir(f"{os.getcwd()}\\EXTERNAL_DRIVES\\E")
            dir = filedialog.askdirectory()
            os.system(f'robocopy "{dir}" "{os.getcwd()}\\EXTERNAL_DRIVES\\E" /E')
            flash.destroy()
        def x(self=None):
            shutil.rmtree(f"{os.getcwd()}\\EXTERNAL_DRIVES\\X")
            os.mkdir(f"{os.getcwd()}\\EXTERNAL_DRIVES\\X")
            dir = filedialog.askdirectory()
            os.system(f'robocopy "{dir}" "{os.getcwd()}\\EXTERNAL_DRIVES\\X" /E')
            flash.destroy()
    Button(flash, text="B: - External drive will be visible as this in the Virtual Machine", font=("arial", 10, "normal"),command=selection.b).grid(row=2, column=0)
    Button(flash, text="D: - External drive will be visible as this in the Virtual Machine",
           font=("arial", 10, "normal"), command=selection.d).grid(row=3, column=0)
    Button(flash, text="E: - External drive will be visible as this in the Virtual Machine",
           font=("arial", 10, "normal"), command=selection.e).grid(row=4, column=0)
    Button(flash, text="X: - External drive will be visible as this in the Virtual Machine",
           font=("arial", 10, "normal"), command=selection.x).grid(row=5, column=0)
    flash.mainloop()
Button(root,text="Insert flash drives",font=("arial",10,"normal"),command=flash).grid(row=1,column=0)
def new():
    name = machine_name.get()
    if (name == "") or (name == None):
        notify = Tk()
        Label(notify,text="Enter machine name!").grid(row=0,column=0)
    else:
        if name in os.listdir(f"{os.getcwd()}\\VirtualMachines"):
            notify = Tk()
            Label(notify,text="Machine with this name already exists!").grid(row=0,column=0)
        else:
            os.mkdir(f"{os.getcwd()}\\VirtualMachines\\{name}")
            open(f"{os.getcwd()}\\VirtualMachines\\{name}\\AUTOEXEC.bat","w").write("")
            os.mkdir(f"{os.getcwd()}\\VirtualMachines\\{name}\\ProgramFiles")
            os.mkdir(f"{os.getcwd()}\\VirtualMachines\\{name}\\Documents")
NewContainer = Frame(root)
NewContainer.grid(row=2,column=0)
Button(NewContainer,text="Create a new machine",font=("arial",10,"normal"),command=new).grid(row=0,column=0)
machine_name = Entry(NewContainer)
Label(NewContainer,text="Machine name:").grid(row=0,column=1)
machine_name.grid(row=0,column=2)

def delmachine():
    name = machine_name_del.get()
    shutil.rmtree(f"{os.getcwd()}\\VirtualMachines\\{name}")

DelContainer = Frame(root)
DelContainer.grid(row=3,column=0)
Button(DelContainer,text="Delete a machine",font=("arial",10,"normal"),command=delmachine).grid(row=0,column=0)
machine_name_del = Entry(DelContainer)
Label(DelContainer,text="Machine name:").grid(row=0,column=1)
machine_name_del.grid(row=0,column=2,pady=20)

def launchInstance(name):
    os.putenv("INSTANCE",name)
    os.system("start dosinterpreter.exe")
Label(root,text="Select a Virtual Machine: ",font=("arial",20,"normal")).grid(row=4,column=0)
starter = 4
for name in os.listdir(f"{os.getcwd()}\\VirtualMachines"):
    starter = starter + 1
    Button(root,text=f"Launch: {name}",command= lambda: launchInstance(name)).grid(row=starter,column=0)


root.mainloop()