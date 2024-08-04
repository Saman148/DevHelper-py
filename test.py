from tkinter import *
from tkinter import ttk, filedialog
import os

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.geometry("700x350")

def open_file():
    file = filedialog.askdirectory()
    if file:
        os.chdir(file)
        # Use os.system to list files in the current directory
        if os.name == 'nt':  # If the OS is Windows
            os.system('dir')
        else:  # For Linux and macOS
            os.system('ls')

# Add a Label widget
label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# Create a Button
ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

win.mainloop()
