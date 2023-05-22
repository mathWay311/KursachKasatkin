import customtkinter as tk
from frame import BaseFrame

class AddDirectionFrame(BaseFrame):
    def create_widgets(self, controller):
        self.label_from = tk.CTkLabel(self, text = "Откуда: ")
        self.label_from.pack()

        self.entry_from = tk.CTkEntry(self)
        self.entry_from.pack()

        self.label_to = tk.CTkLabel(self, text="Куда: ")
        self.label_to.pack()

        self.entry_to = tk.CTkEntry(self)
        self.entry_to.pack()

        self.button_submit = tk.CTkButton(self,text="Создать", command= lambda:controller.add_direction(lambda:self.entry_from.get()))
        self.button_submit.pack(side = tk.RIGHT)

        self.button_cancel = tk.CTkButton(self, text="Отмена", fg_color="#FF7CA3", command=lambda : self.root.destroy())
        self.button_cancel.pack(side=tk.LEFT)

        self.pack(side = tk.TOP,expand = 1, fill= tk.BOTH)