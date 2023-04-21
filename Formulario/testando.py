from infrastructure.classes import Infrastructure, Pessoas

if __name__ == '__main__':
    arquivo = Pessoas()
    arquivo.create_json_if_not_exist()
    arquivo.funciona()