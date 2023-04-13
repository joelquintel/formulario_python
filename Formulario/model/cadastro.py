class Cadastro:
    def __init__(self,id,nome,telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone
 
    def setNome(self,id):
        self.id=id 
    def setNome(self,nome):
        self.nome=nome
    def setTelefone(self,telefone):
        self.telefone = telefone
    
    def getId(self):
        return self.id
            
    def getNome(self):
        return self.nome
    def getTelefone(self):
        return self.telefone
        
