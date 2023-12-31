from Model.Pessoa import Pessoa
from datetime import datetime


class Dependente(Pessoa): # Classe filha

    def __init__(self):
        super().__init__()
        self.__dataNascimento = ""
        self.__funcionario = ""

    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = datetime.strptime(dataNascimento, "%d/%m/%Y")

    def getDataNascimento(self):
        return self.__dataNascimento

    def strDataNascimento(self):
        return self.__dataNascimento.strftime("%d/%m/%y")

    def addFuncionario(self, funcionario):
        self.__funcionario = funcionario

    def listarFuncionario(self):
        return self.__funcionario
