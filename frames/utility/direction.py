import customtkinter as tk
from frame import BaseFrame


class Direction():
    def __init__(self, line ,controller, parent_frame, id):
        self.id = id
        dir_rect = tk.CTkFrame(parent_frame, height=80, width=1600,
                               fg_color="#6FB1DE")
        label = tk.CTkLabel(dir_rect, text=line[1] + " - " + line[2], font=("Roboto", 26))
        button = tk.CTkButton(dir_rect, text="Удалить", fg_color="#FF7CA3", font=("Roboto", 16), text_color="#FFFFFF",
                              command=lambda : controller.delete_by_id("directions", id))
        button.place(relheight=1, relx=0.9)
        label.place(relheight=1, x=50)
        dir_rect.pack(fill=tk.X, pady=1)

