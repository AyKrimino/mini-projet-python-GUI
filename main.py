# importations
import tkinter as tk
from tkinter import ttk, messagebox


def ajouter():
    pass


def modifier():
    pass


def supprimer():
    pass


def afficher():
    pass


def vider_annuaire():
    pass


def reinitialiser_champs():
    pass


def afficher_tous():
    pass


def switch_theme():
    pass


def main() -> None:
    window = tk.Tk()
    window.title('Csv helper')
    window.geometry('800x640')
    
    is_dark_mode = False
    
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
    
    # Frame3 section
    frame3 = tk.Frame(
        window,
    )
    
    # Frame3 widgets
    supprimer_label = tk.Label(
        frame3,
        text='Supprimer',
    )
    nom_contact_supprimer_label = tk.Label(
        frame3,
        text='Nom du contact à supprimer',
    )
    nom_contact_supprimer_entry = tk.Entry(
        frame3,
    )
    supprimer_button = tk.Button(
        frame3,
        text='Supprimer',
        command=supprimer,
    )
    horizontal_line3 = ttk.Separator(
        frame3,
        orient='horizontal',
    )
    
    # Geometry managers for Frame3
    supprimer_label.grid(
        row=1,
        column=0,
    )
    nom_contact_supprimer_label.grid(
        row=0,
        column=1,
    )
    nom_contact_supprimer_entry.grid(
        row=1,
        column=1,
    )
    supprimer_button.grid(
        row=1,
        column=3,
    )
    horizontal_line3.grid(
        row=2,
        columnspan=4,
        sticky='ew',
    )
    
    frame3.pack()
    
    # Frame4 section
    frame4 = tk.Frame(
        window,
    )
    
    # Frame4 widgets
    afficher_label = tk.Label(
        frame4,
        text='Afficher',
    )
    nom_contact_afficher_label = tk.Label(
        frame4,
        text='Nom du contact à afficher',
    )
    nom_contact_afficher_entry = tk.Entry(
        frame4,
    )
    afficher_button = tk.Button(
        frame4,
        text='Afficher',
        command=afficher,
    )
    affichage_listvar = tk.StringVar(value=[])
    affichage_listbox = tk.Listbox(
        frame4,
        listvariable=affichage_listvar,
        height=10,
        width=75,
        selectmode='extended',
    )
    horizontal_line4 = ttk.Separator(
        frame4,
        orient='horizontal',
    )
    
    # Geometry managers for Frame4
    afficher_label.grid(
        row=1,
        column=0,
    )
    nom_contact_afficher_label.grid(
        row=0,
        column=1,
    )
    nom_contact_afficher_entry.grid(
        row=1,
        column=1,
    )
    afficher_button.grid(
        row=1,
        column=2,
    )
    affichage_listbox.grid(
        row=2,
        columnspan=4,
    )
    horizontal_line4.grid(
        row=3,
        columnspan=4,
        sticky='ew',
    )
    
    frame4.pack()
    
    # Frame5 section
    frame5 = tk.Frame(
        window,
    )
    
    # Frame5 widgets
    vider_annuaire_button = tk.Button(
        frame5,
        text='Vider l\'annuaire',
        command=vider_annuaire,
    )
    reinitialiser_champs_button = tk.Button(
        frame5,
        text='Réinitialiser les champs',
        command=reinitialiser_champs,
    )
    afficher_tous_button = tk.Button(
        frame5,
        text='Afficher tous',
        command=afficher_tous,
    )
    switch_theme_button = tk.Button(
        frame5,
        text='Light mode' if is_dark_mode else 'Dark mode',
        command=switch_theme,
    )
    quitter_button = tk.Button(
        frame5,
        text='Quitter',
        command=exit,
    )
    
    # Geometry managers for Frame5
    vider_annuaire_button.grid(
        row=0,
        column=0,
    )
    reinitialiser_champs_button.grid(
        row=0,
        column=1,
    )
    afficher_tous_button.grid(
        row=0,
        column=2,
    )
    switch_theme_button.grid(
        row=0,
        column=3,
    )
    quitter_button.grid(
        row=0,
        column=4,
    )
    
    frame5.pack()
    
    window.mainloop()


if __name__ == '__main__':
    main()