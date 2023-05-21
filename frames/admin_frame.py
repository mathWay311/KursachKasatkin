import customtkinter as tk
from frame import BaseFrame
from PIL import Image

class AdminFrame(BaseFrame):
    def create_widgets(self, controller):
        #   <--------BACKGROUND---------->
        background_image = tk.CTkImage(dark_image=Image.open("images/bg.jpg"), size=(2000, 2000))
        background_label = tk.CTkLabel(self, image=background_image, text = "")
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #   <--------BACKGROUND---------->

        #   <--------HEADER---------->
        self.upper_rect = tk.CTkFrame(self, height=50, fg_color="transparent")
        self.upper_rect.place(relwidth=1)

        self.logolabel = tk.CTkLabel(self.upper_rect, text="G7 Airlines")
        self.logolabel.place(x=30, relheight=1)

        self.label_name = tk.CTkLabel(self.upper_rect, text="Иванович Иван Иванов")
        self.label_name.place(anchor = tk.NE, relx=0.86, relheight = 1)


        #   <--------HEADER---------->

        self.place(relwidth=1, relheight=1)

