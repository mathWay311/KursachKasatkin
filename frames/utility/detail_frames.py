import customtkinter as tk

from database.models.models import *
from frame import BaseFrame
from PIL import Image
from database.models import *
from tkinter import messagebox



def convert_from_plain(text):
    text = text.replace(r"\\n", "\n")
    return text

class PlaneDetail():
    def __init__(self, plane_model : PlaneModel):
        self.plane_model = plane_model

    def create_widgets(self, root, controller):
        plane_logo_img = tk.CTkImage(dark_image=Image.open("database/images/" + self.plane_model.imgPath), size=(300, 300))
        plane_logo = tk.CTkLabel(root, image=plane_logo_img, text="")
        plane_logo.place(x = 30)

        plane_brand_label = tk.CTkLabel(root, text=self.plane_model.brand + " " + self.plane_model.model + " " + self.plane_model.board_number, font=("Roboto", 15))
        plane_brand_label.place(x=340)

        label_additional_info = tk.CTkLabel(root,
                                            text=self.plane_model.print_status(),
                                            font=("Roboto", 14), justify=tk.LEFT)
        label_additional_info.place(x=340, y = 30)
        if self.plane_model.isRepaired:
            label_info = tk.CTkLabel(root, text="Неисправность", font=("Roboto", 15))
            self.malfunction_entry_field = tk.CTkTextbox(root, width=500, height=300)
            self.malfunction_entry_field.insert("1.0", convert_from_plain(self.plane_model.malfunction))
            self.malfunction_entry_field.configure(state="disabled")
            self.malfunction_entry_field.place(x=30, y=380)
            self.button_retrieve = tk.CTkButton(root,text="Вернуть с ремонта", command=lambda: controller.retrieve_plane_from_repair(self.plane_model.id))
            self.button_retrieve.place(x=30, y= 680)
        else:
            label_info = tk.CTkLabel(root, text="Опишите неисправность", font=("Roboto", 15))
            self.malfunction_entry_field = tk.CTkTextbox(root, width = 500, height= 300)
            self.malfunction_entry_field.place(x = 30, y = 380)
            self.button_place_on_repair = tk.CTkButton(root, text="Отправить на ремонт", command=lambda: controller.place_plane_on_repair(self.plane_model.id))
            self.button_place_on_repair.place(x=30, y= 680)
        self.button_delete = tk.CTkButton(root, text="Удалить самолёт", command=lambda: controller.delete_item_by_id("planes",self.plane_model.id), fg_color="#FF7CA3")
        self.button_delete.place(x=30,y=750)

        label_info.place(x = 30, y = 350)


class CrewmemberDetail():
    def __init__(self, crewmember_model : CrewmemberModel):
        self.crewmember_model = crewmember_model

    def create_widgets(self, root, controller):
        crewmember_logo_img = tk.CTkImage(dark_image=Image.open("database/images/" + self.crewmember_model.imagePath), size=(300, 300))
        crewmember_logo = tk.CTkLabel(root, image=crewmember_logo_img, text="")
        crewmember_logo.place(x = 30)

        type_text = "Неизвестный тип. Свяжитесь с администратором, если это ошибка"
        if self.crewmember_model.type == "pilot":
            type_text = "Пилот(-есса)"
        elif self.crewmember_model.type == "stuard":
            type_text = "Стюард(-есса)"

        crewmember_name_info = tk.CTkLabel(root, text=self.crewmember_model.full_name, font=("Roboto", 15))
        crewmember_name_info.place(x=340)

        add_info_text = type_text + "\n" + self.crewmember_model.print_status() + "\n" + self.crewmember_model.info + "\n" + "Летает на типе: " + self.crewmember_model.fliesType

        label_additional_info = tk.CTkLabel(root,
                                            text= convert_from_plain(add_info_text),
                                            font=("Roboto", 14), justify=tk.LEFT)
        label_additional_info.place(x=340, y = 30)

        self.button_delete = tk.CTkButton(root, text="Удалить", command=lambda: controller.delete_item_by_id("crewmembers",self.crewmember_model.id), fg_color="#FF7CA3")
        self.button_delete.place(x=640,y=30)


class UserDetail():
    def __init__(self, user_model : UserModel):
        self.user_model = user_model

    def create_widgets(self, root, controller):
        self.controller = controller
        text = "Неизвестный тип. Свяжитесь с администратором, если это ошибка"
        if self.user_model.role == "admin":
            text = "Администратор"
        if self.user_model.role == "pilot":
            text = "Пилот/Стюард"
        if self.user_model.role == "crew_manager":
            text = "Менеджер ЛС"
        if self.user_model.role == "flight_manager":
            text = "Менеджер Рейсов"
        if self.user_model.role == "plane_manager":
            text = "Менеджер ВС"

        crewmember_name_info = tk.CTkLabel(root, text=self.user_model.full_name, font=("Roboto", 15))
        crewmember_name_info.place(x=30)

        add_info_text = text + "\n" + "Логин: " + self.user_model.login + "\n" + \
                        "Пароль: " + self.user_model.password + "\n" +\
                        "Описание: " + self.user_model.info


        label_additional_info = tk.CTkLabel(root,
                                            text= convert_from_plain(add_info_text),
                                            font=("Roboto", 14), justify=tk.LEFT)
        label_additional_info.place(x=30, y = 30)

        self.button_delete = tk.CTkButton(root, text="Удалить", command=lambda: self.delete_prerequesite(), fg_color="#FF7CA3")
        self.button_delete.place(x=640,y=30)

    def delete_prerequesite(self):
        if self.user_model.role == "admin":
            ans = messagebox.askokcancel("Внимание!", "Вы удаляете администратора, вы уверены?")
            if ans:
                self.controller.delete_item_by_id("users", self.user_model.id)
        else:
            self.controller.delete_item_by_id("users", self.user_model.id)


class CrewDetail():
    def __init__(self, crew_model : CrewModel):
        self.crew_model = crew_model

    def create_widgets(self, root, controller):
        pass

class FlightDetail():
    def __init__(self, flight_model : FlightModel):
        self.flight_model = flight_model

    def create_widgets(self, root, controller):
        overall_plane_info = tk.CTkLabel(root, text=self.flight_model.print(), font=("Roboto", 15))
        overall_plane_info.pack()

        plane_name_info = tk.CTkLabel(root, text="Самолёт: " + self.flight_model.planeName, font=("Roboto", 15))
        plane_name_info.pack()

        deltatime = ""

        time_info = tk.CTkLabel(root, text="Начало: " + self.flight_model.date_start + "\nКонец: " + self.flight_model.date_end + "\nВремя в пути: " + deltatime, font=("Roboto", 15))

        self.button_edit = tk.CTkButton(root, text="Редактировать",
                                          fg_color="#FF7CA3")
        self.button_edit.place(x=640, y=30)

        self.button_delete = tk.CTkButton(root, text="Удалить",
                                          command=lambda: controller.delete_item_by_id("flights", self.flight_model.id),
                                          fg_color="#FF7CA3")
        self.button_delete.place(x=640, y=30)