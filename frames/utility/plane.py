import customtkinter as tk
from frame import BaseFrame
from PIL import Image
from database.models.plane_model import PlaneModel

class Plane():
    def __init__(self, plane_model: PlaneModel ,controller, parent_frame):
        self.model = plane_model

        plane_logo_img = tk.CTkImage(dark_image=Image.open("database/images/" + self.model.imgPath), size=(300, 300))

        dir_rect = tk.CTkFrame(parent_frame, height=300, width=1600,
                               fg_color="#6FB1DE")

        plane_logo = tk.CTkLabel(dir_rect, image=plane_logo_img, text="")
        label_brand = tk.CTkLabel(dir_rect, text=self.model.brand + " " + self.model.model + " " + self.model.board_number, font=("Roboto", 26))


        label_additional_info = tk.CTkLabel(dir_rect,
                                  text=self.model.print_status(),
                                  font=("Roboto", 14), justify=tk.LEFT)

        button = tk.CTkButton(dir_rect, text="Подробно", font=("Roboto", 16), text_color="#FFFFFF",
                              command=lambda : controller.open_plane_details(self.model.id, self.model))



        plane_logo.place(x=0, relheight=1)
        button.place(relheight=0.1, relx=0.9)
        label_brand.place(relheight=0.33, x=350)
        label_additional_info.place(x=350, rely = 0.4)
        dir_rect.pack(fill=tk.X, pady=1)