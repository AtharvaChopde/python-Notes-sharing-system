import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import sys


def CreateWidgets():
    link_Label = Label(root, text="Select Notes To Copy : ",
                       bg="#E8D579")
    link_Label.grid(row=4, column=1,
                    pady=5, padx=5)

    root.sourceText = Entry(root, width=50,
                            textvariable=sourceLocation)
    root.sourceText.grid(row=4, column=2,
                         pady=5, padx=5,
                         columnspan=2)

    source_browseButton = Button(root, text="Browse",
                                 command=SourceBrowse, width=20)
    source_browseButton.grid(row=4, column=4,
                             pady=5, padx=5)

    copyButton = Button(root, text="Add notes",
                        command=CopyFile, width=20)
    copyButton.grid(row=6, column=2,
                    pady=5, padx=5)

    moveButton = Button(root, text="Add notes and delete",
                        command=MoveFile, width=20)
    moveButton.grid(row=6, column=3,
                    pady=5, padx=5)
    openButtn = Button(root, text="Generate QR",
                       command=runQr, width=20)
    openButtn.grid(row=8, column=4,
                   pady=6, padx=6)
    
    link_Label = Label(root, text="Creators : \n\n1.Atharva Chopde \n\n2.Yeligatla Durga Revanth \n\n3.Yashashvi Yaduvanshi\n\n ",font=("Ariel",10),
                       bg="#a1e3e3")
    link_Label.grid(row=13, column=4,
                    pady=15, padx=10)

def SourceBrowse():

    root.files_list = list(filedialog.askopenfilenames(initialdir="C:/Users"))

    root.sourceText.insert('1', root.files_list)


def CopyFile():

    files_list = root.files_list

    destination_location = 'C:/Users/athar/OneDrive'

    for f in files_list:

        shutil.copy(f, 'C:/Users/athar/OneDrive')

    messagebox.showinfo("File Added")


def MoveFile():

    files_list = root.files_list

    destination_location = 'C:/Users/athar/OneDrive'

    for f in files_list:

        shutil.move(f, 'C:/Users/athar/OneDrive')

    messagebox.showinfo("File Added")


def runQr():
    root.destroy()

    import serverfile
    execfile("serverfile.py")
    sys.exit()


root = tk.Tk()


root.geometry("650x300")
root.title("NOTES sharing system")

root.config(background="grey")


sourceLocation = StringVar()
destinationLocation = StringVar()


CreateWidgets()


root.mainloop()
