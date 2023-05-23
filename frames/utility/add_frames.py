import customtkinter as tk
from frame import BaseFrame

class AddDirectionFrame(BaseFrame):
    def create_widgets(self, controller):
        self.label_from = tk.CTkLabel(self, text = "Откуда: ")
        self.label_from.pack()

        self.entry_from = tk.CTkEntry(self)
        self.entry_from.pack()

        self.label_to = tk.CTkLabel(self, text="Куда: ")
        self.label_to.pack()

        self.entry_to = tk.CTkEntry(self)
        self.entry_to.pack()

        self.button_submit = tk.CTkButton(self,text="Создать", command= lambda:controller.add_direction(lambda:self.entry_from.get()))
        self.button_submit.pack(side = tk.RIGHT)

        self.button_cancel = tk.CTkButton(self, text="Отмена", fg_color="#FF7CA3", command=lambda : self.root.destroy())
        self.button_cancel.pack(side=tk.LEFT)

        self.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)

class AddUserFrame(BaseFrame):
    def create_widgets(self, controller):
        self.label_full_name = tk.CTkLabel(self, text = "ФИО")
        self.label_full_name.pack()

        self.entry_full_name= tk.CTkEntry(self)
        self.entry_full_name.pack()

        self.label_login = tk.CTkLabel(self, text="Логин")
        self.label_login.pack()

        self.entry_login = tk.CTkEntry(self)
        self.entry_login.pack()

        self.label_password = tk.CTkLabel(self, text="Пароль")
        self.label_password .pack()

        self.entry_password = tk.CTkEntry(self)
        self.entry_password.pack()



        self.label_role = tk.CTkLabel(self, text="Роль")
        self.label_role.pack()

        self.dropdown_roles = tk.CTkOptionMenu(self)
        self.dropdown_roles.configure(values=["Администратор", "Менеджер Рейсов", "Менеджер ЛС", "Менеджер ВС", "Пилот/Стюардесса"])
        self.dropdown_roles.pack()

        self.label_info = tk.CTkLabel(self, text="Доп. информация")
        self.label_info.pack()

        self.info_entry_field = tk.CTkTextbox(self, width=500, height=100)
        self.info_entry_field.pack()


        self.button_submit = tk.CTkButton(self,text="Создать", command= lambda:controller.add_user())
        self.button_submit.pack(side = tk.RIGHT)

        self.button_cancel = tk.CTkButton(self, text="Отмена", fg_color="#FF7CA3", command=lambda : self.root.destroy())
        self.button_cancel.pack(side=tk.LEFT)

        self.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)

class AddCrewMemberFrame(BaseFrame):
    def create_widgets(self, controller):
        self.label_types = tk.CTkLabel(self, text="Тип")
        self.label_types.pack()

        self.dropdown_types = tk.CTkOptionMenu(self)
        self.dropdown_types.configure(
            values=["Пилот", "Стюардесса"])
        self.dropdown_types.pack()

        self.label_full_name = tk.CTkLabel(self, text="ФИО")
        self.label_full_name.pack()

        self.entry_full_name= tk.CTkEntry(self)
        self.entry_full_name.pack()

        self.label_info = tk.CTkLabel(self, text="Доп. информация")
        self.label_info.pack()

        self.info_entry_field = tk.CTkTextbox(self, width=500, height=100)
        self.info_entry_field.pack()

        self.label_pic = tk.CTkLabel(self, text="Путь до картинки в базе")
        self.label_pic.pack()

        self.entry_picpath = tk.CTkEntry(self)
        self.entry_picpath.pack()

        self.label_flytype = tk.CTkLabel(self, text="Летает на типе")
        self.label_flytype .pack()

        self.entry_flytype = tk.CTkEntry(self)
        self.entry_flytype.pack()

        self.button_submit = tk.CTkButton(self, text="Создать", command=lambda: controller.add_crewmember())
        self.button_submit.pack(side=tk.RIGHT)

        self.button_cancel = tk.CTkButton(self, text="Отмена", fg_color="#FF7CA3", command=lambda: self.root.destroy())
        self.button_cancel.pack(side=tk.LEFT)

        self.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)


class AddPlaneFrame(BaseFrame):
    def create_widgets(self, controller):
        self.label_brand = tk.CTkLabel(self, text="Производитель")
        self.label_brand.pack()

        self.dropdown_brand = tk.CTkOptionMenu(self)
        self.dropdown_brand.configure(values=["Boeing", "Ту", "Airbus"], command=self.optionmenu_callback)
        self.dropdown_brand.pack()

        self.label_type = tk.CTkLabel(self, text="Тип")
        self.label_type.pack()

        self.dropdown_type = tk.CTkOptionMenu(self)
        self.dropdown_type .pack()

        self.label_boardnum = tk.CTkLabel(self, text="Бортовой номер")
        self.label_boardnum.pack()

        self.entry_boardnum = tk.CTkEntry(self, placeholder_text="RA-")
        self.entry_boardnum.pack()

        self.label_pic = tk.CTkLabel(self, text="Путь до картинки в базе")
        self.label_pic.pack()

        self.entry_picpath = tk.CTkEntry(self)
        self.entry_picpath.pack()

        self.button_submit = tk.CTkButton(self, text="Создать", command=lambda: controller.add_plane())
        self.button_submit.pack(side=tk.RIGHT)

        self.button_cancel = tk.CTkButton(self, text="Отмена", fg_color="#FF7CA3", command=lambda: self.root.destroy())
        self.button_cancel.pack(side=tk.LEFT)

        self.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)

    def optionmenu_callback(self, choice):
        if choice == "Boeing":
            self.dropdown_type.configure(values=["737MAX8", "737-800", "747"])
        if choice == "Ту":
            self.dropdown_type.configure(values=["154Б", "154М", "134"])
        if choice == "Airbus":
            self.dropdown_type.configure(values=["A320", "A320neo", "A380"])