import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, master, controller, proportion_x, proportion_y):
        super().__init__(master)
        self.controller = controller

        version = 1.83
        self.label_version = tk.Label(self, text="Version " + str(version), bg='#b4b4b4')
        self.label_version.place(x=int(1395*proportion_x), y=int(780*proportion_y))
        # self.controller.get_image_controller().set_background(self, "image_fond.png")
