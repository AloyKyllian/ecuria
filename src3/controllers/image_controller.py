from models.image_model import ImageModel

class ImageController:
    def __init__(self, app):
        self.app = app
        self.image_model = ImageModel()
        
    def set_background(self,root, image_path):
        self.image_model.set_background(root, image_path)
        
    def add_centered_image(self,root, image_path, width, height):
        return self.image_model.add_centered_image(root, image_path, width, height)
    
    def image(self,root, image_path, width, height):
        return self.image_model.image(root, image_path, width, height)
        