import json
import os.path as os_path
from tkinter import *
from random import choice

class Pessoas:

    def __init__(self, path_file, encoding):
        self.path_file = path_file
        self.encoding = encoding
        self.documents = self.read_json()

    def get_documents(self) -> list:
        return self.documents

    def set_documents(self, document) -> None:
        return self.documents.append(document)

    def create_empty_json(self):
        arquivo = os_path.exists(self.path_file)
        print(arquivo)
        # if not os_path.exists(self.path_file):
        #     with open(self.path_file, 'w') as arquivo:
        #         arquivo.write(json.dumps([]))
        #     print('>>>>>> criado.')
                
        # else:
        #     print(f'The {self.path_file} file exists.')
        
        # if not os_path.isfile(self.path_file) :
        #     with open(self.path_file, 'w', encoding=self.encoding) as arquivo:
        #         json.dump(self.path_file, arquivo, ensure_ascii=False)

    def read_json(self) -> list:

        with open(self.path_file, "r", encoding=self.encoding,) as arquivo:
            return json.loads(arquivo.read() or '[]')

    def write_json(self, data: dict) -> None:

        self.set_documents(data)

        with open(self.path_file, 'w', encoding=self.encoding) as arquivo:
            json.dump(self.get_documents(), arquivo, ensure_ascii=False,indent = 4)

    def __str__(self) -> str:
        return f"Pessoas:{len(self.get_documents()):03}"

listaCadastro = {}

window = Tk()
window.title("Cadastro")
window.geometry('600x300')
lbl = Label(window, text="Nome")
lbl.grid(column=0, row=0)
txtNome = Entry(window,width=10)
txtNome.grid(column=1, row=0)
#Telefone
lbl2 = Label(window, text="Telefone")
lbl2.grid(column=5, row=0)
txtTel = Entry(window,width=10)
txtTel.grid(column=7, row=0)

def clicked():

    nomeCd =  txtNome.get()
    telefoneCd =  txtTel.get()

    listaCadastro.update({"nome":nomeCd,"telefone":telefoneCd})

btn = Button(window, text="Cadastrar", command=clicked)

btn.grid(column=2, row=7)

window.mainloop()    

if __name__ == "__main__":

    try:
        

       # telefones = [{"nome": "Isabela Simone Corte Real",
                   # "telefone": "(94) 98550-6067", "estado": "PA"}]
        
        pessoas = Pessoas(os_path.abspath("./pessoas.json"), 'UTF-8')
        pessoas.create_empty_json()
        pessoas.write_json(listaCadastro)
        print(pessoas.get_documents())

    except Exception as e:
        print("Erro:>>>>>>>>>>>>>>", e)