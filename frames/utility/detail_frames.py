import customtkinter as tk
from frame import BaseFrame
from PIL import Image

def convert_from_plain(text):
    text = text.replace(r"\\n", "\n")
    return text

class PlaneDetail():
    def __init__(self, id, plane_info):
        self.id = id
        self.plane_info = plane_info

    def create_widgets(self, root, controller):
        plane_logo_img = tk.CTkImage(dark_image=Image.open("database/images/" + self.plane_info.imgPath), size=(300, 300))
        plane_logo = tk.CTkLabel(root, image=plane_logo_img, text="")
        plane_logo.place(x = 30)

        plane_brand_label = tk.CTkLabel(root, text=self.plane_info.brand + " " + self.plane_info.model + " " + self.plane_info.board_number, font=("Roboto", 15))
        plane_brand_label.place(x=340)

        label_additional_info = tk.CTkLabel(root,
                                            text=self.plane_info.print_status(),
                                            font=("Roboto", 14), justify=tk.LEFT)
        label_additional_info.place(x=340, y = 30)
        if self.plane_info.isRepaired:
            label_info = tk.CTkLabel(root, text="Неисправность", font=("Roboto", 15))
            self.malfunction_entry_field = tk.CTkTextbox(root, width=500, height=300)
            self.malfunction_entry_field.insert("1.0", convert_from_plain(self.plane_info.malfunction))
            self.malfunction_entry_field.configure(state="disabled")
            self.malfunction_entry_field.place(x=30, y=380)
            self.button_retrieve = tk.CTkButton(root,text="Вернуть с ремонта", command=lambda: controller.retrieve_plane_from_repair(self.id))
            self.button_retrieve.place(x=30, y= 680)
        else:
            label_info = tk.CTkLabel(root, text="Опишите неисправность", font=("Roboto", 15))
            self.malfunction_entry_field = tk.CTkTextbox(root, width = 500, height= 300)
            self.malfunction_entry_field.place(x = 30, y = 380)
            self.button_place_on_repair = tk.CTkButton(root, text="Отправить на ремонт", command=lambda: controller.place_plane_on_repair(self.id))
            self.button_place_on_repair.place(x=30, y= 680)
        self.button_delete = tk.CTkButton(root, text="Удалить самолёт", command=lambda: controller.delete_item_by_id("planes",self.id), fg_color="#FF7CA3")
        self.button_delete.place(x=30,y=750)

        label_info.place(x = 30, y = 350)


class CrewmemberDetail():
    def __init__(self, id, crewmember_info):
        self.id = id
        self.crewmember_info = crewmember_info

    def create_widgets(self, root, controller):
        crewmember_logo_img = tk.CTkImage(dark_image=Image.open("database/images/" + self.crewmember_info.imagePath), size=(300, 300))
        crewmember_logo = tk.CTkLabel(root, image=crewmember_logo_img, text="")
        crewmember_logo.place(x = 30)

        type_text = "Неизвестный тип. Свяжитесь с администратором, если это ошибка"
        if self.crewmember_info.type == "pilot":
            type_text = "Пилот(-есса)"
        elif self.crewmember_info.type == "stuard":
            type_text = "Стюард(-есса)"

        crewmember_name_info = tk.CTkLabel(root, text=self.crewmember_info.full_name, font=("Roboto", 15))
        crewmember_name_info.place(x=340)

        add_info_text = type_text + "\n" + self.crewmember_info.print_status() + "\n" + self.crewmember_info.info + "\n" + "Летает на типе: " + self.crewmember_info.fliesType

        label_additional_info = tk.CTkLabel(root,
                                            text= convert_from_plain(add_info_text),
                                            font=("Roboto", 14), justify=tk.LEFT)
        label_additional_info.place(x=340, y = 30)

        self.button_delete = tk.CTkButton(root, text="Удалить", command=lambda: controller.delete_item_by_id("crewmembers",self.id), fg_color="#FF7CA3")
        self.button_delete.place(x=640,y=30)


class UserDetail():
    def __init__(self, id, user_info):
        self.id = id
        self.user_info = user_info

    def create_widgets(self, root, controller):

        text = "Неизвестный тип. Свяжитесь с администратором, если это ошибка"
        if self.user_info.role == "admin":
            text = "Администратор"
        if self.user_info.role == "pilot":
            text = "Пилот/Стюард"
        if self.user_info.role == "crew_manager":
            text = "Менеджер ЛС"
        if self.user_info.role == "flight_manager":
            text = "Менеджер Рейсов"
        if self.user_info.role == "plane_manager":
            text = "Менеджер ВС"

        crewmember_name_info = tk.CTkLabel(root, text=self.user_info.full_name, font=("Roboto", 15))
        crewmember_name_info.place(x=30)

        add_info_text = text + "\n" + "Логин: " + self.user_info.login + "\n" + \
                        "Пароль: " + self.user_info.password + "\n" +\
                        "Описание: " + self.user_info.info


        label_additional_info = tk.CTkLabel(root,
                                            text= convert_from_plain(add_info_text),
                                            font=("Roboto", 14), justify=tk.LEFT)
        label_additional_info.place(x=30, y = 30)

        self.button_delete = tk.CTkButton(root, text="Удалить", command=lambda: controller.delete_item_by_id("users",self.id), fg_color="#FF7CA3")
        self.button_delete.place(x=640,y=30)

class CrewDetail():
    def __init__(self, id, user_info):
        self.id = id
        self.user_info = user_info

    def create_widgets(self, root, controller):
        pass