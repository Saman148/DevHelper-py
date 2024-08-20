from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import subprocess
import webbrowser
import threading
from openai import OpenAI


class Fa(Tk):
    def __init__(self, geometry, title, bg, icon):
        Tk.__init__(self)
        self.geometry(geometry)
        self.title(title)
        self.resizable(False, False)
        self.config(bg=bg)
        self.iconbitmap(icon)
        self.photo = PhotoImage(file=r"images-main\github64.png")
        self.photo1 = PhotoImage(file=r"images-main\hand.png")
        self.photo2 = PhotoImage(file=r"images-main\3_people.png")
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
                         text='ستاره یادت نره ⭐',
                         font=('arial', 12, 'bold'),
                         activebackground='#478CCF',
                         activeforeground='white',
                         fg='black',
                         bg='#77E4C8',
                         width=18,
                         command=lambda: self.command_myGit(main_fr))
        bt_star.place(x=5, y=216)

        lb_githubb = Label(self,
                            text='github.com/Saman148',
                         font=('arial', 12, 'bold'),
                         fg='black',
                         bg='#77E4C8')
        lb_githubb.place(x=5, y=460)

        lb_version = Label(self,
                         text='1.0.0 V',
                         font=('arial', 12, 'bold'),
                         fg='black',
                         bg='#77E4C8',
)
        lb_version.place(x=65, y=260)

    def clear(self, frame):
        for i in frame.winfo_children():
            i.destroy()

    def command_venv(self, frame):

        frame.config(bg='white', fg='black')
        def get_path():
            try:
                file = filedialog.askdirectory()
                os.chdir(file)
                enGetPath.delete(0, END)
                enGetPath.insert(0, file)
            except:
                messagebox.showerror('خطا', 'اطلاعات وارد شده اشتباه هست')

        def create_venv():

            try:
                nameVenv = enName.get()
                if nameVenv == '':
                    messagebox.showerror(
                        'خطا', 'لطفا اسم ماشین مجازی را تایین کنید')
                else:
                    os.system(f'py -m venv {nameVenv}')
                    messagebox.showinfo(
                        'ماشین مجازی', 'ماشین مجازی با موفقیت ساخته شد')

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
        lbVenv.place(x=255, y=10)

        btGetPath = Button(frame,
                           image=self.photoFolder,
                           command=get_path)
        btGetPath.place(x=575, y=80)

        enGetPath = Entry(frame,
                          width=40,
                          font=('arial', 18, 'bold'),
                          bg='#77E4C8')
        enGetPath.place(x=10, y=100)

        lbVenvName = Label(frame,
                           text=': اسم ماشین مجازی',
                           font=('arial', 18, 'bold'),
                           )
        lbVenvName.place(x=505, y=180)

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
        frame.config(bg='white', fg='black')
        def get_path_git():

            try:
                file = filedialog.askdirectory()
                os.chdir(file)
                enGetPath.delete(0, END)
                enGetPath.insert(0, file)
            except:
                messagebox.showerror('خطا', 'اطلاعات وارد شده اشتباه هست')

        def init_git():
            try:
                file = enGetPath.get()
                os.chdir(file)
                a = subprocess.check_output('git init', shell=True, text=True)
                messagebox.showinfo('گیت', a)
                btAddGit['state'] = 'active'
                btStatusGit['state'] = 'active'
                btCmdGit['state'] = 'active'
                btPublishGit['state'] = 'active'
                btInitGit['state'] = 'disabled'

            except Exception as e:
                messagebox.showerror('خطا', e)

        def add_git():
            try:

                a = subprocess.check_output('git add .', shell=True, text=True)
                messagebox.showinfo('گیت', a)
                btBranchGit['state'] = 'active'
                btCommitGit['state'] = 'active'

            except Exception as e:
                messagebox.showerror('خطا', e)

        def commit_git():
            root = Toplevel()
            root.title('commit name')
            root.config(bg='#36C2CE')
            root.geometry('250x100')
            root.resizable(False, False)

            def commit_final():
                try:
                    messsageCommit = messsage.get()
                    a = subprocess.check_output(
                        f'git commit -m "{messsageCommit}"', shell=True, text=True)
                    messagebox.showinfo('گیت', a)
                    btCheckOutGit['state'] = 'active'
                    btLogGit['state'] = 'active'

                except Exception as e:
                    messagebox.showerror('خطا', e)

            messsage = Entry(root,
                             width=18,
                             font=('arial', 18, 'bold'),
                             bg='#77E4C8')
            messsage.place(x=5, y=5)

            submit = Button(root,
                            text='تایید',
                            font=('arial', 10, 'bold'),
                            activebackground='#478CCF',
                            activeforeground='white',
                            fg='black',
                            bg='#77E4C8',
                            width=18,
                            command=commit_final)
            submit.place(x=40, y=60)

            root.mainloop()

        def branch_git():
            root = Toplevel()
            root.title('branch name')
            root.config(bg='#36C2CE')
            root.geometry('250x100')
            root.resizable(False, False)

            def branch_final():
                try:
                    branchName = messsage.get()
                    a = subprocess.check_output(
                        f'git branch "{branchName}"', shell=True, text=True)
                    messagebox.showinfo('گیت', a)
                    btMergeGit['state'] = 'active'
                    btMergeSquaGit['state'] = 'active'
                    btSwitchGit['state'] = 'active'

                except Exception as e:
                    messagebox.showerror('خطا', e)

            messsage = Entry(root,
                             width=18,
                             font=('arial', 18, 'bold'),
                             bg='#77E4C8')
            messsage.place(x=5, y=5)

            submit = Button(root,
                            text='تایید',
                            font=('arial', 10, 'bold'),
                            activebackground='#478CCF',
                            activeforeground='white',
                            fg='black',
                            bg='#77E4C8',
                            width=18,
                            command=branch_final)
            submit.place(x=40, y=60)

            root.mainloop()

        def switch_git():
            root = Toplevel()
            root.title('switch branch')
            root.config(bg='#36C2CE')
            root.geometry('250x100')
            root.resizable(False, False)

            def switch_final():
                try:
                    branchName = messsage.get()
                    a = subprocess.check_output(
                        f'git switch "{branchName}"', shell=True, text=True)
                    messagebox.showinfo('گیت', a)

                except Exception as e:
                    messagebox.showerror('خطا', e)

            messsage = Entry(root,
                             width=18,
                             font=('arial', 18, 'bold'),
                             bg='#77E4C8')
            messsage.place(x=5, y=5)

            submit = Button(root,
                            text='تایید',
                            font=('arial', 10, 'bold'),
                            activebackground='#478CCF',
                            activeforeground='white',
                            fg='black',
                            bg='#77E4C8',
                            width=18,
                            command=switch_final)
            submit.place(x=40, y=60)

            root.mainloop()

        def merge_git():
            root = Toplevel()
            root.title('merge branch')
            root.config(bg='#36C2CE')
            root.geometry('250x100')
            root.resizable(False, False)

            def merge_final():
                try:
                    branchName = messsage.get()
                    a = subprocess.check_output(
                        f'git merge "{branchName}"', shell=True, text=True)
                    messagebox.showinfo('گیت', a)

                except Exception as e:
                    messagebox.showerror('خطا', e)

            messsage = Entry(root,
                             width=18,
                             font=('arial', 18, 'bold'),
                             bg='#77E4C8')
            messsage.place(x=5, y=5)

            submit = Button(root,
                            text='تایید',
                            font=('arial', 10, 'bold'),
                            activebackground='#478CCF',
                            activeforeground='white',
                            fg='black',
                            bg='#77E4C8',
                            width=18,
                            command=merge_final)
            submit.place(x=40, y=60)

            root.mainloop()

        def merge_squach_git():
            root = Toplevel()
            root.title('merge squach branch')
            root.config(bg='#36C2CE')
            root.geometry('250x100')
            root.resizable(False, False)

            def merge_squach_final():
                try:

                    branchName = messsage.get()
                    a = subprocess.check_output(
                        f'git merge --squach "{branchName}"', shell=True, text=True)
                    messagebox.showinfo('گیت', a)

                except Exception as e:
                    messagebox.showerror('خطا', e)

            messsage = Entry(root,
                             width=18,
                             font=('arial', 18, 'bold'),
                             bg='#77E4C8')
            messsage.place(x=5, y=5)

            submit = Button(root,
                            text='تایید',
                            font=('arial', 10, 'bold'),
                            activebackground='#478CCF',
                            activeforeground='white',
                            fg='black',
                            bg='#77E4C8',
                            width=18,
                            command=merge_squach_final)
            submit.place(x=40, y=60)

            root.mainloop()

        def checkout_commit_git():
            root = Toplevel()
            root.title('checkout commit')
            root.config(bg='#36C2CE')
            root.geometry('250x100')
            root.resizable(False, False)

            def checkout_commit_final():
                try:
                    commitName = messsage.get()
                    a = subprocess.check_output(
                        f'git checkout "{commitName}"', shell=True, text=True)
                    messagebox.showinfo('گیت', a)

                except Exception as e:
                    messagebox.showerror('خطا', e)

            messsage = Entry(root,
                             width=18,
                             font=('arial', 18, 'bold'),
                             bg='#77E4C8')
            messsage.place(x=5, y=5)

            submit = Button(root,
                            text='تایید',
                            font=('arial', 10, 'bold'),
                            activebackground='#478CCF',
                            activeforeground='white',
                            fg='black',
                            bg='#77E4C8',
                            width=18,
                            command=checkout_commit_final)
            submit.place(x=40, y=60)

            root.mainloop()

        def log_git():
            os.system(f"start cmd /k git log")

        def status_git():
            os.system(f"start cmd /k git status")

        def publish_git():
            root = Toplevel()
            root.title('publish on github')
            root.config(bg='#36C2CE')
            root.geometry('250x100')
            root.resizable(False, False)

            def publish_final():
                try:
                    publishUrl = messsage.get()
                    

                    os.system(f"start cmd /c git branch -M main")
                    os.system(f"start cmd /c git remote add origin {publishUrl}") 
                    os.system(f"start cmd /k git push -u origin main") 

                    messagebox.showinfo('گیت', 'هپلود شد در صورت اپلود نشدن مجدد امتحان کنید به اینترنت هم وصل باشید')

                except Exception as e:
                    messagebox.showerror('خطا', e)

            messsage = Entry(root,
                             width=18,
                             font=('arial', 18, 'bold'),
                             bg='#77E4C8')
            messsage.place(x=5, y=5)

            submit = Button(root,
                            text='تایید',
                            font=('arial', 10, 'bold'),
                            activebackground='#478CCF',
                            activeforeground='white',
                            fg='black',
                            bg='#77E4C8',
                            width=18,
                            command=publish_final)
            submit.place(x=40, y=60)

            root.mainloop()

        def open_cmd_git():

            os.system(f"start cmd /k ")

        self.clear(frame)

        lbgit = Label(frame,
                      text='گیت (git)',
                      font=('arial', 18, 'bold'),
                      )
        lbgit.place(x=255, y=10)

        btGetPath = Button(frame,
                           image=self.photoFolder,
                           command=get_path_git)
        btGetPath.place(x=575, y=80)

        enGetPath = Entry(frame,
                          width=30,
                          font=('arial', 18, 'bold'),
                          bg='#77E4C8')
        enGetPath.place(x=160, y=100)

        btInitGit = Button(frame,
                           text='init',
                           font=('arial', 12, 'bold'),
                           activebackground='#478CCF',
                           activeforeground='white',
                           fg='black',
                           bg='#77E4C8',
                           width=10,
                           command=init_git
                           )
        btInitGit.place(x=30, y=100)

        btAddGit = Button(frame,
                          text='add .',
                          font=('arial', 12, 'bold'),
                          activebackground='#478CCF',
                          activeforeground='white',
                          fg='black',
                          bg='#77E4C8',
                          width=10,
                          state='disabled',
                          command=add_git
                          )
        btAddGit.place(x=540, y=195)

        btCommitGit = Button(frame,
                             text='commit -m',
                             font=('arial', 12, 'bold'),
                             activebackground='#478CCF',
                             activeforeground='white',
                             fg='black',
                             bg='#77E4C8',
                             width=10,
                             state='disabled',
                             command=commit_git
                             )
        btCommitGit.place(x=400, y=195)

        btBranchGit = Button(frame,
                             text='Branch',
                             font=('arial', 12, 'bold'),
                             activebackground='#478CCF',
                             activeforeground='white',
                             fg='black',
                             bg='#77E4C8',
                             width=10,
                             state='disabled',
                             command=branch_git
                             )
        btBranchGit.place(x=260, y=195)

        btSwitchGit = Button(frame,
                             text='switch',
                             font=('arial', 12, 'bold'),
                             activebackground='#478CCF',
                             activeforeground='white',
                             fg='black',
                             bg='#77E4C8',
                             width=10,
                             state='disabled',
                             command=switch_git
                             )
        btSwitchGit.place(x=120, y=195)

        btMergeGit = Button(frame,
                            text='merge',
                            font=('arial', 12, 'bold'),
                            activebackground='#478CCF',
                            activeforeground='white',
                            fg='black',
                            bg='#77E4C8',
                            width=10,
                            state='disabled',
                            command=merge_git
                            )
        btMergeGit.place(x=540, y=255)

        btMergeSquaGit = Button(frame,
                                text='merge Squash',
                                font=('arial', 12, 'bold'),
                                activebackground='#478CCF',
                                activeforeground='white',
                                fg='black',
                                bg='#77E4C8',
                                width=13,
                                state='disabled',
                                command=merge_squach_git
                                )
        btMergeSquaGit.place(x=370, y=255)

        btCheckOutGit = Button(frame,
                               text='checkout commit',
                               font=('arial', 12, 'bold'),
                               activebackground='#478CCF',
                               activeforeground='white',
                               fg='black',
                               bg='#77E4C8',
                               width=15,
                               state='disabled',
                               command=checkout_commit_git
                               )
        btCheckOutGit.place(x=170, y=255)

        btLogGit = Button(frame,
                          text='log',
                          font=('arial', 12, 'bold'),
                          activebackground='#478CCF',
                          activeforeground='white',
                          fg='black',
                          bg='#77E4C8',
                          width=10,
                          state='disabled',
                          command=log_git
                          )
        btLogGit.place(x=540, y=315)

        btStatusGit = Button(frame,
                             text='status',
                             font=('arial', 12, 'bold'),
                             activebackground='#478CCF',
                             activeforeground='white',
                             fg='black',
                             bg='#77E4C8',
                             width=10,
                             state='disabled',
                             command=status_git
                             )
        btStatusGit.place(x=400, y=315)

        btPublishGit = Button(frame,
                              text='publish',
                              font=('arial', 12, 'bold'),
                              activebackground='#478CCF',
                              activeforeground='white',
                              fg='black',
                              bg='#77E4C8',
                              width=10,
                              state='disabled',
                              command=publish_git
                              )
        btPublishGit.place(x=260, y=315)

        btCmdGit = Button(frame,
                          text='open cmd',
                          font=('arial', 12, 'bold'),
                          activebackground='#478CCF',
                          activeforeground='white',
                          fg='black',
                          bg='#77E4C8',
                          width=10,
                          state='disabled',
                          command=open_cmd_git
                          )
        btCmdGit.place(x=100, y=315)

    def command_gpt(self, frame):
        self.clear(frame)
        frame.config(bg='white', fg='black')

        root = Toplevel()
        root.title('get api')
        root.config(bg='#36C2CE')
        root.geometry('250x100')
        root.resizable(False, False)

        def publish_final():
            def gpt_submit():
                try:
                    text = tx.get("1.0", 'end-1c')
                    tx.delete("1.0", 'end-1c')

                    client = OpenAI(
                        api_key=api,  # your api key
                    )

                    stream = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": text}],
                        stream=True,
                    )
                    for chunk in stream:
                        if chunk.choices[0].delta.content is not None:
                            a = chunk.choices[0].delta.content, end = ""

                    roo2 = Toplevel()
                    roo2.title('chat gpt')
                    txxx = Text(roo2)
                    txxx.pack()
                    txxx.insert("1.0", a)

                    roo2.mainloop()

                except Exception as e:
                    print(e)
                    messagebox.showerror('خطا', e)

            try:
                
                api = messsage.get()

                tx = Text(frame,
                          width=73,
                          height=20,
                          bg='#478CCF',
                          fg='white',
                          font=('arial', 12, 'bold'),
                          selectbackground='#77E4C8',
                          insertbackground='red',
                          bd=5,
                          )
                tx.pack(padx=10, pady=10)

                bt = Button(frame,
                            text='تایید',
                            font=('arial', 12, 'bold'),
                            activebackground='#478CCF',
                            activeforeground='white',
                            fg='black',
                            bg='#77E4C8',
                            width=10,
                            command=gpt_submit)
                bt.pack(padx=10, pady=10)

            except Exception as e:
                messagebox.showerror('خطا', e)


        messsage = Entry(root,
                            width=18,
                            font=('arial', 18, 'bold'),
                            bg='#77E4C8')
        messsage.place(x=5, y=5)

        submit = Button(root,
                        text='تایید',
                        font=('arial', 10, 'bold'),
                        activebackground='#478CCF',
                        activeforeground='white',
                        fg='black',
                        bg='#77E4C8',
                        width=18,
                        command=publish_final)
        submit.place(x=40, y=60)

        root.mainloop()
 

    def command_note(self, frame):
        self.clear(frame)

    def command_voice(self, frame):
        def start_listen():
            pass

        self.clear(frame)

        frame.config(bg='black', fg='white')
        lb_voice = Label(frame,
                         text='voice assistant',
                         bg = 'black',
                         font=('arial', 18, 'bold'),
                         fg = 'white')
        lb_voice.place(x=270, y=10)

        lb_text = Label(frame,
                        text='',
                         bg='black',
                         font=('arial', 18, 'bold'),
                         fg='white')
        lb_text.place(x=270, y=200)

        bt_start = Button(frame,
                        text='start',
                        bg='darkgray',
                        activebackground='white',
                        activeforeground='black',
                        font=('arial', 14, 'bold'),
                        fg='white',
                        width=15,
                        command=start_listen)
        bt_start.place(x=470, y=400)
                         


    def command_myGit(self, frame):
        webbrowser.open('https://github.com/Saman148')

    def b_github(self):
        webbrowser.open('https://github.com/Saman148')


if __name__ == "__main__":
    obj = Fa('900x500',
             'DevHelper Farsi py',
             '#36C2CE',
             r'images-main\assistant-icon.ico',

             )
    obj.create_lables_buttons_frame()
    obj.mainloop()
