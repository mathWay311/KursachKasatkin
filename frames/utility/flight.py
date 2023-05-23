import customtkinter as tk
from frame import BaseFrame
from PIL import Image

class FlightInfo():
    def __init__(self, line):
        self.id = int(line[0])
        self.planeID= int(line[1])
        self.date_start = line[2]
        self.date_end = line[3]
        self.directionID = int(line[4])
        self.crewID = int(line[5])
        #
        self.crewName = ""
        self.planeName = ""
        self.dirName = ""
    def print(self):
        return self.dirName + " выполняющийся на самолёте " + self.planeName + " экипажем " + self.crewName

class Flight():
    def __init__(self, flight_info ,controller, parent_frame, id):
        self.id = id
        self.flight_info = flight_info


        dir_rect = tk.CTkFrame(parent_frame, height=80, width=1600,
                               fg_color="#6FB1DE")

        label_info = tk.CTkLabel(dir_rect, text=self.flight_info.print(), font=("Roboto", 26))

        button = tk.CTkButton(dir_rect, text="Подробно", font=("Roboto", 16), text_color="#FFFFFF")

        button.place(relheight=1, relx=0.9)
        label_info.place(relheight=1, x=30)
        dir_rect.pack(fill=tk.X, pady=1)