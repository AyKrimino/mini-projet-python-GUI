# importations
import tkinter as tk
from tkinter import ttk, messagebox


def ajouter():
    pass


def modifier():
    pass


def main() -> None:
    window = tk.Tk()
    window.title('Csv helper')
    window.geometry('800x640')
    
    # Frame1 section
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
    
    # Frame2 section
    frame2 = tk.Frame(
        window,
    )
    
    # Frame2 widgets
    modifier_label = tk.Label(
        frame2,
        text='Modifier',
    )
    nom_contact_modifer_label = tk.Label(
        frame2,
        text='Nom du contact à modifier',
    )
    nom_contact_modifier_entry = tk.Entry(
        frame2,
    )
    nouveau_mail_label = tk.Label(
        frame2,
        text='Nouveau mail',
    )
    nouveau_mail_entry = tk.Entry(
        frame2,
    )
    nouveau_nom_label = tk.Label(
        frame2,
        text='Nouveau nom',
    )
    nouveau_nom_entry = tk.Entry(
        frame2,
    )
    modifier_button = tk.Button(
        frame2,
        text='Modifier',
        command=modifier,
    )
    horizontal_line2 = ttk.Separator(
        frame2,
        orient='horizontal',
    )
    
    # Geometry managers for frame2 widgets
    modifier_label.grid(
        row=1,
        column=0,
    )
    nom_contact_modifer_label.grid(
        row=0,
        column=1,
    )
    nom_contact_modifier_entry.grid(
        row=1,
        column=1,
    )
    nouveau_mail_label.grid(
        row=2,
        column=1,
    )
    nouveau_mail_entry.grid(
        row=2,
        column=2,
    )
    nouveau_nom_label.grid(
        row=3,
        column=1,
    )
    nouveau_nom_entry.grid(
        row=3,
        column=2,
    )
    modifier_button.grid(
        row=2,
        column=3,
    )
    horizontal_line2.grid(
        row=4,
        columnspan=4,
        sticky='ew',
    )
    
    frame2.pack()
    
    window.mainloop()


if __name__ == '__main__':
    main()