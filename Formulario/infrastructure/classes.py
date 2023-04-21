import json
import os.path as os_path

class Infrastructure:
    def __init__(self):
        self.path_file = 'pessoas.json'
        self.encoding = 'utf-8'

    def create_json_if_not_exist(self):
        arquivo = os_path.isfile(f'./{self.path_file}')
        create = self.path_file
        if arquivo:
            #pass
            print('existe')
        else:
            with open(create, 'w') as arq:
                dados = json.dumps([])
                arq.write(dados)
            print('arquivo criado')


class Pessoas(Infrastructure):
    def __init__(self):
        super().__init__()
        