# interface.py

import tkinter as tk
from tkinter import messagebox, Toplevel, END, NORMAL, DISABLED
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import os
import shutil
import subprocess
import datetime
from openpyxl import Workbook, load_workbook
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import logging
import zipfile

# Configuration du logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Chemins des fichiers
path_parametre = "parametre/"
path_image = "images/"
path_cheval = "parametre/cheval.txt"
path_cheval_semaine = "parametre/cheval_semaine.txt"
path_Mercredi = "parametre/liste Mercredi.xlsx"
path_Samedi = "parametre/liste Samedi.xlsx"
path_semaine = "parametre/liste semaine.xlsx"
path_mail = "parametre/mail.txt"

# Classes et fonctions
class Cellule:
    def __init__(self):
        self.heure = ""
        self.cheval = ""
        self.eleve = ""
        self.ind_cheval = -1
        self.ind_eleve = -1

    def set_heure(self, heure):
        self.heure = heure

    def set_cheval(self, cheval, ind_cheval):
        self.cheval = cheval
        self.ind_cheval = ind_cheval

    def set_eleve(self, eleve, ind_eleve):
        self.eleve = eleve
        self.ind_eleve = ind_eleve

    def getCellule(self):
        return f"{self.heure} {self.cheval} {self.eleve}"

class Planning:
    def __init__(self):
        self.planning = []
        self.liste_eleve = {}
        self.liste_cheval = {}
        self.ancien_planning = []
        self.ancien_cheval = {}

    def set_planning(self, planning):
        self.planning = planning

    def set_liste_eleve(self, liste_eleve):
        self.liste_eleve = liste_eleve

    def set_cheval(self, liste_cheval):
        self.liste_cheval = liste_cheval

    def set_heure(self, heures):
        self.heures = heures

    def index_cheval(self, cheval):
        return self.liste_cheval[cheval]

    def ancient_cheval_de(self, eleve, heure):
        return self.ancien_cheval.get((eleve, heure), [])

# Fonctions
def get_personne():
    with open("parametre/user.txt", "r") as f:
        return f.read().strip()

def remplir_cheval(dict_cheval, jour):
    liste_cheval = []
    for cheval in dict_cheval[jour]:
        liste_cheval.append([dict_cheval[jour][cheval][0], cheval])
    return liste_cheval

def ecrire_fichier():
    # Logique d'écriture du fichier
    pass

def nouveau_fichier():
    # Logique de création d'un nouveau fichier
    pass

def recup_donne():
    # Logique de récupération des données
    pass

def sauvegarder_mail():
    # Logique de sauvegarde des adresses mail
    pass

def ouvrir_excel():
    # Logique d'ouverture du fichier Excel
    pass

def ecrire_mail():
    # Logique d'envoi du mail
    pass

def fusion():
    # Logique de fusion des plannings
    pass

def on_enter_pressed(event):
    # Logique de gestion des touches Entrée
    pass

def on_delete_pressed(event):
    # Logique de gestion des touches Suppr
    pass

def on_right_pressed(event):
    # Logique de gestion des touches Flèche Droite
    pass

def on_left_pressed(event):
    # Logique de gestion des touches Flèche Gauche
    pass

def on_crtls_pressed(event):
    # Logique de gestion des touches Ctrl+S
    pass

def rafraichir():
    # Logique de rafraîchissement du planning
    pass

def installer(window, user, version):
    # Logique d'installation
    pass

# Initialisation
cellule = Cellule()
planning = Planning()
jour = Jour()
dict_eleve, dict_cheval = lire_parametre()

version = 1.85
user = get_personne()
log_stats.set_user(user)
mail, moniteur = get_mail()

# Création de la fenêtre principale
window = tk.Tk()
window.title("Planning")
window.attributes("-fullscreen", True)
window.update()
wx = window.winfo_width()
wy = window.winfo_height()
proportion_x = wx / 1536
proportion_y = wy / 864

# Bind des événements
window.bind("<Return>", on_enter_pressed)
window.bind("<Right>", on_right_pressed)
window.bind("<Left>", on_left_pressed)
window.bind("<Control-s>", on_crtls_pressed)
window.bind("<Control-S>", on_crtls_pressed)
window.bind("<Delete>", on_delete_pressed)

# Configuration de l'interface
set_background(window, path_image + "image_fond.png")

# Widgets
# Ajouter ici les widgets principaux

# Menu
menubar = Menu(window)
sousmenu = Menu(menubar, tearoff=0)
sousmenu.add_command(label="parametre", command=mode_parametre)
sousmenu.add_command(label="principal", command=mode_default)
menubar.add_command(label="Nouveau", command=nouveau_fichier)
menubar.add_command(label="Jour", command=recup_donne)
menubar.add_cascade(label="Mode", menu=sousmenu)
menubar.add_command(label="Quitter!", command=window.quit)
window.config(menu=menubar)

# Lancement de la boucle principale
window.mainloop()