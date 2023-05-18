import customtkinter as tk
import wincontroller

if __name__ == '__main__':
    root = tk.CTk()
    root.title("G7 Airlines - Авторизация")
    root.geometry("600x600")
    root.resizable(1,1)

    winc = wincontroller.WinController(root)
    root.mainloop()
