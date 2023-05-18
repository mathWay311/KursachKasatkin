import customtkinter as tk
from frame import BaseFrame

class FrameTest(BaseFrame):
    def create_widgets(self, controller):
        self.label_info = tk.CTkLabel(self, text = "PIZDA2")
        self.label_info.pack()
        self.button = tk.CTkButton(self, text="CTkButton", command=lambda: controller.switch_to_frame("WIN2", "AUTH"))
        self.button.pack()