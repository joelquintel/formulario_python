import json
import os.path as os_path

class Infrastructure:
    def __init__(self):
        self.path_file = 'pessoas.json'
        self.encoding = 'utf-8'
        self.data = self.create_json_if_not_exist_or_keep_data()
    
    def create_json_if_not_exist_or_keep_data(self):
        arquivo = os_path.isfile(f'./{self.path_file}')
        create = f'./{self.path_file}'
        if arquivo:
            with open(f'./{self.path_file}', 'r', encoding=self.encoding) as arq:
                return json.loads(arq.read())
                
        else:
            with open(create, 'w') as arq:
                dados = json.dumps([])
                arq.write(dados)
                print('arquivo criado')
            with open(create, 'r', encoding=self.encoding) as arq:
                return json.loads(arq.read())


    
class Pessoa(Infrastructure):
    def __init__(self):
        super().__init__()
        
