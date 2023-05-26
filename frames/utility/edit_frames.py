import datetime

import customtkinter as tk
from frame import BaseFrame
from tkinter import messagebox
from database.models.models import *

class EditDirectionFrame(BaseFrame):
    def __init__(self, root, controller, dir_model:DirectionModel):
        super().__init__(root, controller)
        self.model = dir_model
        self.root = root
        self.controller = controller

    def create_widgets(self, controller):
        self.label_from = tk.CTkLabel(self.root, text = "Откуда: ")
        self.label_from.pack()

        self.entry_from = tk.CTkEntry(self.root)
        self.entry_from.insert(0, self.model.from_)
        self.entry_from.pack()

        self.label_to = tk.CTkLabel(self.root, text="Куда: ")
        self.label_to.pack()

        self.entry_to = tk.CTkEntry(self.root)
        self.entry_to.insert(0, self.model.to_)
        self.entry_to.pack()

        self.button_submit = tk.CTkButton(self.root,text="Изменить", command= lambda:self.controller.edit_direction())
        self.button_submit.pack(side = tk.RIGHT)

        self.button_cancel = tk.CTkButton(self.root, text="Отмена", fg_color="#FF7CA3", command=lambda : self.root.destroy())
        self.button_cancel.pack(side=tk.LEFT)


class EditUserFrame(BaseFrame):
    def __init__(self, root, controller, dir_model:UserModel):
        super().__init__(root, controller)
        self.model = dir_model
        self.root = root
        self.controller = controller
        self.roles_dict_temp = {
            "Администратор": "admin", "Менеджер Рейсов": "flight_manager", "Менеджер ЛС": "crew_manager",
            "Менеджер ВС": "plane_manager", "Пилот/Стюардесса": "pilot"
        }
        self.roles_dict =  {y: x for x, y in self.roles_dict_temp.items()}

    def create_widgets(self, controller):
        self.label_full_name = tk.CTkLabel(self.root, text="ФИО")
        self.label_full_name.pack()

        self.entry_full_name = tk.CTkEntry(self.root)
        self.entry_full_name.insert(0, self.model.full_name)
        self.entry_full_name.pack()

        self.label_login = tk.CTkLabel(self.root, text="Логин")
        self.label_login.pack()

        self.entry_login = tk.CTkEntry(self.root)
        self.entry_login.insert(0, self.model.login)
        self.entry_login.pack()

        self.label_password = tk.CTkLabel(self.root, text="Пароль")
        self.label_password.pack()

        self.entry_password = tk.CTkEntry(self.root)
        self.entry_password.insert(0, self.model.password)
        self.entry_password.pack()

        self.label_role = tk.CTkLabel(self, text="Роль")
        self.label_role.pack()

        self.dropdown_roles = tk.CTkOptionMenu(self.root)
        self.dropdown_roles.configure(
            values=["Администратор", "Менеджер Рейсов", "Менеджер ЛС", "Менеджер ВС", "Пилот/Стюардесса"])
        self.dropdown_roles.set(self.roles_dict[self.model.role])
        self.dropdown_roles.pack()

        self.label_info = tk.CTkLabel(self.root, text="Доп. информация")
        self.label_info.pack()

        self.info_entry_field = tk.CTkTextbox(self.root, width=500, height=100)
        self.info_entry_field.insert("1.0", self.model.info)
        self.info_entry_field.pack()

        self.button_submit = tk.CTkButton(self.root, text="Изменить", command=lambda: self.edit_prerequesite() )
        self.button_submit.pack(side=tk.RIGHT)

        self.button_cancel = tk.CTkButton(self.root, text="Отмена", fg_color="#FF7CA3", command=lambda: self.root.destroy())
        self.button_cancel.pack(side=tk.LEFT)

    def edit_prerequesite(self):
        ans, ans2 = True, True
        flag_selfedit = False
        flag_adminedit = False
        if str(self.controller.id) == str(self.model.id):
            flag_selfedit = True
            ans = messagebox.askokcancel("Внимание", "Вы редактируете свой аккаунт. Вам потребуется совершить повторную авторизацию")
        if str(self.model.role == "admin"):
            flag_adminedit = True
            ans2 = messagebox.askokcancel("Внимание",
                                          "Вы редактируете аккаунт администратора. Вы уверены?")

        if not flag_adminedit and not flag_selfedit:
            self.controller.edit_user()

        flag_reauth = False
        if flag_selfedit:
            flag_reauth = True

        if ans and ans2:
            self.controller.edit_user()

        if flag_reauth:
            self.controller.unauthorize()




