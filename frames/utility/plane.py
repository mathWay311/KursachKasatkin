import customtkinter as tk
from frame import BaseFrame
from PIL import Image
from database.models.models import PlaneModel
from main import WINDOW_WIDTH
from frames.utility.get_image import get_image
class Plane():
    def __init__(self, plane_model: PlaneModel ,controller, parent_frame):
        self.model = plane_model
        path_string = "database/images/" + self.model.imgPath
        plane_logo_img = get_image(path_string, (300,300))

        dir_rect = tk.CTkFrame(parent_frame, height=300, width=WINDOW_WIDTH,
                               fg_color="#6FB1DE")

        if self.model.isFlying:
            dir_rect.configure(fg_color="#4C738F")
        if self.model.isRepaired:
            dir_rect.configure(fg_color="#AEA98E")
        if self.model.isBinded:
            dir_rect.configure(fg_color="#728B72")



        plane_logo = tk.CTkLabel(dir_rect, image=plane_logo_img, text="")
        label_brand = tk.CTkLabel(dir_rect, text=self.model.brand + " " + self.model.model + " " + self.model.board_number, font=("Roboto", 26))


        label_additional_info = tk.CTkLabel(dir_rect,
                                  text=self.model.print_status(),
                                  font=("Roboto", 14), justify=tk.LEFT)

        edit_button = tk.CTkButton(dir_rect, text="Редактировать", font=("Roboto", 16), text_color="#FFFFFF", fg_color="#FFD37C",
                              command=lambda: controller.edit_plane_window(self.model))

        button = tk.CTkButton(dir_rect, text="Подробно", font=("Roboto", 16), text_color="#FFFFFF",
                              command=lambda : controller.open_plane_details(self.model))



        plane_logo.place(x=0, relheight=1)
        edit_button.place(relheight = 0.1, relx = 0.8)
        button.place(relheight=0.1, relx=0.9)
        label_brand.place(relheight=0.33, x=350)
        label_additional_info.place(x=350, rely = 0.4)
        dir_rect.pack(fill=tk.X, pady=1)