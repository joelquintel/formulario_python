def get_data():
    nome = input('digite o nome: ').strip()
    telefone = input('digite o telefone: ').strip()
    return {'nome':nome, 'telefone':telefone}

if __name__ == "__main__":
    try:
               
        with open('pessoas.txt', 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())
        
        novo = input('deseja adicionar novo valor[s/n]: ').lower().strip()
        if novo == 's':
            with open('pessoas.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{get_data()}\n')
            
        # with open ('pessoas.txt', 'r', encoding='utf-8') as arquivo:
        #     print(arquivo.read())
            
    except Exception as e:
        print(e)
