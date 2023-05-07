import tkinter as menuTK
from view.cadastroView import CadastroView
from view.deleteCadastroView import DeleteCadastro
import os
from PIL import ImageTk, Image  

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
        window.configure(bg="#FF8C00")
        #image1 = Image.open("Formulario/view/img/bg_cadastro.png").resize((1367,720))
        #imgBG = ImageTk.PhotoImage(image1)
        #labelBG =  menuTK.Label(window,image = imgBG)
        #labelBG.pack()
        #canvas = menuTK.Canvas(window, width=1367,height=720)
        #canvas.pack()
        #imgBG = ImageTk.PhotoImage(image1)
        #canvas.create_image(1367,720,image=imgBG)
        #adicionar o frame python para telas.
        CadastroView(window)
    
    def deleteCadastro(self):
        window = menuTK.Toplevel()
        width= window.winfo_screenwidth()
        height= window.winfo_screenheight()
        window.geometry("%dx%d" % (width, height))
        window.title("Delete")
        DeleteCadastro(window)
      
       
        
