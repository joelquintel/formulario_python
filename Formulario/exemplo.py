import json

# def get_data():
#     nome = input('digite o nome: ').strip()
#     telefone = input('digite o telefone: ').strip()
#     return {'nome':nome, 'telefone':telefone}

# if __name__ == "__main__":
#     try:
               
#         with open('pessoas.txt', 'r', encoding='utf-8') as arquivo:
#             print(arquivo.read())
        
#         novo = input('deseja adicionar novo valor[s/n]: ').lower().strip()
#         if novo == 's':
#             with open('pessoas.txt', 'a', encoding='utf-8') as arquivo:
#                 arquivo.write(f'{get_data()}\n')
            
        # with open ('pessoas.txt', 'r', encoding='utf-8') as arquivo:
        #     print(arquivo.read())
            
    # except Exception as e:
    #     print(e)

class Pessoas:
    def __init__(self):
        pass
    def ler_json(self):
        with open('pessoas.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print(dados)
            return dados 

    def new_value(self, lista:list ):
        with open ('pessoas.json', 'w', encoding='utf-8') as arquivo:
            dados = {"nome":"josé", "telefone":"12345678"}
            print(lista)
            if lista == []:
                arquivo.write(json.dumps(dados))
            lista.append(dados)
            arquivo.write(json.dumps(lista))
        # [{"nome":"carlos","telefone":"1234-5678"}]
pessoas = Pessoas()

# pessoas.ler_json()

pessoas.new_value(pessoas.ler_json())