import customtkinter as tk
from frame import BaseFrame

class AuthFrame(BaseFrame):
    def create_widgets(self, controller):
        self.label_info = tk.CTkLabel(self, text = "G7 Airlines - Авторизация")
        self.label_info.pack()

        self.label_login = tk.CTkLabel(self, text = "Логин:")
        self.label_login.pack()

        self.field_login = tk.CTkEntry(self)
        self.field_login.pack()

        self.label_password = tk.CTkLabel(self, text="Пароль:")
        self.label_password.pack()

        self.field_password = tk.CTkEntry(self)
        self.field_password.pack()

        self.button = tk.CTkButton(self, text="Войти", command = lambda : controller.switch_to_frame("AuthFrame","PilotFrame"))
        self.button.pack(pady = 10)


        self.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)