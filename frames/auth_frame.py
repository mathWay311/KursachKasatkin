import customtkinter as tk
from frame import BaseFrame

class AuthFrame(BaseFrame):
    def create_widgets(self, controller):
        self.label_info = tk.CTkLabel(self, text = "PIZDA")
        self.label_info.pack()
        self.button = tk.CTkButton(self, text="CTkButton", command = lambda : controller.switch_to_frame("AUTH","WIN2"))
        self.button.pack()
        self.pack()