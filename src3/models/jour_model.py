

class JourModel():
    
    def __init__(self):
        self.jour = ""  # Le nom du jour.
    
    def get_jour(self):
        return self.jour
    
    def set_jour(self, jour):
        self.jour = jour

    def set_mercredi(self):
        """
        Définit le jour comme étant "Mercredi".

        Args:
            self (object): L'instance de la classe qui appelle la méthode.

        Returns:
            None
        """
        self.jour = "Mercredi"

    def set_samedi(self):
        """
        Définit le jour comme étant "Samedi".

        Args:
            self (object): L'instance de la classe qui appelle la méthode.

        Returns:
            None
        """
        self.jour = "Samedi"

    def set_semaine(self):
        """
        Définit le jour comme étant "Samedi".

        Args:
            self (object): L'instance de la classe qui appelle la méthode.

        Returns:
            None
        """
        self.jour = "Semaine"