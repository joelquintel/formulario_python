from gptoca import Agenda
import tkinter as tk
import os.path as os_path

# ctrl + k + f 

class CadastroView(Agenda):
    def __init__(self, window,nome_arquivo) -> None:
        #herança da class Pessoas e Cadastro
        super().__init__(nome_arquivo)
        # Nome
        self.lbl = tk.Label(window, text="Nome:").grid(column=0, row=0)
        self.txtNome = tk.Entry(window, width=10)
        self.txtNome.grid(column=1, row=0)
        # Telefone
        lbl2 = tk.Label(window, text="Telefone:")
        lbl2.grid(column=5, row=0)
        self.txtTel = tk.Entry(window, width=10)
        self.txtTel.grid(column=7, row=0)
        # UF
        #lbl3 = tk.Label(window, text="UF:")
        #lbl3.grid(column=21, row=0)
        #self.txtUF = tk.Entry(window, width=10)
        #self.txtUF.grid(column=28, row=0)
        btn = tk.Button(window, text="Cadastrar", command=self.clicked)

        btn.grid(column=15, row=25)
    #listaCadastro = {}
    def clicked(self):
        # pega os valores inserido no input do formulario
        nomeCd = self.txtNome.get()
        telefoneCd = self.txtTel.get()
        # ufCd = self.txtUF.get()
        print(nomeCd)
        if nomeCd != "" and telefoneCd !="":
            CadastroView.adicionar_contato(self,nome=nomeCd,telefone=telefoneCd)
      

