import customtkinter as tk
from frame import BaseFrame

class TestFrame(BaseFrame):
    def create_widgets(self, controller):
        self.upper_rect = tk.CTkFrame(self, height = 50, fg_color = "#96F2FC")
        self.upper_rect.place(relwidth=1)

        self.logolabel = tk.CTkLabel(self.upper_rect, text="G7 TEST",  fg_color="#000000")
        self.logolabel.place(x = 30, relheight= 1)

        self.auth_rect = tk.CTkFrame(self,width=200,height=200,fg_color = "#96F2FC")
        self.auth_rect.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        self.place(relwidth=1, relheight=1)
