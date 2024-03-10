from Cellule import *


class Planning():
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

    Methods:
        set_planning(self, dict):
            Définit le planning actuel avec un nouveau dictionnaire.

        set_ancien_planning(self, dict):
            Définit le planning précédent avec un nouveau dictionnaire.

        set_ancien_planning2(self, dict):
            Définit le planning antérieur au précédent avec un nouveau dictionnaire.

        set_ancien_planning3(self, dict):
            Définit le planning antérieur à l'antérieur avec un nouveau dictionnaire.

        set_heure(self, dict):
            Met à jour le dictionnaire des heures de travail.

        set_cheval(self, dict):
            Met à jour le dictionnaire des chevaux associés au planning.

        set_liste_eleve(self, liste):
            Met à jour la liste des élèves associés au planning.

        set_nom_fichier(self, name):
            Met à jour le nom de fichier associé au planning.

        ajout(self, cellule):
            Ajoute une cellule au planning en effectuant des vérifications préliminaires.

        supprime(self, cellule):
            Supprime une cellule du planning et met à jour les données associées.

        fichier(self, jour):
            Génère un fichier texte représentant le planning pour une journée donnée.

        index_cheval(self, cheval):
            Retourne l'index d'un cheval dans le dictionnaire des chevaux.

        ancient_cheval_de(self, personne, heure):
            Renvoie les anciens chevaux d'une personne à une heure donnée.

        ancient_eleve_de(self, cheval):
            Renvoie les anciennes personnes associées à un cheval.

        heure_travailler(self, cheval):
            Renvoie les heures de travail d'un cheval.

        nb_heure(self, cheval):
            Renvoie le nombre d'heures de travail d'un cheval.

        append_historique(self, type, donne):
            Ajoute un enregistrement à l'historique des modifications du planning.
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
        """
        Met à jour le planning actuel avec un nouveau dictionnaire fourni en argument.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            dict (dict): Le nouveau dictionnaire représentant le planning actuel.

        Returns:
            None
        """
        self.planning = dict

    def set_ancien_planning(self, dict):
        """
        Met à jour le planning précédent avec un nouveau dictionnaire fourni en argument.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            dict (dict): Le nouveau dictionnaire représentant le planning précédent.

        Returns:
            None
        """
        self.ancien_planning = dict

    def set_ancien_planning2(self, dict):
        """
        Met à jour le planning précédent 2 avec un nouveau dictionnaire fourni en argument.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            dict (dict): Le nouveau dictionnaire représentant le planning précédent 2.

        Returns:
            None
        """
        self.ancien_planning2 = dict

    def set_ancien_planning3(self, dict):
        """
        Met à jour le planning précédent 3 avec un nouveau dictionnaire fourni en argument.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            dict (dict): Le nouveau dictionnaire représentant le planning précédent 3.

        Returns:
            None
        """
        self.ancien_planning3 = dict

    def set_heure(self, dict):
        """
        Met à jour le dictionnaire des heures de travail de la classe Planning.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            dict (dict): Le nouveau dictionnaire des heures de travail à affecter.

        Returns:
            None
        """
        self.liste_heure = dict

    def set_cheval(self, dict):
        """
        Met à jour le dictionnaire des chevaux de la classe Planning.

        Cette méthode permet de mettre à jour le dictionnaire des chevaux de la classe
        Planning avec un nouveau dictionnaire fourni en argument.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            dict (dict): Le nouveau dictionnaire des chevaux à affecter.

        Returns:
            None

        Exemple d'utilisation:
        planning = Planning()
        nouveaux_chevaux = {"Cheval A": [0,4], "Cheval B": [1,5]}
        planning.set_cheval(nouveaux_chevaux)
        """
        self.cheval = dict

    def set_liste_eleve(self, liste):
        """
        Met à jour la liste des élèves de la classe Planning.

        Cette méthode permet de mettre à jour la liste des élèves de la classe Planning
        avec une nouvelle liste fournie en argument.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            liste (list): La nouvelle liste des élèves à affecter.

        Returns:
            None
        """
        self.liste_eleve = liste

    def set_nom_fichier(self, name):
        """
        Met à jour le nom de fichier de la classe Planning.

        Cette méthode permet de mettre à jour le nom de fichier associé à la classe
        Planning avec un nouveau nom fourni en argument.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            name (str): Le nouveau nom de fichier à affecter.

        Returns:
            None

        Exemple d'utilisation:
        planning = Planning()
        nouveau_nom_fichier = "mon_planning.csv"
        planning.set_nom_fichier(nouveau_nom_fichier)
        """
        self.name_fichier = name

    def ajout(self, cellule):
        """
        Ajoute une cellule au planning, en effectuant des vérifications préliminaires.

        Cette méthode permet d'ajouter une cellule au planning actuel, mais elle effectue
        plusieurs vérifications pour s'assurer de la validité de l'opération. Elle renvoie
        des codes d'erreur spécifiques en cas d'échec des vérifications.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            cellule (object): L'objet représentant la cellule à ajouter.

        Returns:
            int: Un code d'erreur spécifique ou 0 si l'ajout est réussi.

        Les codes d'erreur possibles sont :
        -1 : Les attributs de la cellule ne sont pas valides.
        -2 : Une cellule avec la même combinaison (heure, cheval) existe déjà dans le planning.
        -3 : Le cheval a déjà travaillé 4 heures.
        -4 : Le cheval n'est pas dans la liste des chevaux autorisés.

        Note:
        - La méthode trie automatiquement le planning après l'ajout.
        - Elle met à jour le nombre d'heures travaillées par le cheval si nécessaire.

        Exemple d'utilisation:
        planning = Planning()
        cellule = Cellule(heure="10:00", cheval="Cheval A", eleve="Élève B")
        resultat = planning.ajout(cellule)
        if resultat == 0:
            print("Cellule ajoutée avec succès.")
        else:
            print(f"Erreur {resultat}: L'ajout de la cellule a échoué.")
        """
        for i in self.planning:
            if (cellule.heure, cellule.cheval) == (i[0], i[1]):
                return -2
        if cellule.heure == "heure" or cellule.cheval == "cheval" or cellule.eleve == "eleve":
            return -1
        elif len(self.cheval) != 0 and self.cheval[cellule.cheval][0] >= 4:
            return -3
        elif cellule.getCellule() in self.planning:
            return -5
        else:
            self.planning.append(cellule.getCellule())
            self.planning.sort()
            if cellule.cheval in self.cheval:
                self.cheval[cellule.cheval][0] += 1
            else:
                return -4

    def supprime(self, cellule):
        """
        Supprime une cellule du planning et met à jour les données associées.

        Cette méthode prend en argument une cellule à supprimer du planning. Si la cellule
        existe dans le planning, elle la retire et met à jour le nombre d'heures travaillées
        par le cheval associé. Si la cellule n'est pas trouvée dans le planning, elle renvoie
        le code d'erreur -1. Si le cheval de la cellule n'existe pas dans le dictionnaire des
        chevaux, elle renvoie le code d'erreur -4.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            cellule (object): L'objet représentant la cellule à supprimer du planning.

        Returns:
            int: 0 si la suppression est réussie, -1 si la cellule n'est pas trouvée,
                -4 si le cheval de la cellule n'existe pas dans le dictionnaire des chevaux.

        Exemple d'utilisation:
        planning = Planning()
        cellule_a_supprimer = Cellule(heure="10:00", cheval="Cheval A", eleve="Élève B")
        resultat = planning.supprime(cellule_a_supprimer)
        if resultat == 0:
            print("Cellule supprimée avec succès.")
        elif resultat == -1:
            print("Erreur -1 : La cellule n'a pas été trouvée dans le planning.")
        elif resultat == -4:
            print("Erreur -4 : Le cheval de la cellule n'existe pas dans le dictionnaire des chevaux.")
        """
        if cellule.getCellule() in self.planning:
            self.planning.remove(cellule.getCellule())
            if cellule.cheval in self.cheval:
                self.cheval[cellule.cheval][0] -= 1
            else:
                return -4
        else:
            return -1

    def fichier(self, jour):
        """
        Génère un fichier texte représentant le planning pour une journée donnée.

        Cette méthode génère un fichier texte qui représente le planning pour une
        journée spécifiée. Le fichier contiendra les informations sur les heures de travail,
        les chevaux et les élèves pour cette journée.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            jour (str): La journée pour laquelle générer le planning (par exemple, "Lundi").

        Returns:
            str: Une chaîne de caractères représentant le planning pour la journée.

        Exemple d'utilisation:
        planning = Planning()
        jour_a_generer = "Lundi"
        planning_texte = planning.fichier(jour_a_generer)
        with open(f"{jour_a_generer}_planning.txt", "w") as fichier:
            fichier.write(planning_texte)
        """
        heure = 0
        a = 0
        txt = ""
        txt = (f"\tPlanning {jour}")
        self.planning.sort()
        for i in self.planning:
            if heure != i[0]:
                heure = i[0]
                txt = txt + (f"\r\n\r\n{i[0]} :\t ")
            txt = txt + (f"{i[2]} avec {i[1]} | ")
            if a == 1:
                a = -1
                txt += "\r\n\t    "
            a += 1
        return txt

    def index_cheval(self, cheval):
        """
        Retourne l'index d'un cheval dans le dictionnaire des chevaux.

        Cette méthode prend en argument le nom d'un cheval et retourne l'index associé
        à ce cheval dans le dictionnaire des chevaux. L'index est calculé en soustrayant 4
        à la deuxième valeur du tableau associatif du cheval.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            cheval (str): Le nom du cheval dont on souhaite obtenir l'index.

        Returns:
            int: L'index du cheval dans le dictionnaire des chevaux.

        Exemple d'utilisation:
        planning = Planning()
        nom_du_cheval = "Cheval A"
        index = planning.index_cheval(nom_du_cheval)
        print(f"L'index de {nom_du_cheval} est {index}.")
        """
        return self.cheval[cheval][1]-4

    def ancient_cheval_de(self, personne, heure):
        """
        Renvoie les anciens chevaux d'une personne à une heure donnée.

        Cette méthode prend en argument le nom d'une personne ("personne") et une heure
        ("heure"). Elle recherche dans les listes d'anciens (ancien_liste, ancien_liste2,
        ancien_liste3) pour trouver les chevaux associés à cette personne à cette heure.
        Les résultats sont retournés sous forme de liste de tuples contenant le nom du cheval
        et son index.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            personne (str): Le nom de la personne dont on recherche les anciens chevaux.
            heure (int): L'heure à laquelle on souhaite rechercher les anciens chevaux.

        Yields:
            list of tuple: Une liste de tuples contenant le nom du cheval et son index.

        Exemple d'utilisation:
        planning = Planning()
        personne = "Élève B"
        heure = 10
        anciens_chevaux = list(planning.ancient_cheval_de(personne, heure))
        print(f"Anciens chevaux de {personne} à {heure}h : {anciens_chevaux}")
        """
        cavalier = []
        for i in self.ancien_planning:
            if (i[2].upper(), i[0].upper()) == (personne.upper(), heure.upper()) and i[1] in self.cheval:
                cavalier.append((i[1], self.cheval[i[1]][1]-4))
        if len(cavalier) == 0:
            cavalier.append(("cheval", ""))
        for i in self.ancien_planning2:
            if (i[2].upper(), i[0].upper()) == (personne.upper(), heure.upper()) and i[1] in self.cheval:
                cavalier.append((i[1], self.cheval[i[1]][1]-4))
        if len(cavalier) == 1:
            cavalier.append(("cheval1", ""))
        for i in self.ancien_planning3:
            if (i[2].upper(), i[0].upper()) == (personne.upper(), heure.upper()) and i[1] in self.cheval:
                cavalier.append((i[1], self.cheval[i[1]][1]-4))
        if len(cavalier) == 2:
            cavalier.append(("cheval2", ""))
        return cavalier

    def ancient_eleve_de(self, cheval):
        """
        Renvoie les anciennes personnes associées à un cheval.

        Cette méthode prend en argument le nom d'un cheval ("cheval") et recherche dans
        la liste d'anciens (ancien_liste) pour trouver les personnes associées à ce cheval.
        Les résultats sont retournés sous forme de liste de tuples contenant le nom de la
        personne et l'heure associée.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            cheval (str): Le nom du cheval dont on recherche les anciennes personnes.

        Returns:
            list of tuple: Une liste de tuples contenant le nom de la personne et l'heure.

        Exemple d'utilisation:
        planning = Planning()
        cheval = "Cheval A"
        anciennes_personnes = planning.ancient_eleve_de(cheval)
        print(f"Anciennes personnes de {cheval} : {anciennes_personnes}")
        """
        liste = []
        for i in self.ancien_planning:
            if i[1] == cheval:
                liste.append((i[2], i[0]))
        return liste

    def heure_travailler(self, cheval):
        """
        Renvoie les heures de travail d'un cheval.

        Cette méthode prend en argument le nom d'un cheval ("cheval") et parcourt le planning
        pour trouver les heures de travail associées à ce cheval. Les résultats sont renvoyés
        sous forme de générateur de tuples contenant l'heure et le nom de la personne.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            cheval (str): Le nom du cheval dont on souhaite obtenir les heures de travail.

        Yields:
            tuple: Un tuple contenant l'heure et le nom de la personne.

        Exemple d'utilisation:
        planning = Planning()
        cheval = "Cheval A"
        heures_travail = list(planning.heure_travailler(cheval))
        print(f"Heures de travail de {cheval} : {heures_travail}")
        """
        for i in self.planning:
            if i[1] == cheval:
                yield (i[0], i[2])

    def nb_heure(self, cheval):
        """
        Renvoie le nombre d'heures de travail d'un cheval.

        Cette méthode prend en argument le nom d'un cheval ("cheval") et parcourt le planning
        pour compter le nombre d'heures de travail associées à ce cheval.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            cheval (str): Le nom du cheval dont on souhaite obtenir le nombre d'heures de travail.

        Returns:
            int: Le nombre d'heures de travail du cheval.

        Exemple d'utilisation:
        planning = Planning()
        cheval = "Cheval A"
        nombre_heures = planning.nb_heure(cheval)
        print(f"Nombre d'heures de travail de {cheval} : {nombre_heures}")
        """
        nbr = 0
        for i in self.planning:
            if i[1] == cheval:
                nbr = nbr+1
        return nbr

    def append_historique(self, type, donne):
        """
        Ajoute une entrée à l'historique de planning.

        Cette méthode permet d'ajouter une entrée à l'historique de planning de la classe.
        L'historique conserve un historique des actions effectuées sur le planning, telles que
        les ajouts, les suppressions ou d'autres modifications importantes.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            type (str): Le type d'action effectuée (par exemple, "Ajout", "Suppression").
            donne (tuple): Les données associées à l'action, généralement sous forme de tuple.

        Returns:
            None

        Notes:
            - Si la longueur de l'historique dépasse 100 entrées, les 10 entrées les plus anciennes
              sont supprimées pour maintenir une taille maximale de 100.
            - Chaque entrée d'historique est représentée par un tuple contenant le type d'action
              et les données associées.

        Exemple d'utilisation:
        planning = Planning()
        type_action = "Ajout"
        donnees = ("10:00", "Cheval A", "Élève B")
        planning.append_historique(type_action, donnees)
        """
        if len(self.historique) > 100:
            # Si l'historique dépasse 100 entrées, supprimer les 10 entrées les plus anciennes.
            self.historique = self.historique[10:]
        self.historique.append((type, donne))


if __name__ == "__main__":

    planning = Planning()
    cellule = Cellule()
    planning.set_cheval({'VIOLETTE': [0, 4], 'SURPRISE': [0, 5], 'PEPITE': [0, 6], 'PANDA': [0, 7], 'PONPON': [0, 8], 'NUAGE': [0, 9], 'HOUSTON': [0, 10], 'REGLISSE': [0, 11], 'NAVARA': [0, 12], 'P. TONNERRE': [0, 13], 'GRISETTE': [0, 14], 'DANETTE': [0, 15], 'TIC': [0, 16], 'TAC': [0, 17], 'JAZZY': [0, 18], 'LITTLE': [2, 19], 'MANGO': [0, 20], 'SORBET': [0, 21], 'RASTA': [0, 22], 'PEGASE': [0, 23], 'BALKIS': [0, 24], 'BALI': [0, 25], 'CARA': [
        0, 26], 'SAMOURAI': [0, 27], 'FLICKA': [0, 28], 'BANZAI': [0, 29], 'KID ': [0, 30], 'DIESEL': [0, 31], 'SHEITAN': [0, 32], 'SHAMIRA': [0, 33], 'SINAI': [0, 34], 'ETOILE': [0, 35], 'VASCO': [0, 36], 'DOMINO': [0, 37], 'ALTAI': [0, 38], 'ICHIBAI': [0, 39], 'CHOGUN': [0, 40], 'ESPOIR': [0, 41], 'WAR': [0, 42], 'NEVA': [0, 43], 'PAOLA': [0, 44], 'SEGOVIA': [0, 45], 'ICARE': [0, 46], 'ENZO ': [0, 47], 'BRIOSSO': [0, 48]})
    cellule.set_cellule("19h", "VIOLETTE", "lena")
    print(planning.ajout(cellule))
    print(planning.planning)
    print(planning.cheval)
    print(planning.supprime(cellule))
