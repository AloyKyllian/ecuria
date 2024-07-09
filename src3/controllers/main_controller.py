
from controllers.config_controller import ConfigController
from controllers.principal_controller import PrincipalController
from controllers.image_controller import ImageController

class MainController:
    def __init__(self, app):
        self.app = app

        # Initialisation des contrôleurs spécifiques pour chaque vue
        self.config_controller = ConfigController(self)
        self.principal_controller = PrincipalController(self)
        self.image_controller = ImageController(self)
        
    # Méthodes pour diriger vers les différentes vues (frames)
    # def show_config_view(self):
    #     self.app.show_frame("ConfigView")

    # def show_principal_view(self):
    #     self.app.show_frame("PrincipalView")
        
    # Méthodes pour les actions globales ou partagées entre les vues
    # def global_action(self):
    #     print("Action globale")

    # def global_function(self):
    #     print("Fonction globale")
        
    def get_config_controller(self):
        return self.config_controller

    def get_principal_controller(self):
        return self.principal_controller
    
    def get_image_controller(self):
        return self.image_controller
    
    