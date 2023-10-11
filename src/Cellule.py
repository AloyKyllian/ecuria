class Cellule():
    """
    La classe Cellule représente une unité de planification dans le système de gestion de planning.

    Attributes:
        jour (str): Le jour auquel cette cellule est associée.
        heure (str): L'heure à laquelle cette cellule fait référence.
        eleve (str): Le nom du cavalier associé à cette cellule.
        cheval (str): Le nom du cheval associé à cette cellule.
        ind_eleve (int): L'indice du cavalier dans la liste des cavaliers.
        ind_cheval (int): L'indice du cheval dans la liste des chevaux.

    Methods:
        set_cellule(self, heure, cheval, eleve):
            Définit les valeurs de l'heure, du cheval et du cavalier de cette cellule en une seule fois.

        set_jour(self, jour):
            Définit le jour auquel cette cellule est associée.

        set_heure(self, heure):
            Définit l'heure à laquelle cette cellule fait référence.

        set_cavalier(self, eleve, ind=1):
            Définit le nom du cavalier et son indice dans la liste des cavaliers associés à cette cellule.

        set_cheval(self, cheval, ind=1):
            Définit le nom du cheval et son indice dans la liste des chevaux associés à cette cellule.

        getCellule(self):
            Renvoie un tuple contenant les valeurs de l'heure, du cheval et du cavalier associés à cette cellule.

    """

    def __init__(self):
        self.jour = "jour"
        self.heure = "heure"
        self.eleve = "cavalier"
        self.cheval = "cheval"
        self.ind_eleve = 0
        self.ind_cheval = 0

    def set_cellule(self, heure, cheval, eleve):
        """
        Met à jour les attributs de la cellule avec de nouvelles valeurs.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            heure (str): La nouvelle heure de travail à affecter.
            cheval (str): Le nouveau nom du cheval à affecter.
            eleve (str): Le nouveau nom de l'élève à affecter.

        Returns:
            None
        """
        self.heure = heure
        self.eleve = eleve
        self.cheval = cheval

    def set_jour(self, jour):
        """
        Met à jour l'attribut "jour" de la cellule avec une nouvelle valeur.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            jour (str): Le nouveau jour à affecter.

        Returns:
            None
        """
        self.jour = jour

    def set_heure(self, heure):
        """
        Met à jour l'attribut "heure" de la cellule avec une nouvelle valeur.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            heure (str): La nouvelle heure à affecter.

        Returns:
            None
        """
        self.heure = heure

    def set_eleve(self, eleve, ind=1):
        """
        Met à jour l'attribut "eleve" de la cellule avec un nouveau nom d'élève.
        L'indice de l'élève peut également être spécifié.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            eleve (str): Le nouveau nom de l'élève à affecter.
            ind (int, optional): L'indice de l'élève. Par défaut, l'indice est 1.

        Returns:
            None
        """
        self.eleve = eleve
        self.ind_eleve = ind

    def set_cheval(self, cheval, ind=1):
        """
        Met à jour l'attribut "cheval" de la cellule avec un nouveau nom de cheval.
        L'indice du cheval peut également être spécifié.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.
            cheval (str): Le nouveau nom du cheval à affecter.
            ind (int, optional): L'indice du cheval. Par défaut, l'indice est 1.

        Returns:
            None
        """
        self.cheval = cheval
        self.ind_cheval = ind

    def getCellule(self):
        """
        Renvoie un tuple contenant l'heure, le nom du cheval et le nom de l'élève de la cellule.

        Args:
            self (object): L'instance de la classe qui appelle la méthode.

        Returns:
            tuple: Un tuple contenant l'heure, le nom du cheval et le nom de l'élève de la cellule.
        """
        return (self.heure, self.cheval, self.eleve)


if __name__ == "__main__":
    pass
