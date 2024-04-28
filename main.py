# importations
import tkinter as tk
from tkinter import ttk, messagebox
import csv
from constants import *


def is_valid(nom=None, mail=None, tel=None):
    valid = True
    if nom:
        valid = (
            nom.isalnum() and 
            len(nom) <= 30
        )
    if valid and mail:
        if '@' not in mail:
            return False
        mail = mail.split('@')
        nom_mail = mail[0]
        part2_mail = mail[1]
        valid = (
            nom_mail.isalnum() and 
            ' ' not in nom_mail and
            part2_mail == 'isi.utm.tn'
        )  
    if valid and tel:
        valid = (
            len(tel) == 6 and 
            tel.isdigit()
        )
    return valid


def exist(nom=None, mail=None, tel=None):
    with open('data.csv') as f:
        contacts_reader = csv.DictReader(f)
        
        for contact in contacts_reader:
            if (
                (nom and contact['nom'] == nom) or 
                (mail and contact['email'] == mail) or 
                (tel and contact['telephone'] == tel)
            ):
                print('data already exists')
                return True
    return False
    

def ajouter():
    # get the input values provided by the user
    nom = nom_entry.get()
    mail = mail_entry.get()
    tel = tel_entry.get()
    
    # check that all fields aren't empty
    if not nom or not mail or not tel:
        print('data should not be empty')
        return
    
    # check constraints
    if not is_valid(nom, mail, tel):
        print('data is invalid')
        return
    
    # check that they doesn't exist in data.csv
    if exist(nom, mail, tel):
        return

    
    # append data provided by the user to the data.csv file
    with open('data.csv', 'a') as f:
        contact_writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        
        contact_writer.writerow({'nom': nom, 'email':mail, 'telephone': tel})


def modifier():
    nom_contact_modifier = nom_contact_modifier_entry.get()
    nouveau_mail = nouveau_mail_entry.get()
    nouveau_nom = nouveau_nom_entry.get()
    
    found = False
    contacts = []
    
    with open('data.csv') as f:
        contacts = list(csv.DictReader(f, fieldnames=FIELDNAMES))
        
        for contact in contacts:
            if contact['nom'] == nom_contact_modifier:
                found = True
                
                if not nouveau_mail or not nouveau_nom or not is_valid(nouveau_nom, nouveau_mail):
                    print('Data is invalid')
                    return
                
                if exist(nouveau_nom, nouveau_mail):
                    return
                
                contact['nom'] = nouveau_nom
                contact['email'] = nouveau_mail
                break
        
    if not found:
        print('NON EXISTANT')
        return
        
    with open('data.csv', 'w', newline='') as f:
        contacts_writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        
        contacts_writer.writerows(contacts)
                

def supprimer():
    nom_contact_supprimer = nom_contact_supprimer_entry.get()
    
    if not nom_contact_supprimer:
        print('invalid data')
        return
    
    found = False
    contacts = []
    
    with open('data.csv') as f:
        contacts = list(csv.DictReader(f, fieldnames=FIELDNAMES))
        
        for contact in contacts:
            if contact['nom'] == nom_contact_supprimer:
                found = True

                contacts.remove(contact)
                
                break
    
    if not found:
        print('NON EXISTANT')
        return
    
    with open('data.csv', 'w', newline='') as f:
        contacts_writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        
        contacts_writer.writerows(contacts)


def afficher():
    nom_contact_afficher = nom_contact_afficher_entry.get()
    
    if not nom_contact_afficher:
        print('invalid data')
        return
    
    found = False
    
    with open('data.csv') as f:
        contacts = csv.DictReader(f, fieldnames=FIELDNAMES)
        
        for contact in contacts:
            if contact['nom'] == nom_contact_afficher:
                found = True
                
                affichage_textbox.config(state='normal')
                
                affichage_textbox.delete('1.0', 'end')
                affichage_textbox.insert('1.0', f'Nom : {contact["nom"]}    Mail: {contact["email"]}    Tel: {contact["telephone"]}')
                
                affichage_textbox.config(state='disabled')
                
                break
    
    if not found:
        print('NON EXISTANT')


def vider_annuaire():
    with open('data.csv', 'w') as f:
        pass


def reinitialiser_champs():
    nom_entry.delete(0, 'end')
    mail_entry.delete(0, 'end')
    tel_entry.delete(0, 'end')
    nom_contact_modifier_entry.delete(0, 'end')
    nouveau_mail_entry.delete(0, 'end')
    nouveau_nom_entry.delete(0, 'end')
    nom_contact_supprimer_entry.delete(0, 'end')
    nom_contact_afficher_entry.delete(0, 'end')
    
    affichage_textbox.config(state='normal')
    affichage_textbox.delete(1.0, 'end')
    affichage_textbox.config(state='disabled')


def afficher_tous():
    pass


def switch_theme(*args, **kwargs):
    pass


if __name__ == '__main__':
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
    affichage_textbox = tk.Text(
        frame4,
        height=10,
        width=75,
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
    affichage_textbox.grid(
        row=2,
        columnspan=4,
    )
    horizontal_line4.grid(
        row=3,
        columnspan=4,
        sticky='ew',
    )
    
    affichage_textbox.config(state='disabled')  # force the user to not type on the text widget
    
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
        text='Afficher tous les contacts',
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
    
    # Menubar section
    menu_bar = tk.Menu(
        window,
    )
    
    # File menu
    file_menu = tk.Menu(
        menu_bar,
        tearoff=0,
    )
    file_menu.add_command(
        label='Vider l\'annuaire',
        command=vider_annuaire,
    )
    file_menu.add_separator()
    file_menu.add_command(
        label='Quitter',
        command=exit,
    )
    
    # Action menu
    action_menu = tk.Menu(
        menu_bar,
        tearoff=0
    )
    action_menu.add_command(
        label='Afficher tous les contact',
        command=afficher_tous,
    )
    
    # Theme menu
    theme_menu = tk.Menu(
        menu_bar,
        tearoff=0,
    )
    theme_menu.add_command(
        label='Dark theme',
        command=lambda: switch_theme(theme='DARK'),
    )
    theme_menu.add_command(
        label='Light theme',
        command=lambda: switch_theme(theme='LIGHT'),
    )
    
    menu_bar.add_cascade(
        menu=file_menu,
        label='File',
    )
    menu_bar.add_cascade(
        menu=action_menu,
        label='Action',
    )
    menu_bar.add_cascade(
        menu=theme_menu,
        label='Theme',
    )
    
    window.config(
        menu=menu_bar,
    )
    
    window.mainloop()
    