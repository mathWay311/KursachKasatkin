import customtkinter as tk
from frame import BaseFrame
from PIL import Image


class AuthFrame(BaseFrame):
    def create_widgets(self, controller):
        #   <--------BACKGROUND---------->
        background_image = tk.CTkImage(dark_image=Image.open("images/bg.jpg"), size=(2000, 2000))
        background_label = tk.CTkLabel(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #   <--------BACKGROUND---------->

        #   <--------HEADER---------->
        self.upper_rect = tk.CTkFrame(self, height=50, fg_color="transparent")
        self.upper_rect.place(relwidth=1)

        self.logolabel = tk.CTkLabel(self.upper_rect, text="G7 Airlines")
        self.logolabel.place(x=30, relheight=1)
        #   <--------HEADER---------->


        self.auth_rect = tk.CTkFrame(self, width = 300)


        self.label_info = tk.CTkLabel(self.auth_rect, text = "G7 Airlines - Авторизация", font = ("Roboto", 16))
        self.label_info.pack(padx=10, pady = 10)

        self.label_login = tk.CTkLabel(self.auth_rect, text = "Логин:")
        self.label_login.pack()

        self.field_login = tk.CTkEntry(self.auth_rect)
        self.field_login.pack()

        self.label_password = tk.CTkLabel(self.auth_rect, text="Пароль:")
        self.label_password.pack()

        self.field_password = tk.CTkEntry(self.auth_rect, show="*")
        self.field_password.pack()

        self.button = tk.CTkButton(self.auth_rect, text="Войти", command = lambda : controller.authframe_login_submit())
        self.button.pack(pady = 20)



        self.auth_rect.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        self.place(relwidth=1, relheight=1)