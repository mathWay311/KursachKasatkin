import customtkinter as tk
from frame import BaseFrame
from PIL import Image

class PlaneInfo():
    def __init__(self, line):
        self.id = int(line[0])
        self.brand = line[1]
        self.model = line[2]
        self.board_number = line[3]
        self.isOccupied = bool(int(line[4]))
        self.isRepaired = bool(int(line[5]))
        self.malfunction = line[6]
        self.imgPath = line[7]
    def print_status(self):
        text = ""
        print(self.isOccupied)
        if self.isOccupied and self.isRepaired:
            text+= "Статус: Ремонтируется\n"
        elif self.isOccupied:
            text += "Статус: В полёте\n"
        else:
            text+= "Статус: Простаивает\n"

        if self.isOccupied and self.isRepaired:
            text += "Неисправен"
        else:
            text += "Исправен"

        return text


class Plane():
    def __init__(self, plane_info ,controller, parent_frame, id):
        self.id = id
        self.plane_info = plane_info

        plane_logo_img = tk.CTkImage(dark_image=Image.open("database/images/" + self.plane_info.imgPath), size=(300, 300))

        dir_rect = tk.CTkFrame(parent_frame, height=300, width=1600,
                               fg_color="#6FB1DE")

        plane_logo = tk.CTkLabel(dir_rect, image=plane_logo_img, text="")
        label_brand = tk.CTkLabel(dir_rect, text=self.plane_info.brand + self.plane_info.model + self.plane_info.board_number, font=("Roboto", 26))


        label_additional_info = tk.CTkLabel(dir_rect,
                                  text=self.plane_info.print_status(),
                                  font=("Roboto", 14), justify=tk.LEFT)

        button = tk.CTkButton(dir_rect, text="Подробно", font=("Roboto", 16), text_color="#FFFFFF",
                              command=lambda : controller.open_plane_details(self.id, self.plane_info))



        plane_logo.place(x=0, relheight=1)
        button.place(relheight=0.1, relx=0.9)
        label_brand.place(relheight=0.33, x=350)
        label_additional_info.place(x=350, rely = 0.4)
        dir_rect.pack(fill=tk.X, pady=1)