import tkinter as tk
import os
from PIL import ImageTk, Image
from view.menu import Menu

from config import load_toml

def main(configs: dict):

    menu = tk.Tk()
    
    menu.title("CRUD")
    
    width = menu.winfo_screenwidth()
    height = menu.winfo_screenheight()
    
    menu.geometry("%dx%d" % (width, height))
    menu.resizable(False, False)

    image1 = Image.open(configs["bg_menu"]).resize((1367, 720))
    imgBG = ImageTk.PhotoImage(image1)
    labelBG = tk.Label(menu, image=imgBG)
    
    labelBG.pack()

    Menu(menu)
    
    menu.mainloop()


if __name__ == "__main__":

    try:
        configs = load_toml()

    except Exception as e:
        print("Erro:>>>>>>>>>>>>>>", e)
    else:
        main(configs)
