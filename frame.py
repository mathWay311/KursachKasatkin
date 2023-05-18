import customtkinter as tk

class BaseFrame(tk.CTkFrame):
    def __init__(self, root, controller):
        self.root= root
        self.controller = controller
        tk.CTkFrame.__init__(self, self.root)

    def create_widgets(self, controller):
        pass


