import tkinter as tk
from PIL import Image, ImageTk


class PrincipalController:
    def __init__(self, app):
        self.app = app

    def heure_precedant(self):
        print("Heure précédente")

    def heure_suivant(self):
        print("Heure suivante")

    def items_selected(self, event):
        print("Élève sélectionné")

    def items_selected_cheval(self, event):
        print("Cheval sélectionné")

    def ajouter_rattrapage(self):
        print("Ajout rattrapage")

    def ajouter_theme(self):
        print("Ajout du thème")

    def absent(self):
        print("Absent")

    def correction(self):
        print("Correction")

    def ajouter(self):
        print("Ajouter")

    def supprimer(self):
        print("Supprimer")

    def ecrire_fichier(self):
        print("Enregistrer le fichier")

    def ouvrir_excel(self):
        print("Ouvrir Excel")

    def rafraichir(self):
        print("Rafraîchir")

    def ecrire_word(self):
        print("Écrire Word")

    def ecrire_mail(self):
        print("Écrire Mail")

    def fusion(self):
        print("Fusion")

    def items_selected_heure_cheval(self, event):
        print("Heure de travail du cheval sélectionnée")

    def action(self, event):
        print("Action ComboBox")
        
        
    def image(self,root, image_path, width, height):
        original_image = Image.open(image_path)

        # Redimensionner l'image
        resized_image = original_image.resize((width, height), Image.NEAREST)
        photo = ImageTk.PhotoImage(resized_image)

        # Configurer l'image redimensionnée comme arrière-plan de la fenêtre
        image_label = tk.Label(root, borderwidth=0,
                            image=photo, highlightthickness=0, bg="#b4b4b4")
        image_label.image = photo
        return image_label
    

    def set_background(self,root, image_path):
        # Charger l'image
        original_image = Image.open(image_path)

        # Obtenir la taille de l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Redimensionner l'image pour s'adapter à l'écran
        resized_image = original_image.resize((screen_width, screen_height), Image.NEAREST)

        photo = ImageTk.PhotoImage(resized_image)

        # Configurer l'image redimensionnée comme arrière-plan de la fenêtre
        background_label = tk.Label(root, image=photo, bg="#b4b4b4")
        background_label.image = photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        return background_label, photo