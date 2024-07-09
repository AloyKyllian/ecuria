import tkinter as tk
from tkinter import ttk

class PrincipalView(tk.Frame):
    def __init__(self, parent, controller, proportion_x, proportion_y):
        super().__init__(parent)
        self.controller = controller.get_principal_controller()
        self.contr_image = controller.get_image_controller()
        self.place_image(proportion_x,proportion_y)
        self.create_var()
        self.create_widgets(proportion_x,proportion_y)
        self.place_widget(proportion_x,proportion_y)
        
        
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
        # self.user_var.set(user)

    def create_widgets(self,proportion_x,proportion_y):
        self.label_jour = tk.Label(self, textvariable=self.varjour, bg='#b4b4b4',font=("Comic Sans MS", int(15*proportion_x)))

        self.label_heure = tk.Label(self, textvariable=self.varheure, bg='#b4b4b4')

        self.label_user = tk.Label(self, textvariable=self.user_var,font=("Comic Sans MS", int(15*proportion_x)), bg='#b4b4b4')

        # Création d'une étiquette pour le titre
        self.title_label = tk.Label(
            self, text="GESTION PLANNING", font=("Comic Sans MS", int(17*proportion_x)), bg='#b4b4b4')

        # Boutons pour avancer et reculer dans les heures
        self.boutton_avancer_heure = tk.Button(
            self, width=8, bg='#8abd45', text="precedent", command=self.controller.heure_precedant)

        self.boutton_reculer_heure = tk.Button(
            self, width=8, bg='#8abd45', text="suivant", command=self.controller.heure_suivant)

        # Étiquettes pour afficher les informations du cavalier
        self.label_cavalier = tk.Label(
            self, text="INFOS CAVALIER", font=("Corbel", int(14*proportion_x)), bg='#8abd45')

        self.label_cavalier2 = tk.Label(
            self, textvariable=self.varsemaine1, font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')

        self.label_cavalier3 = tk.Label(
            self, textvariable=self.varcavalier, font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')

        self.label_cavalier6 = tk.Label(
            self, textvariable=self.varsemaine2, font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')

        self.label_cavalier4 = tk.Label(
            self, textvariable=self.varcavalier1, font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')

        self.label_cavalier7 = tk.Label(
            self, textvariable=self.varsemaine3, font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')
        self.label_cavalier5 = tk.Label(
            self, textvariable=self.varcavalier2, font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')


        self.boutton_absent = tk.Button(
            self, bg='#8abd45', height=1, width=int(4*proportion_x), text="ABS", command=self.controller.absent, borderwidth=2)
        self.boutton_correction = tk.Button(
            self, bg='#8abd45', height=1, text="correction", command=self.controller.correction)
        # Initialisation des variables de contrôle


        # Liste déroulante pour les élèves
        self.eleve_listbox = tk.Listbox(self,name="eleve_listbox", yscrollcommand=True)

        self.eleve_rattrapage = tk.Entry(self)


        self.label_eleve_rattrapage = tk.Label(
            self, text="Ajouter un nom", font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')
        self.boutton_eleve_rattrapage = tk.Button(
            self, width=int(8*proportion_x), bg='#8abd45', text="rattrapage", command=self.controller.ajouter_rattrapage)

        self.theme_entry = tk.Entry(self)

        self.label_theme = tk.Label(
            self, text="Ajouter un theme", font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')
        self.boutton_theme = tk.Button(
            self, width=int(14*proportion_x), bg='#8abd45', text="ajout du theme", command=self.controller.ajouter_theme)
        self.label_theme_actuelle = tk.Label(
            self, textvariable=self.theme, font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')
        self.label_theme_avant1 = tk.Label(
            self, textvariable=self.theme1, font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')
        self.label_theme_avant2 = tk.Label(
            self, textvariable=self.theme2, font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')
        self.label_theme_avant3 = tk.Label(
            self, textvariable=self.theme3, font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')
        


        # Association de la fonction à l'événement de relâchement du bouton de la souris
        self.eleve_listbox.bind('<<ListboxSelect>>', self.controller.items_selected)

        # Liste déroulante pour les chevaux
        self.cheval_listbox = tk.Listbox(self,name="cheval_listbox", height=int(47*proportion_y))




        # Association de la fonction à l'événement de relâchement du bouton de la souris
        self.cheval_listbox.bind('<<ListboxSelect>>', self.controller.items_selected_cheval)

        # Zone de texte pour afficher le planning
        self.visu_fichier = tk.Text(self, width=int(70*proportion_x),height=int(24*proportion_y))
        self.visu_fichier.config(state='disabled')

        self.label_visu_fichier = tk.Label(
            self, text="PREVISUALISATION", font=("Corbel", int(14*proportion_x)), bg='#8abd45')


        # Étiquette pour afficher des informations sur l'ajout
        self.label_ajout = tk.Label(self, textvariable=self.varajout,
                            font=int(20*proportion_x), bg='#ffffff')


        # Bouton pour ajouter une entrée
        self.boutton_ajouter = tk.Button(
            self, text="Ajouter", command=self.controller.ajouter, width=int(11*proportion_x), height=int(2*proportion_y), bg='#8abd45')


        # Bouton pour supprimer une entrée
        self.boutton_supprimer = tk.Button(
            self, text="Supprimer", command=self.controller.supprimer, width=int(11*proportion_x), height=int(2*proportion_y), bg='#8abd45')


        # Bouton pour enregistrer les modifications
        self.boutton_enregistrer = tk.Button(
            self, text="ENREGISTRER", command=self.controller.ecrire_fichier, width=12, font=("Helvetica", 18, "bold"), bg='#000000', fg='#ffffff')


        # Étiquette pour afficher un message après l'enregistrement
        self.label_enregistrer = tk.Label(
            self, text="Le fichier a bien été enregistré", font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')  # le fichier à bien été enregistré
        self.label_enregistrer.config(fg="#b4b4b4")

        # Étiquette pour afficher l'heure de travail du cheval
        self.label_heure_cheval = tk.Label(
            self, textvariable=self.varheure_cheval, font=("Corbel", int(13*proportion_x)), bg='#8abd45')


        # Liste déroulante pour les heures de travail
        self.heure_listebox = tk.Listbox(self,name="heure_listebox", width=int(25*proportion_x), height=int(5*proportion_y))




        self.bouton_ouvrir_excel = tk.Button(
            self, text="ouvrir", bg="#8abd45", command=self.controller.ouvrir_excel)

        self.bouton_rafraichir = tk.Button(
            self, text="rafraichir", bg="#8abd45", command=self.controller.rafraichir)

        self.bouton_word = tk.Button(
            self, text="word", bg="#8abd45", command=self.controller.ecrire_word)

        self.bouton_mail = tk.Button(
            self, text="mail", bg="#8abd45", command=self.controller.ecrire_mail)

        self.bouton_fusion = tk.Button(
            self, text="fusion", bg="#8abd45", command=self.controller.fusion)

        # Fonction appelée lorsqu'un élément est sélectionné dans la liste des heures de travail


        # Association de la fonction à l'événement de relâchement du bouton de la souris
        self.heure_listebox.bind('<<ListboxSelect>>', self.controller.items_selected_heure_cheval)

        # Étiquette pour afficher l'historique
        self.label_historique = tk.Label(
            self, text="HISTORIQUE", font=("Corbel", int(13*proportion_x)), bg='#8abd45')

        # Zone de texte pour afficher l'historique
        self.historique = tk.Text(self, width=int(60*proportion_x), height=int(13*proportion_y))
        self.historique.config(state='disabled')

        # Création d'une liste déroulante pour sélectionner l'heure
        self.listeCombo = ttk.Combobox(self, height=int(10*proportion_y), width=int(40*proportion_x))


        self.listeCombo.bind("<<ComboboxSelected>>", self.controller.action)
        
    def place_widget(self,proportion_x,proportion_y):
        self.label_jour.place(x=int(240 * proportion_x), y=int(70 * proportion_y))
        self.label_heure.place(x=int(150 * proportion_x), y=int(145 * proportion_y))
        self.title_label.place(x=int(60 * proportion_x), y=int(35 * proportion_y))
        self.boutton_avancer_heure.place(x=int(65 * proportion_x), y=int(140 * proportion_y))
        self.boutton_reculer_heure.place(x=int(260 * proportion_x), y=int(140 * proportion_y))
        self.label_cavalier.place(x=int(470 * proportion_x), y=int(70 * proportion_y))
        self.label_cavalier2.place(x=int(470 * proportion_x), y=int(100 * proportion_y))
        self.label_cavalier3.place(x=int(650 * proportion_x), y=int(100 * proportion_y))
        self.label_cavalier6.place(x=int(470 * proportion_x), y=int(150 * proportion_y))
        self.label_cavalier4.place(x=int(650 * proportion_x), y=int(150 * proportion_y))
        self.label_cavalier7.place(x=int(470 * proportion_x), y=int(200 * proportion_y))
        self.label_cavalier5.place(x=int(650 * proportion_x), y=int(200 * proportion_y))
        self.boutton_absent.place(x=int(755 * proportion_x), y=int(100 * proportion_y))
        self.boutton_correction.place(x=int(810 * proportion_x), y=int(100 * proportion_y))
        self.eleve_listbox.place(x=int(133 * proportion_x), y=int(170 * proportion_y))
        self.eleve_rattrapage.place(x=int(133 * proportion_x), y=int(390 * proportion_y))
        self.label_eleve_rattrapage.place(x=int(137 * proportion_x), y=int(360 * proportion_y))
        self.boutton_eleve_rattrapage.place(x=int(160 * proportion_x), y=int(420 * proportion_y))
        self.cheval_listbox.place(x=int(330 * proportion_x), y=int(35 * proportion_y))
        self.visu_fichier.place(x=int(900 * proportion_x), y=int(395 * proportion_y))
        self.label_visu_fichier.place(x=int(900 * proportion_x), y=int(365 * proportion_y))
        self.label_ajout.place(x=int(470 * proportion_x), y=int(400 * proportion_y))
        self.boutton_ajouter.place(x=int(570 * proportion_x), y=int(480 * proportion_y))
        self.boutton_supprimer.place(x=int(670 * proportion_x), y=int(480 * proportion_y))
        self.boutton_enregistrer.place(x=int(570 * proportion_x), y=int(530 * proportion_y))
        self.label_enregistrer.place(x=int(560 * proportion_x), y=int(585 * proportion_y))
        self.label_heure_cheval.place(x=int(470 * proportion_x), y=int(250 * proportion_y))
        self.heure_listebox.place(x=int(470 * proportion_x), y=int(280 * proportion_y))
        self.historique.place(x=int(900 * proportion_x), y=int(70 * proportion_y))
        self.label_historique.place(x=int(900 * proportion_x), y=int(40 * proportion_y))
        self.label_user.place(x=int(60 * proportion_x), y=int(70 * proportion_y))
        self.listeCombo.place(x=int(65 * proportion_x), y=int(100 * proportion_y))
        self.bouton_ouvrir_excel.place(x=int(1400 * proportion_x), y=int(60 * proportion_y))
        self.bouton_rafraichir.place(x=int(1400 * proportion_x), y=int(100 * proportion_y))
        self.label_theme.place(x=int(133 * proportion_x), y=int(460 * proportion_y))
        self.theme_entry.place(x=int(133 * proportion_x), y=int(490 * proportion_y))
        self.boutton_theme.place(x=int(140 * proportion_x), y=int(520 * proportion_y))
        self.label_theme_actuelle.place(x=int(160 * proportion_x), y=int(550 * proportion_y))
        self.label_theme_avant1.place(x=int(650 * proportion_x), y=int(125 * proportion_y))
        self.label_theme_avant2.place(x=int(650 * proportion_x), y=int(175 * proportion_y))
        self.label_theme_avant3.place(x=int(650 * proportion_x), y=int(225 * proportion_y))
        self.bouton_word.place(x=int(1400 * proportion_x), y=int(140 * proportion_y))
        self.bouton_mail.place(x=int(1400 * proportion_x), y=int(180 * proportion_y))
        self.bouton_fusion.place(x=int(1400 * proportion_x), y=int(220 * proportion_y))
        
        # self.info.place(x=int(460 * proportion_x), y=int(35 * proportion_y))
        # self.info2.place(x=int(1400 * proportion_x), y=int(260 * proportion_y))
        
        


    def place_image(self,proportion_x,proportion_y):
        self.contr_image.set_background(self, "image_fond.png")
        self.image1 = self.contr_image.image(self, "image1.png", int(2388/8.5*proportion_x ), int(1668/8.5*proportion_y))
        self.image2 = self.contr_image.image(self, "image2.png", int(2388/8.5*proportion_x), int(1668/8.5*proportion_y))
        self.image3 = self.contr_image.image(self, "image3.png", int(2388/8.5*proportion_x), int(1668/8.5*proportion_y))
        self.image1.place(x=int(535 * proportion_x), y=int(606 * proportion_y))
        self.image2.place(x=int(70 * proportion_x), y=int(600 * proportion_y))
        self.image3.place(x=int(680 * proportion_x), y=int(220 * proportion_y))