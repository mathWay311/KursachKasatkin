import datetime

import customtkinter as tk
from frame import BaseFrame
from tkinter import messagebox

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

        self.button_submit = tk.CTkButton(self,text="Создать", command= lambda:controller.add_direction())
        self.button_submit.pack(side = tk.RIGHT)

        self.button_cancel = tk.CTkButton(self, text="Отмена", fg_color="#FF7CA3", command=lambda : self.root.destroy())
        self.button_cancel.pack(side=tk.LEFT)

        self.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)

class AddUserFrame(BaseFrame):
    def create_widgets(self, controller):
        self.controller = controller

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


        self.button_submit = tk.CTkButton(self,text="Создать", command= lambda: self.add_prerequisites())
        self.button_submit.pack(side = tk.RIGHT)

        self.button_cancel = tk.CTkButton(self, text="Отмена", fg_color="#FF7CA3", command=lambda : self.root.destroy())
        self.button_cancel.pack(side=tk.LEFT)

        self.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)

    def add_prerequisites(self):
        if self.dropdown_roles.get() == "Пилот/Стюардесса":
            messagebox.showwarning("Предупреждение!", "Создание пилота/стюардессы вне окна ЛС допустимо только в случае утраты пользовательских данных уже существующего члена ЛС.")
        self.controller.add_user()

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

        self.label_login= tk.CTkLabel(self, text="Логин для персонального аккаунта")
        self.label_login.pack()

        self.entry_login = tk.CTkEntry(self)
        self.entry_login.pack()

        self.label_password = tk.CTkLabel(self, text="Пароль для персонального аккаунта")
        self.label_password.pack()

        self.entry_password = tk.CTkEntry(self)
        self.entry_password.pack()

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


class AddCrewFrame(BaseFrame):
    def create_widgets(self, controller):
        self.pilot_counter = 0

        self.controller = controller

        self.name_label = tk.CTkLabel(self, text="Наименование")
        self.name_label.pack()

        self.name_entry = tk.CTkEntry(self)
        self.name_entry.pack()

        self.list_of_pilots_label = tk.CTkLabel(self, text="Список пилотов на рейсе")
        self.list_of_pilots_label.pack()

        self.list_of_pilots = tk.CTkTextbox(self, state=tk.DISABLED, height=60)
        self.list_of_pilots.pack(fill = tk.X)

        self.dropdown_crewmembers = tk.CTkComboBox(self, state="readonly")
        self.dropdown_crewmembers.pack()

        self.button_add_pilot = tk.CTkButton(self, text="Добавить пилота", command=lambda: self.add_pilot())
        self.button_add_pilot.pack()

        available_crewmembers = controller.get_available_crewmembers()
        list_crewmembers_names = []
        for crewmb in available_crewmembers:
            if crewmb.type == "pilot":
                list_crewmembers_names.append(str(crewmb.id) + " " + crewmb.full_name)

        self.dropdown_crewmembers.configure(values=list_crewmembers_names)
        if len(list_crewmembers_names):
            self.dropdown_crewmembers.set(list_crewmembers_names[0])
        else:
            self.dropdown_crewmembers.set("")

        self.label_stuard = tk.CTkLabel(self, text="Стюард(-ессы)")
        self.label_stuard.pack()

        self.list_of_stuards = tk.CTkTextbox(self, state=tk.DISABLED, height=120)
        self.list_of_stuards.pack(fill=tk.X)

        self.dropdown_stuards = tk.CTkComboBox(self, state="readonly")
        self.dropdown_stuards.pack()

        self.button_add_stuard = tk.CTkButton(self, text="Добавить стюарда", command=lambda: self.add_steward())
        self.button_add_stuard.pack()
        list_stuard_names = []
        for crewmb in available_crewmembers:
            if crewmb.type == "stuard":
                list_stuard_names.append(str(crewmb.id) + " " + crewmb.full_name)

        self.dropdown_stuards.configure(values=list_stuard_names)
        if len(list_stuard_names):
            self.dropdown_stuards.set(list_stuard_names[0])
        else:
            self.dropdown_stuards.set("")

        self.button_submit = tk.CTkButton(self, text="Создать", command=lambda: self.add_crew())
        self.button_submit.pack(side=tk.RIGHT)

        self.button_cancel = tk.CTkButton(self, text="Отмена", fg_color="#FF7CA3", command=lambda: self.root.destroy())
        self.button_cancel.pack(side=tk.LEFT)

        self.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)

    def add_pilot(self):
        if self.list_of_pilots.get("1.0", tk.END).find(self.dropdown_crewmembers.get()) != -1:
            messagebox.showerror("Ошибка", "Такой пилот уже добавлен")
        else:
            self.list_of_pilots.configure(state=tk.NORMAL)
            self.list_of_pilots.insert("0.0", self.dropdown_crewmembers.get() + "\n")
            self.list_of_pilots.configure(state=tk.DISABLED)
            self.pilot_counter += 1

    def add_steward(self):
        if self.list_of_stuards.get("1.0", tk.END).find(self.dropdown_stuards.get()) != -1:
            messagebox.showerror("Ошибка", "Такой стюард уже добавлен")
        else:
            self.list_of_stuards.configure(state=tk.NORMAL)
            self.list_of_stuards.insert("0.0", self.dropdown_stuards.get() + "\n")
            self.list_of_stuards.configure(state=tk.DISABLED)

    def add_crew(self):
        if self.list_of_stuards.get("1.0", tk.END).strip() == "" and self.list_of_pilots.get("1.0", tk.END).strip() == "":
            messagebox.showerror("Ошибка", "Недопустимо создание пустого экипажа, добавьте хотя бы одного пилота!")
        elif self.list_of_stuards.get("1.0", tk.END).strip() == "":
            ans = messagebox.askokcancel("Внимание", "Вы создаёте экипаж без стюардов, вы уверены?")
            if ans:
                self.controller.add_crew()
        elif self.pilot_counter == 1:
            ans = messagebox.askokcancel("Внимание", "Вы создаёте экипаж с одним пилотом, вы уверены?")
            if ans:
                self.controller.add_crew()
        else:
            self.controller.add_crew()


class AddFlightFrame(BaseFrame):
    def create_widgets(self, controller):
        self.controller = controller

        # --------------------------------------

        self.plane_label = tk.CTkLabel(self, text="Самолёт")
        self.plane_label.pack()

        self.dropdown_planes = tk.CTkComboBox(self, state="readonly")

        available_planes = controller.get_available_planes()
        list_plane_names = []
        for plane in available_planes:
            list_plane_names.append(str(plane.id) + " " + plane.brand + " " + plane.model + " " + plane.board_number)

        self.dropdown_planes.configure(values=list_plane_names)
        if len(list_plane_names):
            self.dropdown_planes.set(list_plane_names[0])
        else:
            self.dropdown_planes.set("")
        self.dropdown_planes.pack()

        # --------------------------------------

        self.date_start_label = tk.CTkLabel(self, text="Дата начала")
        self.date_start_label.pack()

        self.date_start_entry = tk.CTkEntry(self)
        self.date_start_entry.pack()

        # --------------------------------------

        self.date_end_label = tk.CTkLabel(self, text="Дата конца")
        self.date_end_label.pack()

        self.date_end_entry = tk.CTkEntry(self)
        self.date_end_entry.pack()

        # --------------------------------------

        self.direction_label = tk.CTkLabel(self, text="Направление")
        self.direction_label.pack()

        self.dropdown_directions = tk.CTkComboBox(self, state="readonly")

        available_directions = controller.get_available_directions()
        list_directions = []
        for dir in available_directions:
            list_directions.append(str(dir.id) + " " + dir.from_ + " " + dir.to_)

        self.dropdown_directions.configure(values=list_directions)
        if len(list_directions):
            self.dropdown_directions.set(list_directions[0])
        else:
            self.dropdown_directions.set("")
        self.dropdown_directions.pack()

        # --------------------------------------

        self.crew_label = tk.CTkLabel(self, text="Экипаж")
        self.crew_label.pack()

        self.dropdown_crews = tk.CTkComboBox(self, state="readonly")

        available_crews = controller.get_available_crews()
        list_crews = []
        for crew in available_crews:
            list_crews.append(str(crew.id) + " " + crew.name)

        self.dropdown_crews.configure(values=list_crews)
        if len(list_crews):
            self.dropdown_crews.set(list_crews[0])
        else:
            self.dropdown_crews.set("")
        self.dropdown_crews.pack()

        # --------------------------------------

        self.button_submit = tk.CTkButton(self, text="Создать", command=lambda: self.add_flight())
        self.button_submit.pack(side=tk.RIGHT)

        self.button_cancel = tk.CTkButton(self, text="Отмена", fg_color="#FF7CA3", command=lambda: self.root.destroy())
        self.button_cancel.pack(side=tk.LEFT)

        self.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

    def add_flight(self):
        if self.__check_time():
            self.controller.add_flight()
        else:
            messagebox.showerror("Рейс не создан", "Произошла ошибка при введении времени. Рейс не будет создан.")

    def __check_time(self):
        date_start_str = self.date_start_entry.get()
        date_end_str = self.date_end_entry.get()
        if len(date_start_str.split(" ")) == 2:
            if len(date_start_str.split(" ")[0].split(".")) == 3:
                if len(date_start_str.split(" ")[1].split(":")) == 2:
                    if len(date_end_str.split(" ")) == 2:
                        if len(date_end_str.split(" ")[0].split(".")) == 3:
                            if len(date_end_str.split(" ")[1].split(":")) == 2:
                                start_args_date = date_start_str.split(" ")[0].split(".")
                                for i in range(len(start_args_date)):
                                    try:
                                        start_args_date[i] = int(start_args_date[i])
                                    except:
                                        messagebox.showerror("Ошибка",
                                                             "Недопустимый формат времени!\n Проверьте на соответствие шаблону (DD.MM.YYYY HH:MM)\nПроверьте, что вводите цифры!")
                                        return False
                                start_args_time = date_start_str.split(" ")[1].split(":")
                                for i in range(len(start_args_time)):
                                    try:
                                        start_args_time[i] = int(start_args_time[i])
                                    except:
                                        messagebox.showerror("Ошибка",
                                                             "Недопустимый формат времени!\n Проверьте на соответствие шаблону (DD.MM.YYYY HH:MM)\nПроверьте, что вводите цифры!")
                                        return False

                                end_args_date = date_end_str.split(" ")[0].split(".")
                                for i in range(len(end_args_date)):
                                    try:
                                        end_args_date[i] = int(end_args_date[i])
                                    except:
                                        messagebox.showerror("Ошибка",
                                                             "Недопустимый формат времени!\n Проверьте на соответствие шаблону (DD.MM.YYYY HH:MM)\nПроверьте, что вводите цифры!")
                                        return False

                                end_args_time = date_end_str.split(" ")[1].split(":")
                                for i in range(len(end_args_time)):
                                    try:
                                        end_args_time[i] = int(end_args_time[i])
                                    except:
                                        messagebox.showerror("Ошибка",
                                                             "Недопустимый формат времени!\n Проверьте на соответствие шаблону (DD.MM.YYYY HH:MM)\nПроверьте, что вводите цифры!")
                                        return False

                                date_start = datetime.datetime(year=start_args_date[2], month=start_args_date[1], day=start_args_date[0], hour=start_args_time[0], minute=start_args_time[1])
                                date_end = datetime.datetime(year=end_args_date[2], month=end_args_date[1],
                                                               day=end_args_date[0], hour=end_args_time[0],
                                                               minute=end_args_time[1])

                                print(date_start)
                                print(date_end)
                                print(date_end - date_start)
                                if ((date_start - datetime.datetime.now()).total_seconds() <= 0):
                                    messagebox.showerror("Ошибка", "Дата начала раньше текущей даты или точно совпадает с текущим временем.")
                                    return False
                                if ((date_end - date_start).total_seconds() < 1):
                                    messagebox.showerror("Ошибка", "Дата начала позже даты конца.")
                                    return False
                                if ((date_end - date_start).total_seconds() < 1800):
                                    ans = messagebox.askokcancel("Внимание", "Рейс короче 30 минут, это нормально?")
                                    if ans:
                                        return True
                                return True
        return False
