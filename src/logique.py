"""
Module logique : fonctions métier de l'application (lecture/écriture des fichiers
Excel et texte, tri des heures, calcul de dates, etc.) sans dépendance à l'interface
Tkinter. L'objet `planning` partagé et le logger sont créés ici et importés par
l'interface.
"""

from Planning import *
from Jour import *
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, Border, Side, Alignment, PatternFill
from datetime import datetime, timedelta
from Log import LoggerCounter


# Création du logger
log_stats = LoggerCounter(name="Ecuria", user="init")
logger = log_stats.logger

logger.info("--------------------------------Démarrage du programme--------------------------------\r\n\r\n\r\n")


path_parametre = "parametre/"
path_cavalier_mercredi = path_parametre + "liste_cavalier_mercredi.txt"
path_cavalier_samedi = path_parametre + "liste_cavalier_samedi.txt"
path_cavalier_semaine = path_parametre + "liste_cavalier_semaine.txt"
path_cheval = path_parametre + "liste_cheval.txt"
path_cheval_semaine = path_parametre + "liste_cheval_semaine.txt"
path_mail = path_parametre + "mail.txt"
path_user = "user.txt"
path_Mercredi = path_parametre + "Mercredi.xlsx"
path_Samedi = path_parametre + "Samedi.xlsx"
path_semaine = path_parametre + "Semaine.xlsx"
path_image = "image/"

# Instance partagée de la classe Planning (utilisée par la logique et l'interface)
planning = Planning()


def remplir_cheval(dict_chevaux):
    logger.info("Remplissage des données des chevaux")
    dict_cheval_temp = {}
    logger.debug("remplir_cheval    dict_chevaux %s", dict_chevaux)
    # # print("remplir_cheval    planning.planning",planning.planning)
    for cheval in dict_chevaux:
        dict_cheval_temp[cheval] = [dict_chevaux[cheval][0], planning.nb_heure(cheval)]
    return dict_cheval_temp


def get_personne():
    logger.info("Récupération de l'utilisateur courant depuis get_personne")
    with open(path_user, "r") as file:
        return file.read()


def get_mail():
    logger.info("Récupération des adresses e-mail depuis get_mail")
    moniteur = []
    tableau = []
    with open(path_mail, "r") as file:
        lines = file.readlines()
        tab = [line.strip() for line in lines]
    for val in tab:
        moniteur.append(val.split(":")[0])
        tableau.append(val.split(":")[1])
    logger.debug("tableau %s", tableau)
    logger.debug("moniteur %s", moniteur)
    # # print(tableau)
    # # print(moniteur)
    return tableau, moniteur


def ecrire_excel_ref(jour, dict_cheval, dict_eleve):
    logger.info("Début de la fonction ecrire_excel_ref pour le jour %s", jour)
    # ouverture du fichier reference
    workbook = load_workbook(path_parametre + jour + ".xlsx")
    feuille = workbook.active

    # recuperer la mise en forme du fichier reference
    taillecellule = feuille.column_dimensions["B"].width
    hauteurcellule = feuille.row_dimensions[4].height
    taille_police = feuille.cell(4, 2).font.size

    # creation d'un nouveau fichier excel
    workbook = Workbook()
    sheet = workbook.active

    # # print("ecrire_excel_ref    dict_cheval[jour] ",dict_cheval[jour])
    logger.debug("ecrire_excel_ref    dict_cheval[jour] %s", dict_cheval[jour])
    liste_cheval = list(dict_cheval[jour].keys())
    heure_trier = list(dict_eleve[jour].keys())

    lignes = len(liste_cheval) + 4
    colonnes = len(heure_trier) + 2

    dico_numeros = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z",
    }

    double = Side(border_style="thin", color="000000")

    ind_ligne = 0
    for ligne in range(3, lignes):
        ind_colonne = 0
        # mise en forme de la heuteur des lignes
        for colonne in range(1, colonnes):
            # mise en forme des cellules
            sheet.cell(ligne, colonne).font = Font(size=taille_police)
            sheet.cell(ligne, colonne).alignment = Alignment(
                horizontal="center", vertical="center"
            )
            sheet.cell(ligne, colonne).border = Border(
                left=double, top=double, right=double, bottom=double
            )
            # mise en forme des heures
            if ligne == 3:
                # mise en forme de la largeur des lignes
                sheet.column_dimensions[dico_numeros[colonne]].width = taillecellule
                if colonne != 1:
                    # ajout des heures
                    sheet.cell(ligne, colonne).value = heure_trier[ind_colonne]
                    ind_colonne += 1
                if colonne % 2 == 0:
                    # creation des heures vertes
                    sheet.cell(ligne, colonne).fill = PatternFill(
                        start_color="70AD47", end_color="70AD47", fill_type="solid"
                    )
            # creation des lignes vertes
            if ligne % 2 == 0:
                sheet.cell(ligne, colonne).fill = PatternFill(
                    start_color="A9D08E", end_color="A9D08E", fill_type="solid"
                )
            # mise en forme des chevaux
            if colonne == 1:
                sheet.row_dimensions[ligne].height = hauteurcellule
                if ligne != 3:
                    # ajout des chevaux
                    sheet.cell(ligne, colonne).value = liste_cheval[ind_ligne]
                    ind_ligne += 1

    # ajout du titre theme
    sheet.cell(lignes, 1).value = "theme"

    # sauvegarde du fichier reference
    workbook.save(path_parametre + jour + ".xlsx")


def cmp_dates(d):
    """
    Compare deux dates au format "jour-mois-année".

    Cette fonction prend en argument une date au format "jour-mois-année" et retourne un tuple (année, mois, jour)
    pour permettre une comparaison correcte des dates.

    Args:
        d (str): Une date au format "jour-mois-année".

    Returns:
        tuple: Un tuple (année, mois, jour).
    """
    logger.debug("Comparaison des dates pour %s", d)
    j, m, a = d[0].split("-")

    return (int(a), int(m), int(j))


def recupperation_excel(name):
    """
    Récupère les données depuis un fichier Excel et les organise en listes et dictionnaires.

    Cette fonction prend en argument le nom d'un fichier Excel "name". Elle extrait les données
    de ce fichier, les organise en listes et dictionnaires
    (liste, dict_cheval, dict_heure, planning_theme) et les renvoie.

    Args:
        name (str): Le nom du fichier Excel à lire.

    Returns:
        tuple: Un tuple contenant quatre éléments :
            - Une liste de tuples (heure, cheval, élève).
            - Un dictionnaire des chevaux avec leur indice et ligne.
            - Un dictionnaire des heures avec leur libellé.
            - Un dictionnaire des thèmes par heure.
    """
    logger.info("Récupération des données depuis le fichier Excel %s", name)
    workbook = load_workbook(name)
    sheet = workbook.active
    liste = []
    planning_theme = {}
    dict_heure = {}
    dict_cheval = {}
    heure_temp = {}
    Nb = 0
    for i in range(3, len(sheet["A"]) + 1):
        for j in list(range(1, len(sheet[3]) + 1))[::-1]:
            valeur_case = str(sheet.cell(row=i, column=j).value).strip()

            if valeur_case != "None":
                if i == 3:
                    dict_heure[valeur_case.upper()] = j
                    heure_temp[j] = valeur_case
                elif j == 1:
                    dict_cheval[valeur_case] = [Nb, i]
                    Nb = 0
                elif (
                    j > 1
                    and valeur_case != "MERCREDI"
                    and valeur_case != "SAMEDI"
                    and sheet.cell(row=3, column=j).value is not None
                    and sheet.cell(row=i, column=1).value is not None
                    and str(sheet.cell(row=i, column=1).value).strip() != "theme"
                ):
                    Nb += 1
                    liste.append(
                        (
                            sheet.cell(row=3, column=j).value.strip(),
                            sheet.cell(row=i, column=1).value.strip(),
                            valeur_case,
                        )
                    )
                elif (
                    j > 1 and str(sheet.cell(row=i, column=1).value).strip() == "theme"
                ):
                    planning_theme[heure_temp[j].upper()] = valeur_case
    return liste, dict_cheval, dict_heure, planning_theme


def sort_files_by_date(files):
    logger.info("Tri des fichiers par date")
    # Trie les fichiers par date (les plus récents en premier)
    sorted_files = sorted(files, key=lambda x: x[1], reverse=True)
    return sorted_files


def extract_date_from_filename(filename):
    logger.info("Extraction de la date du nom du fichier %s", filename)
    # Extrait la date du nom du fichier
    date_str = filename.split()[-1].split(".")[0]
    file_date = datetime.strptime(date_str, "%d-%m-%Y")
    return file_date


def ecrire_fichier_cavalier(liste_eleve, carte=False):
    logger.info("Écriture du fichier cavalier")
    txt = ""

    heure_trier = list(liste_eleve.keys())
    eleves = liste_eleve

    # print("ecrire_fichier_cavalier  heure_trier",heure_trier)
    logger.debug("heure_trier %s", heure_trier)
    for heure in heure_trier:
        ind = 0
        for eleve in eleves[heure]:
            if carte and ((eleve[1] >= 0 and eleve[1] <= 10) or eleve[1] == -1):
                txt += (
                    planning.liste_eleve[heure][ind][0]
                    + "/"
                    + str(planning.liste_eleve[heure][ind][1])
                    + "\r"
                )
            elif eleve[1] != -2:
                txt += eleve[0] + "/" + str(eleve[1]) + "\r"
            ind += 1
        txt += "\\heure/" + heure + "\r"
    txt += "\\Fin fichier/"
    return txt


def ecrire_fichier_cheval(dict_chevaux):
    logger.info("Écriture du fichier cheval")
    liste_cheval = []
    for cheval in dict_chevaux:
        liste_cheval.append([dict_chevaux[cheval][0], cheval])
    txt = ""
    for cheval in liste_cheval:
        txt += cheval[1] + "\r"
    return txt


def tri_heure(dictionnaire_eleve, jour):
    logger.info("Tri des heures pour le jour %s", jour)
    liste_heure_non_trier = list(dictionnaire_eleve.keys())
    # print("interface_default liste_heure_non_trier",liste_heure_non_trier)
    logger.debug("liste_heure_non_trier %s", liste_heure_non_trier)
    try:
        if jour != "Semaine":
            liste_heure_trier = sorted(liste_heure_non_trier, key=cmp_heure)
        elif jour == "Semaine":
            liste_heure_trier = sorted(liste_heure_non_trier, key=cmp_heure_semaine)
    except Exception as e:
        logger.error("Erreur lors du tri des heures : %s", e)
        return -1
    return liste_heure_trier


def lire_fichier_chevaux(path):
    logger.info("Lecture du fichier de chevaux : %s", path)
    liste = {}
    fichier = open(path, "r")
    lignes = fichier.read()
    fichier.close()
    lignes = lignes.split("\n")
    i = 0
    for ligne in lignes:
        if ligne != "":
            if ligne[2] == "\t":
                cheval = ligne[3:].strip()
            elif ligne[1] == "\t":
                cheval = ligne[2:].strip()
            else:
                cheval = ligne.strip()
            liste[cheval] = [i, planning.nb_heure(cheval)]
            i += 1
    return liste


def lire_fichier_cavalier(jour):
    logger.info("Lecture du fichier cavalier pour le jour %s", jour)
    liste = []
    liste_eleve = {}
    fichier = open(path_parametre + "liste_cavalier_" + jour + ".txt", "r")
    lignes = fichier.read()
    fichier.close()

    lignes = lignes.split("\n")
    for ligne in lignes:
        if ligne != "":
            if "\\Fin fichier/" in ligne:
                return liste_eleve
            if "\\heure/" in ligne:
                liste_eleve[ligne[7:].strip()] = liste[:]
                liste.clear()
            else:
                nom, numero = ligne.strip().split("/")
                liste.append([nom, int(numero)])


def cmp_heure(d):
    if d[1].isdigit():
        heure = d[:2]
        if d[3] == "3":
            heure += "5"
        else:
            heure += "0"
    elif d[1] == "H":
        heure = d[0]
        if d[2] == "3":
            heure += "5"
        else:
            heure += "0"
    else:
        heure = d[0]
    return int(heure)


def cmp_heure_semaine(d):
    # print("cmp_heure_semaine d",d)
    logger.debug("cmp_heure_semaine d %s", d)
    heure, jour = d.split()
    # print(heure, jour)
    logger.debug("heure %s jour %s", heure, jour)
    jours = {
        "LUNDI": 1,
        "MARDI": 2,
        "MERCREDI": 3,
        "JEUDI": 4,
        "VENDREDI": 5,
        "SAMEDI": 6,
        "DIMANCHE": 7,
    }
    # print(jours[jour], heure)
    logger.debug("jours[jour] %s heure %s", jours[jour], heure)
    return int(jours[jour]), heure


def prochain_jour(semaine, jour_actuel):
    logger.info("Calcul du prochain %s après le %s", semaine, jour_actuel)
    jours_de_la_semaine = [
        "lundi",
        "mardi",
        "mercredi",
        "jeudi",
        "vendredi",
        "samedi",
        "dimanche",
    ]
    jour_cible = jours_de_la_semaine.index(semaine)

    jours_jusquau_prochain = (jour_cible - jour_actuel.weekday() + 7) % 7
    if jours_jusquau_prochain == 0:
        jours_jusquau_prochain = 7

    return jour_actuel + timedelta(days=jours_jusquau_prochain)


def lire_parametre():
    logger.info("Lecture des paramètres")
    dict_eleve = {
        "Semaine": lire_fichier_cavalier("semaine"),
        "Mercredi": lire_fichier_cavalier("mercredi"),
        "Samedi": lire_fichier_cavalier("samedi"),
    }
    dict_cheval = {
        "Semaine": lire_fichier_chevaux(path_cheval_semaine),
        "Samedi": lire_fichier_chevaux(path_cheval),
    }
    dict_cheval["Mercredi"] = dict_cheval["Samedi"]
    # print("eleve : ",dict_eleve)
    # print("\n\n\n\n")
    # print("cheval : ",dict_cheval)
    logger.debug("dict_eleve %s", dict_eleve)
    logger.debug("dict_cheval %s", dict_cheval)

    return dict_eleve, dict_cheval