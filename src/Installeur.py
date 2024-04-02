from Planning import *
from Jour import *
from Word import *
import Parametre as param
from Mail import *
from Zip import *
from Maj import *
from Ftp import *
import tkinter as tk
import os


def installateur(window,version):
    try:
        ftp = Ftp("83.113.54.154","lena","1234")
        connexion=True
    except:
        print("pas de connexion internet")
        connexion =False
    if connexion:
        fichiers = ftp.liste_fichiers()
        if fichiers:
            print(fichiers)
            version_fichiers=[]
            for fiche in fichiers:
                version_fiche  = fiche.replace(".zip","")
                version_fiche = version_fiche.split(" ")[-1]
                version_fichiers.append(float(version_fiche))
                
            version_fiche = max(version_fichiers)
            fiche = fichiers[version_fichiers.index(version_fiche)]
            print(version_fiche)
            print(fiche)
            if float(version_fiche) > version:
                import tkinter.messagebox as messagebox
                response = messagebox.askyesno("Mise à jour disponible", "Une nouvelle version est disponible. Voulez-vous la télécharger ?")
                if response:
                    current_path = os.getcwd()#C:\Users\33621\Documents\cheval_python\ecuria
                    no_current_path = current_path.rsplit('\\', 1)[0]#C:\Users\33621\Documents\cheval_python
                    path_nv_version = os.path.join(no_current_path, fiche.replace(".zip",""))
                    nom_appli_act = current_path.rsplit('\\', 1)[1]#ecuria
                    print(current_path)
                    def telecharger_et_mettre_a_jour():
                        ftp.telecharger_fichier_zip(fiche)
                        dezipper(fiche, no_current_path, suppr_rep_destination=False)
                        os.remove(fiche)

                    def valider():
                        telecharger_et_mettre_a_jour()
                        if raccourci_bureau_var.get():
                            print("raccourci")
                            print("la",no_current_path,fiche.replace(".zip",".exe"))
                            raccourci(no_current_path,fiche.replace(".zip",".exe"))
                            # Code pour créer un raccourci sur le bureau
                            
                        if garder_parametre_var.get():
                            print("garder")
                            # Code pour garder les paramètres
                            
                            path_parametre= os.path.join(path_nv_version, "parametre")
                            if os.path.exists(path_parametre):
                                liste_fichier_parametre = os.listdir(os.path.join(current_path, "parametre"))
                                for fichier in os.listdir(path_parametre):
                                    if fichier in liste_fichier_parametre:
                                        os.remove(os.path.join(path_nv_version, "parametre", fichier))
                                        shutil.copy(os.path.join(current_path, "parametre", fichier), os.path.join(path_nv_version, "parametre"))
                            else:
                                shutil.copytree("parametre", path_parametre)
                        
                        if supprimer_ancienne_version_var.get():
                            print("supprimer")
                            # os.remove(current_path)
                            bureau = os.path.join(os.path.expanduser("~"), "Desktop")
                            try:
                                os.remove(bureau + "\\" + nom_appli_act + ".lnk")
                            except:
                                pass
                            os.startfile(path_nv_version +"\\"+fiche.replace(".zip",".exe"))
                            top.destroy()
                            window.destroy()
                            # Code pour supprimer l'ancienne version
                        else:
                            top.destroy()

                    def annuler():
                        top.destroy()

                    # Création de la fenêtre top
                    top = tk.Toplevel(window)
                    top.title("Mise à jour")
                    top.geometry("300x200")
                    # Création des cases à cocher
                    raccourci_bureau_var = tk.BooleanVar()
                    raccourci_bureau_var.set(True)
                    raccourci_bureau_checkbox = tk.Checkbutton(top, text="Raccourci bureau", variable=raccourci_bureau_var)

                    supprimer_ancienne_version_var = tk.BooleanVar()
                    supprimer_ancienne_version_checkbox = tk.Checkbutton(top, text="Supprimer ancienne version", variable=supprimer_ancienne_version_var)

                    garder_parametre_var = tk.BooleanVar()
                    garder_parametre_checkbox = tk.Checkbutton(top, text="Garder paramètre", variable=garder_parametre_var)

                    # Création des boutons
                    valider_button = tk.Button(top, text="Valider", command=valider)
                    annuler_button = tk.Button(top, text="Annuler", command=annuler)

                    # Placement des éléments dans la fenêtre top
                    raccourci_bureau_checkbox.place(x=10, y=10)
                    supprimer_ancienne_version_checkbox.place(x=10, y=40)
                    garder_parametre_checkbox.place(x=10, y=70)
                    valider_button.place(x=250, y=170)
                    annuler_button.place(x=200, y=170)

                    # Lancement de la boucle principale de la fenêtre top
                    top.mainloop()