import tkinter as tk
from tkinter import ttk

class ConfigView(tk.Frame):
    def __init__(self, parent, controller, proportion_x, proportion_y):
        super().__init__(parent)
        self.controller = controller.get_config_controller()
        self.contr_image = controller.get_image_controller()
        self.create_var()
        self.place_image(proportion_x,proportion_y,controller)
        self.create_widgets(proportion_x,proportion_y)
        self.place_widget(proportion_x,proportion_y)
        
    def create_var(self):
        self.v = tk.IntVar()

    def create_widgets(self,proportion_x,proportion_y):
      
        self.para_visu_fichier = tk.Text(self, width=int(70*proportion_x),height=int(24*proportion_y))
        self.para_visu_fichier.config(state='disabled')

        # Étiquette pour afficher l'historique
        self.para_label_historique = tk.Label(
            self, text="historique", font=("Corbel", int(13*proportion_x)), bg='#b4b4b4')

        # Zone de texte pour afficher l'historique
        self.para_historique = tk.Text(self, width=int(60*proportion_x), height=int(13*proportion_y))
        self.para_historique.config(state='disabled')

        self.para_listebox_heure = tk.Listbox(self,name="para_listebox_heure", width=int(25*proportion_x), height=int(45*proportion_y))
        # Association de la fonction à l'événement de relâchement du bouton de la souris
        self.para_listebox_heure.bind('<<ListboxSelect>>', self.controller.items_selected_heure)


        self.para_listebox_eleve = tk.Listbox(self,name="para_listebox_eleve", width=int(25*proportion_x), height=int(12*proportion_y))
        # Association de la fonction à l'événement de relâchement du bouton de la souris
        self.para_listebox_eleve.bind('<<ListboxSelect>>', self.controller.items_selected_eleve)

        self.para_listebox_chevaux = tk.Listbox(self,name="para_listebox_chevaux", width=int(25*proportion_x), height=int(45*proportion_y))
        # Association de la fonction à l'événement de relâchement du bouton de la souris
        self.para_listebox_chevaux.bind('<<ListboxSelect>>', self.controller.items_selected_cheval)

        # Création d'une liste déroulante pour sélectionner l'heure
        self.para_listeCombo = ttk.Combobox(self,width=int(10*proportion_x))
        self.para_listeCombo['values'] = ["Mercredi", "Samedi","Semaine"]

        self.para_listeCombo_user = ttk.Combobox(self,width=int(10*proportion_x))


        self.para_input_chevaux = tk.Entry(self)
        self.para_input_ind_chevaux = tk.Entry(self, width=3)
        self.para_add_chevaux = tk.Button(
            self, text="ajouter cheval", command=self.controller.add_cheval, width=int(18*proportion_x), bg='#8abd45')
        self.para_suppr_chevaux = tk.Button(
            self, text="supprimer cheval", command=self.controller.suppr_cheval, width=int(18*proportion_x), bg='#8abd45')

        self.para_listeCombo.bind("<<ComboboxSelected>>", self.controller.action)

        self.para_input_heure = tk.Entry(self)

        self.para_add_heure = tk.Button(
            self, text="creer heure", command=self.controller.add_heure, width=int(18*proportion_x), bg='#8abd45')

        # self.para_suppr_heure = tk.Button(
        #     self, text="supprimer heure", command=lambda:suppr_heure(dict_eleve,heure), width=int(18*proportion_x), bg='#8abd45')
        
        self.para_suppr_heure = tk.Button(
            self, text="supprimer heure", command=self.controller.add_heure, width=int(18*proportion_x), bg='#8abd45')


        self.para_input_eleve = tk.Entry(self)

        self.para_add_eleve = tk.Button(
            self, text="creer eleve", command=self.controller.add_eleve, width=int(18*proportion_x), bg='#8abd45')

        self.para_suppr_eleve = tk.Button(
            self, text="supprimer eleve", command=self.controller.suppr_eleve, width=int(18*proportion_x), bg='#8abd45')

        self.para_boutton_enregistrer = tk.Button(
            self, text="ENREGISTRER", command=self.controller.para_enregistrer, width=12, font=("Helvetica", 18, "bold"), bg='#000000', fg='#ffffff')

        self.para_label_mail_karine = tk.Label(self, text="mail karine", font=("Corbel", 13), bg='#b4b4b4')
        self.para_entry_karine = tk.Entry(self, width=int(25*proportion_x))

        self.para_label_mail_lena = tk.Label(self, text="mail lena", font=("Corbel", 13), bg='#b4b4b4')
        self.para_entry_lena = tk.Entry(self, width=int(25*proportion_x))

        self.para_bouton_ouvrir_excel = tk.Button(
            self, text="ouvrir excel reference", bg="#8abd45", command=self.controller.ouvrir_excel)

        self.para_case = tk.Checkbutton (self,variable = self.v,bg='#b4b4b4',text= "eleve à la carte",command=self.controller.toggle_entry_nbcarte)

        self.para_nbcarte = tk.Entry(self)
        self.para_nbcarte.insert(0, "nombre de seances")
        self.para_nbcarte.config(state=tk.DISABLED)

        self.para_nbcarte.bind('<FocusIn>', self.controller.on_para_nbcarte_click)

        self.para_bouton_importer_param = tk.Button(
            self, text="importer parametre",width=15, bg="#8abd45", command=self.controller.importer_param)

        self.para_bouton_exporter_param = tk.Button(
            self, text="exporter parametre",width=15, bg="#8abd45", command=self.controller.exporter_param)


    def place_widget(self,proportion_x,proportion_y):
        
        self.para_visu_fichier.place(x=int(900 * proportion_x), y=int(395 * proportion_y))
        self.para_listebox_heure.place(x=int(400 * proportion_x), y=int(70 * proportion_y))
        self.para_listebox_eleve.place(x=int(730 * proportion_x), y=int(70 * proportion_y))
        self.para_listeCombo.place(x=int(65 * proportion_x), y=int(40 * proportion_y))
        self.para_listeCombo_user.place(x=int(170 * proportion_x), y=int(40 * proportion_y))
        self.para_input_heure.place(x=int(560 * proportion_x), y=int(140 * proportion_y))
        self.para_add_heure.place(x=int(560 * proportion_x), y=int(170 * proportion_y))
        self.para_suppr_heure.place(x=int(560 * proportion_x), y=int(200 * proportion_y))
        self.para_input_eleve.place(x=int(890 * proportion_x), y=int(140 * proportion_y))
        self.para_add_eleve.place(x=int(890 * proportion_x), y=int(170 * proportion_y))
        self.para_suppr_eleve.place(x=int(890 * proportion_x), y=int(200 * proportion_y))
        self.para_boutton_enregistrer.place(x=int(635 * proportion_x), y=int(680 * proportion_y))
        self.para_listebox_chevaux.place(x=int(60 * proportion_x), y=int(70 * proportion_y))
        self.para_input_chevaux.place(x=int(220 * proportion_x), y=int(140 * proportion_y))
        self.para_add_chevaux.place(x=int(220 * proportion_x), y=int(170 * proportion_y))
        self.para_suppr_chevaux.place(x=int(220 * proportion_x), y=int(200 * proportion_y))
        self.para_input_ind_chevaux.place(x=int(360 * proportion_x), y=int(140 * proportion_y))
        self.para_case.place(x=int(890 * proportion_x), y=int(230 * proportion_y))
        self.para_nbcarte.place(x=int(890 * proportion_x), y=int(260 * proportion_y))
        
        
        posymail = 290 * proportion_y
        self.para_label_mail_karine.place(x=int(730 * proportion_x), y=int(posymail))
        self.para_entry_karine.place(x=int(820 * proportion_x), y=int(posymail))
        self.para_label_mail_lena.place(x=int(730 * proportion_x), y=int(posymail + 30))
        self.para_entry_lena.place(x=int(820 * proportion_x), y=int(posymail + 30))
        self.para_bouton_importer_param.place(x=int(1300 * proportion_x), y=int(290 * proportion_y))
        self.para_bouton_exporter_param.place(x=int(1300 * proportion_x), y=int(325 * proportion_y))
        self.para_bouton_ouvrir_excel.place(x=int(1295 * proportion_x), y=int(360 * proportion_y))
        
        
        
        
        
    def place_image(self,proportion_x,proportion_y,controller):
        self.contr_image.set_background(self, "image_fond.png")
        self.para_image1 = self.contr_image.image(self, "image1.png", int(2388/5*proportion_x), int(1668/5*proportion_y))
        self.image3 = self.contr_image.image(self, "image3.png", int(2388/8.5*proportion_x), int(1668/8.5*proportion_y))
        self.image4 = self.contr_image.image(self, "image4.png", int(2388/7*proportion_x), int(1668/7))
        self.para_image1.place(relx=0.48, rely=0.6, anchor=tk.CENTER)
        self.image3.place(x=int(170 * proportion_x), y=int(500 * proportion_y))
        self.image4.place(x=int(1070 * proportion_x), y=int(70 * proportion_y))