import zipfile
import os
import shutil
from Log import LoggerCounter

logger = LoggerCounter(name="Zip").logger


def zip_fichiers(repertoire_source, nom_zip):
    """
    Crée un fichier zip à partir d'un répertoire source.

    Args:
        repertoire_source (str): Le chemin du répertoire à zipper.
        nom_zip (str): Le nom du fichier zip à créer.

    Returns:
        str: Le chemin complet du fichier zip créé.
    """
    chemin_zip = os.path.join(os.getcwd(), nom_zip)
    # Créer un objet ZipFile pour écrire dans le fichier zip
    with zipfile.ZipFile(nom_zip, "w") as fichier_zip:
        # Parcourir tous les fichiers du répertoire source
        for dossier_parent, _, fichiers in os.walk(repertoire_source):
            for fichier in fichiers:
                chemin_complet = os.path.join(dossier_parent, fichier)
                # Ajouter le fichier au zip avec son chemin relatif
                fichier_zip.write(
                    chemin_complet, os.path.relpath(chemin_complet, repertoire_source)
                )
    logger.info("Fichier zip créé : %s", chemin_zip)
    return chemin_zip


def dezipper(chemin_zip, repertoire_destination, suppr_rep_destination=True):
    """
    Décompresse un fichier zip dans un répertoire de destination.

    Args:
        chemin_zip (str): Chemin du fichier zip à extraire.
        repertoire_destination (str): Répertoire où extraire le contenu.
        suppr_rep_destination (bool, optional): Supprime le répertoire existant avant extraction. Defaults to True.

    Returns:
        str | None: Message d'erreur en cas de problème, sinon None.
    """
    erreur = None
    # Supprimer le répertoire de destination s'il existe déjà
    if suppr_rep_destination:
        try:
            if os.path.exists(repertoire_destination):
                shutil.rmtree(repertoire_destination)
            # Créer le répertoire de destination
            os.makedirs(repertoire_destination)
        except Exception as e:
            erreur = f"Erreur lors de la suppression ou création du répertoire : {e}"
            logger.error(erreur)
            return erreur

    try:
        # Ouvrir le fichier zip
        with zipfile.ZipFile(chemin_zip, "r") as fichier_zip:
            # Extraire tous les fichiers
            fichier_zip.extractall(repertoire_destination)
        logger.info("Les fichiers ont été extraits dans le répertoire %s", repertoire_destination)
    except Exception as e:
        erreur = f"Erreur lors de l'extraction du fichier zip : {e}"
        logger.error(erreur)
    return erreur
