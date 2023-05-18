import customtkinter as tk
from frame import BaseFrame

class PilotFrame(BaseFrame):
    def create_widgets(self, controller):
        self.label_info = tk.CTkLabel(self, text = "Добро пожаловать, ")
        self.label_info.pack()
        self.button = tk.CTkButton(self, text="CTkButton", command=lambda: controller.switch_to_frame("PilotFrame", "AuthFrame"))
        self.button.pack()

        self.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)