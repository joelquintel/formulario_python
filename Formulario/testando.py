import json
import os.path as os_path

class Infrastructure:
    def __init__(self, path_file, encoding):
        self.path_file = path_file
        self.encoding = encoding

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
    def __init__(self,path_file, encoding):
        super().__init__(path_file, encoding)
        
    def funciona(self):
        print('funciona')

arquivo = Pessoas('pessoas.json', encoding='utf-8')
arquivo.create_json_if_not_exist()
arquivo.funciona()