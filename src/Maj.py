import win32com.client
import os
import shutil

from Zip import *
from Ftp import *
import tkinter as tk

path_parametre = "parametre/"


def raccourci(path, nom):
    bureau = os.path.join(os.path.expanduser("~"), "Desktop")
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(
        os.path.join(bureau, nom.replace(".exe", "") + ".lnk")
    )
    shortcut.Targetpath = path + "\\" + nom.replace(".exe", "") + "\\" + nom
    print(path + "\\" + nom.replace(".exe", "") + "\\" + nom)
    # shortcut.Targetpath = r"C:\\Users\\33621\\Documents\\cheval_python\\ecuria\\ecuria 1.5\\ecuria v1.5.exe"
    shortcut.WorkingDirectory = path + "\\" + nom.replace(".exe", "")
    print(path + "\\" + nom.replace(".exe", ""))
    # shortcut.WorkingDirectory = r"C:\\Users\\33621\\Documents\\cheval_python\\ecuria\\ecuria 1.5"
    shortcut.save()


def installateur(window, user, version):
    try:
        ftp = Ftp("86.249.193.54", "lena", "1234")
        connexion = True
        if ftp.ftp.getwelcome() == "230 User lena logged in":
            connexion = True
    except:
        print("pas de connexion internet ou serveur hors ligne")
        connexion = False
    if connexion:
        fichiers = ftp.liste_fichiers()
        if fichiers:
            print(fichiers)
            version_fichiers = []
            for fiche in fichiers:
                if ".zip" in fiche:
                    version_fiche = fiche.replace(".zip", "")
                    version_fiche = version_fiche.split(" ")[-1]
                    version_fichiers.append(float(version_fiche))
                elif ".txt" in fiche:
                    desinstallateur(fiche, user, ftp)

            version_fiche = max(version_fichiers)
            fiche = fichiers[version_fichiers.index(version_fiche)]
            print(version_fiche)
            print(fiche)
            if float(version_fiche) > version:
                import tkinter.messagebox as messagebox

                response = messagebox.askyesno(
                    "Mise à jour disponible",
                    "Une nouvelle version est disponible. Voulez-vous la télécharger ?",
                )
                if response:
                    current_path = (
                        os.getcwd()
                    )  # C:\Users\33621\Documents\cheval_python\ecuria
                    no_current_path = current_path.rsplit("\\", 1)[
                        0
                    ]  # C:\Users\33621\Documents\cheval_python
                    path_nv_version = os.path.join(
                        no_current_path, fiche.replace(".zip", "")
                    )
                    nom_appli_act = current_path.rsplit("\\", 1)[1]  # ecuria
                    print(current_path)

                    def telecharger_et_mettre_a_jour():
                        ftp.telecharger_fichier_zip(fiche)
                        dezipper(fiche, no_current_path, suppr_rep_destination=False)
                        os.remove(fiche)

                    def valider():
                        telecharger_et_mettre_a_jour()
                        if raccourci_bureau_var.get():
                            print("raccourci")
                            print("la", no_current_path, fiche.replace(".zip", ".exe"))
                            raccourci(no_current_path, fiche.replace(".zip", ".exe"))
                            # Code pour créer un raccourci sur le bureau

                        if garder_parametre_var.get():
                            print("garder")
                            # Code pour garder les paramètres

                            def verif_case_valid():
                                # Get the selected checkboxes
                                selected_checkboxes = [
                                    files[i]
                                    for i, var in enumerate(vars_checkboxes2)
                                    if var.get() == 1
                                ]

                                path_parametre = os.path.join(
                                    path_nv_version, "parametre"
                                )
                                if os.path.exists(path_parametre):
                                    liste_fichier_parametre = os.listdir(
                                        os.path.join(current_path, "parametre")
                                    )
                                    for fichier in selected_checkboxes:
                                        if fichier in liste_fichier_parametre:
                                            os.remove(
                                                os.path.join(
                                                    path_nv_version,
                                                    "parametre",
                                                    fichier,
                                                )
                                            )
                                            shutil.copy(
                                                os.path.join(
                                                    current_path, "parametre", fichier
                                                ),
                                                os.path.join(
                                                    path_nv_version, "parametre"
                                                ),
                                            )
                                else:
                                    shutil.copytree("parametre", path_parametre)
                                pop.destroy()

                            files = os.listdir(path_parametre)
                            pop = tk.Toplevel(window)
                            pop.title("Choix des paramètres à exporter.")
                            pop.geometry("550x120")

                            # Create buttons for each file
                            # Create checkboxes for each file
                            vars_checkboxes2 = []
                            checkboxes = []
                            for i, file in enumerate(files):
                                var = tk.IntVar()
                                checkbox = tk.Checkbutton(pop, text=file, variable=var)
                                checkboxes.append(checkbox)
                                vars_checkboxes2.append(var)

                            # Place the checkboxes in a grid
                            numx = 0
                            numy = 0
                            num = 0
                            for i, checkbox in enumerate(checkboxes):
                                checkbox.place(x=0 + numx, y=0 + numy)
                                numy += 20
                                num += 1
                                if num > 4:
                                    num = 0
                                    numy = 0
                                    numx += 200
                            # Create buttons for "Annuler" and "Valider"
                            button_annuler = tk.Button(
                                pop, text="Annuler", command=pop.destroy
                            )
                            button_valider = tk.Button(
                                pop, text="Valider", command=verif_case_valid
                            )

                            # Place the buttons at the bottom right of the window
                            button_annuler.place(x=450, y=90)
                            button_valider.place(x=500, y=90)
                            pop.mainloop()

                        if supprimer_ancienne_version_var.get():
                            print("supprimer")
                            nom_fichier = str(user) + "_ecuria " + str(version) + ".txt"
                            ftp.creer_fichier_vide(nom_fichier)
                            bureau = os.path.join(os.path.expanduser("~"), "Desktop")
                            try:
                                os.remove(bureau + "\\" + nom_appli_act + ".lnk")
                            except:
                                pass

                        os.startfile(
                            path_nv_version + "\\" + fiche.replace(".zip", ".exe")
                        )
                        top.destroy()
                        window.destroy()

                    def annuler():
                        top.destroy()

                    # Création de la fenêtre top
                    top = tk.Toplevel(window)
                    top.title("Mise à jour")
                    top.geometry("300x200")
                    # Création des cases à cocher
                    raccourci_bureau_var = tk.BooleanVar()
                    raccourci_bureau_var.set(True)
                    raccourci_bureau_checkbox = tk.Checkbutton(
                        top, text="Raccourci bureau", variable=raccourci_bureau_var
                    )

                    supprimer_ancienne_version_var = tk.BooleanVar()
                    supprimer_ancienne_version_checkbox = tk.Checkbutton(
                        top,
                        text="Supprimer ancienne version",
                        variable=supprimer_ancienne_version_var,
                    )

                    garder_parametre_var = tk.BooleanVar()
                    garder_parametre_checkbox = tk.Checkbutton(
                        top, text="Garder paramètre", variable=garder_parametre_var
                    )

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


def desinstallateur(fiche, user, ftp):
    ftp.supprimer(fiche)
    fiche = fiche.replace(".txt", "")  # Lena_ecuria 1.82
    nom = fiche.split("_")[0]  # ['Lena', 'ecuria 1.82']
    print(fiche, "supprimé du ftp")
    if nom == user:
        print("nom d'utilisateur reconnu pret pour la suppression")
        fichier = "../" + str(fiche.split("_")[1])  # \ecuria 1.82
        print(fichier, os.path.exists(fichier))
        if os.path.exists(fichier):
            shutil.rmtree(fichier)
            print(fichier, "supprimé")
        else:
            print("fichier introuvable")
    else:
        print("nom d'utilisateur non reconnu")
