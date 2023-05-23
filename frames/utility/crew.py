import customtkinter as tk
from frame import BaseFrame
from PIL import Image


class CrewInfo():
    def __init__(self, line):
        self.id = int(line[0])
        self.name = line[1]
        self.pilot1id = int(line[2])
        self.pilot2id = int(line[3])
        self.stuard1id = int(line[4])
        self.stuard1id = int(line[5])
        self.stuard1id = int(line[6])
        self.stuard1id = int(line[7])
        self.stuard1id = int(line[8])
        self.stuard1id = int(line[9])
        self.stuard1id = int(line[10])
        self.isOccupied = bool(int(line[11]))


    def print_status(self):
        text = ""
        if self.isOccupied:
            text+= "Статус: Занят\n"
        else:
            text+= "Статус: Свободен\n"

        return text


class Crew():
    def __init__(self, crew_info ,controller, parent_frame, id):
        self.id = id
        self.crew_info = crew_info


        dir_rect = tk.CTkFrame(parent_frame, height=100, width=1600,
                               fg_color="#6FB1DE")


        label_name = tk.CTkLabel(dir_rect, text=self.crew_info.name, font=("Roboto", 26))


        label_additional_info = tk.CTkLabel(dir_rect,
                                  text= self.crew_info.print_status(),
                                  font=("Roboto", 14), justify=tk.LEFT)

        button = tk.CTkButton(dir_rect, text="Подробно", font=("Roboto", 16), text_color="#FFFFFF",
                              command=lambda : controller.open_crew_details(self.id, self.crew_info))


        button.place(relheight=0.2, relx=0.9)
        label_name.place(relheight=1, x=30)
        label_additional_info.place(relx = 0.5, relheight=1)
        dir_rect.pack(fill=tk.X, pady=1)