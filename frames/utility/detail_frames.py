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
        self.button_delete = tk.CTkButton(root, text="Удалить самолёт", command=lambda: controller.delete_plane_by_id(self.id), fg_color="#FF7CA3")
        self.button_delete.place(x=30,y=750)

        label_info.place(x = 30, y = 350)