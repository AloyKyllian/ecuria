import tkinter as tk

class WaitingView(tk.Frame):
    def __init__(self, parent, controller, proportion_x, proportion_y):
        super().__init__(parent)
        self.controller = controller.get_config_controller()
        self.contr_image = controller.get_image_controller()
        self.place_image()
        # self.create_widgets()
        # self.place_widget(proportion_x,proportion_y)
        


    def create_widgets(self):    
        version = 1.83  # Version actuelle du programme
        self.label_version = tk.Label(self, text="Version " + str(version), bg='#b4b4b4')
        
    def place_widget(self,proportion_x,proportion_y):
        self.label_version.place(x=int(1395*proportion_x), y=int(780*proportion_y))
        
    def place_image(self):
        self.contr_image.set_background(self, "image_fond.png")
        self.image_label = self.contr_image.add_centered_image(self, "logo.png",  169*4, 166*4)
        
    def destroy_image(self):
        self.image_label.destroy()