import tkinter as tk
from tkinter import Menu
from controllers.main_controller import MainController
from views.waiting_view import WaitingView
from views.principal_view import PrincipalView
from views.config_view import ConfigView
# from views.main_view import MainView

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application avec Menu")
        self.attributes('-fullscreen', True)  # Pour démarrer en plein écran
        self.update()
        self.proportion_x = self.winfo_width() / 1536
        self.proportion_y = self.winfo_height() / 864
        # Créer une instance du contrôleur
        self.controller = MainController(self)

        # self.main_view = MainView(self, self.controller, self.proportion_x, self.proportion_y)
        # self.main_view.pack(fill=tk.BOTH, expand=True)

        # Initialiser le menu
        self.create_menu()
        
        # self.background()

        # Initialiser les conteneurs de page
        self.container = tk.Frame(self)
        self.container.pack(fill=tk.BOTH, expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Initialiser les vues (pages)
        self.views = {}
        self.create_views()

    def create_menu(self):
        menubar = Menu(self)

        # Ajout des éléments au menu
        menubar.add_command(label="Nouveau", command=self.nouveau_fichier)
        menubar.add_command(label="Jour", command=self.recup_donne)

        # Sous-menu pour changer de mode
        sousmenu = Menu(menubar, tearoff=0)
        sousmenu.add_command(label="Paramètre", command=lambda: self.show_view("ConfigView"))
        sousmenu.add_command(label="Principal", command=lambda: self.show_view("PrincipalView"))
        menubar.add_cascade(label="Mode", menu=sousmenu)

        menubar.add_command(label="Quitter!", command=self.quit)

        # Affichage du menu dans la fenêtre
        self.config(menu=menubar)
    
    def background(self):
        version = 1.83  # Version actuelle du programme
        self.label_version = tk.Label(self, text="Version " + str(version), bg='#b4b4b4')
        self.label_version.place(x=int(1395*self.proportion_x), y=int(780*self.proportion_y))
        # self.controller.get_image_controller().set_background(self, "image\\image_fond.png")

    def create_views(self):
        for V in (WaitingView, PrincipalView, ConfigView):
            view_name = V.__name__
            frame = V(parent=self.container, controller=self.controller, proportion_x=self.proportion_x, proportion_y=self.proportion_y)
            self.views[view_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_view("WaitingView")

    def show_view(self, view_name):
        frame = self.views[view_name]
        frame.tkraise()

    def nouveau_fichier(self):
        print("Action pour créer un nouveau fichier")

    def recup_donne(self):
        print("Action pour récupérer les données")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
