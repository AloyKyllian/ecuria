from Cellule import *
from Log import LoggerCounter

logger = LoggerCounter(name="Planning").logger


class Planning:
    """
    La classe Planning représente un système de gestion de planning.

    Attributes:
        historique (list): Liste des enregistrements historiques de modifications du planning.
        name_fichier (str): Le nom du fichier associé au planning.
        liste_heure (dict): Dictionnaire des heures de travail.
        cheval (dict): Dictionnaire des chevaux et de leurs heures de travail.
        liste_eleve (dict): Dictionnaire des élèves associés au planning.
        planning (list): Liste des cellules du planning actuel.
        ancien_planning (list): Liste des cellules du planning précédent.
        ancien_planning2 (list): Liste des cellules du planning antérieur au précédent.
        ancien_planning3 (list): Liste des cellules du planning antérieur à l'antérieur.
    """

    def __init__(self):
        # Liste des enregistrements historiques de modifications du planning.
        self.historique = []
        self.name_fichier = ""  # Le nom du fichier associé au planning.
        self.liste_heure = {}  # Dictionnaire des heures de travail.
        # Dictionnaire des chevaux et de leurs heures de travail.
        self.cheval = {}
        self.liste_eleve = {}  # Dictionnaire des élèves associés au planning.
        self.planning = []  # Liste des cellules du planning actuel.
        self.ancien_planning = []  # Liste des cellules du planning précédent.
        # Liste des cellules du planning antérieur au précédent.
        self.ancien_planning2 = []
        # Liste des cellules du planning antérieur à l'antérieur.
        self.ancien_planning3 = []

    def set_planning(self, dict):
        self.planning = dict

    def set_ancien_planning(self, dict):
        self.ancien_planning = dict

    def set_ancien_planning2(self, dict):
        self.ancien_planning2 = dict

    def set_ancien_planning3(self, dict):
        self.ancien_planning3 = dict

    def set_heure(self, dict):
        self.liste_heure = dict

    def set_cheval(self, dict):
        self.cheval = dict

    def set_liste_eleve(self, liste):
        self.liste_eleve = liste

    def set_nom_fichier(self, name):
        self.name_fichier = name

    def ajout(self, cellule):
        # Vérifie si une cellule avec la même heure et cheval existe déjà
        for i in self.planning:
            if (cellule.heure, cellule.cheval) == (i[0], i[1]):
                return -2
        # Vérifie la validité des attributs de la cellule
        if (
            cellule.heure == "heure"
            or cellule.cheval == "cheval"
            or cellule.eleve == "eleve"
        ):
            return -1
        # Vérifie si le cheval a déjà travaillé 4 heures
        elif len(self.cheval) != 0 and self.cheval[cellule.cheval][1] >= 4:
            return -3
        # Vérifie si la cellule existe déjà dans le planning
        elif cellule.getCellule() in self.planning:
            return -5
        else:
            # Ajoute la cellule et trie le planning
            self.planning.append(cellule.getCellule())
            self.planning.sort()
            # Met à jour le nombre d'heures travaillées par le cheval
            if cellule.cheval in self.cheval:
                self.cheval[cellule.cheval][1] += 1
            else:
                return -4

    def supprime(self, cellule):
        # Supprime la cellule si elle existe et met à jour les heures du cheval
        if cellule.getCellule() in self.planning:
            self.planning.remove(cellule.getCellule())
            if cellule.cheval in self.cheval:
                self.cheval[cellule.cheval][1] -= 1
            else:
                return -4
        else:
            return -1

    def fichier(self, jour):
        # Génère le texte du planning pour une journée donnée
        heure = 0
        a = 0
        txt = f"\tPlanning {jour}"
        self.planning.sort()
        for i in self.planning:
            if heure != i[0]:
                heure = i[0]
                txt += f"\r\n\r\n{i[0]} :\t "
            txt += f"{i[2]} avec {i[1]} | "
            if a == 1:
                a = -1
                txt += "\r\n\t    "
            a += 1
        return txt

    def index_cheval(self, cheval):
        # Retourne l'index d'un cheval
        return self.cheval[cheval][0]

    def ancient_cheval_de(self, personne, heure):
        # Renvoie les anciens chevaux d'une personne à une heure donnée
        cavalier = []
        for i in self.ancien_planning:
            if (i[2].upper(), i[0].upper()) == (personne.upper(), heure.upper()) and i[1] in self.cheval:
                cavalier.append((i[1], self.cheval[i[1]][0]))
        if len(cavalier) == 0:
            cavalier.append(("cheval", ""))
        for i in self.ancien_planning2:
            if (i[2].upper(), i[0].upper()) == (personne.upper(), heure.upper()) and i[1] in self.cheval:
                cavalier.append((i[1], self.cheval[i[1]][0]))
        if len(cavalier) == 1:
            cavalier.append(("cheval1", ""))
        for i in self.ancien_planning3:
            if (i[2].upper(), i[0].upper()) == (personne.upper(), heure.upper()) and i[1] in self.cheval:
                cavalier.append((i[1], self.cheval[i[1]][0]))
        if len(cavalier) == 2:
            cavalier.append(("cheval2", ""))
        return cavalier

    def ancient_eleve_de(self, cheval):
        # Renvoie les anciennes personnes associées à un cheval
        liste = []
        for i in self.ancien_planning:
            if i[1] == cheval:
                liste.append((i[2], i[0]))
        return liste

    def heure_travailler(self, cheval):
        # Génère les heures de travail pour un cheval
        for i in self.planning:
            if i[1] == cheval:
                yield (i[0], i[2])

    def nb_heure(self, cheval):
        # Compte le nombre d'heures de travail d'un cheval
        nbr = 0
        for i in self.planning:
            if i[1] == cheval:
                nbr += 1
        return nbr

    def append_historique(self, type, donne):
        # Limite l'historique à 100 entrées
        if len(self.historique) > 100:
            self.historique = self.historique[10:]
        self.historique.append((type, donne))


if __name__ == "__main__":
    planning = Planning()
    cellule = Cellule()

    # Initialisation des chevaux
    planning.set_cheval(
        {
            "VIOLETTE": [0, 4],
            "SURPRISE": [0, 5],
            "PEPITE": [0, 6],
            "PANDA": [0, 7],
            "PONPON": [0, 8],
            "NUAGE": [0, 9],
            "HOUSTON": [0, 10],
            "REGLISSE": [0, 11],
            "NAVARA": [0, 12],
            "P. TONNERRE": [0, 13],
            "GRISETTE": [0, 14],
            "DANETTE": [0, 15],
            "TIC": [0, 16],
            "TAC": [0, 17],
            "JAZZY": [0, 18],
            "LITTLE": [2, 19],
            "MANGO": [0, 20],
            "SORBET": [0, 21],
            "RASTA": [0, 22],
            "PEGASE": [0, 23],
            "BALKIS": [0, 24],
            "BALI": [0, 25],
            "CARA": [0, 26],
            "SAMOURAI": [0, 27],
            "FLICKA": [0, 28],
            "BANZAI": [0, 29],
            "KID ": [0, 30],
            "DIESEL": [0, 31],
            "SHEITAN": [0, 32],
            "SHAMIRA": [0, 33],
            "SINAI": [0, 34],
            "ETOILE": [0, 35],
            "VASCO": [0, 36],
            "DOMINO": [0, 37],
            "ALTAI": [0, 38],
            "ICHIBAI": [0, 39],
            "CHOGUN": [0, 40],
            "ESPOIR": [0, 41],
            "WAR": [0, 42],
            "NEVA": [0, 43],
            "PAOLA": [0, 44],
            "SEGOVIA": [0, 45],
            "ICARE": [0, 46],
            "ENZO ": [0, 47],
            "BRIOSSO": [0, 48],
        }
    )

    # Création d'une cellule
    cellule.set_cellule("19h", "VIOLETTE", "lena")

    # Ajout de la cellule et logging du résultat
    resultat_ajout = planning.ajout(cellule)
    logger.info("Résultat de l'ajout de la cellule : %s", resultat_ajout)
    logger.info("Planning actuel : %s", planning.planning)
    logger.info("Dictionnaire des chevaux : %s", planning.cheval)

    # Suppression de la cellule et logging du résultat
    resultat_supprime = planning.supprime(cellule)
    logger.info("Résultat de la suppression de la cellule : %s", resultat_supprime)
