import tkinter as menuTK
from view.cadastroView import CadastroView
from view.deleteCadastroView import DeleteCadastro
import os

class Menu():
    def __init__(self, menu) -> None:
        largura=150
        altura=70
        #Cadastro
        self.btn = menuTK.Button(menu, text="Cadastrar", command=self.cadastrar,bg="orange",)
        self.btn.place(x=600,y=150,width=largura,height=altura)
        #Delete cadastro
        self.btn = menuTK.Button(menu, text="Delete", command=self.deleteCadastro,bg="orange",)
        self.btn.place(x=600,y=290,width=largura,height=altura) 
    def cadastrar(self):
        
        window = menuTK.Toplevel()
        width= window.winfo_screenwidth()
        height= window.winfo_screenheight()
        window.geometry("%dx%d" % (width, height))
        window.title("Cadastro")
        CadastroView(window)
    
    def deleteCadastro(self):
        window = menuTK.Toplevel()
        width= window.winfo_screenwidth()
        height= window.winfo_screenheight()
        window.geometry("%dx%d" % (width, height))
        window.title("Delete")
        DeleteCadastro(window)
        #canvas = menuTK.Canvas(window, width=1080,height=600)
        #canvas.pack()
        #imgBG = menuTK.PhotoImage(file=pastaImg+"\\img\\bg_cadastro.png")
        #canvas.create_image(10,10,image=imgBG)
       
        
