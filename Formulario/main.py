import json
import shutil
import tempfile
from model.cadastro import Cadastro
from json import JSONEncoder


id = input()

n= input()
t = input()
cadastroPessoas = Cadastro(id,n,t)
#print(cadastroPessoas.getNome())
#print(cadastroPessoas.getTelefone())
dic ={}
dic2 ={}
lista = []
lista.append("r")
print(lista)
   

#dic= dict({"id":cadastroPessoas.getId(),"Nome":cadastroPessoas.getNome(),"Telefone:":cadastroPessoas.getTelefone()})


    
#print("dci",dic)
#dic.update(dic)
print(dic)
#conv = json.dumps(dic,indent=4)
#for chave,valor in dic.items():
  
 #  with open('cadastroPessoas.json','r', encoding='utf-8') as arq, \
  #  tempfile.NamedTemporaryFile('a', delete=False) as out:
    # ler todo o arquivo e obter o objeto JSON
   # 
    #dados = json.load(arq)
    # atualizar os dados com a nova pergunta
   
     
    #dados["PERGUNTA 7"] = "k3"
   
    # escreve o objeto atualizado no arquivo temporário
    #json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))

# se tudo deu certo, renomeia o arquivo temporário
#shutil.move(out.name, 'cadastroPessoas.json')

#with open('cadastroPessoas.json','r') as ff:
 #   abrir = ff.read()

  #  x = json.dumps(abrir)
   # y = json.loads(x)
    #print("mmm",y)
contador_sinal = 0
class ProductEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__
#with open('data.json', 'w') as fp: 
#     json.dump(dic,fp, indent=4, cls=ProductEncoder)

# Serializando os dados em json e salvando em um arquivo de texto


 #json.dump(dic,f,separators=(',',':'), cls=ProductEncoder)
 #f.truncate()


#with open('cadastroPessoas.json','r', encoding='utf-8') as arq, \
 #    tempfile.NamedTemporaryFile('a', delete=False) as out:
    # ler todo o arquivo e obter o objeto JSON
    
  #  dados = json.load(arq)
    # atualizar os dados com a nova pergunta
   
     
   # dados["PERGUNTA 7"] = "k3"
   
    # escreve o objeto atualizado no arquivo temporário
    #json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))

# se tudo deu certo, renomeia o arquivo temporário
#shutil.move(out.name, 'cadastroPessoas.json')



#for preencherLista in cadastroPessoas.getNome(),cadastroPessoas.getTelefone():
 #   lista.append(preencherLista)
#print(lista)

#with open('cadastroPessoas.txt','a') as f:
 #   for gravarArquivo in lista:
  #      f.write('{}\n'.format(gravarArquivo))
    