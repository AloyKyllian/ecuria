import zipfile
import os
from Mail import envoyer_email
import shutil
def zip_fichiers(repertoire_source, nom_zip):
    chemin_zip = os.path.join(os.getcwd(), nom_zip)
    # Créer un objet ZipFile pour écrire dans le fichier zip
    with zipfile.ZipFile(nom_zip, 'w') as fichier_zip:
        # Parcourir tous les fichiers du répertoire source
        for dossier_parent, _, fichiers in os.walk(repertoire_source):
            for fichier in fichiers:
                chemin_complet = os.path.join(dossier_parent, fichier)
                # Ajouter le fichier au zip avec son chemin relatif
                fichier_zip.write(chemin_complet, os.path.relpath(chemin_complet, repertoire_source))
    return chemin_zip

# repertoire_source = 'C:/Users/33621/Documents/cheval_python/ecuria/parametre'
# nom_zip = 'parametre.zip'
# chemin = zip_fichiers(repertoire_source, nom_zip)
# print(chemin)

# envoyer_email("Lena", chemin,"parametre.zip","exportation des parametres")



def dezipper(chemin_zip, repertoire_destination,suppr_rep_destination=True):
    erreur = None
    # Supprimer le répertoire de destination s'il existe déjà
    if suppr_rep_destination:
        try :
            if os.path.exists(repertoire_destination) :
                shutil.rmtree(repertoire_destination)

            # Créer le répertoire de destination
            os.makedirs(repertoire_destination)
        except:
            erreur = "Erreur lors de la suppression du répertoire de destination"
            print(erreur)
            return erreur
    try :
    # Ouvrir le fichier zip
        with zipfile.ZipFile(chemin_zip, 'r') as fichier_zip:
            # Extraire tous les fichiers
            fichier_zip.extractall(repertoire_destination)
        print(f"Les fichiers ont été extraits dans le répertoire {repertoire_destination}")
    except:
        erreur = "Erreur lors de l'extraction du fichier zip"
        print(erreur)
    return erreur
# Utilisation de la fonction pour décompresser un fichier zip
# chemin_zip = 'C:/Users/33621/Downloads/parametre.zip'
# repertoire_destination = 'C:/Users/33621/Documents/cheval_python/ecuria/parametre'

# dezipper(chemin_zip, repertoire_destination)