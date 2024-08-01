from tkinter import *
from tkinter import messagebox

class Fa(Tk):
    def __init__(self, geometry, title, bg, icon):
        
        Tk.__init__(self)
        self.geometry(geometry)
        self.title(title)
        self.resizable(False, False)
        self.config(bg=bg)
        self.iconbitmap(icon)
        # self.photo_github = PhotoImage(file = r"images\github2.png")
        # self.photo_click = PhotoImage(file = r"images\click.png")
        # self.photo_sms = PhotoImage(file = r"images\sms.png")
        # self.photo_logo = PhotoImage(file = r"images\sms.png")
        # self.photo_sms = PhotoImage(file = r"images\sms.png")

        # self.photo_git64 = PhotoImage(file = r"images\github64.png")
        # self.photo_sms64 = PhotoImage(file = r"images\sms64.png")
        # self.photo_auto64 = PhotoImage(file = r"images\auto64.png")
        

    def create_lables_buttons_frame(self):
        pass

if __name__ == "__main__":
    obj = Fa('900x500', 
                'DevHelper Farsi py',
                '#508D4E',
                r'D:\SAMAN\projects-soon\python-projects\git-hub\DevHelper-py\images\assistant-icon.ico')
    obj.mainloop()
