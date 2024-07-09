import tkinter as tk
from PIL import Image, ImageTk

class ImageModel():

    def __init__(self):
        self.path_image = "image\\"
    
    
    
    def set_background(self,root, image_path):
        image_path = self.path_image + image_path
        # Charger l'image
        original_image = Image.open(image_path)

        # Obtenir la taille de l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Redimensionner l'image pour s'adapter à l'écran
        resized_image = original_image.resize((screen_width, screen_height), Image.NEAREST)

        photo = ImageTk.PhotoImage(resized_image)

        # Configurer l'image redimensionnée comme arrière-plan de la fenêtre
        background_label = tk.Label(root, image=photo, bg="#b4b4b4")
        background_label.image = photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        return background_label, photo
    
    def add_centered_image(self,root, image_path, width, height):
        image_path = self.path_image + image_path
        # Charger l'image
        original_image = Image.open(image_path)

        # Redimensionner l'image
        resized_image = original_image.resize((width, height), Image.NEAREST)
        photo = ImageTk.PhotoImage(resized_image)

        # Configurer l'image redimensionnée comme arrière-plan de la fenêtre
        image_label = tk.Label(root, borderwidth=0,
                            image=photo, highlightthickness=0, bg="#b4b4b4")
        image_label.image = photo
        image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        return image_label
    
    def image(self,root, image_path, width, height):
        image_path = self.path_image + image_path
        
        original_image = Image.open(image_path)

        # Redimensionner l'image
        resized_image = original_image.resize((width, height), Image.NEAREST)
        photo = ImageTk.PhotoImage(resized_image)

        # Configurer l'image redimensionnée comme arrière-plan de la fenêtre
        image_label = tk.Label(root, borderwidth=0,
                            image=photo, highlightthickness=0, bg="#b4b4b4")
        image_label.image = photo
        return image_label