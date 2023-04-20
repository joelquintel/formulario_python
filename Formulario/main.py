from tkinter import *
import sys
from view.cadastroView import CadastroView

if __name__ == "__main__":

    try:
        window = Tk()
        window.title("Cadastro")
        window.geometry('600x400')
        window.configure(background="black")
        
        CadastroView(window)
        

     

     

      
        

       # telefones = [{"nome": "Isabela Simone Corte Real",
                   # "telefone": "(94) 98550-6067", "estado": "PA"}]
        
      
        window.mainloop()     
    except Exception as e:
        print("Erro:>>>>>>>>>>>>>>", e)