from Model.Pessoa import Pessoa
from datetime import datetime


class Funcionario(Pessoa):  # Classe filha

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
                    return self.__ocorrencia[ocorrencia].getValorAcrescimo() - self.__ocorrencia[
                        ocorrencia].getValorDesconto()

    def __calcularIdadeDependente(self):
        quantidadeMenores = 0
        for dependente in range(len(self.listarDependente())):
            dataAtual = datetime.now()
            dataNascimento = self.listarDependente()[dependente].getDataNascimento()
            idade = dataAtual.year - dataNascimento.year - (
                    (dataAtual.month, dataAtual.day) < (dataNascimento.month, dataNascimento.day))
            if idade < 18:
                quantidadeMenores += 1
        return quantidadeMenores

    def calcularSalarioLiquido(self, mes, ano):
        return self.__cargo.getSalarioBruto() + self.__calcularOcorrencia(mes, ano) + (
                    self.__calcularIdadeDependente() * 100)

    def __proximoAniversario(self):
        for dependente in range(len(self.listarDependente())):
            dataAtual = datetime.now()
            dataNascimento = self.listarDependente()[dependente].getDataNascimento()
            proximoAniversario = datetime(dataAtual.year, dataNascimento.month, dataNascimento.day)
            if proximoAniversario < dataAtual:
                proximoAniversario = proximoAniversario.replace(year=dataAtual.year + 1)
            diasParaAniversario = (proximoAniversario - dataAtual).days
            proximoAniversarioStr = proximoAniversario.strftime("%d/%m/%y")
            semana = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado",
                      "Domingo"]
            return (f"Data do aniversário: {proximoAniversarioStr}"
                    f"\nDias para o aniversário: {diasParaAniversario}"
                    f"\nDia da semana: {semana[proximoAniversario.weekday()]}")

    def toStr(self, mes, ano):
        print(f"Funcionário:"
              f"\nNome: {self.getNome()}"
              f"\nSalário Liquido: {self.calcularSalarioLiquido(mes, ano)}\n"
              f"\nDependentes:")
        for dependente in range(len(self.listarDependente())):
            print(f"Dependente {dependente + 1}:"
                  f"\nNome: {self.listarDependente()[dependente].getNome()}"
                  f"\nData de Nascimento: {self.listarDependente()[dependente].strDataNascimento()}"
                  f"\n{self.__proximoAniversario()}\n")
