from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import subprocess
import webbrowser

class Fa(Tk):
    def __init__(self, geometry, title, bg, icon):
        Tk.__init__(self)
        self.geometry(geometry)
        self.title(title)
        self.resizable(True, True)
        self.config(bg=bg)
        self.iconbitmap(icon)
        self.photo = PhotoImage(file = r"images-main\github64.png")
        self.photo1 = PhotoImage(file = r"images-main\hand.png")
        self.photo2 = PhotoImage(file = r"images-main\3_people.png")
        self.photoFolder = PhotoImage(file=r'images-main\folder_64.png')

        

    def create_lables_buttons_frame(self): 
        main_fr = LabelFrame(self,
                             text='صفحه اصلی',
                             bd=6,
                             width=695,
                             height=490)
        main_fr.place(x=200, y=5)

        lWelcome = Label(main_fr, 
                         text='خیلی خوش اومدی',
                         font=('arial', 22, 'bold'))
        lWelcome.place(x=270, y=10)

        lGithub = Label(main_fr, 
                         text='https://github.com/Saman148',
                         font=('arial', 18, 'bold'))
        lGithub.place(x=200, y=400)

        lGithubPhoto = Label(main_fr, 
                         font=('arial', 18, 'bold'),
                         image=self.photo)
        lGithubPhoto.place(x=315, y=200)

        lhand = Label(main_fr, 
                         font=('arial', 18, 'bold'),
                         image=self.photo1)
        lhand.place(x=115, y=200)

        lpeople = Label(main_fr, 
                         font=('arial', 18, 'bold'),
                         image=self.photo2)
        lpeople.place(x=515, y=200)

        bt_venv = Button(self, 
                         text='ماشین مجازی (venv)',
                         font=('arial', 12, 'bold'),
                         activebackground='#478CCF',
                         activeforeground='white',
                         fg='black',
                         bg='#77E4C8',
                         width=18,
                         command=lambda: self.command_venv(main_fr))
        bt_venv.place(x=5, y=11)

        bt_git = Button(self, 
                         text='گیت (git)',
                         font=('arial', 12, 'bold'),
                         activebackground='#478CCF',
                         activeforeground='white',
                         fg='black',
                         bg='#77E4C8',
                         width=18,
                         command=lambda: self.command_git(main_fr))
        bt_git.place(x=5, y=51)

        bt_gpt = Button(self, 
                         text='هوش مصنوعی',
                         font=('arial', 12, 'bold'),
                         activebackground='#478CCF',
                         activeforeground='white',
                         fg='black',
                         bg='#77E4C8',
                         width=18,
                         command=lambda: self.command_gpt(main_fr))
        bt_gpt.place(x=5, y=92)

        bt_note = Button(self, 
                         text="یادداشت",
                         font=('arial', 12, 'bold'),
                         activebackground='#478CCF',
                         activeforeground='white',
                         fg='black',
                         bg='#77E4C8',
                         width=18,
                         command=lambda: self.command_note(main_fr))
        bt_note.place(x=5, y=133)

        bt_voice = Button(self, 
                         text='دستیار صوتی',
                         font=('arial', 12, 'bold'),
                         activebackground='#478CCF',
                         activeforeground='white',
                         fg='black',
                         bg='#77E4C8',
                         width=18,
                         command=lambda: self.command_voice(main_fr))
        bt_voice.place(x=5, y=175)

        bt_star = Button(self, 
                         text='ستاره یادت نره',
                         font=('arial', 12, 'bold'),
                         activebackground='#478CCF',
                         activeforeground='white',
                         fg='black',
                         bg='#77E4C8',
                         width=18,
                         command=lambda: self.command_myGit(main_fr))
        bt_star.place(x=5, y=216)
        
    def clear(self, frame):
            for i in frame.winfo_children() :
                i.destroy()
    

    def command_venv(self, frame):

        def get_path():
            try:
                file = filedialog.askdirectory()
                os.chdir(file)
                enGetPath.delete(0, END)
                enGetPath.insert(0,file)
            except:
                messagebox.showerror('خطا', 'اطلاعات وارد شده اشتباه هست')

        def create_venv():
            
            try:
                nameVenv = enName.get()
                if nameVenv == '':
                    messagebox.showerror('خطا', 'لطفا اسم ماشین مجازی را تایین کنید')
                else:
                    os.system(f'py -m venv {nameVenv}')
                    messagebox.showinfo('ماشین مجازی', 'ماشین مجازی با موفقیت ساخته شد')
                
                    btActiveVenv['state'] = 'active'
                
            except Exception as e:
                messagebox.showerror('خطا', e)

        
        def active_venv():
            
            main_path = enGetPath.get()
            nameVenv = enName.get()
            path = os.path.join(main_path, nameVenv, 'Scripts')
            os.chdir(path)
            command = 'activate.bat'
            os.system(f"start cmd /k {command}")


        self.clear(frame)

        lbVenv = Label(frame,
                       text='ماشین مجازی (venv)',
                       font=('arial', 18, 'bold'),
                       )
        lbVenv.place(x=255, y= 10)


        btGetPath = Button(frame,
                           image=self.photoFolder,
                           command=get_path)
        btGetPath.place(x=575, y= 80)

        enGetPath = Entry(frame,
                       width=40,
                       font=('arial', 18, 'bold'),
                       bg='#77E4C8')
        enGetPath.place(x=10, y=100)

        lbVenvName = Label(frame,
                       text=': اسم ماشین مجازی',
                       font=('arial', 18, 'bold'),
                       )
        lbVenvName.place(x=505, y= 180)

        enName = Entry(frame,
                       width=20,
                       font=('arial', 18, 'bold'),
                       justify='center',
                       bg='#77E4C8')
        enName.place(x=195, y=186)

        btCreateVenv = Button(frame,
                              text=' ساختن',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              command=create_venv,
                              )
        btCreateVenv.place(x=80, y=187)

        btActiveVenv = Button(frame,
                              text='فعال کردن',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              state='disabled',
                              command=active_venv
                              )
        btActiveVenv.place(x=300, y=300)

    def command_git(self, frame):
        def get_path_git():
            try:
                file = filedialog.askdirectory()
                os.chdir(file)
                enGetPath.delete(0, END)
                enGetPath.insert(0,file)
            except:
                messagebox.showerror('خطا', 'اطلاعات وارد شده اشتباه هست')

        self.clear(frame)

        lbgit = Label(frame,
                       text='گیت (git)',
                       font=('arial', 18, 'bold'),
                       )
        lbgit.place(x=255, y= 10)


        btGetPath = Button(frame,
                           image=self.photoFolder,
                           command=get_path_git)
        btGetPath.place(x=575, y= 80)

        enGetPath = Entry(frame,
                       width=30,
                       font=('arial', 18, 'bold'),
                       bg='#77E4C8')
        enGetPath.place(x=160, y=100)

        btInitGit  = Button(frame,
                              text= 'init',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=10
                              )
        btInitGit.place(x=30, y=100)

        btAddGit  = Button(frame,
                              text= 'add .',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=10,
                              state='disabled'
                              )
        btAddGit.place(x=540, y=195)

        btCommitGit  = Button(frame,
                              text= 'commit -m',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=10,
                              state='disabled'
                              )
        btCommitGit.place(x=400, y=195)

        btBranchGit  = Button(frame,
                              text= 'Branch',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=10,
                              state='disabled'
                              )
        btBranchGit.place(x=260, y=195)

        btSwitchGit  = Button(frame,
                              text= 'switch',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=10,
                              state='disabled'
                              )
        btSwitchGit.place(x=120, y=195)

        btMergeGit  = Button(frame,
                              text= 'merge',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=10,
                              state='disabled'
                              )
        btMergeGit.place(x=540, y=255)

        btMergeSquaGit  = Button(frame,
                              text= 'merge Squash',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=13,
                              state='disabled'
                              )
        btMergeSquaGit.place(x=370, y=255)

        btCheckOutGit  = Button(frame,
                              text= 'checkout commit',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=15,
                              state='disabled'
                              )
        btCheckOutGit.place(x=170, y=255)

        btLogGit  = Button(frame,
                              text= 'log',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=10,
                              state='disabled'
                              )
        btLogGit.place(x=540, y=315)

        btStatusGit  = Button(frame,
                              text= 'status',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=10,
                              state='disabled'
                              )
        btStatusGit.place(x=400, y=315)

        btPublishGit  = Button(frame,
                              text= 'publish',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=10,
                              state='disabled'
                              )
        btPublishGit.place(x=260, y=315)

        btCmdGit  = Button(frame,
                              text= 'open cmd',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=10,
                              state='disabled'
                              )
        btCmdGit.place(x=100, y=315)


    def command_gpt(self, frame):
        self.clear(frame)

    def command_note(self, frame):
        self.clear(frame)

    def command_voice(self, frame):
        self.clear(frame)

    def command_myGit(self, frame):
        self.clear(frame)



    def b_github(self):
        webbrowser.open('https://github.com/Saman148/Strange-App')

    

if __name__ == "__main__":
    obj = Fa('900x500', 
                'DevHelper Farsi py',
                '#36C2CE',
                r'images-main\assistant-icon.ico',
                
                )
    obj.create_lables_buttons_frame()
    obj.mainloop()
