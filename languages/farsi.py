from tkinter import *
from tkinter import messagebox
import webbrowser

class Fa(Tk):
    def __init__(self, geometry, title, bg, icon):
        
        Tk.__init__(self)
        self.geometry(geometry)
        self.title(title)
        self.resizable(False, False)
        self.config(bg=bg)
        self.iconbitmap(icon)

        

    def create_lables_buttons_frame(self):
        pass

    def b_github(self):
        webbrowser.open('https://github.com/Saman148/Strange-App')

    def clear(self, frame):
        for i in frame.winfo_children() :
            i.destroy()

if __name__ == "__main__":
    obj = Fa('900x500', 
                'DevHelper Farsi py',
                '#36C2CE',
                r'images-lang\assistant-icon.ico',
                
                )
    obj.create_lables_buttons_frame()
    obj.mainloop()
