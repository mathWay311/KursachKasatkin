import customtkinter as tk
from frame import BaseFrame
from PIL import Image
from frames.scrollable_Frame import ScrollableFrame
from tkinter import messagebox

BUTTON_RELX = 0.33
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

class PilotFrame(BaseFrame):
    def create_widgets(self, controller):
        #   <--------BACKGROUND---------->
        background_image = tk.CTkImage(dark_image=Image.open("images/bg.jpg"), size=(2000, 2000))
        background_label = tk.CTkLabel(self, image=background_image, text="")
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #   <--------BACKGROUND---------->

        #   <--------HEADER---------->

        self.upper_rect = tk.CTkFrame(self, height=50, fg_color="transparent", border_width=1, corner_radius=0)
        self.upper_rect.pack(side=tk.TOP, fill=tk.X, anchor=tk.N)

        self.logolabel = tk.CTkLabel(self.upper_rect, text="G7 Airlines")
        self.logolabel.place(x=30, relheight=1)

        self.label_name = tk.CTkLabel(self.upper_rect, text="Иванович Иван Иванов")
        self.label_name.place(anchor=tk.NE, relx=0.7, relheight=1)

        self.button_unauth = tk.CTkButton(self.upper_rect, text="Выйти", font=("Roboto", 16), text_color="#FFFFFF",
                                          command=lambda: self.unauth())
        self.button_unauth.place(relx=0.9, relheight=1)
        #   <--------HEADER---------->

        #   <--------SELPANEL---------->


        #   <--------SELPANEL---------->

        #       <---------FIND AND ADD UPPER PANEL--------->
        self.upper_panel = tk.CTkFrame(self, height=50, fg_color="#6FB1DE", corner_radius=0)
        self.upper_panel.pack(side=tk.TOP, fill=tk.X, expand=0)


        self.button_refresh = tk.CTkButton(self.upper_panel, text="Обновить", fg_color="#6FB1DE", font=("Roboto", 20),
                                           corner_radius=0, text_color="#FFFFFF", width=40, height=40,
                                           command=lambda: controller.refresh())
        self.button_refresh.place(relx=0.5, relheight=1)


        #       <--------FIND AND ADD UPPER PANEL---------->

        #   <--------CONTENT PANEL---------->
        self.content_panel = tk.CTkFrame(self)
        self.content_panel.pack(expand = 1, fill = tk.BOTH, padx = 30, pady = 30)

        self.info_label = tk.CTkLabel(self.content_panel, text = "Нет информации о назначениях")
        self.info_label.pack(pady = 20)
        # self.content_panel.pack()


        self.place(relwidth=1, relheight=1)

    def unauth(self):
        ans = messagebox.askokcancel("Выход из аккаунта", "Вы выходите из аккаунта. Вы уверены?")
        if ans:
            self.controller.unauthorize()
