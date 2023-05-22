import customtkinter as tk
from frame import BaseFrame
from PIL import Image
from frames.scrollable_Frame import ScrollableFrame


class TestFrame(BaseFrame):
    def create_widgets(self, controller):
        #   <--------BACKGROUND---------->
        background_image = tk.CTkImage(dark_image=Image.open("images/bg.jpg"), size=(2000, 2000))
        background_label = tk.CTkLabel(self, image=background_image, text="")
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #   <--------BACKGROUND---------->

        #   <--------HEADER---------->
        for c in range(3): self.columnconfigure(index=c, weight=1)
        for r in range(3): self.rowconfigure(index=r, weight=1)

        self.upper_rect = tk.CTkFrame(self, height=50, width = 1000)
        self.upper_rect.grid(columnspan = 3, row = 0, column = 0, sticky = "nsew")

        self.left_select_panel = tk.CTkFrame(self, width=300, height=400)
        # self.left_select_panel.place(rely=0.2, relx=0)
        self.left_select_panel.grid(row = 2, column = 0, sticky="n")
        #   <--------HEADER---------->

        #   <--------SELPANEL---------->

        #self.left_select_panel = tk.CTkFrame(self, width=300, height=400)
        # self.left_select_panel.place(rely=0.2, relx=0)


        self.place(relheight = 1, relwidth = 1)