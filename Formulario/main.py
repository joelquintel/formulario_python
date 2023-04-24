from tkinter import *
import os
from PIL import ImageTk, Image  
from view.menu import Menu
if __name__ == "__main__":

    try:
        pastaImg= os.path.dirname(__file__)
        menu = Tk()
        menu.title("CRUD")
        width= menu.winfo_screenwidth()
        height= menu.winfo_screenheight()
        menu.geometry("%dx%d" % (width, height))
        menu.resizable(False,False)

        image1 = Image.open("Formulario/view/img/bg_menu.png").resize((1367,720))
        imgBG = ImageTk.PhotoImage(image1)
        labelBG = Label(menu,image = imgBG)
        labelBG.pack()
        Menu(menu)
        
        

     

     

      
        

       # telefones = [{"nome": "Isabela Simone Corte Real",
                   # "telefone": "(94) 98550-6067", "estado": "PA"}]
        
        menu.mainloop()
        #window.mainloop()     
    except Exception as e:
        print("Erro:>>>>>>>>>>>>>>", e)