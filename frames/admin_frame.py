import customtkinter as tk
from frame import BaseFrame
from PIL import Image

BUTTON_RELX = 0.33

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


        #   <--------SELPANEL---------->

        self.left_select_panel = tk.CTkFrame(self, width = 300, height = 400)
        self.left_select_panel.place(rely=0.2, relx=0)

        self.button_flights = tk.CTkButton(self.left_select_panel, text="Рейсы", fg_color="#5A97C0")
        self.button_flights.place(rely=0.2, relx = BUTTON_RELX)

        self.button_directions = tk.CTkButton(self.left_select_panel, text="Направления", fg_color="#5A97C0")
        self.button_directions.place(rely=0.4, relx=BUTTON_RELX)

        self.button_planes = tk.CTkButton(self.left_select_panel, text="ВС", fg_color="#5A97C0")
        self.button_planes.place(rely=0.6, relx=BUTTON_RELX)

        self.button_planes = tk.CTkButton(self.left_select_panel, text="ВС", fg_color="#5A97C0")
        self.button_planes.place(rely=0.6, relx=BUTTON_RELX)

        #   <--------SELPANEL---------->


        self.place(relwidth=1, relheight=1)

    def change_auth_info(self, name):
        self.label_name.configure(text = name)

