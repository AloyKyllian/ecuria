import customtkinter as ctk
import tkinter as tk


class PrincipalView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.create_var()
        self.create_layout()
        self.create_widgets()
        self.place_widgets()

    # ---------------- VARIABLES ---------------- #
    def create_var(self):
        self.user_var = tk.StringVar(value="Utilisateur")
        self.varheure_cheval = tk.StringVar(value="Heure du cheval")

    # ---------------- STYLE ---------------- #
    def style_button(self, parent, text, command):
        return ctk.CTkButton(
            parent,
            text=text,
            command=command,
            fg_color="#8abd45",
            hover_color="#6f9f2f",
            text_color="black",
            corner_radius=8
        )

    def style_label(self, parent, text=None, textvar=None, size=12, bold=False):
        return ctk.CTkLabel(
            parent,
            text=text,
            textvariable=textvar,
            font=("Segoe UI", size, "bold" if bold else "normal")
        )

    def style_entry(self, parent, placeholder=""):
        return ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            corner_radius=8
        )

    def style_textbox(self, parent):
        return ctk.CTkTextbox(
            parent,
            corner_radius=8
        )

    # ---------------- LAYOUT ---------------- #
    def create_layout(self):
        self.grid_rowconfigure(0, weight=0)   # header
        self.grid_rowconfigure(1, weight=1)   # main
        self.grid_columnconfigure(0, weight=1)

        # HEADER
        self.header = ctk.CTkFrame(self)
        self.header.grid(row=0, column=0, sticky="ew")

        # MAIN
        self.main = ctk.CTkFrame(self)
        self.main.grid(row=1, column=0, sticky="nsew")

        # 3 colonnes principales :
        # gauche = cavaliers
        # centre = actions
        # droite = chevaux + historique
        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_columnconfigure(1, weight=2)
        self.main.grid_columnconfigure(2, weight=2)

        self.main.grid_rowconfigure(0, weight=1)

        self.left_frame = ctk.CTkFrame(self.main)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.center_frame = ctk.CTkFrame(self.main)
        self.center_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.right_frame = ctk.CTkFrame(self.main)
        self.right_frame.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

    # ---------------- WIDGETS ---------------- #
    def create_widgets(self):
        # HEADER
        self.title = self.style_label(self.header, "GESTION ÉCURIE", size=18, bold=True)
        self.user_label = self.style_label(self.header, textvar=self.user_var)

        # LEFT (CAVALIERS)
        self.label_cavaliers = self.style_label(self.left_frame, "Cavaliers", bold=True)
        self.list_cavaliers = tk.Listbox(self.left_frame)

        # RIGHT TOP (CHEVAUX)
        self.label_chevaux = self.style_label(self.right_frame, "Chevaux", bold=True)
        self.list_chevaux = tk.Listbox(self.right_frame)

        # RIGHT BOTTOM (HISTORIQUE)
        self.label_historique = self.style_label(self.right_frame, "Historique", bold=True)
        self.text_historique = self.style_textbox(self.right_frame)

        # CENTER (ACTIONS)
        self.entry_nom = self.style_entry(self.center_frame, "Nom")
        self.entry_theme = self.style_entry(self.center_frame, "Thème")

        self.btn_add = self.style_button(self.center_frame, "Ajouter", self.controller.ajouter)
        self.btn_delete = self.style_button(self.center_frame, "Supprimer", self.controller.supprimer)
        self.btn_save = self.style_button(self.center_frame, "Enregistrer", self.controller.ecrire_fichier)

        self.label_heure = self.style_label(self.center_frame, textvar=self.varheure_cheval)

        # VISU
        self.label_visu = self.style_label(self.right_frame, "Prévisualisation", bold=True)
        self.text_visu = self.style_textbox(self.right_frame)

    # ---------------- PLACE ---------------- #
    def place_widgets(self):
        # HEADER
        self.title.pack(side="left", padx=20, pady=10)
        self.user_label.pack(side="right", padx=20)

        # LEFT (cavaliers)
        self.label_cavaliers.pack(pady=5)
        self.list_cavaliers.pack(fill="both", expand=True, padx=5, pady=5)

        # RIGHT (chevaux + historique)
        self.label_chevaux.pack(pady=5)
        self.list_chevaux.pack(fill="both", expand=True, padx=5, pady=5)

        self.label_historique.pack(pady=5)
        self.text_historique.pack(fill="both", expand=True, padx=5, pady=5)

        self.label_visu.pack(pady=5)
        self.text_visu.pack(fill="both", expand=True, padx=5, pady=5)

        # CENTER (actions)
        self.label_heure.pack(pady=10)
        self.entry_nom.pack(pady=5)
        self.entry_theme.pack(pady=5)

        self.btn_add.pack(pady=5)
        self.btn_delete.pack(pady=5)
        self.btn_save.pack(pady=5)


# ---------------- TEST DIRECT ---------------- #
if __name__ == "__main__":
    class MockController:
        def ajouter(self): print("Ajouter")
        def supprimer(self): print("Supprimer")
        def ecrire_fichier(self): print("Enregistrer")

    root = ctk.CTk()
    root.geometry("1200x700")

    view = PrincipalView(root, MockController())
    view.pack(fill="both", expand=True)

    root.mainloop()
