import json
import os.path as os_path
from tkinter import *
from random import choice

class Pessoas:

    def __init__(self, path_file, encoding):
        self.path_file = path_file
        self.encoding = encoding
        self.documents = self.read_json()

    def get_documents(self) -> list:
        return self.documents

    def set_documents(self, document) -> None:
        return self.documents.append(document)

    def create_empty_json(self):
        arquivo = os_path.exists(self.path_file)
        print(arquivo)
        # if not os_path.exists(self.path_file):
        #     with open(self.path_file, 'w') as arquivo:
        #         arquivo.write(json.dumps([]))
        #     print('>>>>>> criado.')
                
        # else:
        #     print(f'The {self.path_file} file exists.')
        
        # if not os_path.isfile(self.path_file) :
        #     with open(self.path_file, 'w', encoding=self.encoding) as arquivo:
        #         json.dump(self.path_file, arquivo, ensure_ascii=False)

    def read_json(self) -> list:

        with open(self.path_file, "r", encoding=self.encoding,) as arquivo:
            return json.loads(arquivo.read() or '[]')

    def write_json(self, data: dict) -> None:

        self.set_documents(data)

        with open(self.path_file, 'w', encoding=self.encoding) as arquivo:
            json.dump(self.get_documents(), arquivo, ensure_ascii=False,indent = 4)

    def __str__(self) -> str:
        return f"Pessoas:{len(self.get_documents()):03}"


