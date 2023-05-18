import customtkinter
import pymssql

customtkinter.set_default_color_theme("custom_theme.json")
def button_callback():
    print("button pressed")

loginwindow = customtkinter.CTk()
loginwindow.title("G7 Airlines - Авторизация")
loginwindow.geometry("400x400") # Разрешение
loginwindow.resizable(False, False) # Неизменямые размеры

for c in range(5): loginwindow.columnconfigure(index=c, weight=1)
for r in range(5): loginwindow.rowconfigure(index=r, weight=1)

label = customtkinter.CTkLabel(loginwindow, text="G7 Airlines", fg_color="transparent", font=('Roboto',24))
label.grid(row=0, column = 2, padx=20, pady=20)

login_field = customtkinter.CTkEntry(loginwindow)
login_field.grid(row = 1, column = 2)

login_info_label = customtkinter.CTkLabel(loginwindow, text="Логин", fg_color="transparent")
login_info_label.grid(row = 1, column = 1)

password_field = customtkinter.CTkEntry(loginwindow)
password_field.grid(row = 2, column = 2)

password_info_label = customtkinter.CTkLabel(loginwindow, text="Пароль", fg_color="transparent")
password_info_label.grid(row = 2, column = 1)

button = customtkinter.CTkButton(loginwindow, text="Вход", command=button_callback, width=150,height=50)
button.grid(row=3, column=2, padx=20, pady=20)




if __name__ == '__main__':
    loginwindow.mainloop()

