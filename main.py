# importations
import tkinter as tk
from tkinter import ttk
import csv

from constants import *
from custom_components import CustomMessageBox as ShowMessage


def is_valid(nom=None, mail=None, tel=None):
    '''
    Determines the validity of input data for a person's name, email, and telephone number.

    Args:
        nom (str, optional): The person's name. Defaults to None.
        mail (str, optional): The person's email address. Defaults to None.
        tel (str, optional): The person's telephone number. Defaults to None.

    Returns:
        bool: True if all input data is valid, False otherwise.

    The function checks the validity of input data for a person's name, email, and telephone number
    based on certain criteria:
    - For the name (nom): It must consist of alphanumeric characters and be no longer than 30 characters.
    - For the email (mail): It must contain an '@' symbol and must be in the format 'username@domain' where
      the domain is 'isi.utm.tn'. The username part must consist of alphanumeric characters only, no spaces.
    - For the telephone number (tel): It must be exactly 6 digits and consist only of numeric characters.

    If any of the input data fails to meet its respective criteria, the function returns False indicating
    invalid input. If all input data passes the validation, the function returns True.
    '''
    valid = True
    if nom:
        valid = (
            nom.isalnum() and 
            len(nom) <= 30
        )
    if valid and mail:
        if '@' not in mail:
            return False
        '''
        test@isi.utm.tn
        ['test', 'isi.utm.tn']
        '''
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
    """
    Checks if a given contact exists in the 'data.csv' file and determines if the file is empty.

    Args:
        nom (str, optional): The name of the contact. Defaults to None.
        mail (str, optional): The email of the contact. Defaults to None.
        tel (str, optional): The telephone number of the contact. Defaults to None.

    Returns:
        tuple: A tuple containing two values:
            - bool: True if the contact exists in the file, False otherwise.
            - str: Indicates if the 'data.csv' file is empty or not. Possible values are 'yes' or 'no'.

    This function reads the 'data.csv' file and checks if a contact with the provided name, email, or telephone
    number already exists in the file. If any of these values are provided (not None), it searches for an exact match
    in the respective columns of the CSV file. If a match is found, the function returns a tuple with the first value
    being True to indicate that the contact exists, along with the status of the file ('no' indicating it's not empty).

    If no match is found or if the file is empty, the function returns a tuple with the first value as False,
    indicating that the contact does not exist, along with the status of the file ('yes' indicating it's empty).

    Note: The CSV file must have column headers corresponding to 'nom', 'email', and 'telephone' for this function
    to work properly.
    """
    file_is_empty = 'yes'
    
    with open('data.csv') as f:
        contacts_reader = csv.DictReader(f, fieldnames=FIELDNAMES)
        
        for contact in contacts_reader:
            file_is_empty = 'no'
            if (
                (nom and contact['nom'] == nom) or 
                (mail and contact['email'] == mail) or 
                (tel and contact['telephone'] == tel)
            ):
                return True, file_is_empty
    return False, file_is_empty
    

def ajouter():
    # get the input values provided by the user
    nom = nom_entry.get()
    mail = mail_entry.get()
    tel = tel_entry.get()
    
    # check that all fields aren't empty
    if not nom or not mail or not tel:
        ShowMessage(
            window, 
            'Donées invalides', 
            'Ces champs doivent être non vide!', 
            DARK_MODE if is_dark_mode else LIGHT_MODE,
            FONT,
        )
        return
    
    # check constraints
    if not is_valid(nom, mail, tel):
        ShowMessage(
            window, 
            'Donées invalides', 
            'Les contraintes de données ne sont pas respectées!', 
            DARK_MODE if is_dark_mode else LIGHT_MODE,
            FONT,
        )
        return
    
    # check that they doesn't exist in data.csv
    data_exist, file_is_empty = exist(nom, mail, tel)
    if data_exist:
        ShowMessage(
            window, 
            'Donées existante', 
            'Données déja existe dans la base de données!', 
            DARK_MODE if is_dark_mode else LIGHT_MODE,
            FONT,
        )
        return

    # append data provided by the user to the data.csv file
    with open('data.csv', 'a', newline='') as f:
        contact_writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        
        if file_is_empty == 'yes':
            contact_writer.writeheader()
        
        contact_writer.writerow({'nom': nom, 'email':mail, 'telephone': tel})
        
    ShowMessage(
        window,
        'Succés',
        'donnée ajoutée avec succés!',
        DARK_MODE if is_dark_mode else LIGHT_MODE,
        FONT,
    )


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
                    ShowMessage(
                        window, 
                        'Donées invalides', 
                        'Ces champs ne doivent pas être vide!', 
                        DARK_MODE if is_dark_mode else LIGHT_MODE,
                        FONT,
                    )
                    return
                
                existe = exist(nouveau_nom, nouveau_mail)[0]
                
                if existe:
                    ShowMessage(
                        window, 
                        'Donées existante', 
                        'Données déja existe dans la base de données!', 
                        DARK_MODE if is_dark_mode else LIGHT_MODE,
                        FONT,
                    )
                    return
                
                contact['nom'] = nouveau_nom
                contact['email'] = nouveau_mail
                break
        
    if not found:
        ShowMessage(
            window, 
            'Donée non existante', 
            'ce nom n\'existe pas dans la base de données!', 
            DARK_MODE if is_dark_mode else LIGHT_MODE,
            FONT,
        )
        return
        
    with open('data.csv', 'w', newline='') as f:
        contacts_writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        
        contacts_writer.writerows(contacts)
        
    ShowMessage(
        window,
        'Succés',
        'donnée modifiée avec succés!',
        DARK_MODE if is_dark_mode else LIGHT_MODE,
        FONT,
    )
                

def supprimer():
    nom_contact_supprimer = nom_contact_supprimer_entry.get()
    
    if not nom_contact_supprimer:
        ShowMessage(
                    window, 
                    'Donées invalides', 
                    'Ce champ doit être non vide!', 
                    DARK_MODE if is_dark_mode else LIGHT_MODE,
                    FONT,
                    )
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
        ShowMessage(
            window, 
            'Donée non existante', 
            'ce nom n\'existe pas dans la base de données!', 
            DARK_MODE if is_dark_mode else LIGHT_MODE,
            FONT,
        )
        return
    
    with open('data.csv', 'w', newline='') as f:
        contacts_writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        
        contacts_writer.writerows(contacts)
    
    ShowMessage(
        window,
        'Donnée supprimée',
        'Données supprimée avec succés!',
        DARK_MODE if is_dark_mode else LIGHT_MODE,
        FONT,
    )


def afficher():
    nom_contact_afficher = nom_contact_afficher_entry.get()
    
    if not nom_contact_afficher:
        ShowMessage(
            window, 
            'Donée invalide', 
            'Ce champ doit être non vide!', 
            DARK_MODE if is_dark_mode else LIGHT_MODE,
            FONT,
        )
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
        ShowMessage(
            window, 
            'Donée non existante', 
            'Données n\'existe pas dans la base de données!', 
            DARK_MODE if is_dark_mode else LIGHT_MODE,
            FONT,
        )


def vider_annuaire():
    with open('data.csv', 'w') as f:
        ShowMessage(
            window,
            'Données supprimées',
            'Tous les données sont supprimées',
            DARK_MODE if is_dark_mode else LIGHT_MODE,
            FONT,
        )


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
    affichage_textbox.config(state='normal')
    affichage_textbox.delete(1.0, 'end')

    with open('data.csv') as f:
        contacts_reader = csv.DictReader(f, fieldnames=FIELDNAMES)
        
        contacts_reader.__next__()
        
        for idx, contact in enumerate(contacts_reader):

            affichage_textbox.insert(f'{idx + 1}.0', f'Nom : {contact["nom"]}    Mail: {contact["email"]}    Tel: {contact["telephone"]}\n')
            
    affichage_textbox.config(state='disabled')


def switch_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    
    theme = LIGHT_MODE
    if is_dark_mode:
        switch_theme_button.config(text='Toggle light mode')
        theme = DARK_MODE
        
    window.config(bg=theme['bg'])
    
    for widget1 in window.winfo_children():
        widget1.config(bg=theme['bg'])
        for widget2 in widget1.winfo_children():
            widget_type = widget2.winfo_class()
            
            if widget_type == 'Label':
                widget2.config(bg=theme['bg'], fg=theme['fg'])
            elif widget_type == 'Entry' or widget_type == 'Text':
                widget2.config(bg=theme['entry_bg'], fg=theme['entry_fg'], insertbackground=theme['fg'])
            elif widget_type == 'Button':
                widget2.config(bg=theme['btn_bg'], fg=theme['btn_fg'])
            elif widget_type == 'Menu':
                widget2.config(bg=theme['bg'], fg=theme['fg'])


# Global variables
is_dark_mode = False


if __name__ == '__main__':
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
        font=FONT,
    )
    nom_label = tk.Label(
        frame1,
        text='Nom',
        font=FONT,
    )
    nom_entry = tk.Entry(
        frame1,
        font=FONT,
    )
    mail_label = tk.Label(
        frame1,
        text='Mail',
        font=FONT,
    )
    mail_entry = tk.Entry(
        frame1,
        font=FONT,
    )
    tel_label = tk.Label(
        frame1,
        text='Tel',
        font=FONT,
    )
    tel_entry = tk.Entry(
        frame1,
        font=FONT,
    )
    ajouter_button = tk.Button(
        frame1,
        text='Ajouter',
        command=ajouter,
        font=FONT,
    )
    horizontal_line1 = ttk.Separator(
        frame1,
        orient='horizontal',
    )
    
    # Geometry manager for frame1 widgets
    ajout_contact_label.grid(
        padx=10,
        pady=5,
        sticky='new',
        row=1, 
        column=0,
    )
    nom_label.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=0,
        column=1,
    )
    nom_entry.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=1,
        column=1,
    )
    mail_label.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=0,
        column=2,
    )
    mail_entry.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=1,
        column=2,
    )
    tel_label.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=0,
        column=3,
    )
    tel_entry.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=1,
        column=3,
    )
    ajouter_button.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=2,
        column=3,
    )
    horizontal_line1.grid(
        padx=10,
        pady=5,
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
        font=FONT,
    )
    nom_contact_modifer_label = tk.Label(
        frame2,
        text='Nom du contact à modifier',
        font=FONT,
    )
    nom_contact_modifier_entry = tk.Entry(
        frame2,
        font=FONT,
    )
    nouveau_mail_label = tk.Label(
        frame2,
        text='Nouveau mail',
        font=FONT,
    )
    nouveau_mail_entry = tk.Entry(
        frame2,
        font=FONT,
    )
    nouveau_nom_label = tk.Label(
        frame2,
        text='Nouveau nom',
        font=FONT,
    )
    nouveau_nom_entry = tk.Entry(
        frame2,
        font=FONT,
    )
    modifier_button = tk.Button(
        frame2,
        text='Modifier',
        command=modifier,
        font=FONT,
    )
    horizontal_line2 = ttk.Separator(
        frame2,
        orient='horizontal',
    )
    
    # Geometry managers for frame2 widgets
    modifier_label.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=1,
        column=0,
    )
    nom_contact_modifer_label.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=0,
        column=1,
    )
    nom_contact_modifier_entry.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=1,
        column=1,
    )
    nouveau_mail_label.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=2,
        column=1,
    )
    nouveau_mail_entry.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=2,
        column=2,
    )
    nouveau_nom_label.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=3,
        column=1,
    )
    nouveau_nom_entry.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=3,
        column=2,
    )
    modifier_button.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=2,
        column=3,
    )
    horizontal_line2.grid(
        padx=10,
        pady=5,
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
        font=FONT,
    )
    nom_contact_supprimer_label = tk.Label(
        frame3,
        text='Nom du contact à supprimer',
        font=FONT,
    )
    nom_contact_supprimer_entry = tk.Entry(
        frame3,
        font=FONT,
    )
    supprimer_button = tk.Button(
        frame3,
        text='Supprimer',
        command=supprimer,
        font=FONT,
    )
    horizontal_line3 = ttk.Separator(
        frame3,
        orient='horizontal',
    )
    
    # Geometry managers for Frame3
    supprimer_label.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=1,
        column=0,
    )
    nom_contact_supprimer_label.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=0,
        column=1,
    )
    nom_contact_supprimer_entry.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=1,
        column=1,
    )
    supprimer_button.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=1,
        column=3,
    )
    horizontal_line3.grid(
        padx=10,
        pady=5,
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
        font=FONT,
    )
    nom_contact_afficher_label = tk.Label(
        frame4,
        text='Nom du contact à afficher',
        font=FONT,
    )
    nom_contact_afficher_entry = tk.Entry(
        frame4,
        font=FONT,
    )
    afficher_button = tk.Button(
        frame4,
        text='Afficher',
        command=afficher,
        font=FONT,
    )
    affichage_textbox = tk.Text(
        frame4,
        height=10,
        width=75,
        font=FONT,
    )
    horizontal_line4 = ttk.Separator(
        frame4,
        orient='horizontal',
    )
    
    # Geometry managers for Frame4
    afficher_label.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=1,
        column=0,
    )
    nom_contact_afficher_label.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=0,
        column=1,
    )
    nom_contact_afficher_entry.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=1,
        column=1,
    )
    afficher_button.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=1,
        column=2,
    )
    affichage_textbox.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=2,
        columnspan=4,
    )
    horizontal_line4.grid(
        padx=10,
        pady=5,
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
        font=FONT,
    )
    reinitialiser_champs_button = tk.Button(
        frame5,
        text='Réinitialiser les champs',
        command=reinitialiser_champs,
        font=FONT,
    )
    afficher_tous_button = tk.Button(
        frame5,
        text='Afficher tous les contacts',
        command=afficher_tous,
        font=FONT,
    )
    switch_theme_button = tk.Button(
        frame5,
        text='Toggle dark mode',
        command=switch_theme,
        font=FONT,
    )
    quitter_button = tk.Button(
        frame5,
        text='Quitter',
        command=exit,
        font=FONT,
    )
    
    # Geometry managers for Frame5
    vider_annuaire_button.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=0,
        column=0,
    )
    reinitialiser_champs_button.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=0,
        column=1,
    )
    afficher_tous_button.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=0,
        column=2,
    )
    switch_theme_button.grid(
        padx=10,
        pady=5,
        sticky='news',
        row=0,
        column=3,
    )
    quitter_button.grid(
        padx=10,
        pady=5,
        sticky='news',
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
        label='Switch theme',
        command=switch_theme,
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
    