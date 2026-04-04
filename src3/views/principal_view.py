import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# 🎨 COULEURS
GREEN = "#8abd45"
GREEN_HOVER = "#6f9f2f"
TEXT = "#2f2f2f"


class PrincipalView(ctk.CTkFrame):

    def __init__(self, parent, controller, proportion_x, proportion_y):
        super().__init__(parent)

        self.controller = controller.get_principal_controller()
        self.contr_image = controller.get_image_controller()

        self.proportion_x = proportion_x
        self.proportion_y = proportion_y

        self.create_var()
        self.place_image(proportion_x, proportion_y)
        self.create_widgets()
        self.place_widget()

    # ---------------- STYLE HELPERS ---------------- #
    def style_button(self, text, command):
        return ctk.CTkButton(
            self,
            text=text,
            command=command,
            width=10,
            fg_color=GREEN,
            hover_color=GREEN_HOVER,
            text_color="black",
            corner_radius=8,
            bg_color="#b4b4b4"
        )

    def style_label(self, text=None, textvar=None, size=12, bold=False):
        return ctk.CTkLabel(
            self,
            text=text,
            textvariable=textvar,
            font=("Segoe UI", size, "bold" if bold else "normal"),
            text_color=TEXT,
            fg_color="#b4b4b4"
        )
    
    def style_entry(self, placeholder=""):
        return ctk.CTkEntry(
            self,
            placeholder_text=placeholder,
            fg_color="#ffffff",          # fond blanc propre
            text_color="#000000",
            border_color="#8abd45",      # ton vert
            border_width=2,
            corner_radius=10,
            bg_color="#b4b4b4"           # 🔥 CRUCIAL pour les coins
        )

    def style_textbox(self, width=200, height=100):
        return ctk.CTkTextbox(
            self,
            width=width,
            height=height,
            fg_color="#cccccc",          # fond blanc
            text_color="#000000",
            border_color="#8abd45",
            border_width=2,
            corner_radius=10,
            bg_color="#b4b4b4"           # 🔥 pour les coins
        )







    # ---------------- VARIABLES ---------------- #
    def create_var(self):
        self.varjour = tk.StringVar(value="Jour")
        self.varheure = tk.StringVar(value="Heure")
        self.user_var = tk.StringVar(value="Utilisateur")

        self.varsemaine1 = tk.StringVar(value="Semaine 1")
        self.varcavalier = tk.StringVar(value="Cavalier")
        self.varsemaine2 = tk.StringVar(value="Semaine 2")
        self.varcavalier1 = tk.StringVar(value="Cavalier 1")
        self.varsemaine3 = tk.StringVar(value="Semaine 3")
        self.varcavalier2 = tk.StringVar(value="Cavalier 2")

        self.varajout = tk.StringVar(value="Ajout")
        self.varheure_cheval = tk.StringVar(value="Heure du Cheval")

        self.theme = tk.StringVar(value="Thème")
        self.theme1 = tk.StringVar(value="Thème 1")
        self.theme2 = tk.StringVar(value="Thème 2")
        self.theme3 = tk.StringVar(value="Thème 3")

    # ---------------- WIDGETS ---------------- #
    def create_widgets(self):

        # HEADER
        self.title_label = self.style_label("GESTION PLANNING", size=18, bold=True)
        self.label_user = self.style_label(textvar=self.user_var)

        # NAV
        self.boutton_avancer_heure = self.style_button("precedent", self.controller.heure_precedant)
        self.boutton_reculer_heure = self.style_button("suivant", self.controller.heure_suivant)

        # INFOS
        self.label_cavalier = self.style_label("INFOS CAVALIER", size=14, bold=True)

        self.label_cavalier2 = self.style_label(textvar=self.varsemaine1)
        self.label_cavalier3 = self.style_label(textvar=self.varcavalier)
        self.label_cavalier6 = self.style_label(textvar=self.varsemaine2)
        self.label_cavalier4 = self.style_label(textvar=self.varcavalier1)
        self.label_cavalier7 = self.style_label(textvar=self.varsemaine3)
        self.label_cavalier5 = self.style_label(textvar=self.varcavalier2)

        # ACTIONS
        self.boutton_absent = self.style_button("ABS", self.controller.absent)
        self.boutton_correction = self.style_button("correction", self.controller.correction)

        # LISTBOX
        self.eleve_listbox = tk.Listbox(self)
        self.cheval_listbox = tk.Listbox(self)

        for lb in [self.eleve_listbox, self.cheval_listbox]:
            lb.config(
                bg="#ffffff",
                fg=TEXT,
                selectbackground=GREEN,
                selectforeground="black",
                relief="flat",
                borderwidth=0
            )

        self.eleve_listbox.bind('<<ListboxSelect>>', self.controller.items_selected)
        self.cheval_listbox.bind('<<ListboxSelect>>', self.controller.items_selected_cheval)

        # PREVIEW
        self.visu_fichier = self.style_textbox(
            width=int(500*self.proportion_x),
            height=int(380*self.proportion_y)
        )
        # self.visu_fichier.config(bg="#ffffff", fg=TEXT, insertbackground="black", relief="flat")

        self.label_visu_fichier = self.style_label("PREVISUALISATION", size=14, bold=True)

        # HISTORIQUE
        self.label_historique = self.style_label("HISTORIQUE", size=13, bold=True)

        self.historique = self.style_textbox(
            width=int(450*self.proportion_x),
            height=int(280*self.proportion_y)
        )
        # self.historique.config(bg="#ffffff", fg=TEXT, insertbackground="black", relief="flat")

        # HEURES
        self.label_heure_cheval = self.style_label(textvar=self.varheure_cheval)

        self.heure_listebox = tk.Listbox(self)
        self.heure_listebox.config(
            bg="#ffffff",
            fg=TEXT,
            selectbackground=GREEN,
            relief="flat",
            borderwidth=0
        )

        self.heure_listebox.bind('<<ListboxSelect>>', self.controller.items_selected_heure_cheval)

        # COMBO
        self.listeCombo = ttk.Combobox(self, values=[])
        self.listeCombo.bind("<<ComboboxSelected>>", self.controller.action)

        # ENTRIES
        self.eleve_rattrapage = self.style_entry("Ajouter un nom")
        self.theme_entry = self.style_entry("Ajouter un theme")

        # THEME
        self.label_theme = self.style_label("Theme")
        self.boutton_theme = self.style_button("ajout du theme", self.controller.ajouter_theme)

        # ACTION BUTTONS
        self.boutton_ajouter = self.style_button("Ajouter", self.controller.ajouter)
        self.boutton_supprimer = self.style_button("Supprimer", self.controller.supprimer)
        self.boutton_enregistrer = self.style_button("ENREGISTRER", self.controller.ecrire_fichier)

        # EXTRA
        self.bouton_ouvrir_excel = self.style_button("ouvrir", self.controller.ouvrir_excel)
        self.bouton_rafraichir = self.style_button("rafraichir", self.controller.rafraichir)
        self.bouton_word = self.style_button("word", self.controller.ecrire_word)
        self.bouton_mail = self.style_button("mail", self.controller.ecrire_mail)
        self.bouton_fusion = self.style_button("fusion", self.controller.fusion)

    # ---------------- PLACE ---------------- #
    def place_widget(self):

        px = self.proportion_x
        py = self.proportion_y

        self.title_label.place(x=int(60 * px), y=int(35 * py))
        self.label_user.place(x=int(60 * px), y=int(70 * py))

        self.boutton_avancer_heure.place(x=int(65 * px), y=int(140 * py))
        self.boutton_reculer_heure.place(x=int(260 * px), y=int(140 * py))

        self.label_cavalier.place(x=int(470 * px), y=int(70 * py))

        self.label_cavalier2.place(x=int(470 * px), y=int(100 * py))
        self.label_cavalier3.place(x=int(650 * px), y=int(100 * py))
        self.label_cavalier6.place(x=int(470 * px), y=int(150 * py))
        self.label_cavalier4.place(x=int(650 * px), y=int(150 * py))
        self.label_cavalier7.place(x=int(470 * px), y=int(200 * py))
        self.label_cavalier5.place(x=int(650 * px), y=int(200 * py))

        self.boutton_absent.place(x=int(755 * px), y=int(100 * py))
        self.boutton_correction.place(x=int(810 * px), y=int(100 * py))

        self.eleve_listbox.place(x=int(133 * px), y=int(170 * py))
        self.cheval_listbox.place(x=int(330 * px), y=int(35 * py))

        self.visu_fichier.place(x=int(900 * px), y=int(395 * py))
        self.label_visu_fichier.place(x=int(900 * px), y=int(365 * py))

        self.label_historique.place(x=int(900 * px), y=int(40 * py))
        self.historique.place(x=int(900 * px), y=int(70 * py))

        self.label_heure_cheval.place(x=int(470 * px), y=int(250 * py))
        self.heure_listebox.place(x=int(470 * px), y=int(280 * py))

        self.listeCombo.place(x=int(65 * px), y=int(100 * py))

        self.eleve_rattrapage.place(x=int(133 * px), y=int(390 * py))
        self.theme_entry.place(x=int(133 * px), y=int(490 * py))

        self.label_theme.place(x=int(133 * px), y=int(460 * py))
        self.boutton_theme.place(x=int(140 * px), y=int(520 * py))

        self.boutton_ajouter.place(x=int(570 * px), y=int(480 * py))
        self.boutton_supprimer.place(x=int(670 * px), y=int(480 * py))
        self.boutton_enregistrer.place(x=int(570 * px), y=int(530 * py))

        self.bouton_ouvrir_excel.place(x=int(1400 * px), y=int(60 * py))
        self.bouton_rafraichir.place(x=int(1400 * px), y=int(100 * py))
        self.bouton_word.place(x=int(1400 * px), y=int(140 * py))
        self.bouton_mail.place(x=int(1400 * px), y=int(180 * py))
        self.bouton_fusion.place(x=int(1400 * px), y=int(220 * py))

    # ---------------- IMAGE ---------------- #
    def place_image(self, proportion_x, proportion_y):
        self.contr_image.set_background(self, "image_fond.png")

        self.image1 = self.contr_image.image(self, "image1.png", int(2388/8.5*proportion_x), int(1668/8.5*proportion_y))
        self.image2 = self.contr_image.image(self, "image2.png", int(2388/8.5*proportion_x), int(1668/8.5*proportion_y))
        self.image3 = self.contr_image.image(self, "image3.png", int(2388/8.5*proportion_x), int(1668/8.5*proportion_y))

        self.image1.place(x=int(535 * proportion_x), y=int(606 * proportion_y))
        self.image2.place(x=int(70 * proportion_x), y=int(600 * proportion_y))
        self.image3.place(x=int(680 * proportion_x), y=int(220 * proportion_y))
