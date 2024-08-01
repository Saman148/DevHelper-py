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
        #self.photo_github = PhotoImage(file = r'images-main\github2.png')


        #self.photo_git64 = PhotoImage(file = r'images-main\github64.png')

        

    def create_lables_buttons_frame(self):
        b_spammer = Button(self,
                        text="اسپمر " ,
                        font=('arial', 12, 'bold'),
                        activebackground='darkgreen',
                        activeforeground='white',
                        fg='black',
          #              compound=RIGHT,
                        bg='#80AF81',
                        command=lambda: self.b_page_spammer(fr_main),
                        width=202)
        b_spammer.place(x=5, y=10)

        b_autoClicker = Button(self,
                        text="اتو کیلیکر ",
                        font=('arial', 12, 'bold'),
                        activebackground='darkgreen',
                        activeforeground='white',
                        fg='black',
                #        compound=RIGHT,
                        bg='#80AF81',
                        command=lambda:self.b_page_autoClicker(fr_main),
                        width=202)
        b_autoClicker.place(x=5, y=55)

        b_github = Button(self,
                        text=" ستاره یادت نره ",
                        font=('arial', 12, 'bold'),
                        activebackground='darkgreen',
                        activeforeground='white',
                        fg='black',
                        bg='#80AF81',
                  #      image=self.photo_github,
                  #      compound=RIGHT,
                        command=self.b_github,
                        width=202)
        b_github.place(x=5, y=100)

        fr_main = LabelFrame(self, 
                             text='صفحه اصلی',
                        bd=5, 
                        width=675, 
                        fg='black',
                        height=490,
                        bg='#D6EFD8')
        fr_main.place(x=220, y=5)

        lb_wel2 = Label(fr_main,
                    text='Starage App',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_wel2.place(x=310, y=80)

        lb_wel = Label(fr_main,
                    text='خیلی خوش اومدی',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_wel.place(x=300, y=190)

        lb_info = Label(fr_main,
                    text='⭐ یادت نره حتما ستاره رو بدی ❤ ',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_info.place(x=220, y=240)

        lb_photosms = Label(fr_main,
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_photosms.place(x=250, y=300)

        lb_photogit = Label(fr_main,
                    font=('arial', 18, 'bold'),
                    pady=15,
                  #  image=self.photo_git64,
                    background='#D6EFD8',
                    foreground='black')
        lb_photogit.place(x=350, y=300)

        lb_photoauto = Label(fr_main,
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#D6EFD8',
                    foreground='black')
        lb_photoauto.place(x=450, y=300)

        lb_saman = Label(fr_main,
                         text=' github.com/Saman148',
                    font=('arial', 18, 'bold'),
                 #   image=self.photo_github,
                #    compound=LEFT,
                    background='#D6EFD8',
                    foreground='black')
        lb_saman.place(x=230, y=390)

        lb_saman2 = Label(self,
                         text=' github.com/Saman148',
                    font=('arial', 12, 'bold'),
              #      image=self.photo_github,
             #       compound=LEFT,
                    background='#508D4E',
                    foreground='black')
        lb_saman2.place(x=0, y=450)

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
