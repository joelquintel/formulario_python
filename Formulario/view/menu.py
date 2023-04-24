import tkinter as menuTK
from view.cadastroView import CadastroView
import os

class Menu():
    def __init__(self, menu) -> None:
        self.btn = menuTK.Button(menu, text="Cadastrar", command=self.cadastrar,bg="orange",)
        self.btn.place(x=540,y=250)
    def cadastrar(self):
        
        window = menuTK.Toplevel()
        width= window.winfo_screenwidth()
        height= window.winfo_screenheight()
        window.geometry("%dx%d" % (width, height))
        window.title("Cadastro")
        CadastroView(window)
        
        #canvas = menuTK.Canvas(window, width=1080,height=600)
        #canvas.pack()
        #imgBG = menuTK.PhotoImage(file=pastaImg+"\\img\\bg_cadastro.png")
        #canvas.create_image(10,10,image=imgBG)
       
        
