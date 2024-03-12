class Jour:
    """
    La classe Jour représente un jour de la semaine.

    Attributes:
        j (str): Le nom du jour.

    Methods:
        set_mercredi(self):
            Définit le jour comme étant "Mercredi".

        set_samedi(self):
            Définit le jour comme étant "Samedi".
    """

    def __init__(self):
        self.j = ""  # Le nom du jour.

    def set_mercredi(self):
        """
        Définit le jour comme étant "Mercredi".

        Args:
            self (object): L'instance de la classe qui appelle la méthode.

        Returns:
            None
        """
        self.j = "Mercredi"

    def set_samedi(self):
        """
        Définit le jour comme étant "Samedi".

        Args:
            self (object): L'instance de la classe qui appelle la méthode.

        Returns:
            None
        """
        self.j = "Samedi"

    def set_semaine(self):
        """
        Définit le jour comme étant "Samedi".

        Args:
            self (object): L'instance de la classe qui appelle la méthode.

        Returns:
            None
        """
        self.j = "Semaine"