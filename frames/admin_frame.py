import customtkinter as tk
from frame import BaseFrame
from PIL import Image

BUTTON_RELX = 0.33
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

class ScrollableFrame(tk.CTkFrame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.CTkCanvas(self)
        scrollbar = tk.CTkScrollbar(self, orientation="vertical", command=canvas.yview)
        self.scrollable_frame = tk.CTkFrame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class AdminFrame(BaseFrame):
    def create_widgets(self, controller):
        #   <--------BACKGROUND---------->
        background_image = tk.CTkImage(dark_image=Image.open("images/bg.jpg"), size=(2000, 2000))
        background_label = tk.CTkLabel(self, image=background_image, text = "")
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #   <--------BACKGROUND---------->

        #   <--------HEADER---------->

        self.upper_rect = tk.CTkFrame(self, height=50, fg_color="transparent")
        self.upper_rect.pack(side = tk.TOP, expand = True, fill = tk.X, anchor = tk.N)

        self.logolabel = tk.CTkLabel(self.upper_rect, text="G7 Airlines")
        self.logolabel.place(x=30, relheight=1)

        self.label_name = tk.CTkLabel(self.upper_rect, text="Иванович Иван Иванов")
        self.label_name.place(anchor = tk.NE, relx=0.86, relheight = 1)

        #   <--------HEADER---------->


        #   <--------SELPANEL---------->

        self.left_select_panel = tk.CTkFrame(self, width = 300, height = 400)
        #self.left_select_panel.place(rely=0.2, relx=0)
        self.left_select_panel.pack(side = tk.LEFT)

        self.button_flights = tk.CTkButton(self.left_select_panel, text="Рейсы", fg_color="#5A97C0", font=("Roboto", 20) , corner_radius=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text_color = "#FFFFFF")
        self.button_flights.pack()

        self.button_directions = tk.CTkButton(self.left_select_panel, text="Направления", fg_color="#5A97C0", font=("Roboto", 20), corner_radius=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text_color = "#FFFFFF", command = lambda : controller.populate_panel_with_content("Directions"))
        self.button_directions.pack()

        self.button_planes = tk.CTkButton(self.left_select_panel, text="ВС", fg_color="#5A97C0", font=("Roboto", 20), corner_radius=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text_color = "#FFFFFF")
        self.button_planes.pack()

        self.button_crew = tk.CTkButton(self.left_select_panel, text="ЛС", fg_color="#5A97C0", font=("Roboto", 20), corner_radius=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text_color = "#FFFFFF")
        self.button_crew.pack()

        self.button_workers = tk.CTkButton(self.left_select_panel, text="Сотрудники", fg_color="#5A97C0", font=("Roboto", 20), corner_radius=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text_color = "#FFFFFF")
        self.button_workers.pack()

        #   <--------SELPANEL---------->

        self.content_container = tk.CTkFrame(self, width = 1200, height= 700)
        self.content_container.pack(side = tk.RIGHT)

        #       <---------FIND AND ADD UPPER PANEL--------->
        self.upper_panel = tk.CTkFrame(self.content_container, height=50, fg_color="#6FB1DE", corner_radius=0)
        self.upper_panel.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.button_create_new = tk.CTkButton(self.upper_panel, text="+", fg_color="#5A97C0", font=("Roboto", 20),
                                              corner_radius=50, text_color="#FFFFFF", width=40, height=40)
        self.button_create_new.pack(side=tk.LEFT)

        self.button_prev_range = tk.CTkButton(self.upper_panel, text="<", fg_color="#6FB1DE", font=("Roboto", 20),
                                              corner_radius=0, text_color="#FFFFFF", width=40, height=40)
        self.button_prev_range.place(relx = 0.45)

        self.label_range = tk.CTkLabel(self.upper_panel, text="0-5", font = ("Roboto", 20))
        self.label_range.place(relx = 0.5, relheight = 1)

        self.button_next_range = tk.CTkButton(self.upper_panel, text=">", fg_color="#6FB1DE", font=("Roboto", 20),
                                              corner_radius=0, text_color="#FFFFFF", width=40, height=40)
        self.button_next_range.place(relx=0.55)

        self.field_find = tk.CTkEntry(self.upper_panel)
        self.field_find.pack(side=tk.RIGHT)

        #       <--------FIND AND ADD UPPER PANEL---------->

        #   <--------CONTENT PANEL---------->
        self.content_panel = tk.CTkFrame(self.content_container)
        #self.content_panel.place(relx=0.2, anchor=tk.NW, rely = 0.2)
        self.content_panel.pack()


        #   <--------CONTENT PANEL---------->

        #   <--------TEST---------->
        '''
        self.testrect = tk.CTkFrame(self.content_panel, fg_color="#00FF00", height=80, width=1200)
        self.testrect.pack(fill=tk.X)

        self.testlabel = tk.CTkLabel(self.testrect, text="TEST - TEST")
        self.testlabel.place(relx = 0.2, relheight = 1)
        '''



        #   <--------TEST---------->

        self.place(relwidth=1, relheight=1)


    def change_auth_info(self, name):
        self.label_name.configure(text = name)

