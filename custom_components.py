import tkinter as tk


class CustomMessageBox(tk.Toplevel):
    
    def __init__(self, master, title, message, theme, font):
        super().__init__(master)
        
        self.theme = theme
        self.title(title)
        self.geometry('400x100')
        self.config(bg=self.theme['bg'])
        
        self.label = tk.Label(
            self,
            text=message,
            bg=self.theme['bg'],
            fg=self.theme['fg'],
            font=font,
        )
        
        self.label.pack(pady=20, padx=20)
        
        self.ok_button = tk.Button(
            self,
            text='OK',
            bg=self.theme['btn_bg'],
            fg=self.theme['btn_fg'],
            font=font,
            command=self.destroy,
        )
        self.ok_button.pack(pady=10)