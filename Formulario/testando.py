from infrastructure.classes import Infrastructure, Pessoa

if __name__ == '__main__':
    arquivo = Pessoa()
    dados = arquivo.create_json_if_not_exist_or_keep_data()
    print(dados)