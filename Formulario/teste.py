
#n = int(input("digite n:6 "))
#i = int(input("digite n:2 "))
#j = input("digite n:3 ")

#while n:
 #   n = int(input("digite n:6 "))

#for numero in n,i,j:
#    if numero != 0:
#        print(numero)

import json
import shutil
import tempfile
from model.cadastro import Cadastro


cadastroPessoas = Cadastro(id="8",nome="carlos",telefone="4774-4774")
#print(cadastroPessoas.getNome())
#print(cadastroPessoas.getTelefone())

lista ={"alberto":199}
#lista.update(nome =j)

dic= {"id":cadastroPessoas.getId(),"Nome":cadastroPessoas.getNome(),"Telefone:":cadastroPessoas.getTelefone()}
dic.update(id = cadastroPessoas.getId(),nome =cadastroPessoas.getNome(),telefone=cadastroPessoas.getTelefone())

for item in lista.items():
 chave,valor =item
 with open('cadastroPessoas.json','a') as f:
  f.seek(0)

  json.dump(dic,f,separators=(',',':'))
 f.truncate()
 print(item)

