import tkinter as deleteCadastroTK

class DeleteCadastro():
    def __init__(self, window) -> None:
        # herança da class Pessoas
        #super().__init__()
        # Nome
        lbl = deleteCadastroTK.Label(window, text="Nome:").grid(column=0, row=0)
        self.txtNome = deleteCadastroTK.Entry(window, width=10)
        self.txtNome.grid(column=1, row=0)
        # Telefone
        lbl2 = deleteCadastroTK.Label(window, text="Telefone:")
        lbl2.grid(column=5, row=0)
        self.txtTel = deleteCadastroTK.Entry(window, width=10)
        self.txtTel.grid(column=7, row=0)
        # UF
        lbl3 = deleteCadastroTK.Label(window, text="UF:")
        lbl3.grid(column=21, row=0)
        self.txtUF = deleteCadastroTK.Entry(window, width=10)
        self.txtUF.grid(column=28, row=0)
        btn = deleteCadastroTK.Button(window, text="Delete", command=self.clicked)

        btn.grid(column=15, row=25)

    def clicked(self):
        # pega os valores inserido no input do formulario
        nomeCd = self.txtNome.get()
        telefoneCd = self.txtTel.get()
        ufCd = self.txtUF.get()

        print(nomeCd)  