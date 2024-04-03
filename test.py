# # # import tkinter as tk


# # # def toggle_widgets():
# # #     global show_widgets

# # #     if show_widgets:
# # #         # Supprimer les widgets existants
# # #         for widget in widgets_to_show:
# # #             widget.pack_forget()
# # #         show_widgets = False
# # #     else:
# # #         # Afficher à nouveau les widgets
# # #         for widget in widgets_to_show:
# # #             widget.pack()
# # #         show_widgets = True


# # # app = tk.Tk()
# # # app.title("Exemple de gestion de widgets avec Tkinter")

# # # # Liste des widgets que vous souhaitez ajouter/supprimer
# # # widgets_to_show = []
# # # show_widgets = False

# # # # Créez des widgets que vous souhaitez afficher ou masquer
# # # label = tk.Label(app, text="Ceci est un label")
# # # entry = tk.Entry(app)
# # # button = tk.Button(app, text="Ceci est un bouton")
# # # widgets_to_show.extend([label, entry, button])

# # # # Afficher les widgets initiaux
# # # for widget in widgets_to_show:
# # #     widget.pack()

# # # # Créer un bouton "Paramètres" pour ajouter/supprimer des widgets
# # # param_button = tk.Button(app, text="Paramètres", command=toggle_widgets)
# # # param_button.pack()

# # # app.mainloop()


# # # from docx import Document
# # # from docx.shared import Pt
# # # from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
# # # from docx.shared import Inches
# # # from docx.shared import Pt
# # # from docx.enum.section import WD_ORIENT

# # # # Créer un nouveau document Word
# # # doc = Document()

# # # # Définir le document en mode paysage
# # # section = doc.sections[0]
# # # new_width, new_height = section.page_height, section.page_width
# # # section.orientation = WD_ORIENT.LANDSCAPE
# # # section.page_width = new_width
# # # section.page_height = new_height

# # # # Ajouter un tableau avec 3 lignes et 3 colonnes
# # # rows = 3
# # # cols = 3
# # # table = doc.add_table(rows=rows, cols=cols)
# # # table.style = "Dark List"


# # # # Définir les bordures des cellules comme transparentes
# # # for row in table.rows:
# # #     for cell in row.cells:
# # #         cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
# # #         # cell.text_frame.paragraphs[0].runs[0].font.size = Pt(
# # #         #     10)  # Taille du texte dans la cellule
# # #         # Police du texte dans la cellule
# # #         # cell.text_frame.paragraphs[0].runs[0].font.name = 'Arial'
# # #         # cell.text_frame.paragraphs[0].runs[0].font.color.rgb = (
# # #         #     0, 0, 0)  # Couleur du texte dans la cellule
# # #         for paragraph in cell.paragraphs:
# # #             for run in paragraph.runs:
# # #                 for border in run._element.xpath('.//w:borders'):
# # #                     border.attrib.clear()


# # # # Sauvegarder le document Word
# # # doc.save('tableau_word_paysage.docx')


# # # Import docx NOT python-docx
# # from docx import Document
# # import docx
# # from docx.enum.section import WD_ORIENT
# # # Create an instance of a word document
# # # doc = docx.Document("gfg.docx")
# # doc = docx.Document()


# # section = doc.sections[-1]
# # new_width, new_height = section.page_height, section.page_width
# # section.orientation = WD_ORIENT.LANDSCAPE
# # section.page_width = new_width
# # section.page_height = new_height
# # # Add a Title to the document
# # # doc.add_heading('GeeksForGeeks', 0)

# # # Table data in a form of list
# # date = "01-11-2023"
# # jour = date[0:2]
# # mois = date[3:5]
# # anne = date[6:10]

# # nombre_jours_par_mois = {
# #     1: 31,   # Janvier
# #     2: 28,   # Février (29 en année bissextile)
# #     3: 31,   # Mars
# #     4: 30,   # Avril
# #     5: 31,   # Mai
# #     6: 30,   # Juin
# #     7: 31,   # Juillet
# #     8: 31,   # Août
# #     9: 30,   # Septembre
# #     10: 31,  # Octobre
# #     11: 30,  # Novembre
# #     12: 31   # Décembre
# # }


# # # Creating a table object


# # colonne = 1

# # if int(jour) < 7:
# #     journee = int(jour)
# #     while journee <= nombre_jours_par_mois[int(mois)]:
# #         journee += 7
# #         colonne += 1

# # table = doc.add_table(rows=1, cols=colonne)
# # row = table.rows[0].cells


# # row = table.add_row().cells


# # if int(jour) < 7:
# #     journee = int(jour)
# #     while journee <= nombre_jours_par_mois[int(mois)]:
# #         journee += 7


# # table.style = 'Table Grid'
# # doc.save('gfg.docx')

# # # # Adding heading in the 1st row of the table
# # # row = table.column[0].cells
# # # row[0].text = 'jour/heure'
# # # row[1].text = 'date1'
# # # row[2].text = 'date2'
# # # row[3].text = 'date3'
# # # row[4].text = 'date4'

# # # # Adding data from the list to the table
# # # for id, name in data:

# # #     # Adding a row and then adding data in it.
# # #     row = table.add_row().cells
# # #     # Converting id to string as table can only take string input
# # #     row[0].text = str(id)
# # #     row[1].text = name

# # # row = table.add_row().cells
# # # row[0].text = 'jour/heure'
# # # row[1].text = 'date1'
# # # row[2].text = 'date2'
# # # row[3].text = 'date3'
# # # row[4].text = 'date4'
# # # row = table.add_row().cells
# # # row[0].text = '\r\r'
# # # row[1].text = 'date1'
# # # row[2].text = 'date2'
# # # row[3].text = 'date3'
# # # row[4].text = 'date4'
# # # # Now save the document to a location
# # # doc.save('gfg.docx')


# # # # document = Document()

# # # # section = document.sections[-1]

# # # # new_width, new_height = section.page_height, section.page_width
# # # # section.orientation = WD_ORIENT.LANDSCAPE
# # # # section.page_width = new_width
# # # # section.page_height = new_height


# # # # document.add_heading('text')
# # # # document.save('demo.docx')


# # # from openpyxl import load_workbook
# # # import datetime
# # # import locale
# # # import os
# # # import time

# # # fichier = "quittance chaumes\\"

# # # locale.setlocale(locale.LC_ALL, 'fr_FR')

# # # workbook = load_workbook("modele.xlsx")
# # # sheet = workbook.active

# # # lieu = "Capens, le "
# # # quittance = "QUITTANCE N° Q "


# # # mois = datetime.datetime.today().strftime('%m')

# # # sheet["G10"] = lieu + datetime.datetime.today().strftime('%d/%m/%Y')
# # # sheet["B14"] = quittance + datetime.datetime.today().strftime('%d %m %Y')
# # # sheet["D25"] = datetime.datetime.today().strftime('%B %Y')
# # # sheet["G36"] = datetime.datetime.today().strftime('%m-%Y')

# # # if mois == "06" or mois == "01":
# # #     rep = input("voulez-vous changé les charges ? (o/n) :")
# # #     if rep.lower == "o":
# # #         charge = input(
# # #             "quelle montant HT en € voulez vous pour les charges ? :")
# # #         sheet["D28"] = float(charge)
# # #         workbook.save("modele.xlsx")
# # #         workbook = load_workbook("modele.xlsx")
# # #     rep = input("voulez-vous changé la regul charges n-1 ? (o/n) :")
# # #     if rep.lower == "o":
# # #         charge = input(
# # #             "quelle montant HT en € voulez vous pour la regul charges n-1 ? :")
# # #         sheet["D29"] = float(charge)
# # # else:
# # #     sheet["D29"] = None

# # # if mois == "11":
# # #     rep = input("voulez-vous changé le loyer ? (o/n) :")
# # #     print(rep)
# # #     print(rep.lower() == "o")
# # #     if rep.lower() == "o":
# # #         loyer = input("quelle montant HT en € voulez vous mettre ? :")
# # #         sheet["D27"] = float(loyer)
# # #         workbook.save("modele.xlsx")

# # #         workbook = load_workbook("modele.xlsx")

# # # chemin_fichier_excel = fichier+datetime.datetime.today().strftime('%m %Y')+".xlsx"


# # # workbook.save(chemin_fichier_excel)

# # # os.system(f'start excel "{chemin_fichier_excel}"')


# from datetime import datetime, timedelta

# # Fonction pour trouver la prochaine occurrence du jour de la semaine spécifié


# def prochain_jour(semaine, jour_actuel):
#     jours_de_la_semaine = ["lundi", "mardi", "mercredi",
#                            "jeudi", "vendredi", "samedi", "dimanche"]
#     jour_cible = jours_de_la_semaine.index(semaine)

#     jours_jusquau_prochain = (jour_cible - jour_actuel.weekday() + 7) % 7
#     if jours_jusquau_prochain == 0:
#         jours_jusquau_prochain = 7

#     return jour_actuel + timedelta(days=jours_jusquau_prochain)


# # Obtenir la date actuelle
# date_actuelle = datetime.now()

# # Vérifier si aujourd'hui est déjà un mercredi
# if date_actuelle.weekday() == 2:  # Le code de semaine pour mercredi est 2 (0 pour lundi, 1 pour mardi, etc.)
#     prochains_mercredis = [date_actuelle]
#     prochain_mercredi = date_actuelle
# else:
#     # Trouver le prochain mercredi
#     prochain_mercredi = prochain_jour("mercredi", date_actuelle)

#     # Ajouter les trois prochains mercredis au tableau
#     prochains_mercredis = [prochain_mercredi]
# for _ in range(2):
#     prochain_mercredi = prochain_jour("mercredi", prochain_mercredi)
#     prochains_mercredis.append(prochain_mercredi)


# if date_actuelle.weekday() == 5:  # Le code de semaine pour mercredi est 2 (0 pour lundi, 1 pour mardi, etc.)
#     prochains_samedis = [date_actuelle]
#     prochain_samedi = date_actuelle
# else:
#     # Trouver le prochain mercredi
#     prochain_samedi = prochain_jour("samedi", date_actuelle)

#     # Ajouter les trois prochains mercredis au tableau
#     prochains_samedis = [prochain_samedi]
# for _ in range(2):
#     prochain_samedi = prochain_jour("samedi", prochain_samedi)
#     prochains_samedis.append(prochain_samedi)

# print("Dates des trois prochains mercredis:")
# for mercredi in prochains_samedis:
#     print(mercredi.strftime("%Y-%m-%d"))


# import tkinter as tk

# from tkinter import ttk
# import tkinter as tk
# from PIL import Image, ImageTk
# fenetre = tk.Tk()
# fenetre.title("Planning")  # Titre de la fenêtre
# fenetre.attributes('-fullscreen', True)  # Affichage en mode plein écran
# fenetre.bind('<Escape>', lambda e: fenetre.destroy())
# image = tk.PhotoImage(
#     file="1342060.png")  # Ton image

# # Le canvas, il faut régler sa taille pour qu'il occupe toute la fenêtre
# canvas = tk.Canvas(fenetre, width=fenetre.winfo_screenwidth(),
#                    height=fenetre.winfo_screenheight())
# # On ajoute l'image dans le canvas
# canvas.create_image(0, 0, image=image)

# # On ajoute le texte
# canvas.create_text(120, 50, text="Le texte que je veux afficher",
#                    fill="black", font=("Helvetica", 24))

# # Configurer le pack pour remplir et étendre le canvas
# canvas.pack(fill=tk.BOTH, expand=True)

# fenetre.mainloop()


# def create_button_styles(root):
#     # Style 1: Bouton par défaut
#     default_button = tk.Button(root, text="Default Button")

#     # Style 2: Bouton avec couleur de fond personnalisée
#     colored_button = tk.Button(root, text="Colored Button", bg="lightblue")

#     # Style 3: Bouton avec relief en relief
#     raised_button = tk.Button(root, text="Raised Button", relief=tk.RAISED)

#     # Style 4: Bouton avec relief en creux
#     sunken_button = tk.Button(root, text="Sunken Button", relief=tk.SUNKEN)

#     # Style 5: Bouton avec bordure en ridge
#     ridge_button = tk.Button(root, text="Ridge Button", relief=tk.RIDGE)

#     # Style 6: Bouton avec bordure en solid
#     solid_button = tk.Button(root, text="Solid Button", relief=tk.SOLID)

#     # Style 7: Bouton avec bordure en groove
#     groove_button = tk.Button(root, text="Groove Button", relief=tk.GROOVE)

#     # Style 8: Bouton avec bordure en flat
#     flat_button = tk.Button(root, text="Flat Button", relief=tk.FLAT)

#     # Style 9: Bouton avec texte gras
#     bold_button = tk.Button(root, text="Bold Button",
#                             font=("Helvetica", 12, "bold"))

#     # Style 10: Bouton avec police de caractères personnalisée
#     custom_font_button = tk.Button(
#         root, text="Custom Font Button", font=("Courier", 10))

#     # Style 11: Bouton avec relief plat et couleur de fond personnalisée
#     custom_style_button = tk.Button(
#         root, text="Custom Style Button", relief=tk.FLAT, bg="orange")

#     # Utilisation de ttk (themed Tkinter) pour des styles plus avancés
#     # Style 12: Bouton avec style "TButton"
#     themed_button = ttk.Button(root, text="Themed Button", style="TButton")

#     # Style 13: Bouton avec style "Toolbutton"
#     tool_button = ttk.Button(root, text="Tool Button", style="Toolbutton")

#     # Style 14: Bouton avec style "Outline.TButton"
#     outline_button = ttk.Button(
#         root, text="Outline Button", style="Outline.TButton")

#     # Pack les boutons dans la fenêtre
#     default_button.pack(pady=5)
#     colored_button.pack(pady=5)
#     raised_button.pack(pady=5)
#     sunken_button.pack(pady=5)
#     ridge_button.pack(pady=5)
#     solid_button.pack(pady=5)
#     groove_button.pack(pady=5)
#     flat_button.pack(pady=5)
#     bold_button.pack(pady=5)
#     custom_font_button.pack(pady=5)
#     custom_style_button.pack(pady=5)
#     themed_button.pack(pady=5)
#     tool_button.pack(pady=5)
#     outline_button.pack(pady=5)

#     root.mainloop()


# # Créer la fenêtre principale
# root = tk.Tk()
# root.title("Styles de Boutons")

# # Appeler la fonction pour créer les boutons avec différents styles
# create_button_styles(root)


# def create_button_styles(root):
#     # Créer un canevas pour l'arrière-plan
#     canvas = tk.Canvas(root, width=400, height=300, bg="lightgray")
#     canvas.pack(expand=True, fill="both")

#     # Style 1: Bouton par défaut
#     default_button = tk.Button(canvas, text="Default Button")

#     # Style 2: Bouton avec couleur de fond personnalisée
#     colored_button = tk.Button(canvas, text="Colored Button", bg="lightblue")

#     # ... (Ajoutez les autres boutons comme précédemment)

#     # Utilisation de ttk (themed Tkinter) pour des styles plus avancés
#     # Style 12: Bouton avec style "TButton"
#     themed_button = ttk.Button(canvas, text="Themed Button", style="TButton")

#     # ... (Ajoutez les autres boutons ttk comme précédemment)

#     # Pack les boutons dans le canevas
#     default_button.pack(pady=5)
#     colored_button.pack(pady=5)
#     # ... (Pack les autres boutons comme précédemment)
#     themed_button.pack(pady=5)

#     # Lancer la boucle principale
#     root.mainloop()


# # Créer la fenêtre principale
# root = tk.Tk()
# root.title("Styles de Boutons")

# # Appeler la fonction pour créer les boutons avec différents styles et un fond
# create_button_styles(root)


# def create_button_styles(root):

#     image_path = "1342060.png"
#     original_image = Image.open(image_path)

#     # Obtenir la taille de l'écran
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()

#     # Redimensionner l'image pour s'adapter à l'écran
#     resized_image = original_image.resize(
#         (screen_width, screen_height), Image.ANTIALIAS)
#     photo = ImageTk.PhotoImage(resized_image)

#     # Créer un canevas pour l'arrière-plan
#     canvas = tk.Canvas(root, width=screen_width, height=screen_height)

#     # Configurer l'image redimensionnée comme arrière-plan du canevas
#     canvas.create_image(0, 0, anchor=tk.NW, image=photo)
#     canvas.pack(expand=True, fill="both")

#     # canvas = tk.Canvas(root, width=400, height=300, bg="lightgray")
#     # canvas.pack(expand=True, fill="both")

#     # Charger une image (remplacez le chemin par le chemin de votre image)
#     image_path = "0f382f680a13445c8e6484ecbbe2a2b5.png"

#     image = tk.PhotoImage(file=image_path)

#     # Style 1: Bouton par défaut avec image en fond
#     default_button = tk.Button(
#         canvas, text="Default Button", image=image, compound="center", height=86, width=100)

#     # Style 2: Bouton avec couleur de fond personnalisée et image en fond
#     colored_button = tk.Button(
#         canvas, text="Colored Button", bg="lightblue", image=image, compound="center")

#     # ... (Ajoutez les autres boutons comme précédemment)

#     # Utilisation de ttk (themed Tkinter) pour des styles plus avancés
#     # Style 12: Bouton avec style "TButton" et image en fond
#     themed_button = ttk.Button(
#         canvas, text="Themed Button", style="TButton", image=image, compound="center")

#     # ... (Ajoutez les autres boutons ttk comme précédemment)

#     # Pack les boutons dans le canevas
#     default_button.pack(pady=5)
#     colored_button.pack(pady=5)
#     # ... (Pack les autres boutons comme précédemment)
#     themed_button.pack(pady=5)

#     # Lancer la boucle principale
#     root.mainloop()


# window = tk.Tk()  # Création de la fenêtre principale
# window.title("Planning")  # Titre de la fenêtre
# # Permet de quitter en appuyant sur la touche "Échap"
# window.attributes('-fullscreen', True)  # Affichage en mode plein écran
# window.bind('<Escape>', lambda e: window.destroy())
# window_width = window.winfo_width()
# window_height = window.winfo_height()

# # Appeler la fonction pour créer les boutons avec différents styles et un fond
# create_button_styles(window)

# from ftplib import FTP
# from tkinter import Tk, filedialog, Listbox, Button

# # Informations d'identification
# adresse_serveur = "83.113.54.154"
# nom_utilisateur = "lena"
# mot_de_passe = "1234"

# # Fonction pour télécharger un fichier Excel depuis le serveur FTP


# def telecharger_fichier_ftp(ftp, fichier_distant, fichier_local):
#     with open(fichier_local, 'wb') as fichier:
#         ftp.retrbinary(f'RETR {fichier_distant}', fichier.write)
#     print(
#         f"Le fichier {fichier_distant} a été téléchargé avec succès depuis le serveur FTP.")

# # Fonction appelée lors du téléchargement du fichier sélectionné


# def selectionner_fichier():
#     fichier_distant = liste_fichiers.get(liste_fichiers.curselection())
#     if fichier_distant:
#         # Utilisation de la boîte de dialogue pour sélectionner un fichier local
#         fichier_local_telecharge = filedialog.asksaveasfilename(defaultextension=".xlsx",
#                                                                 filetypes=[
#                                                                     ("Fichiers Excel", "*.xlsx")],
#                                                                 title="Sélectionnez l'emplacement de sauvegarde")
#         if fichier_local_telecharge:
#             telecharger_fichier_ftp(
#                 ftp, fichier_distant, fichier_local_telecharge)
#             print(f"Contenu du fichier {fichier_distant} téléchargé :")
#             # Ajoutez ici votre logique pour traiter le fichier Excel téléchargé
#             print("Traitement du fichier...")


# # Connexion au serveur FTP
# try:
#     ftp = FTP(adresse_serveur)
#     ftp.login(user=nom_utilisateur, passwd=mot_de_passe)
#     print(
#         f"Connecté au serveur FTP à {adresse_serveur} en tant que {nom_utilisateur}")

#     # Liste des fichiers présents sur le serveur
#     fichiers_sur_serveur = ftp.nlst()
#     print(fichiers_sur_serveur)

#     # Configuration de l'interface graphique Tkinter
#     fenetre = Tk()
#     fenetre.title("Sélection du fichier à télécharger")

#     # Création d'une liste pour afficher les fichiers du serveur FTP
#     liste_fichiers = Listbox(fenetre, selectmode="SINGLE")
#     for fichier in fichiers_sur_serveur:
#         liste_fichiers.insert("end", fichier)
#     liste_fichiers.pack()

#     # Bouton pour déclencher le téléchargement
#     bouton_selection = Button(
#         fenetre, text="Sélectionner un fichier", command=selectionner_fichier)
#     bouton_selection.pack()

#     # Lancement de la boucle principale Tkinter
#     fenetre.mainloop()

#     # Déconnexion
#     ftp.quit()

# except Exception as e:
#     print(f"Erreur de connexion au serveur FTP : {e}")


# def ecrire_dans_fichier(tableau_tuples, nom_fichier='donnees.txt'):
#     with open(nom_fichier, 'w') as fichier:
#         for ligne in tableau_tuples:
#             fichier.write(','.join(ligne) + '\n')


# def lire_depuis_fichier(nom_fichier='donnees.txt'):
#     tableau_tuples = []
#     with open(nom_fichier, 'r') as fichier:
#         lignes = fichier.readlines()
#         for ligne in lignes:
#             heure, cheval, personne = ligne.strip().split(',')
#             tableau_tuples.append((heure, cheval, personne))
#     return tableau_tuples


# # Exemple d'utilisation
# tableau_tuples = [('16H00 L', 'VIOLETTE', 'ANNA'), ('11H30 L', 'VIOLETTE', 'VALENTINE'), ('11H30 L', 'SURPRISE', 'CHLOE'), ('11H30 L', 'PEPITE', 'GABIN'), ('9h30 L', 'PANDA', ''), ('16H00 L', 'PONPON', 'SARAH'), ('11H30 L', 'PONPON', 'JABAL'), ('16H00 L', 'NUAGE', 'LEA'), ('11H30 L', 'NUAGE', 'PIERRE'), ('16H00 L', 'HOUSTON', 'LEXIE'), ('11H30 L', 'HOUSTON', 'MEYSSON'), ('16H00 L', 'REGLISSE', 'MAEL'), ('11H30 L', 'REGLISSE', 'PAUL'), ('16H00 L', 'NAVARA', 'MAYRA'), ('12H00 L', 'P. TONNERRE', 'CLARISSE'), ('14H00 L', 'GRISETTE', 'AELYS'), ('14H00 L', 'DANETTE', 'JULIEN'), ('12H00 L', 'DANETTE', 'CLEMENCE'), ('10H30 L', 'DANETTE', 'MAELLE'), ('14H00 L', 'TIC', 'VALENTINE'), ('12H00 L', 'TIC', 'ZACK'), ('10H30 L', 'TIC', 'HELOISE'), ('14H00 L', 'TAC', 'AMANDINE'), ('12H00 L', 'TAC', 'OCEANE'), ('9h30 L', 'TAC', 'CELIA FA'), ('14H00 L', 'SEGOVIA', 'MAELYS'), ('10H30 L', 'LITTLE', 'CLOE'), ('12H00 L', 'PAOLA', 'MANON'), ('17H00 L', 'MANGO', 'THAIS'), ('10H30 L', 'MANGO', 'LENA'), ('9h30 L', 'MANGO', 'LILY'), ('14H00 K', 'SORBET', 'AMELIE'), ('12H00 L', 'SORBET', 'AMBRE'), ('9h30 L', 'SORBET', 'CELIA FR'), ('14H00 K', 'RASTA', 'CLEMENCE'), ('9h30 L', 'RASTA', 'MAILYS'), ('17H00 K', 'PEGASE', 'SOLENE'), ('15H00 L', 'PEGASE', 'JULIE'), ('11H30 K', 'PEGASE', 'AYMIE'), ('9H30 K', 'PEGASE', 'MARINE'), ('16H00 K', 'BALI', 'NELL'), ('14H00 K', 'BALI', 'EVE'), ('12H00 L', 'BALI', 'ENZO'), ('10H30 K', 'BALI', 'SANDRINE'), ('17H00 K', 'CARA', 'CANDICE'), ('15H00 L', 'CARA', 'GIULIA'), ('10H30 L', 'CARA', 'MAELINE'), ('9H30 K', 'CARA', 'MAIWENN'), ('17H00 K', 'SAMOURAI', 'ELISE'), ('15H00 L', 'SAMOURAI', 'ELINA'), ('10H30 K', 'SAMOURAI', 'ANNABELLE'), ('9H30 K', 'SAMOURAI', 'TESSA'), ('18H00 K', 'FLICKA', 'ANGELIQUE'), ('15H00 L', 'FLICKA', 'LOANE'), ('10H30 L', 'FLICKA', 'NOA'), ('9H30 K', 'FLICKA', 'ILONA'), ('18H00 K', 'BANZAI',
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    'ANAIS'), ('13H00 K', 'BANZAI', 'HELENA'), ('18H00 K', 'KID', 'STEPHANIE'), ('15H00 L', 'KID', 'EMMA P'), ('9H30 K', 'KID', 'CHLOE'), ('17H00 K', 'DIESEL', 'ELINA'), ('13H00 K', 'DIESEL', 'CHARLOTTE'), ('17H00 L', 'SHEITAN', 'CHARLYNE'), ('14H00 K', 'SHEITAN', 'LEA'), ('10H30 K', 'SHEITAN', 'EMILIE'), ('9h30 L', 'SHEITAN', 'MARION'), ('17H00 L', 'SHAMIRA', 'ELISA'), ('14H00 K', 'SHAMIRA', 'CLEMENT'), ('12H00 L', 'SHAMIRA', 'LEELOU'), ('10H30 L', 'SHAMIRA', 'CLEMENT'), ('17H00 L', 'NEVA', 'CHARLINE'), ('16H00 K', 'NEVA', 'EMMA'), ('12H00 L', 'NEVA', 'SASHA'), ('9h30 L', 'NEVA', 'CELIA SF'), ('16H00 K', 'BRIOSSO', 'MATHILDE'), ('13H00 K', 'BRIOSSO', 'CLARA'), ('10H30 K', 'BRIOSSO', 'SANDRINE'), ('16H00 K', 'SINAI', 'LAURA'), ('13H00 K', 'SINAI', 'MAYA'), ('11H30 K', 'SINAI', 'ISELINE'), ('9h30 L', 'SINAI', 'JADE'), ('17H00 L', 'ETOILE', 'MAEVA'), ('14H00 K', 'ETOILE', 'CHLOE'), ('10H30 L', 'ETOILE', 'MAHILYS'), ('9H30 K', 'ETOILE', 'LEANE'), ('18H00 K', 'VASCO', 'BENBEN'), ('15H00 L', 'VASCO', 'EMMA L'), ('11H30 K', 'VASCO', 'INES'), ('9H30 K', 'VASCO', 'ENOLA'), ('17H00 L', 'DOMINO', 'ILONA'), ('16H00 K', 'DOMINO', 'CLARA'), ('11H30 K', 'DOMINO', 'LOLA'), ('10H30 K', 'DOMINO', 'NINA'), ('16H00 K', 'ESPOIR', 'LOEVA'), ('11H30 K', 'ESPOIR', 'JULIETTE'), ('16H00 K', 'JAZZY', 'MARGOT'), ('11H30 K', 'JAZZY', 'EVA'), ('17H00 K', 'ICHIBAI', 'JADE'), ('14H00 K', 'ICHIBAI', 'LAURA'), ('10H30 L', 'ICHIBAI', 'LISA'), ('17H00 K', 'CHOGUN', 'CARLA'), ('15H00 L', 'CHOGUN', 'LOUISE'), ('11H30 K', 'CHOGUN', 'FAUSTINE'), ('17H00 K', 'ALTAI', 'ALYSON'), ('16H00 K', 'ALTAI', 'MORGANE'), ('14H00 K', 'ALTAI', 'ILYANA'), ('11H30 K', 'ALTAI', 'ORANE'), ('13H00 K', 'WAR', 'CANDICE'), ('9H30 K', 'TALIA', 'LOU-ANN'), ('17H00 K', 'TANGO', 'LANA'), ('13H00 K', 'TANGO', 'JULIA'), ('16H00 K', 'ENZO', 'LOLA'), ('10H30 K', 'ENZO', 'GAEL')]

# # Écrire dans le fichier
# ecrire_dans_fichier(tableau_tuples)

# # Lire depuis le fichier
# nouveau_tableau = lire_depuis_fichier()

# # Afficher le nouveau tableau
# print(nouveau_tableau)


# from ftplib import FTP
# from datetime import datetime


# def download_files_from_ftp(host, username, password):
#     ftp = FTP(host)
#     ftp.login(user=username, passwd=password)
#     files = ftp.nlst()

#     samedi_files = []

#     mercredi_files = []

#     for file in files:
#         if "samedi" in file.lower():
#             samedi_files.append((file, extract_date_from_filename(file)))
#         elif "mercredi" in file.lower():
#             mercredi_files.append((file, extract_date_from_filename(file)))

#     print("samedi_files:", samedi_files)
#     print("mercredi_files:", mercredi_files)

#     samedi_files = sort_files_by_date(samedi_files)
#     mercredi_files = sort_files_by_date(mercredi_files)

#     samedi_file_names = [file[0] for file in samedi_files]
#     mercredi_file_names = [file[0] for file in mercredi_files]

#     print("samedi_file_names:", samedi_file_names)
#     print("mercredi_file_names:", mercredi_file_names)

#     ftp.quit()


# def sort_files_by_date(files):
#     # Trie les fichiers par date (les plus récents en premier)
#     sorted_files = sorted(files, key=lambda x: x[1], reverse=True)
#     return sorted_files


# def extract_date_from_filename(filename):
#     # Extrait la date du nom du fichier
#     date_str = filename.split()[-1].split('.')[0]
#     file_date = datetime.strptime(date_str, "%d-%m-%Y")
#     return file_date


# if __name__ == "__main__":
#     ftp_host = "83.113.54.154"
#     ftp_username = "lena"
#     ftp_password = "1234"

#     download_files_from_ftp(ftp_host, ftp_username, ftp_password)




# import tkinter as tk

# def on_enter_pressed(event):
#     focused_widget = root.focus_get()
#     print(str(focused_widget)[2:])
#     if isinstance(focused_widget, tk.Listbox):
#         print("La Listbox actuellement sélectionnée est :", focused_widget.get(tk.ACTIVE))
#     else:
#         print("Aucune Listbox n'est actuellement sélectionnée.")

# root = tk.Tk()

# listbox3 = tk.Listbox(root,name="listbox3")
# listbox3.insert(tk.END, "Option 1")
# listbox3.insert(tk.END, "Option 2")
# listbox3.pack()

# listbox5 = tk.Listbox(root)
# listbox5.insert(tk.END, "Option A")
# listbox5.insert(tk.END, "Option B")
# listbox5.pack()

# root.bind("<Return>", on_enter_pressed)

# root.mainloop()

# import os
# import stat
# import shutil
# fichier = '../ecuria 1.8'
# try:
#     # Changer les autorisations du fichier pour qu'il soit accessible en écriture pour tous les utilisateurs
#     os.chmod(fichier, stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)
#     print(f"Les autorisations du fichier '{fichier}' ont été modifiées avec succès.")
# except Exception as e:
#     print(f"Erreur lors de la modification des autorisations du fichier '{fichier}': {e}")
# print(os.path.exists("../ecuria 1.8"))
# try:
#     os.unlink("../ecuria 1.8")
#     print("reussi")
# except:
#     pass
# shutil.rmtree("../ecuria 1.8")

from ecuria.src.Ftp import *

ftp = Ftp("83.113.54.154","lena","1234")
nom_fichier = "Lena_ecuria 1.8.txt"
ftp.creer_fichier_vide(nom_fichier)