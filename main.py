# importations
import tkinter as tk
from tkinter import ttk, messagebox


def ajouter():
    pass


def main() -> None:
    window = tk.Tk()
    window.title('Csv helper')
    window.geometry('800x640')
    
    frame1 = tk.Frame(
        window,
    )
    
    # Frame1 widgets
    ajout_contact_label = tk.Label(
        frame1,
        text='Ajout d\'un contact',
    )
    nom_label = tk.Label(
        frame1,
        text='Nom',
    )
    nom_entry = tk.Entry(
        frame1,
    )
    mail_label = tk.Label(
        frame1,
        text='Mail',
    )
    mail_entry = tk.Entry(
        frame1,
    )
    tel_label = tk.Label(
        frame1,
        text='Tel',
    )
    tel_entry = tk.Entry(
        frame1,
    )
    ajouter_button = tk.Button(
        frame1,
        text='Ajouter',
        command=ajouter,
    )
    horizontal_line1 = ttk.Separator(
        frame1,
        orient='horizontal',
    )
    
    # Geometry manager for frame1 widgets
    ajout_contact_label.grid(
        row=1, 
        column=0,
    )
    nom_label.grid(
        row=0,
        column=1,
    )
    nom_entry.grid(
        row=1,
        column=1,
    )
    mail_label.grid(
        row=0,
        column=2,
    )
    mail_entry.grid(
        row=1,
        column=2,
    )
    tel_label.grid(
        row=0,
        column=3,
    )
    tel_entry.grid(
        row=1,
        column=3,
    )
    ajouter_button.grid(
        row=2,
        column=3,
    )
    horizontal_line1.grid(
        row=3,
        columnspan=4,
        sticky='ew',
    )
    
    frame1.pack()
    
    window.mainloop()


if __name__ == '__main__':
    main()