from Model.Pessoa import Pessoa
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

    def __calcularOcorrencia(self, mes, ano):
        for ocorrencia in range(len(self.listarOcorrencia())):
            if ano == self.listarOcorrencia()[ocorrencia].getDataOcorrencia().year:
                if mes == self.listarOcorrencia()[ocorrencia].getDataOcorrencia().month:
                    return self.__ocorrencia[ocorrencia].getValorAcrescimo() - self.__ocorrencia[ocorrencia].getValorDesconto()

    def __calcularIdadeDependente(self):
        quantidadeMenores = 0
        for dependente in range(len(self.listarDependente())):
            if (date.today().year - self.__dependente[dependente].getDataNascimento().year) < 18:
                quantidadeMenores += 1
        return quantidadeMenores

    def calcularSalarioLiquido(self, mes, ano):
        return self.__cargo.getSalarioBruto() + self.__calcularOcorrencia(mes, ano) + (self.__calcularIdadeDependente() * 100)

    def __calcularProximoAniversario(self):
        for dependente in range(len(self.listarDependente())):
            dataNascimento = self.listarDependente()[dependente].getDataNascimento()
            proximoAniversario = date.today().year, dataNascimento.month, dataNascimento().day
            if proximoAniversario < date.today():
                proximoAniversario = dataNascimento.day, dataNascimento.month, (date.today().year + 1)
            diasParaAniversario = (proximoAniversario - date.today()).days
            diasDaSemana = ["Segunda - Feira", "Terça - Feira", "Quarta - Feira", "Quinta - Feira", "Sexta - Feira", "Sábado", "Domingo"]
        return (f"Próximo Aniversário: {proximoAniversario}"
                f"Dias para o aniversário: {diasParaAniversario}"
                f"Dia da semana: {diasDaSemana[proximoAniversario.weekday()]}")

    def toStrFuncionario(self, mes, ano):
        return (f"Funcionário: {self.getNome()}"
                f"\nSalário Liquido: {self.calcularSalarioLiquido(mes, ano)}")

    def toStrDependente(self):
        for dependente in range(len(self.listarDependente())):
            return (f"Dependente {dependente + 1}: {self.listarDependente()[dependente].getNome()}"
                    f"\nData de Nascimento: {self.listarDependente()[dependente].strDataNascimento()}"
                    f"\n{self.__calcularProximoAniversario()}")
