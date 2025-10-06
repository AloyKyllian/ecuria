from ftplib import FTP
from io import BytesIO
from openpyxl import load_workbook
from datetime import datetime
from Log import LoggerCounter

logger = LoggerCounter(name="Ftp").logger

class Ftp:
    def __init__(self, adresse_serveur, nom_utilisateur, mot_de_passe):
        self.adresse_serveur = adresse_serveur
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe
        self.ftp = FTP(self.adresse_serveur)

    def liste_fichiers(self):
        self.connexion()
        fichiers = self.ftp.nlst()
        self.deconnexion()
        return fichiers

    def connexion(self):
        logger.info("Connexion au serveur FTP %s", self.adresse_serveur)
        self.ftp = FTP(self.adresse_serveur)
        self.ftp.login(user=self.nom_utilisateur, passwd=self.mot_de_passe)

    def deconnexion(self):
        logger.info("Déconnexion du serveur FTP")
        self.ftp.close()

    def telecharger_fichier_zip(self, fichier_zip):
        self.connexion()
        logger.info("Téléchargement du fichier ZIP : %s", fichier_zip)
        with open(fichier_zip, "wb") as local_file:
            self.ftp.retrbinary(f"RETR {fichier_zip}", local_file.write)
        self.deconnexion()

    def telecharger_fichier_ftp(self, fichiers):
        self.connexion()
        logger.info("Téléchargement des fichiers FTP")
        for fichier_local in fichiers:
            wb = load_workbook(fichier_local)
            excel_content = BytesIO()
            wb.save(excel_content)
            excel_content.seek(0)
            self.ftp.storbinary("STOR " + fichier_local, excel_content)
            logger.info("Fichier %s téléchargé avec succès sur le serveur FTP.", fichier_local)
        self.deconnexion()

    def download_files_from_ftp(self):
        self.connexion()
        logger.info("Récupération de la liste des fichiers depuis le FTP")
        files = self.ftp.nlst()

        samedi_files, mercredi_files = [], []

        for file in files:
            if "samedi" in file.lower():
                samedi_files.append((file, self.extract_date_from_filename(file)))
            elif "mercredi" in file.lower():
                mercredi_files.append((file, self.extract_date_from_filename(file)))

        samedi_files = self.sort_files_by_date(samedi_files)
        mercredi_files = self.sort_files_by_date(mercredi_files)

        self.deconnexion()
        return [f[0] for f in samedi_files], [f[0] for f in mercredi_files]

    def sort_files_by_date(self, files):
        return sorted(files, key=lambda x: x[1], reverse=True)

    def extract_date_from_filename(self, filename):
        date_str = filename.split()[-1].split(".")[0]
        return datetime.strptime(date_str, "%d-%m-%Y")

    def ecrire_dans_fichier(self, tableau_tuples, nom_fichier="donnees.txt"):
        with open(nom_fichier, "w") as fichier:
            for ligne in tableau_tuples:
                fichier.write(",".join(ligne) + "\n")
        logger.info("Écriture dans le fichier %s terminée.", nom_fichier)

    def lire_depuis_fichier(self, nom_fichier="donnees.txt"):
        tableau_tuples = []
        with open(nom_fichier, "r") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                heure, cheval, personne = ligne.strip().split(",")
                tableau_tuples.append((heure, cheval, personne))
        logger.info("Lecture du fichier %s terminée.", nom_fichier)
        return tableau_tuples

    def download_files(self, files):
        self.connexion()
        logger.info("Téléchargement des fichiers : %s", files)
        for file in files:
            with open(file, "wb") as local_file:
                self.ftp.retrbinary(f"RETR {file}", local_file.write)
        self.deconnexion()

    def download_selected_and_recent_files(self, day, selected_file):
        samedi_file_names, mercredi_file_names = self.download_files_from_ftp()
        files = samedi_file_names if day.lower() == "samedi" else mercredi_file_names
        selected_ind = next(i for i, f in enumerate(files) if f == selected_file)
        self.download_files(files[selected_ind:selected_ind + 4])
        return files[selected_ind:selected_ind + 4]

    def supprimer(self, fiche):
        self.connexion()
        self.ftp.delete(fiche)
        logger.info("Fichier supprimé : %s", fiche)
        self.deconnexion()

    def creer_fichier_vide(self, nom_fichier):
        self.connexion()
        with open(nom_fichier, "rb") as f:
            self.ftp.storbinary("STOR " + nom_fichier, f)
        logger.info("Fichier vide créé : %s", nom_fichier)
        self.deconnexion()
