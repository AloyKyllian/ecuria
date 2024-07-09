import tkinter as tk
from PIL import Image, ImageTk


class ConfigController:
    def __init__(self, app):
        self.app = app

    def add_cheval(self):
        print("Ajouter cheval action")

    def suppr_cheval(self):
        print("Supprimer cheval action")

    def add_heure(self):
        print("Créer heure action")
    
    def suppr_heure(self):
        print("Supprimer heure action")

    def add_eleve(self):
        print("Créer élève action")

    def suppr_eleve(self):
        print("Supprimer élève action")

    def para_enregistrer(self):
        print("Enregistrer paramètres action")

    def ouvrir_excel(self):
        print("Ouvrir fichier Excel action")

    def toggle_entry_nbcarte(self):
        entry_state = self.app.views["ConfigView"].para_nbcarte.cget('state')
        new_state = tk.NORMAL if entry_state == tk.DISABLED else tk.DISABLED
        self.app.views["ConfigView"].para_nbcarte.config(state=new_state)

    def on_para_nbcarte_click(self, event):
        widget = event.widget
        if widget.get() == "nombre de seances":
            widget.delete(0, tk.END)

    def importer_param(self):
        print("Importer paramètres action")

    def exporter_param(self):
        print("Exporter paramètres action")

    def items_selected_heure(self, event):
        print("Heure sélectionnée")

    def items_selected_eleve(self, event):
        print("Élève sélectionné")

    def items_selected_cheval(self, event):
        print("Cheval sélectionné")

    def action(self, event):
        print("Action de la liste déroulante")
        
    def nouveau_fichier(self):
        print("Création d'un nouveau fichier")

    def recup_donne(self):
        print("Récupération des données")

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
    
    def add_centered_image(self,root, image_path, width, height):
        # Charger l'image
        original_image = Image.open(image_path)

        # Redimensionner l'image
        resized_image = original_image.resize((width, height), Image.NEAREST)
        photo = ImageTk.PhotoImage(resized_image)

        # Configurer l'image redimensionnée comme arrière-plan de la fenêtre
        image_label = tk.Label(root, borderwidth=0,
                            image=photo, highlightthickness=0, bg="#b4b4b4")
        image_label.image = photo
        image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        return image_label
    
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