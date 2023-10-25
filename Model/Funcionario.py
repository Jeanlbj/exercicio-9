from Model.Pessoa import Pessoa
from datetime import datetime
from datetime import date

class Funcionario(Pessoa): # Classe filha

    def __init__(self):
        super().__init__()
        self.__cargo = ""
        self.__dependente = []
        self.__ocorrencia = []

    def addCargo(self, cargo):
        self.__cargo = cargo

    def listarCargo(self):
        return self.__cargo

    def addDependente(self, dependente):
        self.__dependente.append(dependente)

    def removerDependente(self, dependente):
        self.__dependente.remove(dependente)

    def listarDependente(self):
        return self.__dependente

    def addOcorencia(self, ocorrencia):
        self.__ocorrencia.append(ocorrencia)

    def removerOcorencia(self, ocorrencia):
        self.__ocorrencia.remove(ocorrencia)

    def listarOcorrencia(self):
        return self.__ocorrencia

    # Métodos da Classe

    def calcularOcorrencia(self, ano, mes):
        for ocorrencia in range(len(self.listarOcorrencia())):
            if ano == self.listarOcorrencia()[ocorrencia].getDataOcorrencia().year:
                if mes == self.listarOcorrencia()[ocorrencia].getDataOcorrencia().month:
                    return self.__ocorrencia[ocorrencia].getValorAcrescimo() - self.__ocorrencia[ocorrencia].getValorDesconto()

    def calcularIdadeDependente(self):
        quantidadeMenores = 0
        for dependente in range(len(self.listarDependente())):
            if (date.today().year - self.__dependente[dependente].getDataNascimento().year) < 18:
                quantidadeMenores += 1
        return quantidadeMenores

    def calcularSalarioLiquido(self, ano, mes):
        return self.__cargo.getSalarioBruto() + self.calcularOcorrencia(ano, mes) + (self.calcularIdadeDependente() * 100)
