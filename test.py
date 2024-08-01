import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("RadioButton Toggle Example")
        self.geometry("300x200")
        
        # متغیر برای کنترل وضعیت RadioButton
        self.radio_var = tk.StringVar(value="off")  # مقدار پیش‌فرض "off"
        
        # ایجاد RadioButton
        self.radio = tk.Radiobutton(self, text="Option 1", variable=self.radio_var, value="on")
        self.radio.pack(pady=10)
        
        # دکمه برای خاموش و روشن کردن RadioButton
        self.toggle_button = tk.Button(self, text="Toggle RadioButton", command=self.toggle_radiobutton)
        self.toggle_button.pack(pady=10)
        
    def toggle_radiobutton(self):
        # بررسی وضعیت RadioButton و خاموش یا روشن کردن آن
        if self.radio['state'] == 'normal':
            self.radio.config(state='disabled')  # غیرفعال کردن RadioButton
            self.radio_var.set("off")  # تنظیم متغیر به "off"
        else:
            self.radio.config(state='normal')  # فعال کردن RadioButton
            self.radio_var.set("on")  # تنظیم متغیر به "on"

if __name__ == "__main__":
    app = App()
    app.mainloop()
