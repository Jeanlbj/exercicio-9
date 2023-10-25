from Model.Pessoa import Pessoa

class Funcionario(Pessoa): # Classe filha

    def __init__(self):
        super().__init__()
        self.__cargo = ""
        self.__dependente = []

    def addCargo(self, cargo):
        self.__cargo  = cargo

    def listarCargo(self):
        return self.__cargo

    def addDependente(self, dependente):
        self.__dependente.append(dependente)

    def removerDependente(self, dependente):
        self.__dependente.remove(dependente)

    def listarDependente(self):
        return self.__dependente
