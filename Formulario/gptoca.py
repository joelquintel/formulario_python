import json
import os

class Agenda:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.contatos = []
        self._verificar_arquivo()

    def _verificar_arquivo(self) -> None:
        if not os.path.exists(self.nome_arquivo):
            # print('created.')
            with open(self.nome_arquivo, 'w') as arquivo:
                json.dump([], arquivo)
                
        # elif os.path.exists(self.nome_arquivo):
        #     return True

    def carregar_contatos(self):
        with open(self.nome_arquivo, 'r') as arquivo:
            self.contatos = json.load(arquivo)

    def salvar_contatos(self):
        with open(self.nome_arquivo, 'w') as arquivo:
            json.dump(self.contatos, arquivo)

    def adicionar_contato(self, nome, telefone):
        novo_contato = {'nome': nome, 'telefone': telefone}
        self.contatos.append(novo_contato)
        self.salvar_contatos()

    def alterar_contato(self, indice, nome=None, telefone=None):
        if nome:
            self.contatos[indice]['nome'] = nome
        if telefone:
            self.contatos[indice]['telefone'] = telefone
        self.salvar_contatos()

    def deletar_contato(self, indice):
        del self.contatos[indice]
        self.salvar_contatos()

lista_telefônica = Agenda('pessoas.json')

#print(lista_telefônica._verificar_arquivo())
lista_telefônica.carregar_contatos()
print(lista_telefônica.contatos)
