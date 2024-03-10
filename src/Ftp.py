from ftplib import FTP
from io import BytesIO
import openpyxl
from openpyxl import load_workbook, Workbook
from datetime import datetime, timedelta


class Ftp():

    def __init__(self, adresse_serveur, nom_utilisateur, mot_de_passe):
        self.adresse_serveur = adresse_serveur
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe
        self.ftp=FTP(self.adresse_serveur)
        # return download_files_from_ftp()

    # adresse_serveur = "83.113.54.154"
    # nom_utilisateur = "lena"
    # mot_de_passe = "1234"
    def liste_fichiers(self):
        self.connexion()
        fichiers = self.ftp.nlst()
        self.deconnexion()
        return fichiers

    def connexion(self):
        print("connexion")
        # print(self.nom_utilisateur)
        # print(self.mot_de_passe)
        self.ftp=FTP(self.adresse_serveur)
        # print(self.ftp.login(user=self.nom_utilisateur, passwd=self.mot_de_passe))
        self.ftp.login(user=self.nom_utilisateur, passwd=self.mot_de_passe)
#       230-Welcome to TrueNAS FTP Server
#       230 User lena logged in

    def deconnexion(self):
        print("deconnexion")
        self.ftp.close()

    def telecharger_fichier_zip(self, fichier_zip):
        self.connexion()
        print("telecharger_fichier_zip")
        with open(fichier_zip, "wb") as local_file:
            self.ftp.retrbinary(f"RETR {fichier_zip}", local_file.write)
        self.deconnexion()

    def telecharger_fichier_ftp(self, fichier):
        self.connexion()
        print("telecharger_fichier_ftp")
        for fichier_local in fichier:
            wb = load_workbook(fichier_local)

            # Créez un fichier en mémoire pour stocker le contenu du fichier Excel
            excel_content = BytesIO()
            wb.save(excel_content)

            # Téléversez le fichier Excel en mémoire sur le serveur FTP
            excel_content.seek(0)  # Revenir au début du fichier en mémoire
            self.ftp.storbinary('STOR ' + fichier_local, excel_content)
            print(
                f"Le fichier {fichier_local} a été téléchargé avec succès depuis le serveur FTP.")

        self.deconnexion()

    def download_files_from_ftp(self):
        self.connexion()
        print("download_files_from_ftp")
        files = self.ftp.nlst()

        samedi_files = []

        mercredi_files = []

        for file in files:
            if "samedi" in file.lower():
                samedi_files.append(
                    (file, self.extract_date_from_filename(file)))
            elif "mercredi" in file.lower():
                mercredi_files.append(
                    (file, self.extract_date_from_filename(file)))

        samedi_files = self.sort_files_by_date(samedi_files)
        mercredi_files = self.sort_files_by_date(mercredi_files)

        samedi_file_names = [file[0] for file in samedi_files]
        mercredi_file_names = [file[0] for file in mercredi_files]

        self.deconnexion()

        return samedi_file_names, mercredi_file_names

    def sort_files_by_date(self, files):
        # Trie les fichiers par date (les plus récents en premier)
        sorted_files = sorted(files, key=lambda x: x[1], reverse=True)
        return sorted_files

    def extract_date_from_filename(self, filename):
        # Extrait la date du nom du fichier
        date_str = filename.split()[-1].split('.')[0]
        file_date = datetime.strptime(date_str, "%d-%m-%Y")
        return file_date

    def ecrire_dans_fichier(self, tableau_tuples, nom_fichier='donnees.txt'):
        with open(nom_fichier, 'w') as fichier:
            for ligne in tableau_tuples:
                fichier.write(','.join(ligne) + '\n')

    def lire_depuis_fichier(self, nom_fichier='donnees.txt'):
        tableau_tuples = []
        with open(nom_fichier, 'r') as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                heure, cheval, personne = ligne.strip().split(',')
                tableau_tuples.append((heure, cheval, personne))
        return tableau_tuples

    def download_files(self, files):
        self.connexion()
        print("download_files")
        for file in files:
            with open(f"{file}", "wb") as local_file:
                self.ftp.retrbinary(f"RETR {file}", local_file.write)
        self.deconnexion()

    def download_selected_and_recent_files(self, day, selected_file):
        samedi_file_names, mercredi_file_names = self.download_files_from_ftp()
        # suppr_excel()
        if day.lower() == "samedi":
            files = samedi_file_names
        elif day.lower() == "mercredi":
            files = mercredi_file_names
        # Récupère les trois fichiers les plus récents du même jour
        for i in range(len(files)):
            if files[i] == selected_file:
                selected_ind = i

        # Upload des fichiers
        self.download_files(files[selected_ind:selected_ind+4])
        return files[selected_ind:selected_ind+4]
        # recup_donne2(files[selected_ind:selected_ind+4])
