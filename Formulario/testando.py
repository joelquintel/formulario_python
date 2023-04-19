class Pessoas:
    def __init__(self,path_file):
        self.path_file = path_file

    def create_json_if_not_exist(self):
        arquivo = os_path.isfile(f'./{self.path_file}')
        create = self.path_file
        if arquivo:
            pass
            #print('existe')
        else:
            with open(create, 'w') as arq:
                dados = json.dumps([])
                arq.write(dados)
            #print('não existe')

class Infrastructure:
    def __init__(self, path_file, encoding):
        self.path_file = path_file
        self.encoding = encoding