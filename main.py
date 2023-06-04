import customtkinter as tk
import wincontroller

WINDOW_WIDTH = 1366

if __name__ == '__main__':


    tk.set_default_color_theme("custom_theme.json")
    root = tk.CTk()
    root.title("G7 Airlines - Авторизация")
    root.geometry(str(WINDOW_WIDTH) + "x768")
    root.resizable(True,True)
    winc = wincontroller.WinController(root)
    root.mainloop()
