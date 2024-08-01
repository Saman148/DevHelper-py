from tkinter import (Button, 
                     Radiobutton, 
                     Label, 
                     StringVar , 
                     TOP,
                     Tk,
                     LEFT,
                     BooleanVar,
                     PhotoImage,
                     messagebox)
from languages.farsi import Fa
import webbrowser

class Main(Tk):
    def __init__(self, geometry, title, bg, icon):
        
        Tk.__init__(self)
        self.geometry(geometry)
        self.title(title)
        self.resizable(False, False)
        self.config(bg=bg)
        self.iconbitmap(icon)
        self.photo = PhotoImage(file = r"images-main\github2.png")

    def create_lables_buttons_radios(self):
        lb_info = Label(self,
                    text='Welcome to DevHelper python',
                    font=('arial', 18, 'bold'),
                    pady=15,
                    background='#36C2CE',
                    foreground='black')
        lb_info.pack()


        # Radio buttons
        values = {"فارسی" : "fa", 
                "English (soon)" : "en"} 
        
        v = StringVar(self, "fa") 

        for (text, value) in values.items(): 
            Radiobutton(self, text = text, variable = v, bg='#36C2CE', fg='black', activebackground='darkgreen',font=('arial', 12, 'bold'),
                value = value).pack(side = TOP, ipady = 5) 

        # buttons
        b_submit = Button(self,
                        text="Submit",
                        font=('arial', 12, 'bold'),
                        activebackground='#478CCF',
                        activeforeground='white',
                        fg='black',
                        bg='#77E4C8',
                        command=lambda:self.select_lang(v, v1),
                        width=10)
        b_submit.place(x=197, y=200)

        b_github = Button(self,
                        text=" Give me ⭐",
                        font=('arial', 12, 'bold'),
                        activebackground='#478CCF',
                        activeforeground='white',
                        fg='black',
                        cursor='star',
                        image=self.photo,
                        compound=LEFT,
                        bg='#77E4C8',
                        command=self.link_github)
        b_github.place(x=30, y=200)

        v1 = BooleanVar(value=False) 

        Radiobutton(self, text = "Don't show me again", variable = v1, bg='#36C2CE', fg='black', activebackground='darkgreen',font=('arial', 12, 'bold'),
                value = True, command=lambda:self.dont_show(v1)).place(x=30, y=250)

    def link_github(self):
        webbrowser.open('https://github.com/Saman148/DevHelper-py')  #repostory url

    def dont_show(self, show):
        value = show.get()
        if value:
            with open(r'txt\show.txt', 'w') as f:
                f.write('True')
            
    def select_lang(self, lang, a):
        lang_value = lang.get()
        with open(r'txt/lang.txt', 'w') as f:
            f.write(lang_value)

        if lang_value == 'fa': #farsi language
                self.destroy()
                obj = Fa('900x500', 
                'DevHelper Farsi py',
                '#36C2CE',
                r'images-main/assistant-icon.ico',)
                obj.create_lables_buttons_frame()
                obj.mainloop()

        if lang_value == 'en': #english language
            messagebox.showinfo('language', 'English comming soon')    #open english file

if __name__ == "__main__":
    
    with open(r'txt/show.txt', 'r') as f:
        show = f.read()
    with open(r'txt/lang.txt', 'r') as f:
        lang = f.read()

    if show == 'True':
        if lang == 'fa':
            pass

        elif lang == 'en':
            pass   #open english file
    else:
        obj1 = Main('500x300',
                    "DevHelper py",
                    '#36C2CE',
                    "images-main/assistant-icon.ico",)
        obj1.create_lables_buttons_radios()
        obj1.mainloop()
