from datetime import datetime

class Ocorrencia:

    def __init__(self):
        self.__dataOcorencia = ""
        self.__valorAcrescimo = 0
        self.__valorDesconto = 0
        self.__historicoOcorrencia = []
        self.__funcionario = []

    def setDataOcorencia(self, dataOcorrencia):
        self.__dataOcorencia = datetime.strptime(dataOcorrencia, "%d/%m/%y")

    def getDataOcorrencia(self):
        return self.__dataOcorencia

    def setValorAcrescimo(self, valorAcrescimo):
        self.__valorAcrescimo = valorAcrescimo

    def getValorAcrescimo(self):
        return self.__valorAcrescimo

    def setValorDesconto(self, valorDescnto):
        self.__valorDesconto = valorDescnto

    def getValorDesconto(self):
        return self.__valorDesconto

    def addHistoricoOcorrencia(self, historicoOcorencia):
        self.__historicoOcorrencia.append(historicoOcorencia)

    def removerHistoricoOcorrencia(self, historicoOcorencia):
        self.__historicoOcorrencia.remove(historicoOcorencia)

    def listarHistoricoOcorrencia(self):
        return self.__historicoOcorrencia

    def addFuncionario(self, funcionario):
        self.__funcionario.append(funcionario)

    def removerFuncionario(self, funcionario):
        self.__funcionario.remove(funcionario)

    def listarFuncionario(self):
        return self.__funcionario
