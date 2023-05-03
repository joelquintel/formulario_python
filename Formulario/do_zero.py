import json
import os.path as path

class Phone_book:
    def __init__(self):
        self.nome_arquivo = 'pessoas.json'
        self.encode = 'utf-8'
        self.dados = self.leitura()
        

    def verificar_arquivo(self) -> None:
        if not path.isfile(self.nome_arquivo):
            with open(self.nome_arquivo, 'w', encoding=self.encode) as arquivo:
                json.dump([],arquivo)

    def leitura(self) -> list:
        if path.isfile(self.nome_arquivo):
            with open(self.nome_arquivo, 'r', encoding=self.encode) as arquivo:
                try:
                    return json.load(arquivo)
                except json.JSONDecodeError:
                    return []
        else:
            return []

    def novo_contato(self, nome, telefone):
        novo = {"nome":nome, "telefone":telefone}
        self.dados.append(novo)
        # with open(self.nome_arquivo, 'w', encoding=self.encode) as arquivo:
        #     json.dump(self.dados(), arquivo)

    def write_on_file(self):
        with open(self.nome_arquivo, 'w', encoding=self.encode) as arquivo:
            json.dump(self.dados, arquivo)

if __name__ == "__main__":
    try:
        agenda = Phone_book()
        agenda.verificar_arquivo()
        agenda.novo_contato("josué", "1515-1515")
        print(agenda.dados)
        agenda.write_on_file()
    except Exception as e:
        print(e)