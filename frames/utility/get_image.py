import os.path
from PIL import Image
import customtkinter as tk

def get_image(path : str, size):
    if os.path.isfile(path):
        return tk.CTkImage(dark_image=Image.open(path), size=(size[0], size[1]))
    else:
        return tk.CTkImage(dark_image=Image.open("database/images/placeholder.png"), size=(size[0], size[1]))