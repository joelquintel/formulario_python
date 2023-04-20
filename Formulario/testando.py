from infrastructure.testando2 import Infrastructure
class Pessoas(Infrastructure):
    def __init__(self):
        super().__init__()
        
    def funciona(self):
        print('funciona')


if __name__ == '__main__':
    arquivo = Pessoas()
    arquivo.create_json_if_not_exist()
    arquivo.funciona()