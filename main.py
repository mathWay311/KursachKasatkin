import customtkinter as tk
import wincontroller

if __name__ == '__main__':
    tk.set_default_color_theme("custom_theme.json")
    root = tk.CTk()
    root.title("G7 Airlines - Авторизация")
    root.geometry("1600x900")
    root.resizable(True,True)

    winc = wincontroller.WinController(root)
    root.mainloop()
