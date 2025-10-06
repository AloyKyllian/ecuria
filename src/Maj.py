import win32com.client
import os
import shutil

from Zip import *
from Ftp import *
import tkinter as tk
from Log import LoggerCounter

logger = LoggerCounter(name="Maj").logger

path_parametre = "parametre/"


def raccourci(path, nom):
    bureau = os.path.join(os.path.expanduser("~"), "Desktop")
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(
        os.path.join(bureau, nom.replace(".exe", "") + ".lnk")
    )
    shortcut.Targetpath = path + "\\" + nom.replace(".exe", "") + "\\" + nom
    logger.info("Target path du raccourci : %s", shortcut.Targetpath)
    shortcut.WorkingDirectory = path + "\\" + nom.replace(".exe", "")
    logger.info("Working directory du raccourci : %s", shortcut.WorkingDirectory)
    shortcut.save()


def installateur(window, user, version):
    try:
        ftp = Ftp("86.249.193.54", "lena", "1234")
        connexion = True
        if ftp.ftp.getwelcome() == "230 User lena logged in":
            connexion = True
    except Exception as e:
        logger.error("Pas de connexion internet ou serveur hors ligne : %s", e)
        connexion = False

    if connexion:
        fichiers = ftp.liste_fichiers()
        if fichiers:
            logger.info("Fichiers disponibles sur le FTP : %s", fichiers)
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
            logger.info("Version la plus récente : %s", version_fiche)
            logger.info("Nom du fichier correspondant : %s", fiche)

            if float(version_fiche) > version:
                import tkinter.messagebox as messagebox

                response = messagebox.askyesno(
                    "Mise à jour disponible",
                    "Une nouvelle version est disponible. Voulez-vous la télécharger ?",
                )
                if response:
                    current_path = os.getcwd()
                    no_current_path = current_path.rsplit("\\", 1)[0]
                    path_nv_version = os.path.join(no_current_path, fiche.replace(".zip", ""))
                    nom_appli_act = current_path.rsplit("\\", 1)[1]
                    logger.info("Chemin courant : %s", current_path)

                    def telecharger_et_mettre_a_jour():
                        ftp.telecharger_fichier_zip(fiche)
                        dezipper(fiche, no_current_path, suppr_rep_destination=False)
                        os.remove(fiche)

                    def valider():
                        telecharger_et_mettre_a_jour()
                        if raccourci_bureau_var.get():
                            logger.info("Création d'un raccourci sur le bureau")
                            raccourci(no_current_path, fiche.replace(".zip", ".exe"))

                        if garder_parametre_var.get():
                            logger.info("Conservation des paramètres existants")

                            def verif_case_valid():
                                selected_checkboxes = [
                                    files[i]
                                    for i, var in enumerate(vars_checkboxes2)
                                    if var.get() == 1
                                ]

                                path_parametre = os.path.join(path_nv_version, "parametre")
                                if os.path.exists(path_parametre):
                                    liste_fichier_parametre = os.listdir(
                                        os.path.join(current_path, "parametre")
                                    )
                                    for fichier in selected_checkboxes:
                                        if fichier in liste_fichier_parametre:
                                            os.remove(
                                                os.path.join(
                                                    path_nv_version, "parametre", fichier
                                                )
                                            )
                                            shutil.copy(
                                                os.path.join(current_path, "parametre", fichier),
                                                os.path.join(path_nv_version, "parametre"),
                                            )
                                else:
                                    shutil.copytree("parametre", path_parametre)
                                pop.destroy()

                            files = os.listdir(path_parametre)
                            pop = tk.Toplevel(window)
                            pop.title("Choix des paramètres à exporter.")
                            pop.geometry("550x120")

                            vars_checkboxes2 = []
                            checkboxes = []
                            for i, file in enumerate(files):
                                var = tk.IntVar()
                                checkbox = tk.Checkbutton(pop, text=file, variable=var)
                                checkboxes.append(checkbox)
                                vars_checkboxes2.append(var)

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

                            button_annuler = tk.Button(pop, text="Annuler", command=pop.destroy)
                            button_valider = tk.Button(pop, text="Valider", command=verif_case_valid)
                            button_annuler.place(x=450, y=90)
                            button_valider.place(x=500, y=90)
                            pop.mainloop()

                        if supprimer_ancienne_version_var.get():
                            logger.info("Suppression de l'ancienne version")
                            nom_fichier = f"{user}_ecuria {version}.txt"
                            ftp.creer_fichier_vide(nom_fichier)
                            bureau = os.path.join(os.path.expanduser("~"), "Desktop")
                            try:
                                os.remove(os.path.join(bureau, f"{nom_appli_act}.lnk"))
                            except Exception as e:
                                logger.warning("Impossible de supprimer le raccourci : %s", e)

                        os.startfile(os.path.join(path_nv_version, fiche.replace(".zip", ".exe")))
                        top.destroy()
                        window.destroy()

                    def annuler():
                        top.destroy()

                    top = tk.Toplevel(window)
                    top.title("Mise à jour")
                    top.geometry("300x200")

                    raccourci_bureau_var = tk.BooleanVar(value=True)
                    raccourci_bureau_checkbox = tk.Checkbutton(top, text="Raccourci bureau", variable=raccourci_bureau_var)

                    supprimer_ancienne_version_var = tk.BooleanVar()
                    supprimer_ancienne_version_checkbox = tk.Checkbutton(top, text="Supprimer ancienne version", variable=supprimer_ancienne_version_var)

                    garder_parametre_var = tk.BooleanVar()
                    garder_parametre_checkbox = tk.Checkbutton(top, text="Garder paramètre", variable=garder_parametre_var)

                    valider_button = tk.Button(top, text="Valider", command=valider)
                    annuler_button = tk.Button(top, text="Annuler", command=annuler)

                    raccourci_bureau_checkbox.place(x=10, y=10)
                    supprimer_ancienne_version_checkbox.place(x=10, y=40)
                    garder_parametre_checkbox.place(x=10, y=70)
                    valider_button.place(x=250, y=170)
                    annuler_button.place(x=200, y=170)

                    top.mainloop()


def desinstallateur(fiche, user, ftp):
    ftp.supprimer(fiche)
    fiche = fiche.replace(".txt", "")
    nom = fiche.split("_")[0]
    logger.info("%s supprimé du FTP", fiche)
    if nom == user:
        logger.info("Nom d'utilisateur reconnu, suppression locale possible")
        fichier = "../" + str(fiche.split("_")[1])
        if os.path.exists(fichier):
            shutil.rmtree(fichier)
            logger.info("%s supprimé localement", fichier)
        else:
            logger.warning("Fichier introuvable localement : %s", fichier)
    else:
        logger.warning("Nom d'utilisateur non reconnu : %s", nom)
